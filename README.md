# 这可事 QQ 机器人

~~您是否经常为找不到合适的 emoji/表情包 而苦恼？~~

苦恼个*, 现在有了【这可事QQ机器人】, 这都不是问题~

## 怎么部署?

记得使用 `python >= 3.8` 版本

### 1. 安装依赖

```bash
pip uninstall -y websocket
pip install rel requests websocket-client
```

### 2. 部署 [gocqhttp](https://docs.go-cqhttp.org/guide/#go-cqhttp)

- http 端口: `5700`
- 正向 websocket 端口: `5701`

### 3. 运行机器人

```bash
python main.py
```

## 命令列表

|命令|参数|功能|示例|
|:--:|:--:|:--:|:--:|
|`.ping`||检查机器人能否工作|`.ping`|
|`.r`|`短语[数量]`或`短语数量[短语数量][...][短语[数量]]`|发送表情/贴纸/自定义内容|`.r th`,`.r nya`,`.r cr2ca1hea`,`.r .hel`|
