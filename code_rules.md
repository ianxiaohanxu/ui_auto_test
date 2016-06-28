[Reference: python code style guide](https://www.python.org/dev/peps/pep-0008/)

1. 不要用tab，用4个空格替代，在你的IDE或者Editor中事先设置好

2. 缩进用4个空格

3. 一行最大长度是79个字符

4. 对于长语句，用 \ 进行分行

5. 类和一级函数，前后加两个空行。类的方法，前后加一个空行。函数内部的逻辑代码块，前后加一个空行。

6. import语句分成三部分：build-in，第三方，自己写的。每部分之间用一个空行隔开，顺序是：build-in，第三方，自己写的

7. import语句请分开写

    不推荐：

    ```python
    import sys, os
    ```

    推荐：

    ```python
    import sys
    import os
    ```

8. 最低优先级的二元操作符前后加一个空格

    函数默认参数中使用的=，前后不加空格

9. 逗号，冒号，分号前面不加空格，后面加一个空格

    切片中的冒号，前后不加空格

10. 括号（大中小）前后不加空格

11. 文件第一行指定编码格式：```#-*- coding: UTF-8 -*-```

12. if或者for代码块，即使只有一条语句，也要分行写

13. 注释

    1. 注释块

       ```python
       # Hello, this is a comments block.
       # Yes, as you see, this is the second line.
       #
       # And this is the fourth line.
       ```

    2. 行内注释

       ```python
       x = x + 1		# Increment x
       ```

14. docstring

    ```python
    def add(x, y):
        """
        This function is calculate x+y
        """
        return x + y
    ```

15. 命名规则

    1. 包名要求简短，全小写字母，不推荐用下划线
    2. 模块名要求简短，全小写字母，可以用下划线
    3. 类名，CapWords格式，不推荐用下划线
    4. 函数名，全小写字母，可以用下划线
    5. 常量，全大写字母，可以用下划线
    6. 变量，全小写字母，可以用下划线