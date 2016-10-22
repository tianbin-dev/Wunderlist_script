# Wunderlist_script

该脚本主要实现解析奇妙清单备份Json文件，并将指定清单的数据以自定义格式输出到Markdown文件。



## 使用方法

1. 导出备份Json文件。（只有网页版才支持此功能）点击 用户名 －－》账户设置 －－》创建备份
2. 将导出的Json文件重命名为data.json
3. 下载脚本到本地 
4. 将data.json移动到wunderlist_script文件夹中
5. 参照下面提供的方法可以修改清单名，输出的Markdown文件名
6. 在Terminal中输入 python wunderlist.py
7. wunderlist文件夹中会出现blog.md，即清单数据文件



## 修改清单名称

```python
qingdan = parse_json.parse('data.json','qingdan_name')
```

将`qingdan_name`替换为自己要导出的清单名称



## 版本说明

* V0.1：完成数据解析并输出Markdown文件





