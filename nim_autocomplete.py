import sublime_plugin

PROCS = [("echo\tautoComp", "echo ${1:arg}"), ("echo_string\tautoComp", "echo \"${1:arg}\""), ("echo_file_gen_ok\tautoComp", "echo(\"*** ... File: \$# ... Generated Ok ... ***\" % ${1:file_name_path})"), ("stdout_write\tautoComp", "stdout.write(${1:arg})"), ("stdout_write_space\tautoComp", "stdout.write(${1:arg} & \" \")"), ("stdout_write_string\tautoComp", "stdout.write(\"${1:arg}\")"), ("stdout_flush_file\tautoComp", "stdout.flushFile()"), ("stderr_write_line\tautoComp", "stderr.writeLine(${1:str})"), ("proc\tautoComp", "proc ${1:name}(${2:arg}) = ${3:exp}"), ("proc_return\tautoComp", "proc ${1:name}(${2:arg}): ${3:returns} = ${4:exp}"), ("proc_block\tautoComp", "proc ${1:name}(${2:arg}) =\n\t${3:exp}"), ("proc_return_block\tautoComp", "proc ${1:name}(${2:arg}): ${3:returns} =\n\t${4:exp}"), ("proc_generic\tautoComp", "proc ${1:name}[${2:T}](${3:arg}): ${2:T} =\n\t${4:exp}"), ("iterator\tautoComp", "iterator ${1:name}(${2:arg}): ${3:returns} =\n\t${4:exp}"), ("for_iter\tautoComp", "for ${1:x} in ${2:iter}: ${3:exp}"), ("for_iter_block\tautoComp", "for ${1:x} in ${2:iter}:\n\t${3:exp}"), ("for_range\tautoComp", "for ${1:i} in ${2:0} .. ${3:int}: ${4:exp}"), ("for_range_block\tautoComp", "for ${1:i} in ${2:0} .. ${3:int}:\n\t${4:exp}"), ("for_low_high\tautoComp", "for ${1:i} in ${2:iter}.low() .. ${2:iter}.high(): ${3:exp}"), ("for_low_high_block\tautoComp", "for ${1:i} in ${2:iter}.low() .. ${2:iter}.high():\n\t${3:exp}"), ("for_countup\tautoComp", "for ${1:i} in countup(${2:start}, ${3:end}): ${4:exp}"), ("for_countup_block\tautoComp", "for ${1:i} in countup(${2:start}, ${3:end}):\n\t${4:exp}"), ("for_countup_step\tautoComp", "for ${1:i} in countup(${2:start}, ${3:end}, ${4:step}): ${5:exp}"), ("for_countup_step_block\tautoComp", "for ${1:i} in countup(${2:start}, ${3:end}, ${4:step}):\n\t${5:exp}"), ("for_countdown\tautoComp", "for ${1:i} in countdown(${2:start}, ${3:end}): ${4:exp}"), ("for_countdown_block\tautoComp", "for ${1:i} in countdown(${2:start}, ${3:end}):\n\t${4:exp}"), ("for_countdown_step\tautoComp", "for ${1:i} in countdown(${2:start}, ${3:end}, ${4:step_positive}): ${5:exp}"), ("for_countdown_step_block\tautoComp", "for ${1:i} in countdown(${2:start}, ${3:end}, ${4:step_positive}):\n\t${5:exp}"), ("for_kv\tautoComp", "for ${1:k}, ${2:v} in ${3:iter}: ${4:exp}"), ("for_kv_block\tautoComp", "for ${1:k}, ${2:v} in ${3:iter}:\n\t${4:exp}"), ("for_lines\tautoComp", "for line in lines(\"${1:file_name_path}\"): ${2:exp}"), ("for_lines_block\tautoComp", "for line in lines(\"${1:file_name_path}\"):\n\t${2:exp}"), ("for_walk_dir_block\tautoComp", "for ${1:kind}, ${2:path} in walkDir(${3:str_dir_path}):\n\t${4:exp}"), ("for_cmd_params_block\tautoComp", "for ${1:pa} in commandLineParams():\n\t${2:exp}"), ("param_count\tautoComp", "paramCount()"), ("param_str\tautoComp", "paramStr(${1:index})"), ("marshal_store\tautoComp", "store(${1:stream_writeable}, ${2:data})"), ("marshal_load\tautoComp", "load(${1:stream_readable}, ${2:varType})"), ("is_nil\tautoComp", "isNil(${1:arg})"), ("var_args\tautoComp", "varargs[${1:type}]"), ("if\tautoComp", "if ${1:test}: ${2:exp}"), ("if_else\tautoComp", "if ${1:test}: ${2:exp_true} else: ${3:exp_false}"), ("if_elif\tautoComp", "if ${1:test}: ${2:exp_true} elif ${3:test_elif}: ${4:exp_elif} else: ${5:exp_false}"), ("if_block\tautoComp", "if ${1:test}:\n\t${2:exp}"), ("if_else_block\tautoComp", "if ${1:test}:\n\t${2:exp_true}\nelse:\n\t${3:exp_false}"), ("if_elif_block\tautoComp", "if ${1:test}:\n\t${2:exp_true}\nelif ${3:test_elif}:\n\t${4:exp_elif}\nelse:\n\t${5:exp_false}"), ("case_block\tautoComp", "case ${1:exp}\n\tof ${2:test_1}: ${3:exp_1}\n\tof ${4:test_2}: ${5:exp_2}"), ("case_else_block\tautoComp", "case ${1:exp}\n\tof ${2:test_1}: ${3:exp_1}\n\tof ${4:test_2}: ${5:exp_2}\n\telse: ${6:discard}"), ("while_block\tautoComp", "while ${1:test}:\n\t${2:exp}"), ("kv\tautoComp", "\"${1:key}\": ${2:value},"), ("kv_n\tautoComp", "\"${1:key}\": ${2:value},\n${3:}"), ("type_declaration\tautoComp", "type\n\t${1:Name} = ${2:object}\n\t\t${3:field}: ${4:type}"), ("type_declaration_object\tautoComp", "type\n\t${1:Name} = object\n\t\t${2:field}: ${3:type}"), ("type_declaration_object_ref\tautoComp", "type\n\t${1:Name} = ref object\n\t\t${2:field}: ${3:type}"), ("type_declaration_tuple\tautoComp", "type\n\t${1:Name} = tuple\n\t\t${2:field}: ${3:type}"), ("type_object_creation\tautoComp", "${1:NameType}(${2:field_1}: ${3:val_1}, ${4:field_2}: ${5:val_2})"), ("type_tuple_creation\tautoComp", "${1:variable}: ${2:NameType} = (${3:field_1}: ${4:val_1}, ${5:field_2}: ${6:val_2})"), ("type_declaration_enum\tautoComp", "type\n\t${1:Name} = enum\n\t\t${2:aLabel}, ${3:bLabel}"), ("type_declaration_enum_short\tautoComp", "type ${1:Name} = enum ${2:aLabel}, ${3:bLabel}"), ("tuple_declaration_without_fields\tautoComp", "(${1:type_1}, ${2:type_2})"), ("tuple_declaration_with_fields\tautoComp", "tuple[${1:field_1}: ${2:type_1}, ${3:field_2}: ${4:type_2}]"), ("tuple_assignment\tautoComp", "(${1:val_1}, ${2:val_2})"), ("tuple_assignment_with_fields\tautoComp", "(${1:field_1}: ${2:type_1}, ${3:field_2}: ${4:type_2})"), ("array_declaration\tautoComp", "${1:name}: array[${2:len}, ${3:type}]"), ("seq_declaration\tautoComp", "${1:name}: seq[${2:type}]"), ("seq_assignment\tautoComp", "${1:name} = @[${2:}]"), ("seq_newSeq_returns_seq\tautoComp", "${1:declared_var}.newSeq ${2:len_elements}"), ("seq_newSeq_decl_plus_assignment\tautoComp", "newSeq[${1:type}] ${2:len_elements}"), ("with\tautoComp", "with(${1:arg}, ${2:call1}, ${3:call2})"), ("with_block\tautoComp", "with ${1:arg}:\n\t${2:call1}\n\t${3:call2}"), ("with_add_block\tautoComp", "with ${1:arg}:\n\tadd ${2:exp1}\n\tadd ${3:exp2}"), ("code_block\tautoComp", "block ${1:label}:\n\t${2:exp}"), ("swap\tautoComp", "${1:item_a}.swap ${2:item_b}"), ("static_exec\tautoComp", "staticExec(\"${1:command}\")"), ("static_exec_full\tautoComp", "${1:const} ${2:str} = staticExec \"${3:command}\""), ("exec_cmd_ex\tautoComp", "execCmdEx(\"${1:command}\")"), ("exec_cmd_ex_full\tautoComp", "${1:var} (${2:output}, ${3:code}) = execCmdEx \"${4:command}\""), ("assert\tautoComp", "assert(${1:bool_test}, \"${2:message}\")"), ("converter\tautoComp", "converter ${1:name}(${2:arg}): ${3:type} = ${4:exp}"), ("quit\tautoComp", "quit(\"${1:arg}\")"), ("str_find\tautoComp", "${1:r}find(${2:sub_str_char_charset})"), ("str_find_start\tautoComp", "${1:r}find(${2:sub_str_char_charset}, ${3:start})"), ("str_find_start_last\tautoComp", "${1:r}find(${2:sub_str_char_charset}, ${3:start}, ${4:last})"), ("str_is_empty_or_whitespace\tautoComp", "isEmptyOrWhitespace()"), ("str_replace\tautoComp", "replace(${1:from}, ${2:to})"), ("str_fmt\tautoComp", "fmt\"{${1:x}}\""), ("str_fmt_2\tautoComp", "fmt\"{${1:x}} ... {${2:y}}\""), ("str_fmt_equal\tautoComp", "fmt\"{${1:x} = }\""), ("str_fmt_equal_2\tautoComp", "fmt\"{${1:x} = } ... {${2:y} = }\""), ("str_format\tautoComp", "\"\$#${1:}\".format(${2:arg})"), ("str_format_2\tautoComp", "\"\$# ... \$#\".format(${1:arg1}, ${2:arg2})"), ("str_quote_raw\tautoComp", "r\"${1:str}\""), ("str_quote_triple\tautoComp", "\"\"\"${1:str}\"\"\""), ("str_quote_triple_block\tautoComp", "\"\"\"\n${1:str}\n\"\"\""), ("seq_filter\tautoComp", "${1:arr_seq}.filter(${2:x} => ${3:exp_bool})"), ("seq_filter_it\tautoComp", "${1:arr_seq}.filterIt(${2:it}${3:exp_bool})"), ("seq_map\tautoComp", "${1:arr_seq}.map(${2:x} => ${3:exp})"), ("seq_apply\tautoComp", "${1:arr_seq_VAR}.apply(${2:x} => ${3:exp})"), ("macro_block\tautoComp", "macro ${1:name}(${2:arg}) =\n\t${3:exp}"), ("macro_return_block\tautoComp", "macro ${1:name}(${2:arg}): ${3:untyped} =\n\t${4:exp}"), ("static_block\tautoComp", "static:\n\t${1:exp}"), ("echo_static\tautoComp", "static: echo \"${1:exp}\""), ("echo_stars\tautoComp", "echo \"*********************\""), ("echo_stars_static\tautoComp", "static: echo \"*********************\""), ("echo_stars_sandwitch\tautoComp", "echo \"*********************\"\necho ${1:exp}\necho \"*********************\""), ("tbl_init_table\tautoComp", "initTable[${1:key_type}, ${2:val_type}]()"), ("tbl_init_ordered_table\tautoComp", "initOrderedTable[${1:key_type}, ${2:val_type}]()"), ("tbl_get_or_default\tautoComp", "getOrDefault(${1:key}, ${2:val_default})"), ("proc_anon_std\tautoComp", "proc (${1:x}: ${2:type}): ${3:returns} = ${4:exp}"), ("proc_anon_std_sugar\tautoComp", "(${1:x}: ${2:type}) -> ${3:returns} => ${4:exp}"), ("proc_anon_short_sugar\tautoComp", "(${1:x}) => ${2:exp}"), ("json_parse_file\tautoComp", "parseFile ${1:file_name}"), ("json_to\tautoComp", "${1:jsn}.to ${2:type}"), ("json_get_str\tautoComp", "${1:jsn}[\"${2:key}\"].getStr"), ("json_get_int\tautoComp", "${1:jsn}[\"${2:key}\"].getInt"), ("json_get_biggest_int\tautoComp", "${1:jsn}[\"${2:key}\"].getBiggestInt"), ("json_get_float\tautoComp", "${1:jsn}[\"${2:key}\"].getFloat"), ("json_get_bool\tautoComp", "${1:jsn}[\"${2:key}\"].getBool"), ("json_get_array_elems\tautoComp", "${1:jsn}[\"${2:key}\"].getElems"), ("json_get_fields\tautoComp", "${1:jsn}[\"${2:key}\"].getFields"), ("import\tautoComp", "import ${1:module}"), ("import_multiple\tautoComp", "import ${1:path}/[${2:module_1}, ${3:module_2}]"), ("import_multiple_block\tautoComp", "import ${1:path}/[\n\t${2:module_1}, ${3:module_2}\n]"), ("import_block\tautoComp", "import\n\t${1:module}"), ("comment\tautoComp", "#[ ${1:comment} ]#"), ("comment_block\tautoComp", "#[\n\t${1:comment}\n]#"), ("comment_header\tautoComp", "#[****************************** BEGIN ... ${1:header} ... BEGIN ******************************]#"), ("comment_footer\tautoComp", "#[****************************** END ... ${1:footer} ... END ******************************]#"), ("comment_header_footer\tautoComp", "#[****************************** BEGIN ... ${1:section_title} ... BEGIN ******************************]#\n\n${2:code}\n\n#[****************************** END ... ${1:section_title} ... END ******************************]#"), ("comment_partition_short\tautoComp", "#******************************"), ("comment_partition_long\tautoComp", "#******************************************************************************************"), ("var_declaration\tautoComp", "var ${1:name}: ${2:type}"), ("var_assignment\tautoComp", "var ${1:name} = ${2:exp}"), ("var_block\tautoComp", "var\n\t${1:name}"), ("let_assignment\tautoComp", "let ${1:name} = ${2:exp}"), ("let_block\tautoComp", "let\n\t${1:name}"), ("const_assignment\tautoComp", "const ${1:name} = ${2:value}"), ("const_block\tautoComp", "const\n\t${1:name}"), ("file_write\tautoComp", "writeFile(\"${1:file_name_path}\", ${2:str})"), ("file_read\tautoComp", "readFile(\"${1:file_name_path}\")"), ("file_stream\tautoComp", "newFileStream(\"${1:file_name_path}\"${2:, fmWrite})"), ("file_read_line_bool\tautoComp", "readLine(${1:file}, ${2:varLine})"), ("file_read_line_string\tautoComp", "readLine()"), ("file_read_line_stdin\tautoComp", "stdin.readLine()"), ("template\tautoComp", "template ${1:name}(${2:arg}): ${3:type} = ${4:exp}"), ("template_block\tautoComp", "template ${1:name}(${2:arg}): ${3:type} =\n\t${4:exp}"), ("exception_try_except\tautoComp", "(try: ${1:exp_try} except: ${2:exp_exc})"), ("exception_try_except_block\tautoComp", "try:\n\t${1:exp_try}\nexcept ${2:excpt_type} as e:\n\t${3:exp_exc}"), ("exception_try_except_finally\tautoComp", "try:\n\t${1:exp_try}\nexcept ${2:excpt_type} as e:\n\t${3:exp_exc}\nfinally:\n\t${4:exp_fnl}"), ("exception_get_current_exception\tautoComp", "getCurrentException()"), ("exception_get_current_exception_msg\tautoComp", "getCurrentExceptionMsg()"), ("exception_raise\tautoComp", "raise newException(${1:excpt_type}, \"${2:msg}\")"), ("exception_defer\tautoComp", "defer: ${1:exp}"), ("exception_defer\tautoComp", "defer:\n\t${1:exp}")]

class NimAutoComplete(sublime_plugin.EventListener):

  def on_query_completions(self, view, prefix, locations):
    return PROCS if view.match_selector(locations[0], 'source.nim - string - comment') else None

# Copyright (c) 2021 civAnimal ... Email: civanimal@gmail.com ... Twitter: civAnimal
# Released under ... MIT License