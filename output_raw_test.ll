; ModuleID = "arabic_compiler_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

declare void @"panic_div_zero"()

define i32 @"main"()
{
entry:
  %"العمر" = alloca i32
  store i32 25, i32* %"العمر"
  %"السنة_القادمة" = alloca i32
  %"العمر_val" = load i32, i32* %"العمر"
  %"addtmp" = add i32 %"العمر_val", 1
  store i32 %"addtmp", i32* %"السنة_القادمة"
  %"str_ptr" = getelementptr inbounds [56 x i8], [56 x i8]* @".str_0", i32 0, i32 0
  %"print_call" = call i32 (i8*, ...) @"printf"(i8* %"str_ptr")
  %"str_ptr.1" = getelementptr inbounds [45 x i8], [45 x i8]* @".str_1", i32 0, i32 0
  %"print_call.1" = call i32 (i8*, ...) @"printf"(i8* %"str_ptr.1")
  %"str_ptr.2" = getelementptr inbounds [4 x i8], [4 x i8]* @".str_2", i32 0, i32 0
  %"السنة_القادمة_val" = load i32, i32* %"السنة_القادمة"
  %"print_call.2" = call i32 (i8*, ...) @"printf"(i8* %"str_ptr.2", i32 %"السنة_القادمة_val")
  ret i32 0
}

@".str_0" = private constant [56 x i8] c"\d8\a3\d9\87\d9\84\d8\a7 \d8\a8\d9\83 \d9\81\d9\8a \d9\84\d8\ba\d8\aa\d9\83 \d8\a7\d9\84\d8\b9\d8\b1\d8\a8\d9\8a\d8\a9\d8\a7\d9\84\d8\ae\d8\a7\d8\b5\d8\a9\0a\00"
@".str_1" = private constant [45 x i8] c"\d8\b9\d9\85\d8\b1\d9\83 \d8\a7\d9\84\d8\b9\d8\a7\d9\85 \d8\a7\d9\84\d9\82\d8\a7\d8\af\d9\85 \d8\b3\d9\8a\d9\83\d9\88\d9\86\0a\00"
@".str_2" = private constant [4 x i8] c"%d\0a\00"