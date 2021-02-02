# tutorial
Tutorial for programming languages

## Go vs Python3
### 1. 注释
```go
《Go注释》
// 单行注释
/*
 Author by kevin
 我是多行注释
*/
```
```python
《Python注释》
# 单行注释
"""
 Author by kevin
 我是多行注释
"""
```

### 2. 函数定义
```go
《Go函数》
func function_name(input1 type1, input2 type2) (return_type1, return_type2) {
    // doing something
}
```

```python
《Python函数》
def function_name(input1, input2):
    // doing something
```

### 3. 匿名函数
```go
《Go匿名函数》
func getSequence() func() int {
    i := 0
    return func() int {
    	i += 1
    	return i
    }   
}
```

```python
《Python匿名函数》
lambda arg1, arg2: arg1 + arg2
```

#### 4. 读写数据

