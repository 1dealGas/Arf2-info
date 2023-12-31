# Arf2-info

Info of **Aerials Chart[fumen] Format 2**.

## EaseType

`ESIN`  ->  Sin ( ratio * π/2 )            `ECOS`  ->  1 - Cos ( ratio * π/2 ) 

|           | 0        | 1        | 2      | 3                                                    |
|:---------:|:--------:|:--------:|:------:|:----------------------------------------------------:|
| **PosX**  | `Linear` | `ESIN`   | `ECOS` | `InQuad`  if  `sgn >= 0` ,  `OutQuad`  if  `sgn < 0` |
| **PosY**  | `Linear` | `ECOS`   | `ESIN` | `InQuad`  if  `sgn >= 0` ,  `OutQuad`  if  `sgn < 0` |
| **Angle** | `Stasis` | `Linear` | `ESIN` | `ECOS`                                               |

## Editor Arf2 Structure

```gdscript
# Compressible
class AngleNode:
    18 var ms:int   # [0,512000]   # Precision: 2ms
    2 var easetype:int
    12 var degree:int   # [-1800,1800]

class PosNode:
    9 var curve_init:float   # [0,1]   # Precision: 1/512
    9 var curve_end:float   # [0,1]   # Precision: 1/512
    2 var easetype:int   # sgn: curve_end - curve_init
    13 var x:float   # [-16,32]   # Precision: 1/128
    12 var y:float   # [8,16]   # Precisin: 1/128
    19 var ms:int   # [0,512000]

class DeltaNode:
    # ratio = bpm * scale / 15000
    # ratio = dx/d(mstime) or dy/d(mstime)
    # dbpm(bpm*scale) range: [-2400, -0.15]&[0.15, 2400]
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
    # Non-Judged:         TAG==0 ->  Not-lit    TAG==1 ->  Lit
    # Judged:             TAG==0 ->  No Hint    TAG==1 ->  With Hint
    # judged_mstime == 1: Sweeped Hint, TAG should be always 0.
    19 var judged_mstime:int   # [0,512000]
    1 var TAG:bool


# Inompressible
class WishChild:
    32 var dtime_x105:int   # See Class "DeltaNode".
    8 var anodes:Array[AngleNode]   # MaxSize: 256   # DtLimit: 16384ms

class WishGroup:
    16 var max_visible_distance:float   # [0,8)   # Precision: 1/8192
    1 var layer:int   # 0 or 1

    5 var nodes:Array[PosNode]   # MaxSize: 32   # DtLimit: 8192ms
    10 var childs:Array[WishChild]   # MaxSize: 1024

    # Editor Only
    - var label:String   # Will be omited in the compiling result.

class Arf2Index:
    var widx:Array[int]
    var hidx:Array[int]

class Arf2:

    # Info
    var before:int
    var total_hints:int
    var wgo_required:int
    var hgo_required:int

    # Chart[fumen] body
    var wish:Array[WishGroup]   # MaxSize: 65536
    var hint:Array[Hint]   # MaxSize: 65536

    # Traits
    # Camera Args will be adjustable at runtime, and so is panel texts.
    var special_hint:int
    var dts_layer1:Array[DeltaNode]   # MaxSize: 65536
    var dts_layer2:Array[DeltaNode]   # DtLimit: 16384ms
    var index:Array[Arf2Index]
```

## Arf2 JSON Output  (Encoded)

`0` represents an encoded interger, `[0]` represents multiple encoded intergers.

```json
{
    "before": 0,
    "total_hints": 0,
    "wgo_required": 0,
    "hgo_required": 0,
    "wish": [
        {
            "info": 0,
            "nodes": [0],
            "childs": [
                {
                    "p": 0,
                    "dt": 0,
                    "anodes": [0]
                }
            ]
        }
    ],
    "hint": [0],
    "special_hint": 0,
    "dts_layer1": [0],
    "dts_layer2": [0],
    "index": [
        {
            "widx": [0],
            "hidx": [0]
        }
    ]
}
```

## How to play an `Arf` work in `AcPlay`

============================

**Deprecated, working in progress**

============================

1. ~~Acquire `Arf2.fbs` and `flatc` (the [FlatBuffers](https://github.com/google/flatbuffers/releases) compiler) .~~

2. ~~Export the work, and use the command below to convert the output `export.json` :~~
   
   ~~`flatc -b --force-defaults Arf2.fbs export.json`~~

3. ~~Utilize the conversion result `export.bin` :~~
   
   ```lua
   local fm = sys.get_resource("Arf/export.bin")
   Arf2.InitArf(fm)
   ```
   
   ~~(Usually, we rename the conversion result to `[id].arf` .)~~
