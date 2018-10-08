from math import exp

h = 1./1000
a = -1./2

apprx = [0] * 1000
error = [0] * 1000

apprx[0] = exp(0)
apprx[1] = exp(h*a)
apprx[2] = exp(2*h*a)

exact = apprx

for n in range(0,1000):
    
    if n > 2:
        apprx[n] = apprx[n-1] + h*a*(23*apprx[n-1]/12 - 4*apprx[n-2]/3 + 5*apprx[n-3]/12)    
    
    exact[n] = exp(n*h*a)
    error[n] = apprx[n] - exact[n]
    
    print "Approx = %1.10f, Exact = %1.10f" % (approx[n], exact[n]) 
    print "Error = %1.10f" % error[n]