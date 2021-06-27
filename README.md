## Nim Auto-Complete for Sublime Text

This auto-complete plugin contains __150+__ snippets for Nim programming language. Most snippets are available as _One-Liners_. However, some snippets do have _Block-Form_ variant/s available as well. You could pick the one that best meets your requirement. Completion tags have been set up with consistency and ease-of-use in mind. This feather-weight plugin has no external dependencies. You don't need a resource-intensive server to use this plugin.


### One-Liner Examples

 Text Entered  |  Result
-------------- | -------------------------------------------------
 `pro`         | `proc name(arg) = exp`
 `vrd`         | `var name: type`
 `let`         | `let name = exp`
 `ife`         | `if test: exp_true else: exp_false`
 `sqd`         | `name: seq[type]`
 `strf`        | `rfind(sub_str_char_charset)`
 `strfl`       | `rfind(sub_str_char_charset, start, last)`
 `fori`        | `for x in iter: exp`
 `forlh`       | `for i in iter.low() .. iter.high(): exp`
 `ens`         | `type Name = enum aLabel, bLabel`
 `swa`         | `item_a.swap item_b`
 `conv`        | `converter name(arg): type = exp`
 `asr`         | `assert(bool_test, "message")`
 `seqf`        | `arr_seq.filter(x => exp_bool)`
 `tbli`        | `initTable[key_type, val_type]()`
 `proas`       | `(x: type) -> returns => exp`
 `jsgf`        | `jsn["key"].getFloat`
 `imm`         | `import path/[module_1, module_2]`
 `com`         | `#[ comment ]#`


### Block-Form Examples

`itra`
```nim
iterator name(arg): returns =
  exp
```

`forcsb`
```nim
for i in countup(start, end, step):
  exp
```

`forw`
```nim
for kind, path in walkDir(str_dir_path):
  exp
```

`ifeb`
```nim
if test:
  exp_true
else:
  exp_false
```

`tyor`
```nim
type
  Name = ref object
    field: type
```

`wib`
```nim
with arg:
  call1
  call2
```

`extb`
```nim
try:
  exp_try
except excpt_type as e:
  exp_exc
```

### Tips

* You need to type only a few letters of a procedure's name. Observe the patterns used in examples.
* In the Auto-Complete popup, you'll come across several entries with embedded `_` character. Please note that the `_` character has been added only for better readability. You don't need to type this character.
* All _Block-Form_ tags have a `block` suffix attached. It is intended to help you identify which items have _Block-Form_ variant available.
* If you accidentally invoke an undesirable completion, performing a simple Undo `ctrl + z` might be a better fix, rather than manually deleting the unwanted bits.


### Installation

* Download the plugin (or clone this repository).
* After extraction, copy `nim_autocomplete` folder to Sublime Text's _Packages_ folder.
* You can locate this folder from Sublime Text by using the menu command: _Preferences_ → _Browse Packages_.
* You could start using this plugin straight away; no restart required.


### Notes

* The data is based upon Nim 1.4.2.
* This plugin is released under ... MIT License.


### Feedback & Comments

* Email:     civanimal@gmail.com
* Twitter:  `civAnimal`


Copyright © 2021 civAnimal
