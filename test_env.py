from semantic.symbols import VariableSymbol
from semantic.environment import Environment, SemanticError

def main():
    print("--- بدء اختبار جدول الرموز والنطاقات ---")
    
    # 1. إنشاء النطاق العام (Global Scope) [cite: 407]
    print("\n[إنشاء النطاق العام]") 
    global_env = Environment()
    
    try:
        global_env.define("س", VariableSymbol("س", "صحيح")) 
        global_env.define("مجموع", VariableSymbol("مجموع", "عشري")) 
        global_env.print_stack() 
        
        # 2. الدخول في كتلة محلية (Local Scope 1) مثل جملة "إذا" [cite: 414]
        print("\n[دخول كتلة: جملة إذا]") 
        local_env_1 = Environment(enclosing=global_env) # نمرر الأب لتوليد السلسلة [cite: 416]
        
        # ميزة التظليل (Shadowing): تعريف "س" بنوع جديد داخل النطاق المحلي (مسموح) [cite: 417]
        local_env_1.define("س", VariableSymbol("س", "نص")) 
        local_env_1.define("ص", VariableSymbol("ص", "صحيح")) 
        local_env_1.print_stack() 
        
        # اختبار البحث (يجب أن يجد "س" النصية القريبة، ويصعد ليجلب "مجموع" من الأب) [cite: 422]
        print(f"\nالبحث عن 'س' من داخل (إذا): {local_env_1.resolve('س')}") 
        print(f"البحث عن 'مجموع' من داخل (إذا): {local_env_1.resolve('مجموع')}") 
        
        # 3. محاولة تعريف متغير بنفس الاسم في نفس النطاق (ممنوع منعاً باتاً) [cite: 427]
        print("\n[محاولة تعريف 'ص' مرتين في نفس النطاق]") 
        local_env_1.define("ص", VariableSymbol("ص", "عشري")) # سيفجر خطأ دلالي [cite: 428, 429]
        
    except SemanticError as e:
        print(f"\nتم التقاط خطأ بنجاح: {e}") 
        
    # 4. محاولة استخدام متغير وهمي غير معرف [cite: 432]
    print("\n[محاولة البحث عن متغير غير معرف]") 
    try:
        local_env_1.resolve("ع") # سيفجر خطأ دلالي [cite: 435]
    except SemanticError as e:
        print(f"\nتم التقاط خطأ بنجاح: {e}") 

if __name__ == "__main__":
    main()