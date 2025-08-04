// دالة التكامل
function f(x) {
    return x * x;  // مثلا نكامل x^2
}

// التكامل بالتقريب بطريقة المستطيلات
function integrate(a, b, n) {
    const dx = (b - a) / n;  // عرض المستطيل
    let area = 0;

    for (let i = 0; i < n; i++) {
        let x = a + i * dx;
        area += f(x) * dx;  // مساحة المستطيل = f(x) * dx
    }

    return area;
}

// مثال الاستخدام
const result = integrate(0, 3, 1000);  // تكامل x^2 من 0 إلى 3
console.log("قيمة التكامل التقريبية:", result);
