# Arf2-utils

Info and tools of **Aerials Chart[fumen] Format 2**.

### EaseType

| init<end | 0      | 1          | 2          | 3               | 4          | 5          | 6               | 7          |
|:--------:|:------:|:----------:|:----------:|:---------------:|:----------:|:----------:|:---------------:|:----------:|
| **x**    | Linear | **InQuad** | **InCirc** | **Sin(rt*π/2)** | Linear     | Linear     | Linear          | **InQuad** |
| **y**    | Linear | Linear     | Linear     | Linear          | **InQuad** | **InCirc** | **Sin(rt*π/2)** | **InQuad** |

| init>end | 0      | 1           | 2           | 3               | 4           | 5           | 6               | 7           |
|:--------:|:------:|:-----------:|:-----------:|:---------------:|:-----------:|:-----------:|:---------------:|:-----------:|
| **x**    | Linear | **OutQuad** | **OutCirc** | **Cos(rt*π/2)** | Linear      | Linear      | Linear          | **OutQuad** |
| **y**    | Linear | Linear      | Linear      | Linear          | **OutQuad** | **OutCirc** | **Cos(rt*π/2)** | **OutQuad** |

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
    12 var y:float   # [8,16]   # Precisin: 1/128
    18 var ms:int   # [0,512000]   # Precision: 2ms

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
    19 var judged_mstime:int   # [0,512000]
    1 var terminated:bool


# Inompressible
class WishChild:
    32 var dtime_x105:int   # See Class "DeltaNode".
    8 var anodes:Array[AngleNode]   # MaxSize: 256   # DtLimit: 8192ms

class WishGroup:
    16 var max_visible_distance:float   # [0,8)   # Precision: 1/8192
    1 var layer:int   # 0 or 1

    5 var nodes:Array[PosNode]   # MaxSize: 32   # DtLimit: 16384ms
    10 var childs:Array[WishChild]   # MaxSize: 1024

    # Editor Only
    - var label:String   # Will be omited in the compiling result.

class Arf2Index:
    var widx:Array[int]
    var hidx:Array[int]

class Arf2:

    # Info
    var init_ms:int
    var end_ms:int
    var total_hints:int
    var wgo_required:int
    var hgo_required:int

    # Chart[fumen] body
    var wish:Array[WishGroup]
    var hint:Array[Hint]

    # Traits
    # Camera Args will be adjustable at runtime, and so is panel texts.
    var special_hint:int
    var dts_layer1:Array[DeltaNode]
    var dts_layer2:Array[DeltaNode]
    var index:Array[Arf2Index]
```

## Arf2 JSON Output  (Encoded)

`0` represents an encoded interger, `[0]`  &  `""` represent multiple encoded intergers.

```json
{
    "init_ms": 0,
    "end_ms": 0,
    "total_hints": 0,
    "wgo_required": 0,
    "hgo_required": 0,
    "wish": [
        [
            0,
            [0],
            [
                [0, ""]
            ]
        ]
    ],
    "hint": [0],
    "special_hint": 0,
    "dts_layer1": [0],
    "dts_layer2": [0],
    "index": [
        [
            [0],
            [0]
        ]
    ]
}
```

## Runtime Variables

```cpp
// API
Arf2 Arf;
float xscale;
float yscale;
float xdelta;
float ydelta;
float rotdeg;

// Internal
// Maps & Pointers Omitted
int special_hint;
int dt_progress;
int dt_layer1;
int dt_layer2;

// Cache
extern float SIN[901];
extern float ECOS[901];
extern float ESIN[1001];
extern float ECOS[1001];
extern float SQRT[1001];
extern double RCP[8192];
```

## Tools

### JSON  ->  *.arf  Converter

1. Get the `export.json` from `Arf`,  and then Put it into your working directory.

2. Gather files below:
   
   - `Arf2.py`  (In `FlatBuffers-Gemerated` volume)
   
   - `Arf2Index.py` (In `FlatBuffers-Gemerated` volume)
   
   - `WishChild.py` (In `FlatBuffers-Gemerated` volume)
   
   - `WishGroup.py` (In `FlatBuffers-Gemerated` volume)
   
   - `ConvertToArf2.py`

3. Open a Terminal and Run `python ConvertToArf2.py export.json` in your working directory.
