Coding API
==========

此项目汇聚了从 [Coding-Android](https://coding.net/u/coding/p/Coding-Android/git) 项目中提取出来的 Coding API。

当前只包含部分 API （大概为 Coding-Android 中的一多半），仍在完善过程中。


View
----

可立即浏览已整理的文档： http://api-doc.coding.io/


Source
------

文档的源码都在 raml 目录下，由 raml/coding-api.raml 描述，它使用是 [RAML](http://raml.org) 格式。

它引用其他目录下的资源:

- raml/doc 为 markdown 格式的内嵌文档

- raml/samples 为样本数据

- raml/schemas 为 API 各实体的 JSON Schema 描述


RAML
----

RAML 是一种 RESTful API 的建模语言。

RAML 规格说明：http://raml.org/spec.html

RAML 基础文档：http://raml.org/docs.html

RAML 进阶文档：http://raml.org/docs-200.html


JSON Schema
-----------

JSON Schema 是一种用于描述/验证 JSON 数据的结构的声明方式.

官网: http://json-schema.org/

学习文档: http://spacetelescope.github.io/understanding-json-schema/

在线验证: http://jsonschema.net/#/


HTML
----

index.html 是通过 [raml2html](https://github.com/kevinrenskers/raml2html) 生成的。

生成 index.html 的命令为：

    $ raml2html raml/coding-api.raml > index.html


Pull Request
------------

欢迎有兴趣的人一起补充与完善这些 API。

比如：

- 更新样本数据，位于 raml/samples 目录下。

- 完善 schema, 位于 raml/schemas 目录下。

- 完善API说明，或新增接口，即 raml/coding-api.raml 文件

- 改善生成的页面，可将页面生成工具放在 tools 目录下。


License
=======

Coding-API is available under the MIT license.
