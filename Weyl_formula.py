#calculates the weyl formula for number of size of total CI expansion

'''
@author = npokhrel
'''

#arguments are
#N_elect = number of electrons
#n_orbital = number of orbitals
#N_spin = spin(s) 0 for singlet 1 for triplet


from math import factorial
def compute_binomial(x,y):
    binomial = (factorial(x))/((factorial(y)*(factorial(x-y))))
    return int(binomial)

def compute_weyl(N_elect, n_orbital, N_spin):
    comb1 = compute_binomial(n_orbital+1,N_elect/2-N_spin)
    comb2 = compute_binomial(n_orbital+1, N_elect/2+N_spin+1)
    N_Cas = (2*N_spin+1)/(n_orbital+1) * comb1 * comb2
    return ("The output with " + str(N_elect) + " electrons and "+ str(n_orbital) +  
            " orbitals and spin " +str(N_spin) +    " is " + str(N_Cas)   )


print(compute_weyl(2,2,0))
print(compute_weyl(2,2,1))

print(compute_weyl(4,3,0))
print(compute_weyl(4,3,1))

print(compute_weyl(6,4,0))
print(compute_weyl(6,4,1))
#print(compute_binomial(4,1))
#print(compute_binomial(4,2))
#print(compute_binomial(4,3))
#print(compute_binomial(4,4))




