; ModuleID = "arabic_compiler_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare i32 @"printf"(i8* %".1", ...)

define i32 @"main"()
{
entry:
  %"str_ptr" = getelementptr inbounds [88 x i8], [88 x i8]* @".str_0", i32 0, i32 0
  %"print_call" = call i32 (i8*, ...) @"printf"(i8* %"str_ptr")
    ret i32 0
}

@".str_0" = private constant [88 x i8] c"\d8\a3\d9\87\d9\84\d8\a7\d9\8b \d8\a8\d9\83\d9\85 \d9\8a\d8\a7 \d9\85\d9\87\d9\86\d8\af\d8\b3\d9\8a\d9\86 \d9\81\d9\8a \d8\b9\d8\a7\d9\84\d9\85 \d8\a7\d9\84\d9\85\d8\aa\d8\b1\d8\ac\d9\85\d8\a7\d8\aa \d8\a7\d9\84\d8\ad\d9\82\d9\8a\d9\82\d9\8a!\0a\00"