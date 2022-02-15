from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt

def Pay(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        amount: 50000
        currency: 'INR'
        client = razorpay.Cilent(auth=("rzp_test_4kN0SEtglJ1MFN","sa40lwM1zsrZIBCqdbtCXaYn"))
        Payment = cilent.order.create({'amount': amount , 'currency': 'INR' , 'payment_capture': '1'})
    return render(request , 'Pay.html')

@csrf_exempt
def success(request):
    return render(request, "success.html")
