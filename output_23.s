	.file	"<string>"
	.section	.ltext,"axl",@progbits
	.globl	main
	.p2align	4
	.type	main,@function
main:
	pushq	%rsi
	pushq	%rdi
	subq	$40, %rsp
.L0$pb:
	leaq	.L0$pb(%rip), %rax
	movabsq	$_GLOBAL_OFFSET_TABLE_-.L0$pb, %rsi
	addq	%rax, %rsi
	movabsq	$.L.str_0@GOTOFF, %rcx
	addq	%rsi, %rcx
	movabsq	$printf, %rdi
	movl	$15, %edx
	callq	*%rdi
	movabsq	$.L.str_1@GOTOFF, %rcx
	addq	%rsi, %rcx
	movl	$10, %edx
	callq	*%rdi
	xorl	%eax, %eax
	addq	$40, %rsp
	popq	%rdi
	popq	%rsi
	retq
.Lfunc_end0:
	.size	main, .Lfunc_end0-main

	.type	.L.str_0,@object
	.section	.lrodata,"al",@progbits
.L.str_0:
	.asciz	"%d\n"
	.size	.L.str_0, 4

	.type	.L.str_1,@object
.L.str_1:
	.asciz	"%d\n"
	.size	.L.str_1, 4

	.section	".note.GNU-stack","",@progbits
