绝大部分接口的响应类型为 application/json。此时，响应的JSON对象中都包含一个 `error_code` 字段，这用于标识请求成功与否：

1. `error_code` 为 0，此时成功执行了请求。
   对应的数据位于`data`字段。
   它的具体类型跟接口有关。

   如：

       {
           "error_code": 0,
           "data": "",
           "message": ""
       }

2. `error_code` 不为 0，此时请求未能正常完成。
   对应的错误信息位于`message`字段。
   它的类型为string。

   如：

       {
            "error_code": 1001,
            "data": "",
            "message": "cluster not exists"
       }
