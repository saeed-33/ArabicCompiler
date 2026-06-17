	.def	@feat.00;
	.scl	3;
	.type	0;
	.endef
	.globl	@feat.00
.set @feat.00, 0
	.file	"<string>"
	.def	main;
	.scl	2;
	.type	32;
	.endef
	.text
	.globl	main
	.p2align	4
main:
	pushq	%rsi
	subq	$32, %rsp
	movabsq	$.L.str_0, %rcx
	movabsq	$printf, %rsi
	movl	$15, %edx
	callq	*%rsi
	movabsq	$.L.str_1, %rcx
	movl	$10, %edx
	callq	*%rsi
	xorl	%eax, %eax
	addq	$32, %rsp
	popq	%rsi
	retq

	.section	.rdata,"dr"
.L.str_0:
	.asciz	"%d\n"

.L.str_1:
	.asciz	"%d\n"

