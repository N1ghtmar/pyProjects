from random import randint
import os

# Aqui eu tentei copiar a mecânica de quimica de um jogo chamado Space Station 13
# Me considero ainda iniciante em python, então qualquer dica é bem vinda!

os.system('cls')
tem_Beaker = False
beaker = {"total": 0}
el = "hidrogenio oxigenio silicio fosforo enxofre carbono azoto agua nitrogenio litio açucar acido_sulfurico cobre mercurio sodio iodo bromo etanol cloro potassio aluminio radio fluor ferro combustivel prata plasma"
elem = el.split(" ")
temperatura = 273
nome = ""
arq = {}
print("pense nisso como uma máquina de refrigerante!\n")
print("para ter ajuda digite: help")
exp = False

while True:
    command = input(">> ")
    if " " in command:
        args = command.split(" ")
        if args[0] == "add":

            if args[1] == "beaker":
                if tem_Beaker == False:
                 tem_Beaker = True
                 if len(args) == 3:
                    if args[2] in arq:
                        nome = args[2]
                        beaker = arq[args[2]]
                    else:
                        nome = args[2]
                        beaker = {"total": 0}
                        arq[nome] = beaker
                else:
                    print("já tem um beaker na máquina, tire ele digitando 'quit'!")
            elif args[1] in elem:
                if tem_Beaker == False:
                    print("A máquina está vazia, adicione o beaker antes!")
                else:
                    if beaker["total"] == 100:
                        print("A vasilha está cheia")
                    else:
                        beaker[args[1]] = int(args[2])
                        beaker["total"] += int(args[2])
                        while beaker["total"] > 200:
                            beaker[args[1]] -= 1
                            beaker["total"] -= 1
            elif len(args) > 3:
                if args[3] == "yumekui":
                    beaker[args[1]] = int(args[2])
                    beaker["total"] += int(args[2])
        elif args[0] == "del":
            if tem_Beaker == False:
                print("A máquina está vazia")
            else:
                if args[1] in beaker:
                    if args[1] == "total":
                        print("Você não pode mudar isso")
                    else:
                        if beaker["total"] == 0:
                            print("A vasilha está vazia")
                        else:
                            if args[1] in beaker:
                                if float(args[2]) > beaker[args[1]]:
                                    print("você não pode excluir mais que o conteúdo que existe")
                                else:
                                    beaker[args[1]] -= float(args[2])
                                    beaker["total"] -= float(args[2])
                                
                                    if beaker[args[1]] <= 0:
                                        del beaker[args[1]]
                            else:
                                print("Não há esssa substancia na vasilha")
                if args[1] == 'all':
                    beaker = {"total": 0}
        elif args[0] == "hot":
            if tem_Beaker == False:
                print("A máquina está vazia")
            else:
                temperatura = int(args[1])
                print(f"A temperatura foi para {temperatura}K")
        elif args[0] == "help":
            if len(args) > 1:
                if args[1] == "add":
                    print("O add adiciona beaker e os elementos da máquina:")
                    print("Comece adicionando o beaker(vasilha) na maquina!")
                    print("add beaker <de uma etiqueta ao beaker, pode ser qualquer nome>")
                    print("Por exemplo: add beaker teste\n")
                    print("Agora com o beaker já na máquina, vamos adicionar elementos!")
                    print("add <elemento> <quantidade em ml>")
                    print("Por exemplo: add enxofre 30\n")
                    print("um beaker aguenta até ducentos ml\npara ver a lista de elementos adicionáveis digite: help ")
                elif args[1] == "del":
                    print("O del é usado para deletar elemntos do beaker")
                    print("Certifique-se de que o elemnto está no beaker!") 
                    print("del <elemento> <quantidade>")
                    print("Por exemplo: del enxofre 20\n")
                elif args[1] == "end":
                    print("Se você escrever end o programa se fecha ;-;\n")
                elif args[1] == "empty":
                    print("Se você errou em alguma mistura")
                    print("ou se quer começar de novo escreva 'empty' para esvaziar o beaker!\n")
                elif args[1] == "quit":
                    print("Se você quer começar de novo, \nmas não quer perder o que estava fazendo")
                    print("para isso temos o 'quit'!")
                    print("o quit guarda o beaker pra você")
                    print("e para pega-lo de novo?\n")
                    print("digite: add beaker <etiqueta que você botou no beaker>")
                    print("por exemplo: se você colocou a etiqueta 'teste' antes:\nadd beaker teste")
                elif args[1] == "hot":
                    print("Tem certas misturas que precisam de uma certa temperatura pra acontecer")
                    print("um exemplo é o formaldeido que precisa de 480K")
                    print("para usar é: hot <temperatura em Kelvin>\n")
                elif args[1] == "transfer":
                    print("Esse eu considero um comando difícil de usar")
                    print("mas pode ser muito bem aproveitado!\n")
                    print("com o transfer é usado para transferir substancias")
                    print("se você tem dois beakers e queria colocar um elemento\nque tem num para o outro, faça o seguinte:")
                    print("transfer <remetente> <elemento> <quantidade> <destinatário>")
                    print("por exemplo: transfer teste enxofre 10 teste2")
        elif args[0] == "transfer":
            if len(args) > 1:
                rem = args[1]
                if len(args) > 2:
                    ele_rem = args[2]
                    if len(args) > 3:
                        ele_rem_qua = float(args[3])
                        if len(args) > 4:
                            des = args[4]
                            if rem in arq:
                                if ele_rem in arq[rem]:
                                    if arq[rem][ele_rem] >= ele_rem_qua:
                                        if des in arq:
                                            if ele_rem in arq[des]:
                                                arq[des][ele_rem] += ele_rem_qua
                                                arq[des]["total"] += ele_rem_qua
                                            else:
                                                arq[des][ele_rem] = ele_rem_qua
                                                arq[des]["total"] += ele_rem_qua
                                            if tem_Beaker == False:
                                                arq[rem][ele_rem] -= ele_rem_qua
                                                arq[rem]["total"] -= ele_rem_qua
                                                if arq[rem]["total"] < 0:
                                                    arq[rem]["total"] = 0
                                                if arq[rem][ele_rem] <= 0:
                                                    del arq[rem][ele_rem]
                                            elif tem_Beaker ==  True:
                                                if nome == rem:
                                                    beaker[ele_rem] -= ele_rem_qua
                                                    arq[rem]["total"] -= ele_rem_qua
                                                    if arq[rem]["total"] < 0:
                                                        arq[rem]["total"] = 0
                                                    if beaker[ele_rem] <= 0:
                                                        del beaker[ele_rem]
                                                elif nome == des:
                                                    arq[rem][ele_rem] -= ele_rem_qua
                                                    arq[rem]["total"] -= ele_rem_qua
                                                    if arq[rem]["total"] < 0:
                                                        arq[rem]["total"] = 0
                                                    if arq[rem][ele_rem] <= 0:
                                                        del arq[rem][ele_rem]
                                            if rem == nome:
                                                if tem_Beaker == True:
                                                    beaker = arq[nome]
                                        else:
                                            print("não há o beaker destinatário")
                                    else:
                                        print("não há essa quantidade de elemento no beaker")
                                else:
                                    print("não há esse elemento no beaker")
                            else:
                                print("não há esse beaker guardado")
        def verify(ab, minimo, vezes=1):
            beaker[ab] -= minimo*vezes
            if beaker[ab] <= 0:
                del beaker[ab]
        def novo(res, minimo, vezes):
            if res in beaker:
                beaker[res] += minimo*vezes
            else:
                beaker[res] = minimo*vezes
            
        def mer(ab,bc,cd,res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        lista = [beaker[ab], beaker[bc], beaker[cd]]
                        minimo = min(lista)
                        novo(res, minimo, 3)
                        verify(ab, minimo)
                        verify(bc, minimo)
                        verify(cd, minimo)
        def faetem(ab, bc, tem):
            if ab in beaker:
                if temperatura >= tem:
                    novo(res, minimo, 1)
                    del beaker[ab]
        def merfae(ab, bc, res):
            if ab in beaker:
                if bc in beaker:
                    lista = [beaker[ab]/3, beaker[bc]]
                    minimo = min(lista)
                    verify(ab, minimo, 3)
                    verify(bc, minimo)
                    novo(res, minimo, 4)
        def merfaefae(ab, bc, cd, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        lista = [beaker[ab]/3, beaker[bc], beaker[cd]]
                        minimo = min(lista)
                        verify(ab, minimo, 3)
                        verify(bc, minimo)
                        verify(cd, minimo)
                        novo(res, minimo, 5)
                        
        def ted(ab, bc, cd, de, ef, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        if de in beaker:
                            if ef in beaker:
                                lista = [beaker[ab], beaker[bc], beaker[cd], beaker[de], beaker[ef]]
                                minimo = min(lista)
                                novo(res, minimo, 5)
                                verify(ab, minimo)
                                verify(bc, minimo)
                                verify(cd, minimo)
                                verify(de, minimo)
                                verify(ef, minimo)

        def jorfaefae(ab, bc, cd, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        lista = [beaker[ab]/2, beaker[bc], beaker[cd]]
                        minimo = min(lista)
                        novo(res, minimo, 4)
                        verify(ab, minimo, 2)
                        verify(bc, minimo)
                        verify(cd, minimo)
        def ted3fae(ab, bc, cd, de, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        if de in beaker:
                            lista = (beaker[ab]/5, beaker[bc], beaker[cd], beaker[de])
                            minimo = min(lista)
                            novo(res, minimo, 8)
                            verify(ab, minimo, 5)
                            verify(bc, minimo)
                            verify(cd, minimo)
                            verify(de, minimo)
        def jor3fae(ab, bc, cd, de, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        if de in beaker:
                            lista = (beaker[ab]/2, beaker[bc], beaker[cd], beaker[de])
                            minimo = min(lista)
                            novo(res, minimo, 5)
                            verify(ab, minimo, 2)
                            verify(bc, minimo)
                            verify(cd, minimo)
                            verify(de, minimo)
        def jor(ab, bc, res):
            if ab in beaker:
                if bc in beaker:
                    lista = [beaker[ab], beaker[bc]]
                    minimo = min(lista)  
                    novo(res, minimo, 2)
                    verify(ab, minimo)
                    verify(bc, minimo)
        def jormerfae(ab, bc, cd, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        lista = [beaker[ab]/2, beaker[bc]/3, beaker[cd]]
                        minimo = min(lista)
                        novo(res, minimo, 6)
                        verify(ab, minimo, 2)
                        verify(bc, minimo, 3)
                        verify(cd, minimo)
        def hiu(ab, bc, cd, de, ef, fg, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        if de in beaker:
                            if ef in beaker:
                              if fg in beaker:
                                lista = [beaker[ab], beaker[bc], beaker[cd], beaker[de], beaker[ef], beaker[fg]]
                                minimo = min(lista)
                                novo(res, minimo, 6)
                                verify(ab, minimo)
                                verify(bc, minimo)
                                verify(cd, minimo)
                                verify(de, minimo)
                                verify(ef, minimo)
                                verify(fg, minimo)
        def mer3fae(ab, bc, cd, de, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        if de in beaker:
                            if ef in beaker:
                                lista = [beaker[ab]/3, beaker[bc], beaker[cd], beaker[de]]
                                minimo = min(lista)
                                novo(res, minimo, 6)
                                verify(ab, minimo, 3)
                                verify(bc, minimo)
                                verify(cd, minimo)
                                verify(de, minimo)
        def tedfaefae(ab, bc, cd, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        lista = [beaker[ab]/5, beaker[bc], beaker[cd]]
                        minimo = min(lista)
                        novo(res, minimo, 7)
                        verify(ab, minimo, 5)
                        verify(bc, minimo)
                        verify(cd, minimo)
        def dos(ab, bc, cd, de, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        if de in beaker:
                            lista = [beaker[ab], beaker[bc], beaker[cd], beaker[de]]
                            minimo = min(lista)
                            novo(res, minimo, 4)
                            verify(ab, minimo)
                            verify(bc, minimo)
                            verify(cd, minimo)
                            verify(de, minimo)
        def jojofafa(ab, bc, cd, de, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        if de in beaker:
                            lista = [beaker[ab]/2, beaker[bc]/2, beaker[cd], beaker[de]]
                            minimo = min(lista)
                            novo(res, minimo, 6)
                            verify(ab, minimo, 2)
                            verify(bc, minimo, 2)
                            verify(cd, minimo)
                            verify(de, minimo)
        def jorfae(ab, bc, res):
            if ab in beaker:
                if bc in beaker:
                    lista = [beaker[ab]/2, beaker[bc]]
                    minimo = min(lista)
                    novo(res, minimo, 3)
                    verify(ab, minimo, 2)
                    verify(bc, minimo)
        def jorjorfae(ab, bc, cd, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        lista = [beaker[ab]/2, beaker[bc]/2, beaker[cd]]
                        minimo = min(lista)
                        novo(res, minimo, 5)
                        verify(ab, minimo, 2)
                        verify(bc, minimo, 2)
                        verify(cd, minimo)
        def fae(ab, bc, cd, de, ef, fg, gh, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        if de in beaker:
                            if ef in beaker:
                                if fg in beaker:
                                    if gh in beaker:
                                        lista = [beaker[ab], beaker[bc], beaker[cd], beaker[de], beaker[ef], beaker[fg], beaker[gh]]
                                        minimo = min(lista)
                                        novo(res, minimo, 7)
                                        verify(ab, minimo)
                                        verify(bc, minimo)
                                        verify(cd, minimo)
                                        verify(de, minimo)
                                        verify(ef, minimo)
                                        verify(fg, minimo)
                                        verify(gh, minimo)
        def tedjorfaefae(ab, bc, cd, de, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        if de in beaker:
                            lista = [beaker[ab]/5, beaker[bc]/2, beaker[cd], beaker[de]]
                            minimo = min(lista)
                            novo(res, minimo, 9)
                            verify(ab, minimo, 5)
                            verify(bc, minimo, 2)
                            verify(cd, minimo)
                            verify(de, minimo)
        def tedjor(ab, bc, res):
            if ab in beaker:
                if bc in beaker:
                    lista = [beaker[ab]/5, beaker[bc]/2]
                    minimo = min(lista)
                    novo(res, minimo, 7)
                    verify(ab, minimo, 5)
                    verify(bc, minimo, 2)
        def daidai(ab, bc, res):
            if ab in beaker:
                if bc in beaker:
                    lista = [beaker[ab]/10, beaker[bc]/10]
                    minimo = min(lista)
                    novo(res, minimo, 20)
                    verify(ab, minimo, 10)
                    verify(bc, minimo, 10)
        def daidaidai(ab, bc, cd, res):
            if ab in beaker:
              if bc in beaker:
                  if cd in beaker:
                    lista = [beaker[ab]/10, beaker[bc]/10, beaker[cd]/10]
                    minimo = min(lista)
                    novo(res, minimo, 30)
                    verify(ab, minimo, 10)
                    verify(bc, minimo, 10)
                    verify(cd, minimo, 10)
        def tedmerjor(ab, bc, cd, res):
            if ab in beaker:
              if bc in beaker:
                  if cd in beaker:
                    lista = [beaker[ab]/5, beaker[bc]/3, beaker[cd]/2]
                    minimo = min(lista)
                    novo(res, minimo, 10)
                    verify(ab, minimo, 5)
                    verify(bc, minimo, 3)
                    verify(cd, minimo, 2)
        def tedfae(ab, bc, res):
            if ab in beaker:
                if bc in beaker:
                    lista = [beaker[ab]/5, beaker[bc]]
                    minimo = min(lista)
                    novo(res, minimo, 6)
                    verify(ab, minimo, 5)
                    verify(bc, minimo)
        def tedtedfae(ab, bc, cd, res):
            if ab in beaker:
                if bc in beaker:
                  if cd in beaker:
                    lista = [beaker[ab]/5, beaker[bc]/5, beaker[cd]]
                    minimo = min(lista)
                    novo(res, minimo, 11)
                    verify(ab, minimo, 5)
                    verify(bc, minimo, 5)
                    verify(cd, minimo)
        def merjorfae(ab, bc, cd, res):
            if ab in beaker:
                if bc in beaker:
                    if cd in beaker:
                        lista = [beaker[ab]/3, beaker[bc]/2, beaker[cd]]
                        minimo = min(lista)
                        novo(res, minimom, 6)
                        verify(ab, minimo, 3)
                        verify(bc, minimo, 2)
                        verify(cd, minimo)
                            
        merfaefae("oxigenio", "potassio", "nitrogenio", "salitre")
        mer("combustivel", "carbono", "hidrogenio", "oleo")
        faetem("oleo", "cinzas", 480)
        mer("oleo", "combustivel", "oxigenio", "acetona")
        ted3fae("ferro", "cloreto_de_sodio", "carbono", "acido_sulfurico", "granibitaluri")
        mer("alumini0", "potassio", "nitrogenio", "seiver")
        merfae("hidrogenio", "nitrogenio", "amonia")
        mer("libital", "sangue", "carbono", "synthflesh")
        jor3fae("oxido_de_nitrogenio", "toxina", "fluor", "enxofre", "syriniver")
        if temperatura <= 47:
            merfaefae("criostalino", "lixivia", "bromo", "hercuri")
        if temperatura >= 380:
            jor("cloreto_de_sodio", "cinzas", "multiver")
        jor("amonia", "etanol", "dietmalina")
        mer("oleo", "cloro", "agua", "fenol") 
        mer("agua", "sodio", "cloro", "cloreto_de_sodio")               
        mer("sodio", "hidrogenio", "oxigenio", "lixivia")
        mer("cloro", "oxigenio", "agua", "peroxido_de_hidrogenio")
        if temperatura >= 420:
            mer("etanol", "oxigenio", "prata", "formaldeido")
        if temperatura >= 450:
            merfaefae("formaldeido", "acetaldeido", "agua", "pentaeritricol")
        mer("acetona", "agua", "formaldeido", "acetaldeido")
        jorfaefae("acetona", "peroxido_de_hidrogenio", "oxigenio", "oxido_de_acetona")
        mer("fenol", "nitrogenio", "oxigenio", "libital")
        mer("carbono", "fluor", "açucar", "helbital")
        jorfaefae("acetona", "cobre", "fosforo", "probital")
        jorfaefae("hidrogenio", "amonia", "acido_sulfurico", "aiuri")
        ted("amonia", "prata", "enxofre", "oxigenio", "cloro", "lenturi")
        jormerfae("acetona", "nitrogenio", "acido_sulfurico", "tirimol")
        if temperatura >= 370:
            mer("oleo", "fluor", "hidrogenio", "convermol")
        ted("fenol", "sodio", "carbono", "oxigenio", "acido_sulfurico", "acido_salicilico")
        ted("acido_salicilico", "amonia", "aluminio", "bromo", "litio", "salbutamol")
        hiu("cianeto", "formaldeido", "amonia", "combustivel", "sodio", "cloro", "acido_pentetico")
        ted("acetona", "dietmalina", "fenol", "etanol", "acido_sulfurico", "atropina")
        if temperatura >= 374:
            jor("cloro", "mercurio", "calomel")
        mer3fae("carbono", "fenol", "hidrogenio", "oxigenio", "oxandrolona")
        mer("acetona", "mutageno_instavel", "plasma", "crioxadona")
        jor("slime", "crioxadona", "piroxadona")
        mer("crioxadona", "criptobiolina", "cobre", "rezadona")
        tedfaefae("plasma", "crioxadona", "sodio", "clonexadona")
        mer("mutageno_instavel", "acetona", "bromo", "mutadone")
        mer("hidrogenio", "agua", "açucar", "manitol")
        mer("acetona", "manitol", "oxigenio", "neurina")
        jor("potassio", "iodo", "iodeto_de_potassio")
        mer("açucar", "cloreto_de_sodio", "agua", "salina_glicose")
        dos("dietmalina", "oleo", "hidrogenio", "açucar", "efedrina")
        ted("dietmalina", "oleo", "bromo", "carbono", "etanol", "difenidramina")
        mer("multiver", "carbono", "hidrogenio", "oculina")
        mer("multiver", "carbono", "agua", "inacusado")
        hiu("dietmalina", "acetona", "fenol", "cloro", "hidrogenio", "oxigenio", "epinefrina")
        mer("multiver", "cobre", "etanol", "antihol")
        mer("açucar", "litio", "agua", "sinaptizina")
        jor("epinefrina", "criptobiolina", "espacilina")
        hiu("bromo", "amonia", "fenol", "dietmalina", "acetona", "acido_sulfurico", "modafinil")
        jojofafa("carbono", "hidrogenio", "oxigenio", "etanol", "morfina")
        ted("oleo", "iodeto_de_potassio", "aluminio", "cloro", "fluor", "haloperidol")
        tedfaefae("plasma", "silicio", "cobre", "leporazina")
        jorfae("fenol", "litio", "higadrite")
        jorjorfae("manitol", "agua", "impedrezene", "psicodina")
        mer("pentaeritricol", "acetona", "acido_nitrico", "penthrite")
        if temperatura <= 380:
            hiu("difenidramina", "detergente", "morfina", "fosforo", "potassio", "combustivel", "krokodil")
        if temperatura <= 390:
            ted("difenidramina", "amonia", "litio", "acido_sulfurico", "combustivel", "crack")
        if temperatura <= 374:
            dos("efedrina", "hidrogenio", "iodo", "fosforo", "metanfetamina")
        fae("salitre", "detergente", "comida_estragada", "enzima", "nutrimento", "cha", "mercurio", "crack")
        mer("epinefrina", "atropina", "morpina", "aranesp")
        tedjorfaefae("plasma", "oxido_nitroso", "epinefrina", "etanol", '"happy"')
        mer("litio", "mercurio", "açucar", "spacedrugs")
        tedjor("cafe", "epinefrina", "bomba")
        mer("ferro", "oxigenio", "hidrogenio", "estabilizador")
        jorjorfae("carbono", "fluor", "acido_sulfurico", "fluoro-sufactante")
        mer("fosforo", "potassio", "açucar", "fumaça")
        dos("fosforo", "potassio", "açucar", "estabilizador", "po_de_fumaça")
        mer("aluminio", "potassio", "enxofre", "po_de_flash")
        mer("fosforo", "acido_sulfurico", "plasma", "flogisto")
        mer("oleo", "combustivel", "etanol", "napalm")
        mer("oxigenio", "cola", "fosforo", "po_sonico")
        mer("plasma", "radio", "fosforo", "pyrosium")
        mer("agua", "plasma", "nitrogenio", "criostilano")
        if temperatura >= 424:
            merfae("fluor", "cloro", "trifluoreto_de_cloro")
        dos("carbono", "mercurio", "nitrogenio", "oxigenio", "sorium")
        mer("carbono", "plasma", "radio", "materia_escura_liquida")
        mer("multiver", "salitre", "enxofre", "polvora")
        mer("glicerol", "acido_nitrico", "acido_sulfurico", "nitroglicerina")
        if "nitroglicerina" in beaker:
            exp = True
        if temperatura >= 404:
            jor3fae("fenol", "oxido_de_acetona", "acido_nitrico", "ouro", "RDX")
            if temperatura >= 474:
                exp = True
        lvl = randint(401, 499)
        if temperatura >= lvl:
            mer("oxido_de_acetona", "acido_nitrico", "pentaeritricol", "TaTP")
            exp = True
        if "potassio" in beaker and "agua" in beaker:
            exp = True
        jor("ferro", "uranio", "EMP")
        if temperatura >= 420:
            mer("plasma", "prata", "polvora", "teslium")
            if "agua" in beaker:
                exp = True
        mer("aluminio", "ferro", "oxigenio", "thermite")
        if temperatura >= 395:
            mer("soda_caustica", "acido_sulfurico", "rádio", "baldium")
        if temperatura >= 374:
            daidai("gibs", "oxigenio", "vela")
        if temperatura >= 777:
            jorfae("oxigenio", "carbono", "dioxido_de_carbono")
        jor("spacedrugs", "sangue", "tapete")
        ted("citrico_triplo", "crioxadona", "spacedrugs", "radio", "plasma", "reagente_colorido")
        tedfae("etanol", "oleo de capsaicina", "capsaicina_concentrada")
        if temperatura >= 524:
            if "celulose" in beaker:
                beaker["celulose_carbonizada"] = beaker["celulose"]
                del beaker["celulose"]
        dos("reagente_colorido", "reagente_estranho", "nutricao", "sangue", "corgium")
        mer("oxigenio", "potassio", "açucar", "criptobiolina")
        jorfaefae("plasma", "etanol", "sodio", "agente_secante")
        jor("litio", "hidrogenio", "agente_espumante")
        if temperatura <= 200:
            mer("estabilizador", "fluoro-surfactante", "carbono", "espuma_de_extintor")
        merfae("oleo", "acido_sulfurico", "glicerol")
        mer("mercurio", "oxigenio", "açucar", "impredezene")
        mer("reagente_colorido", "spacedrugs", "radio", "tinta_de_cabelo")
        jor("açucar", "suco_de_banana", "gás_do_riso")
        daidaidai("reagente_colorido", "spacedrugs", "radio", "carne")
        merfaefae("ferro", "acido_fluorossulfurico", "agente_espumante", "espuma_de_metal")
        merfaefae("agente_espumante", "acetona", "ferro", "agente_inteligente_espumante")
        merfaefae("aluminio", "agente_inteligente_espumante", "acido_fluorossulfurico", "espuma_de_metal_inteligente")
        if temperatura >= 525:
            jorjorfae("amonia", "oxigenio", "nitrogenio", "oxido_nitroso")
        if temperatura >= 374:
            tedmerjor("oleo", "cinzas", "acido_sulfurico", "plastico")
            daidai("soda_caustica", "gibs", "sabonete")
        jor("amonia", "agua", "detergente")
        mer("oxigenio", "silicio", "agua", "lubrificante")
        mer("multiver", "cloro", "etanol", "esterilizina")
        tedfae("sangue", "crioxadona", "carne_sintetica")
        merjorfae("formaldeido", "oligomeros_de_polipirilio", "celulose", "sutura_medicada")
        jorjorfae("celulose", "suco_de_aloe", "esterilizina", "malha_regenerativa")
        mer("toxina_mindbreaker", "sinaptizina", "agua", "pax")
        jorfaefae("nutricao", "suco_de_banana", "gibs", "pó_de_macaco")
        tedfae("agua", "eletricidade", "eletronise")
        if temperatura >= 374:
            tedtedfae("creme", "vinho_lagarto", "reagente_estranho", "grito")
        jor("agua", "leite", "virus_alimentar")
        jor("virus_alimentar", "sinaptizina", "ração_de_virus")
        mer("cloro", "sodio", "radio", "mutageno_instavel")
        jor("mutageno_instavel", "virus_alimentar", "agar_mutagenico")
        jor("agar_mutagenico", "salina-glicose", "agar_de_sacarose")
        jor("plasma_de_virus", "sinaptizina", "plasma_de_virus_enfraquecido")
        jor("virus_alimentar", "plasma", "plasma_de_virus")
        jor("virus_alimentar", "uranio", "gel_de_uranio_em_decomposiçao")
        tedfae("uranio", "plasma_de_virus", "gel_de_uranio_instavel")
        daidaidai("uranio", "plasma", "aluminio", "gel_de_urario_estavel")

    else:
        if command == "empty":
            beaker = {"total": 0}
        if command == "quit":
            arq[nome] = beaker
            tem_Beaker = False
        if command == "help":
            print("Para mais informações escreva: help <nome do comando>\n Lista de comandos:\nadd: adiciona elementos e beakers\ndel: deleta elementos\nend: fecha o programa\nempty: esvazia o beaker\nquit: guarda o beaker\nhot: altera a temperatura\ntransfer: transfere substancias\n\n Lista de elementos adicionaveis:\nhidrogenio oxigenio silicio fosforo \nenxofre carbono azoto agua nitrogenio \nlitio açucar acido_sulfurico cobre \nmercurio sodio iodo bromo etanol \ncloro potassio aluminio radio fluor \nferro combustivel prata plasma")
    if tem_Beaker == True:
        print(beaker)
    beaker["total"] = sum(beaker.values())-beaker["total"]
    lista = []
    if command == "end":
        break
    beaker["total"] = sum(beaker.values())-beaker["total"]
    arq[nome] = beaker  
    if exp:
        print("a maquina explodiu")
        break
