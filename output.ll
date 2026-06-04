; ModuleID = "arabic_compiler_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"س" = alloca i32
  store i32 5, i32* %"س"
  %"س_val" = load i32, i32* %"س"
  %"addtmp" = add i32 %"س_val", 1
  store i32 %"addtmp", i32* %"س"
  ret i32 0
}
