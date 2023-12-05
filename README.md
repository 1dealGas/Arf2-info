# Arf2-Utils

Info and tools of **Aerials Chart[fumen] Format 2**.

### EaseType

Under Construction

### Editor Arf2 Structure

```gdscript
# Compressible
class AngleNode:
    19 var ms:int   # [0,512000]
    13 var degree:int   # [-4096,4095]

class PosNode:
    9 var curve_init:float   # [0,1]   # Precision: 1/512
    9 var curve_end:float   # [0,1]   # Precision: 1/512
    3 var easetype:int   # See "EaseType" Section.
    13 var x:float   # [-16,32]   # Precision: 1/128
    12 var y:float   # [-8,16]   # Precisin: 1/128
    18 var ms:int   # [0,512000]   # Precision: 2ms

class DeltaNode:
    # ratio = bpm * scale / 15000
    # ratio = dx/d(mstime) or dy/d(mstime)
    14 var ratio_x105:int   # [0,16000]

    18 var init_ms:int   # [0,512000]   # Precision: 2ms
    32 var base_x105:int   # Must be non-negative
    # ratio will be ratio_x105/(-100000.f) if base_x105[i]>base_x105[i+1]
    # x105 -> *100000

class Hint:
    13 var x:float   # [-16,32]   # Precision: 1/128
    12 var y:float   # [-8,16]   # Precision: 1/128
    19 var ms:int   # [0,512000]

    # Runtime Only
    19 var judged_mstime:int   # [0,512000]
    1 var terminated:bool


# Inompressible
class WishChild:
    32 var dtime_x100000:int   # See Class "DeltaNode".
    13 var anode:Array[AngleNode]   # MaxSize: 8192   # DtLimit: 8192ms

class WishGroup:
    5 var nodes:Array[PosNode]   # MaxSize: 32   # DtLimit: 16384ms
    10 var childs:Array[WishChild]   # MaxSize: 1024

    1 var layer:int   # 0 or 1
    16 var max_visible_distance:float   # [0,8)   # Precision: 1/8192

    # Editor Only
    - var label:String   # Will be omited in the compiling result.

class Arf2:

    # Info
    var init_ms:int
    var end_ms:int
    var total_hints:int
    var wgo_required:int
    var hgo_required:int

    # Traits
    # Camera Args will be adjustable at runtime, and so is panel texts.
    var special_hint:int
    var dts_layer1:Array[DeltaNode]
    var dts_layer2:Array[DeltaNode]

    # Chart[fumen] body
    var wish:Array[WishGroup]
    var hint:Array[Hint]

    # Index
    # Inner Arrays are filled with ints.
    var widx:Array[Array]
    var hidx:Array[Array]


# Runtime(API)
var Arf:Arf2
var xscale:float
var yscale:float
var xdelta:float
var ydelta:float
var rotdeg:float

# Runtime(Internal)
# Maps & Pointers Omitted
var dt_progress:int
var dt_layer1:int
var dt_layer2:int
# float SIN[901];
# float ECOS[901];
# float ESIN[1001];
# float ECOS[1001];
# float SQRT[1001];
# double RCP[8192];
```

## Arf2 JSON Output  (Encoded)

"0" represents an encoded interger.

```json
{
    "init_ms": 0,
    "end_ms": 0,
    "total_hints": 0,
    "wgo_required": 0,
    "hgo_required": 0,
    "special_hint": 0,
    "dts_layer1": [0],
    "dts_layer2": [0],
    "wish": [
        [
            0,
            [0],
            [
                [0,···]
            ]
        ]
    ],
    "hint": [0],
    "widx": [
        [0]
    ],
    "hidx": [
        [0]
    ]
}
```

## JSON  ->  *.arf  Converter

Under Construction
