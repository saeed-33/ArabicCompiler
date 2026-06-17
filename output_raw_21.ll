; ModuleID = "arabic_compiler_module"
target triple = "x86_64-pc-windows-msvc"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare void @"panic_div_zero"()

define i32 @"main"()
{
entry:
  %"س" = alloca i32
  store i32 5, i32* %"س"
  %"ص" = alloca i32
  store i32 10, i32* %"ص"
  %"ع" = alloca i32
  %"س_val" = load i32, i32* %"س"
  %"ص_val" = load i32, i32* %"ص"
  %"addtmp" = add i32 %"س_val", %"ص_val"
  store i32 %"addtmp", i32* %"ع"
  %"مجهول" = alloca i32
  store i32 999, i32* %"مجهول"
  %"النتيجة" = alloca i32
  %"ص_val.1" = load i32, i32* %"ص"
  %"is_zero_trap" = icmp eq i32 %"ص_val.1", 0
  br i1 %"is_zero_trap", label %"panic_block", label %"math_block"
panic_block:
  call void @"panic_div_zero"()
  unreachable
math_block:
  %"divtmp" = sdiv i32 100, %"ص_val.1"
  store i32 %"divtmp", i32* %"النتيجة"
  %"str_ptr" = getelementptr inbounds [4 x i8], [4 x i8]* @".str_0", i32 0, i32 0
  %"ع_val" = load i32, i32* %"ع"
  %"print_call" = call i32 (i8*, ...) @"printf"(i8* %"str_ptr", i32 %"ع_val")
  %"str_ptr.1" = getelementptr inbounds [4 x i8], [4 x i8]* @".str_1", i32 0, i32 0
  %"النتيجة_val" = load i32, i32* %"النتيجة"
  %"print_call.1" = call i32 (i8*, ...) @"printf"(i8* %"str_ptr.1", i32 %"النتيجة_val")
  ret i32 0
}

@".str_0" = private constant [4 x i8] c"%d\0a\00"
@".str_1" = private constant [4 x i8] c"%d\0a\00"