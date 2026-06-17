; ModuleID = "arabic_compiler_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare void @"panic_div_zero"()

define i32 @"main"()
{
entry:
  %"س" = alloca i32
  store i32 10, i32* %"س"
  %"ص" = alloca i32
  store i32 0, i32* %"ص"
  %"النتيجة" = alloca i32
  %"س_val" = load i32, i32* %"س"
  %"ص_val" = load i32, i32* %"ص"
  %"is_zero_trap" = icmp eq i32 %"ص_val", 0
  br i1 %"is_zero_trap", label %"panic_block", label %"math_block"
panic_block:
  call void @"panic_div_zero"()
  unreachable
math_block:
  %"divtmp" = sdiv i32 %"س_val", %"ص_val"
  store i32 %"divtmp", i32* %"النتيجة"
  %"str_ptr" = getelementptr inbounds [56 x i8], [56 x i8]* @".str_0", i32 0, i32 0
  %"print_call" = call i32 (i8*, ...) @"printf"(i8* %"str_ptr")
  ret i32 0
}

@".str_0" = private constant [56 x i8] c"\d9\84\d9\86 \d9\8a\d8\aa\d9\85 \d8\b7\d8\a8\d8\a7\d8\b9\d8\a9 \d9\87\d8\b0\d9\87 \d8\a7\d9\84\d8\ac\d9\85\d9\84\d8\a9 \d8\a3\d8\a8\d8\af\d9\8b\d8\a7!\0a\00"