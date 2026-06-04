from backend.ir_generator import IRGeneratorVisitor

def main():
    print("--- جاري اختبار بيئة LLVM الأساسية ---")
    
    # 1. إنشاء نسخة من مولد الـ IR الخاص بنا
    generator = IRGeneratorVisitor()
    
    # 2. نطلب منه إنهاء التوليد فوراً (بدون المرور على شجرة)
    # هذا سيختبر قدرته على بناء الـ Module، والـ Function، وكتلة الـ Entry
    llvm_ir_code = generator.finish_generation()
    
    print("\n✅ تم توليد كود LLVM IR بنجاح! إليكم نظرة خاطفة على الهيكل:")
    print("==========================================================")
    print(llvm_ir_code)
    print("==========================================================")

if __name__ == '__main__':
    main()