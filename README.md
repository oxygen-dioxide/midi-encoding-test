# midi-encoding-test
midi文件支持歌词信息。但是，由于没有得到标准化，不同软件导出与支持导入的歌词编码不同。而且，很少有软件支持在导入Midi时自动判断或手动选择编码。

本仓库将包含以下内容：
* 不同语言，不同歌词编码的midi文件，用于对软件进行测试。
* 对多种支持歌词的midi编辑器（主要是歌声合成编辑器和乐谱排版软件）的测试结果

以下测试结果在Windows 11 简体中文版进行。
## 测试结果
### midi编辑器
|编辑器|支持自动判断|支持手动选择|zh-UTF8|zh-GBK|ja-UTF8|ja-ShiftJIS|
|-|-|-|-|-|-|-|
|[ACE Studio](http://ace-studio.timedomain.ai/)|×|×|√|默认歌词|√|默认歌词|
|DeepVocal|×|×|乱码|√|乱码|乱码|
|[MuseScore](http://musescore.org/)|×|×|√|乱码|√|乱码|
|[OpenUTAU](http://www.openutau.com/)|√|×|√|√|√|√|
|[UTAU](http://utau2008.xrea.jp/)|×|×|乱码|乱码|乱码|√|