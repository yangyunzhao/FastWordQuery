# FastWordQuery Addon For Anki

感谢原作者提供这么方便的插件，也感谢 ChatGPT 和 Codex 帮我升级到可在 Anki 25.09.2 使用的版本，特别开心！！！
Thanks to the original author for this convenient addon, and thanks to ChatGPT and Codex for helping me upgrade it to work with Anki 25.09.2 — so happy!!!

  [Supported Dictionaries](docs/services.md)

  [为单词添加真人发音（朗文mdx词典）](docs/get_mdx_ldoce6_sounds.md)



## Features

This addon query words definitions or examples etc. fields from local or online dictionaries to fill into the Anki note.  
It forks from [WordQuery](https://github.com/finalion/WordQuery), added **multi-thread** feature, improve stability, and some other features.

  - Querying Words and Making Cards, IMMEDIATELY!
  - Support querying in mdx and stardict dictionaries.
  - Support querying in web dictionaries.
  - Support **Multi-Thread** to query faster.

## 克隆后改动记录
- 适配 Anki 25.09.2
- 修复下载音频文件失效的问题

## Post-clone Changes
- Adapted for Anki 25.09.2
- Fixed audio download failures

## 克隆后安装方式
1. 在原插件的同级目录新建任意文件夹（推荐命名为 fastwq）。
2. git clone 本项目到本地磁盘，将 `${root}/addons21/fastwq` 下的全部文件复制到刚刚新建的文件夹中。
3. 禁用之前的 fastwq 插件。
4. 重启 Anki 即可。

## Post-clone Installation
1. Create a new folder alongside the original addon folder (recommended name: `fastwq`).
2. `git clone` this project locally, then copy everything under `${root}/addons21/fastwq` into the newly created folder.
3. Disable the previous fastwq addon.
4. Restart Anki.

## Install

   1. Place addons or addons21 folder of this repository to anki addon folder.  
    **OR**
   2. Use the installation code: **1807206748**


## Setting

### Shortcut
  1. Click Menu **"Tools -> Add-ons -> FastWQ -> Edit..."**  
      ![](screenshots/setting_menu.png)
  2. Edit the code and click **Save**  
      ![](screenshots/setting_shortcut.png)

### Config
  1. In Browser window click menu **"FastWQ -> Options"**  
      ![](screenshots/setting_config_01.png)

  2. Click **Settings** button in the Options window  
      ![](screenshots/setting_config_02.png)  
      - **Force Updates of all fields** : Update all fields even if it's None
      - **Ignore Accents** : Ignore accents symbol of word in querying
      - **Auto check new version** : Check new version at startup
      - **Number of Threads** : The number of threads running at the same time
  
  
## Usage

### Set the query fields

  1. Click menu **"Tools ->  FastWQ"**, or in Browser window click menu **"FastWQ -> Options"**
  2. Select note type  
      ![](screenshots/options_01.png)
  3. Select Dictionary  
      ![](screenshots/options_02.png)
  4. Select Fields  
      ![](screenshots/options_03.png)
  5. Click **OK** button  

### 'Browser' Window
  1. Select single or multiple words, click menu **"FastWQ -> Query Selected"** or press shortcut Default is **Ctrl+Q**.  
      ![](screenshots/options_04.png)
  2. Waiting query finished  
      ![](screenshots/use_01.png)
  
### 'Add' Window
  1. Click Add button in Browser window, open Add window  
      ![](screenshots/use_02.png)
  2. Edit key field and click Query button  
      ![](screenshots/use_03.png)


## Other Projects Used
  - [mdict-query](https://github.com/mmjang/mdict-query)
  - [pystardict](https://github.com/lig/pystardict)
  - [WordQuery](https://github.com/finalion/WordQuery)
  - [AnkiHub](https://github.com/dayjaby/AnkiHub)
  - [snowball_py](https://github.com/shibukawa/snowball_py)
