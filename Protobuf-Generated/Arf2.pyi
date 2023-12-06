from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WishChild(_message.Message):
    __slots__ = ("info", "anodes")
    INFO_FIELD_NUMBER: _ClassVar[int]
    ANODES_FIELD_NUMBER: _ClassVar[int]
    info: int
    anodes: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, info: _Optional[int] = ..., anodes: _Optional[_Iterable[int]] = ...) -> None: ...

class WishGroup(_message.Message):
    __slots__ = ("info", "nodes", "childs")
    INFO_FIELD_NUMBER: _ClassVar[int]
    NODES_FIELD_NUMBER: _ClassVar[int]
    CHILDS_FIELD_NUMBER: _ClassVar[int]
    info: int
    nodes: _containers.RepeatedScalarFieldContainer[int]
    childs: _containers.RepeatedCompositeFieldContainer[WishChild]
    def __init__(self, info: _Optional[int] = ..., nodes: _Optional[_Iterable[int]] = ..., childs: _Optional[_Iterable[_Union[WishChild, _Mapping]]] = ...) -> None: ...

class Arf2Index(_message.Message):
    __slots__ = ("widx", "hidx")
    WIDX_FIELD_NUMBER: _ClassVar[int]
    HIDX_FIELD_NUMBER: _ClassVar[int]
    widx: _containers.RepeatedScalarFieldContainer[int]
    hidx: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, widx: _Optional[_Iterable[int]] = ..., hidx: _Optional[_Iterable[int]] = ...) -> None: ...

class Arf2(_message.Message):
    __slots__ = ("init_ms", "end_ms", "total_hints", "wgo_required", "hgo_required", "wish", "hint", "special_hint", "dts_layer1", "dts_layer2", "index")
    INIT_MS_FIELD_NUMBER: _ClassVar[int]
    END_MS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_HINTS_FIELD_NUMBER: _ClassVar[int]
    WGO_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    HGO_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    WISH_FIELD_NUMBER: _ClassVar[int]
    HINT_FIELD_NUMBER: _ClassVar[int]
    SPECIAL_HINT_FIELD_NUMBER: _ClassVar[int]
    DTS_LAYER1_FIELD_NUMBER: _ClassVar[int]
    DTS_LAYER2_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    init_ms: int
    end_ms: int
    total_hints: int
    wgo_required: int
    hgo_required: int
    wish: _containers.RepeatedCompositeFieldContainer[WishGroup]
    hint: _containers.RepeatedScalarFieldContainer[int]
    special_hint: int
    dts_layer1: _containers.RepeatedScalarFieldContainer[int]
    dts_layer2: _containers.RepeatedScalarFieldContainer[int]
    index: _containers.RepeatedCompositeFieldContainer[Arf2Index]
    def __init__(self, init_ms: _Optional[int] = ..., end_ms: _Optional[int] = ..., total_hints: _Optional[int] = ..., wgo_required: _Optional[int] = ..., hgo_required: _Optional[int] = ..., wish: _Optional[_Iterable[_Union[WishGroup, _Mapping]]] = ..., hint: _Optional[_Iterable[int]] = ..., special_hint: _Optional[int] = ..., dts_layer1: _Optional[_Iterable[int]] = ..., dts_layer2: _Optional[_Iterable[int]] = ..., index: _Optional[_Iterable[_Union[Arf2Index, _Mapping]]] = ...) -> None: ...
