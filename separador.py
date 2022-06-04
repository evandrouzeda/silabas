vogais = ["a", "â", "á", "e", "é", "i", "í", "o", "ó", "u"]
consoantes = ["b", "c", "ç", "d", "f", "g", "h", "j", "k", "l", "m",
              "n", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
digrafro1 = ["q", "g"]
digrafro2 = ["l", "n", "c"]
digrafro3 = ["r", "s", "x"]
digrafro4 = ["r", "s", "c", "ç"]
meio = ["h", "l", "r"]
finais = [" ", "-"]
pontuacao = [".", ",", ";", ":"]

q1 = {
    "semi": "q3",
    "vogal": "q4",
    "digrafo1": "q9",
    "consoante": "q2"
}
q2 = {
    "semi": "q3",
    "vogal": "q4",
    "digrafo1": "q9",
    "consoante": "q2"
}
q3 = {
    "a":"q5",
    "semi": "q5",
    "vogal": "q4",
    "digrafo1": "q9",
    "consoante": "q7"
}
q4 = {
    "semi": "q3",
    "vogal": "q5",
    "digrafo1": "q9",
    "consoante": "q7"
}
q5 = {
    "semi": "q3",
    "vogal": "q4",
    "digrafo1": "q9",
    "consoante": "q7"
}
q6 = {
    "semi": "q3",
    "vogal": "q4",
    "meio": "q8",
    "digrafo1": "q9",
    "consoante": "q7"
}
q7 = {
    "semi": "q3",
    "vogal": "q4",
    "meio": "q8",
    "digrafo1": "q11",
    "consoante": "q6"
}
q8 = {
    "semi": "q3",
    "vogal": "q4",
    "digrafo1": "q9",
    "consoante": "q7"
}
q9 = {
    "u": "q10",
    "vogal": "q4",
}
q10 = {
    "vogal": "q4",
    "consoante": "q7"
}
q11 = {
    "u": "q10",
    "vogal": "q4",
}
states = {
    "q1": q1,
    "q2": q2,
    "q3": q3,
    "q4": q4,
    "q5": q5,
    "q6": q6,
    "q7": q7,
    "q8": q8,
    "q9": q9,
    "q10": q10,
    "q11": q11,
}

transitions = {
    "vogal": vogais,
    "digrafo1": digrafro1,
    "digrafro2": digrafro2,
    "digrafo3": digrafro3,
    "digrafo4": digrafro4,
    "consoante": consoantes,
    "meio": meio,
    "semi": ["i", "u"],
    "u": ["u"],
    "h": ["h"],
    "r": ["r"],
    "a": ["a"],
}

def getState(state, char):
    for tran in states[state]:
        if char in transitions[tran]: return states[state][tran]
    return "q1"

def separa(text, i, state):
    if i == len(text): return text
    print(state, "-->",text[i], "-->", getState(state, text[i]))
    if getState(state, text[i]) == "q7" and i + 1 < len(text): 
        text = text[0:i] + "-" + text[i:]
        i+=1
    if getState(state, text[i]) == "q9" and i > 0: 
        text = text[0:i] + "-" + text[i:]
        i+=1
    if getState(state, text[i]) == "q6" or getState(state, text[i]) == "q11": 
        text = text[0:i-2]+ text[i-1] + "-" + text[i:]

    if getState(state, text[i]) == "q5": 
        text = text[0:i] + "-" + text[i:]
        i+=1
    # if state == "q4" or text[i+1] == "-" or text[i] in pontuacao: return i + 1
    return separa(text, i+1, getState(state, text[i]))

palavra = "palavra"
separado = separa(palavra, 0, "q1")
esperado = " → pa-la-vra"
print(separado, esperado)
# Saida esperada:
""" 
    q1 --> p --> q2
    q2 --> a --> q4
    q4 --> l --> q7
    q7 --> a --> q4
    q4 --> v --> q7
    q7 --> r --> q8
    q8 --> a --> q4
    pa-la-vra  → pa-la-vra
"""
# Se nao quer ver mais o passo a passo, basta comentar a linha 111 => print(state, "-->",text[i], "-->", getState(state, text[i]))

#Palavras que possuem conflitos
""" print(separa("gratuito", 0, "q1"), " → gra-tui-to")
print(separa("fluido", 0, "q1"), " → flui-do")
print(separa("fluidez", 0, "q1"), " → flu-i-dez")
print(separa("fluente", 0, "q1"), " → flu-en-te")
print(separa("contribuinte", 0, "q1"), " → con-tri-bu-in-te")
print(separa("sublime", 0, "q1"), " → su-bli-me")
print(separa("sublingual", 0, "q1"), " → sub-lin-gual") """

# Palavras que em principio entao funcionando
""" print(separa("ninho", 0, "q1"))
print(separa("chave", 0, "q1"))
print(separa("quero", 0, "q1"))
print(separa("sagu", 0, "q1"))
print("###")
print(separa("terra", 0, "q1"))
print(separa("passo", 0, "q1"))
print(separa("crescer", 0, "q1"))
print(separa("clique", 0, "q1"))
print(separa("nasça", 0, "q1"))
print(separa("exceto", 0, "q1"))
print(separa("guerra", 0, "q1"))
print("###")
print(separa("adepto", 0, "q1"))
print(separa("objeto", 0, "q1"), " → ob-je-to")
print(separa("submeter", 0, "q1"), " → sub-me-ter")
print(separa("caracteres", 0, "q1"), " → ca-rac-te-res")
print(separa("recepção", 0, "q1"), " → re-cep-ção")
print("###")
print(separa("psicólogo", 0, "q1"), " → psi-có-lo-go")
print(separa("pneumático", 0, "q1"), " → pneu-má-ti-co")
print("###")
print(separa("bisneto", 0, "q1"), " → bis-ne-to")
print(separa("sublingual", 0, "q1"), " → sub-lin-gual")
print("###")
print(separa("subentender", 0, "q1"), " →  su-ben-ten-der")
print(separa("desigual", 0, "q1"), " → de-si-gual")
print(separa("bisavô", 0, "q1"), " → bi-sa-vô")
print("###")
print(separa("seccional", 0, "q1"), " →  sec-cio-nal")
print("###")
print(separa("saída", 0, "q1"), " → sa-í-da")
print(separa("lagoa", 0, "q1"), " → la-go-a")
print(separa("enjoo", 0, "q1"), " → en-jo-o")
print(separa("hiato", 0, "q1"), " → hi-a-to")
print("###")
print(separa("saara", 0, "q1"), " → sa-a-ra")
print("###")
print(separa("quaisquer", 0, "q1"), " → quais-quer")
print(separa("desiguais", 0, "q1"), " → de-si-guais")
print(separa("série", 0, "q1"), " → sé-rie")
print(separa("cílios", 0, "q1"), " → cí-lios")
print(separa("ambiguidade", 0, "q1"), " →  am-bi-gui-da-de")
print(separa("guerra", 0, "q1"), " → guer-ra")
print("###")
print(separa("declarar", 0, "q1"), " → de-cla-rar")
print(separa("flanela", 0, "q1"), " → fla-ne-la")
print(separa("preço", 0, "q1"), " → pre-ço")
print(separa("cravo", 0, "q1"), " → cra-vo") """
