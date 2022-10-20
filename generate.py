import yaml
import mido
#将ustx转为midi，使用指定的字符编码
def convert(inputfile:str,outputfile:str,encoding:str):
    ustx=yaml.load(open(inputfile,encoding="utf8"),Loader=yaml.FullLoader)
    midifile = mido.MidiFile(charset=encoding)
    for ustxpart in ustx["voice_parts"]:
        miditrack=mido.MidiTrack()
        time=0
        for ustxnote in ustxpart["notes"]:
            lyric=ustxnote["lyric"]
            if(lyric.startswith("+")):
                lyric="-"
            miditrack.append(mido.MetaMessage('lyrics',text=lyric,time=(int(ustxnote["position"])-time)))#歌词
            miditrack.append(mido.Message('note_on', note=int(ustxnote["tone"]),velocity=64,time=0))
            miditrack.append(mido.Message('note_off',note=int(ustxnote["tone"]),velocity=64,time=int(ustxnote["duration"])))
            time=int(ustxnote["position"])+int(ustxnote["duration"])
        miditrack.append(mido.MetaMessage('end_of_track'))
        midifile.tracks.append(miditrack)
    midifile.save((outputfile))

convert("zh.ustx","zh-UTF8.mid","UTF-8")
convert("zh.ustx","zh-GBK.mid","GBK")
convert("zh-hant.ustx","zh-BIG5.mid","BIG5")
convert("ja.ustx","ja-UTF8.mid","UTF-8")
convert("ja.ustx","ja-ShiftJIS.mid","shiftjis")