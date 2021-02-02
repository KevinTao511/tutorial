## Go语言教程
### 1. 数据类型
在 Go 编程语言中，数据类型用于声明函数和变量。常用数据类型有：
#### 1.1 布尔型
只有`true`和`false`，默认为`false`。

#### 1.2 数字型
整型有：`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`。

浮点型有：`float32`、`float64`。

#### 1.3 字符型
使用双引号`""`来表示字符串`string`。

#### 1.4 数组类型
数组是一个固定长度的序列，由一个或多个元素组成，长度固定，不能动态变化。

#### 1.5 切片类型
切片是一种动态数组，长度不固定，可以进行追加和删除。

#### 1.6 Map集合类型
`Map`集合是无序的`key-value`数据结构，`key`属于同一数据类型，`value`属于同一数据类型，`key`和`value`的数据类型可以不同。

#### 1.7 指针类型
指针变量是指向一个值的内存地址，先定义指针变量，然后为指针变量赋值，最后访问指针变量中指向地址的值。

#### 1.8 结构体类型
结构体是由一系列相同类型或不同类型的数据构成的数据集合，使用`type`和`struct`来定义结构体。

### 2. 控制语句
#### 2.1 if-else 语句
```go
if true {
    // doing something
} else {
    // doing something
}
```

#### 2.2 for 循环语句
```go
// 形式一
for init; condition; post {
    /*
    init: 一般为赋值表达式，给控制变量赋初值；
    condition：关系或逻辑表达式，控制条件；
    post：一般为赋值表达式，给控制变量增量或减量。
    */
}

// 形式二
for condition { 
    // doing something
}

// 形式三 
for {
    // 无限循环下去
}
```

#### 2.3 switch 语句
`switch`默认情况下`case`最后自带`break`语句，匹配成功后就不会执行其他`case`，如果我们需要执行后面的`case`，可以使用关键词`fallthrough`。
```go
switch type {
    case type1:
    	...
    case type2:
        ...
        fallthrough
    case type3:
        ...
    default:
    	...
}
```

#### 2.4 select 语句
`select`语句中每个`case`必须是一个通信操作，随机执行一个可运行的`case`。如果没有`case`可运行，它将阻塞，直到有`case`可运行。

如果有多个`case`都可以运行，`select`会随机公平地选出一个执行，其他不会执行。如果有`default`子句，则执行该语句。如果没有`default`子句，`select`将阻塞，直到某个通信可以运行。

```go
select {
    case communication clause:
    	statement(s)
    case communication clause:
    	statement(s)
    default:
    	statement(s)
}
```

#### 2.5 for-range 语句
`for-range`循环可以对`string`、`数组`、`slice`、`map`等进行迭代循环。
```go
for key, value := range oldMap {
    // doing something
}
```

### 3.函数、接口
#### 3.1 函数定义
```go
func function_name(input1 type1, input2 type2) (return_type1, return_type2) {
    // doing somethings
    return value1, value2
}
```

#### 3.2 函数接口
`interface`把所有的具有共性的方法定义在一起，任何其他类型只要实现了这些方法就是实现了这个接口。
```go
/* 定义接口 */
type interface_name interface {
    method_name1 [return_type]
    method_name2 [return_type]
    ...
}

/* 定义结构体 */
type struct_name struct {
    member definition
    member definition
    ...
}

/* 实现接口方法 */
func (struct_name_variable struct_name) method_name1() [return_type] {
    // doing somethings
}

func (struct_name_variable struct_name) method_name2() [return_type] {
    // doing somethings
}
```

### 4.读写数据

### 5.错误处理

### 6.并发编程

### 7.网络编程
