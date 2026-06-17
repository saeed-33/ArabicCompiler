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
	movabsq	$.Lstr, %rcx
	movabsq	$puts, %rsi
	callq	*%rsi
	movabsq	$.Lstr.1, %rcx
	callq	*%rsi
	movabsq	$.L.str_2, %rcx
	movabsq	$printf, %rax
	movl	$26, %edx
	callq	*%rax
	xorl	%eax, %eax
	addq	$32, %rsp
	popq	%rsi
	retq

	.section	.rdata,"dr"
.L.str_2:
	.asciz	"%d\n"

.Lstr:
	.asciz	"\330\243\331\207\331\204\330\247 \330\250\331\203 \331\201\331\212 \331\204\330\272\330\252\331\203 \330\247\331\204\330\271\330\261\330\250\331\212\330\251\330\247\331\204\330\256\330\247\330\265\330\251"

.Lstr.1:
	.asciz	"\330\271\331\205\330\261\331\203 \330\247\331\204\330\271\330\247\331\205 \330\247\331\204\331\202\330\247\330\257\331\205 \330\263\331\212\331\203\331\210\331\206"

