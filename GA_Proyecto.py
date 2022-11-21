import numpy as np
import matplotlib.pyplot as plt

from population import *
from gray2real import *
from fitness import *
from selection import *
from crossover import *
from mutation import *
from newindiv import *

def main():
    #create initial population
    n = 32    #num. of individuals
    c_len = 24 #length of chromosome
    g_len = 8  #length of genes
    bestfits_g=[]
    pop = population(n,c_len)
    sol=[]
    tolWL=0.2
    #######################################
    print("*** Genetic Algorithm ***")
    print("Population size:\t",n)
    print("Chromosome length:\t",c_len)
    tg=int(input("Number of generations:\t"))

    for _ in range(tg):
        fit=[]
        for indiv in pop:
            fit.append(fitness(gray2real(indiv)))

        fit_index=selection(fit)
        parent0=pop[fit_index]

        fit_index=selection(fit)
        parent1=pop[fit_index]

        while parent1==parent0:
            fit_index=selection(fit)
            parent1=pop[fit_index]

        offspring0,offspring1=crossover(parent0,parent1)
        offspring0,offspring1=mutation(offspring0),mutation(offspring1)

        fitp0=fitness(gray2real(parent0))
        fitp1=fitness(gray2real(parent1))
        fito0=fitness(gray2real(offspring0))
        fito1=fitness(gray2real(offspring1))

        newpop=[]
        #selection of parents/offsprings

        if fito0>=fitp0 or fito0>=fitp1:
            newpop.append(offspring0)
        if fito1>=fitp0 or fito1>=fitp1:
            newpop.append(offspring1)
        if fitp0>=fito0 and fitp0>=fito1:
            newpop.append(parent0)
        if fitp1>=fito0 and fitp1>=fito1:
            newpop.append(parent1)

        #include best individual (elitism) that fits restriction
        bestfit=max(fit)
        bestindex=fit.index(bestfit)
        bestvals=gray2real(pop[bestindex])
        ratio=bestvals[2]/bestvals[3]
        
        while abs(ratio-1)>tolWL or abs(1/ratio-1)>tolWL:
            del fit[bestindex]
            del pop[bestindex]
            bestfit=max(fit)
            bestindex=fit.index(bestfit)
            bestvals=gray2real(pop[bestindex])
            ratio=bestvals[2]/bestvals[3]
        
        newpop.append(pop[bestindex])
        sol.append(gray2real(pop[bestindex]))
        bestfits_g.append(bestfit)

        #extended elitism
        meanfit=np.mean(fit)
        stdfit=np.std(fit)

        for i in range(len(fit)):
            if fit[i]>meanfit+stdfit:
                newpop.append(pop[i])


        #fillers
        while(len(newpop)<n):
            newpop.append(newindiv(c_len))

        pop=newpop

    solution=sol[-1]
    print("\nW:\t",round(solution[0]*0.3,1),"\u03BCm")
    print("L:\t",round(solution[1]*0.3,1),"\u03BCm")
    print("m:\t",solution[2])
    print("n:\t",solution[3])
    print("R:\t",res(solution[2],solution[3])/1000,"k\u03A9")
    print("MSE: ",round(-bestfits_g[-1],6))
    plt.figure(1)
    plt.plot(-1*np.array(bestfits_g))
    plt.show()

main()