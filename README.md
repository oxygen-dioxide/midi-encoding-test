# midi-encoding-test
midi文件支持歌词信息。但是，由于没有得到标准化，不同软件导出与支持导入的歌词编码不同。而且，很少有软件支持在导入Midi时自动判断或手动选择编码。

本仓库将包含以下内容：
* 不同语言，不同歌词编码的midi文件，用于对软件进行测试。这些文件使用[generate.py](generate.py)由ustx转换得到。使用mido库写入midi文件。
* 对多种支持歌词的midi软件（主要是歌声合成编辑器和乐谱排版软件）的测试结果，包括：
  * 支持导入的midi文本编码
  * 导出的midi文本编码

以下测试结果在启用了“使用UTF-8提供全球语言支持”的 Windows 11 简体中文版进行。
## 测试结果
### midi导入
|软件|支持自动判断|支持手动选择|zh-UTF8|zh-GBK|zh-BIG5|ja-UTF8|ja-ShiftJIS|
|-|-|-|-|-|-|-|-|
|[ACE Studio](http://www.acestudio.ai/) 1.3.0|×|×|√|默认歌词|默认歌词|√|默认歌词|
|DeepVocal 2.1.0|×|×|√|乱码|乱码|√|乱码|
|[MuseScore](http://musescore.org/) 3.5.2|×|√|√|√|√|√|√|
|[OpenSVIP](https://openvpi.github.io/home/) 1.4.1<br/>midi插件 0.8.3|×|×|√|乱码|乱码|√|乱码|
|[OpenUTAU](http://www.openutau.com/) 0.1.2|√|×|√|√|√|√|√|
|[QVogen](https://gitee.com/functioner/qvogenclient) 0.2.2|×|×|乱码|√|乱码|乱码|乱码|
|[UTAU](http://utau2008.xrea.jp/) 0.4.18|×|×|乱码|乱码|乱码|乱码|乱码|

以下编辑器支持导入midi，但不支持导入歌词：
* [X Studio](https://singer.xiaoice.com/) 1.8.0
* AISingers（桌面版） 1.06

### midi导出
|软件|编码|
|-|-|
|[OpenSVIP](https://openvpi.github.io/home/)|支持在不同制式的Unicode和本地编码间手动选择|
|[OpenUTAU](http://www.openutau.com/)|UTF-8|

以下编辑器支持导出midi，但不支持导出歌词：
* [MuseScore](http://musescore.org/)