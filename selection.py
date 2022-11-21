import random
def selection(fit):
    fit_index=0
    total_fit=sum(fit)
    pick=random.random()
    fit_p=[]
    for i in range(0,len(fit)):
        fit_p.append((fit[i]/total_fit))
    fit_acc=0
    for i in range(0,len(fit)):
        fit_acc+=fit_p[i]
        if fit_acc>=pick:
            fit_index=i
            break
    return fit_index