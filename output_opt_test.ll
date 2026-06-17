; ModuleID = '<string>'
source_filename = "<string>"
target triple = "x86_64-pc-windows-msvc"

@.str_0 = private constant [4 x i8] c"%d\0A\00"
@.str_1 = private constant [4 x i8] c"%d\0A\00"

; Function Attrs: nofree nounwind
declare noundef i32 @printf(ptr nocapture noundef readonly, ...) local_unnamed_addr #0

; Function Attrs: nofree nounwind
define noundef i32 @main() local_unnamed_addr #0 {
entry:
  %print_call = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str_0, i32 15)
  %print_call.1 = tail call i32 (ptr, ...) @printf(ptr nonnull dereferenceable(1) @.str_1, i32 10)
  ret i32 0
}

attributes #0 = { nofree nounwind }
