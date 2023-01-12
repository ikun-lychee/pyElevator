# pyElevator
![Size](https://img.shields.io/github/repo-size/ikun-lychee/pyElevator)
![Version](https://img.shields.io/badge/版本-v0.0-green)
![State](https://img.shields.io/badge/状态-预发布-red)
## 电梯运行原理
> 公式： ~~上下上下上下上下......~~

----------
它的意思：电梯先上去，上到上面没人了再下来，下来下到没人了再上来，重复执行，直到电梯坏了 ~~（doge）~~

写成代码：
```python
while True:
    state = "要上楼"
    if state == "要上楼":
        if "已经到顶了":
            state = "要下楼"
            continue
        # 上楼
        pass
    if state == "要下楼":
        if "已经到顶了":
            state = "要上楼"
            continue
        # 下楼
        pass

#doge
```


<br/><br/><br/><br/><br/><br/>怎么样？

根据这样的思路，我下回还会做个Scratch版的 ~~（doge）~~

----------

> 当然，**代码很多啊啾咪**

----------

## 文件直通车：
[人数管理](peoList.py)

[UI界面](main.py)

[依赖库](requirements.txt)

[徽标](icon.png)

----------

## 网上代码：

| github(?)                                                                  | [gitee](https://gitee.com/ikun-lychee/py-elevator) |
|-----------------------------------------------------------------------------|----------------------------------------------------|
| UI界面(?)                                                                     | 等等                                                 |
| 徽标(?)                                                                       | 等等                                                 |
| 人数管理(?)                                                                    | 等等                                                 |
| 依赖库(?)                                                                     | 等等                                                 |
| README.md(?!)                                                                | [README.md](https://gitee.com/ikun-lychee/py-elevator/blob/master/README.md) |



----------
声明一下，我之所以做这个电梯模拟器，是因为**整个社区没一个*作品*是*能进行全局管理的***（doge保护）

----------

*版本0.0*
