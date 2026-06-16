; ModuleID = "arabic_compiler_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

define i32 @"main"()
{
entry:
  %"عداد" = alloca i32
  store i32 3, i32* %"عداد"
  br label %"while_cond"
while_cond:
  %"عداد_val" = load i32, i32* %"عداد"
  %"Gttemp" = icmp sgt i32 %"عداد_val", 0
  br i1 %"Gttemp", label %"while_body", label %"while_end"
while_body:
  %"عداد_val.1" = load i32, i32* %"عداد"
  %"subtmp" = sub i32 %"عداد_val.1", 1
  store i32 %"subtmp", i32* %"عداد"
  %"عداد_val.2" = load i32, i32* %"عداد"
  %"Eqtemp" = icmp eq i32 %"عداد_val.2", 1
  br i1 %"Eqtemp", label %"then", label %"ifcont"
while_end:
  ret i32 0
then:
  br label %"while_end"
ifcont:
  br label %"while_cond"
}

declare i32 @"printf"(i8* %".1", ...)
