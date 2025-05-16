from django.shortcuts import render,redirect
from django.views import View
from app1.forms import *
from decimal import Decimal

class home(View):
    def get(self,request):
        return render(request,'home.html')



class bank(View):
    def get(self,request):
        form=Bankform()
        return render(request,'bank.html',{'form':form})
    
    def post(self,request):
        form=Bankform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request,'bank.html',{'form':form})



                



class dep(View):

    def get(self, request):
        form = acc_pass()
        return render(request, 'dep.html', {'form': form})
    
    def post(self, request):
        form = acc_pass(request.POST)
        if form.is_valid():
            acc = request.POST.get('acc')
            password = request.POST.get('password')
            user = ATM.objects.filter(acc=acc, password=password).first()
            if user:
                request.session['acc'] = user.acc
                request.session['name'] = user.name

                return redirect('deposit')
            else:
                form.add_error(None, "Invalid acc_no or password.")
        return render(request, 'dep.html', {'form': form})


class deposit(View):

    def get(self, request):
        form = amount()
        acc = request.session.get('acc')
        name = request.session.get('name')

        if not acc or not name:
            return render(request, 'dep.html', {'form': acc_pass()})

        return render(request, 'deposit.html', {
            'form': form,
            'acc': acc,
            'name': name
        })
    
    def post(self, request):
        form = amount(request.POST)
        acc = request.session.get('acc')
        name = request.session.get('name')

        if not acc or not name:
            return render(request, 'dep.html', {'form': acc_pass()})

        if form.is_valid():
            amount_val = form.cleaned_data['amount']
            user = ATM.objects.filter(acc=acc).first()
            
            if user:
                amount_val = Decimal(amount_val)

                user.balance += amount_val
                user.save()
                
                res = 'Deposit successfully'

                return render(request, 'deposit.html', {
                    'amount': amount_val,
                    'res': res,
                    'acc': acc,
                    'name': user.name,
                    'form': amount()
                })
            else:
                form.add_error(None, "Account not found.")
        
        return render(request, 'deposit.html', {
            'form': form,
            'acc': acc,
            'name': name
        })


class wdr(View):
    def get(self, request):
        form = acc_pass()
        return render(request, 'dep.html', {'form': form})
    
    def post(self, request):
        form = acc_pass(request.POST)
        if form.is_valid():
            acc = request.POST.get('acc')
            password = request.POST.get('password')
            user = ATM.objects.filter(acc=acc, password=password).first()
            if user:
                request.session['acc'] = user.acc
                request.session['name'] = user.name

                return redirect('withdrawal')
            else:
                form.add_error(None, "Invalid acc_no or password.")
        return render(request, 'dep.html', {'form': form})



class withdrawal(View):

    def get(self, request):
        form = amount()
        acc = request.session.get('acc')
        name = request.session.get('name')

        if not acc or not name:
            return render(request, 'dep.html', {'form': acc_pass()})

        return render(request, 'withdrawal.html', {
            'form': form,
            'acc': acc,
            'name': name
        })

    def post(self, request):
        form = amount(request.POST)
        acc = request.session.get('acc')
        name = request.session.get('name')

        if not acc or not name:
            return render(request, 'dep.html', {'form': acc_pass()})

        if form.is_valid():
            amount_val = form.cleaned_data['amount']
            user = ATM.objects.filter(acc=acc).first()
            
            if user:
                amount_val = Decimal(amount_val)

                user.balance -=amount_val
                user.save()
                
                res = 'Withdrawal successfully'

                return render(request, 'withdrawal.html', {
                    'amount': amount_val,
                    'res': res,
                    'acc': acc,
                    'name': user.name,
                    'form': amount()
                })
            else:
                form.add_error(None, "Account not found.")
        
        return render(request, 'withdrawal.html', {
            'form': form,
            'acc': acc,
            'name': name
        })


class balance(View):
    def get(self, request):
        form = acc_pass()
        return render(request, 'blnc.html', {'form': form})

    def post(self, request):
        form = acc_pass(request.POST)

        if form.is_valid():
            acc = request.POST.get('acc')
            password = request.POST.get('password')
            user = ATM.objects.filter(acc=acc, password=password).first()

            if user:
                acc = user.acc
                name = user.name
                balance = user.balance
                return render(request, 'blnc.html', {
                    'form': form,
                    'acc': acc,
                    'name': name,
                    'balance': balance
                })
            else:
                form.add_error(None, "Invalid account number or password.")

        return render(request, 'blnc.html', {'form': form})


class change_pin(View):
    def get(self,request):
        form=acc_pass()
        return render(request,'dep.html',{'form':form})

    
    def post(self,request):
        form=acc_pass(request.POST)
        if form.is_valid():
            acc=request.POST.get('acc')
            password=request.POST.get('password')
            user=ATM.objects.filter(acc=acc,password=password).first()
            if user:
                request.session['acc'] = acc
                request.session['name'] = user.name 
                return redirect('new_pin')
            else:
                return redirect('home')
        
        return render(request,'dep.html',{'form':form})
    


class new_pin(View):
    def get(self,request):
        form=pin_form()
        name=request.session.get('name')
        acc=request.session.get('acc')
        if not acc or not name:
            return render(request,'cng_pin.html',{'form':acc_pass})
        
        return render(request,'new_pin.html',{'acc':acc,'name':name,'form':form})
    
    def post(self,request):
        form=pin_form(request.POST)
        if form.is_valid():
            new_password=form.cleaned_data.get('new_password')
            name=request.session.get('name')
            acc=request.session.get('acc')
            if not acc or not name:
                return render(request,'cng_pin.html',{'form':form})
            
            if not new_password:
                form.add_error('new_password','This field should not empty')
                return render(request, 'new_pin.html', {
                    'form': form,
                    'acc': acc,
                    'name': name
                })
            
            user=ATM.objects.filter(acc=acc).first()
            if user:
                user.password=new_password
                user.save()
                res='Password Change Successfully'
                return render(request,'new_pin.html',{'acc':acc,'name':name,'form':pin_form,'res':res})

        return render(request,'new_pin.html',{'form':form})