import pulp as pl

def pLinear(nvar,f_obj,rest):
    #Criar o modelo do problema
    model = pl.LpProblem("Maximize", pl.LpMaximize)

    #Definir as variáveis
    vars = []
    for i in range(nvar):
        vars.append(pl.LpVariable(chr(97+i), lowBound=0)) #add vars em ordem alfabética
    print(vars)
    
    #Adicionar função objetivo:
    print(sum(f_obj[i] * vars[i] for i in range(nvar)))
    model += sum(f_obj[i] * vars[i] for i in range(nvar))

    #Adicionar restrições
    for i in range(len(rest)):
        model += sum(rest[i][j] * vars[j] for j in range(nvar)) <= rest[i][-1]

    #Resolver
    model.solve()
    
    #Salvar ponto ótimo
    p_otimo = []
    for i in range(nvar): 
        p_otimo.append(vars[i].varValue)
    lucro_otimo = pl.value(model.objective)

    return [p_otimo, lucro_otimo]


#Testar com valores predifinidos
nvar = 3
f_obj = [5,7,8]
rest = [[1,1,2,1190],[2,4.5,1,4000]]
result = pLinear(nvar, f_obj, rest)

for vars in result[0]:
    print(vars)
print("Z = ",result[1])
