# Libraries

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

import time
import re

df = pd.read_csv("lista.csv") # lista de nomes

resumos = dict() # lista de resumos
nao_alunos = list() # lista de alunos que não tiveram/têm nenhum vínculo com uece
ultimo = dict() #mostra todos os nomes que já interagiram (Gambiarra para "tratamento de erro")

robo = webdriver.Firefox() 
robo.get('https://buscatextual.cnpq.br/buscatextual/busca.do?metodo=apresentar') # abre a pesquisa do lattes

time.sleep(1)

for i in df["PESSOAS"]:

    ultimo.append(i) # controle de erro (Pode ser desconsiderado)
    
    robo.find_element(By.XPATH,r'//*[@id="buscarDemais"]').click() # clica em "demais pesquisadores"
    time.sleep(1)
    
    aluno = robo.find_element(By.NAME,"textoBusca") # seleciona busca
    time.sleep(1)
    
    aluno.send_keys(str(i)) # escreve nome do aluno
    
    robo.find_element(By.ID,'botaoBuscaFiltros').click() # busca aluno
    time.sleep(2)

    
    resultados = robo.find_elements(By.XPATH,'/html/body/form/div/div[4]/div/div/div/div[3]/div/div[3]/ol/li')

    print("Imprimiu os resultados")

    for j in range(len(resultados)):
        element = WebDriverWait(robo, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,f'/html/body/form/div/div[4]/div/div/div/div[3]/div/div[3]/ol/li[{j+1}]/b/a')
            )
        )
        element.click()
        
        #print("clicou")
        time.sleep(1)
        
        # abre curriculo em outra aba
        xpath = 'idbtnabrircurriculo'
        
        botao = WebDriverWait(robo, 10).until(
        EC.presence_of_element_located(
            (By.ID,xpath)
            )
        )
        botao.click()
        #print('clicou botao')

        time.sleep(1)
        # Pega todos os identificadores de janelas/abas
        abas = robo.window_handles

        time.sleep(0.5)
        # troca pra nova aba
        robo.switch_to.window(abas[1])

        # pega o texto e salva num dicionpário
        time.sleep(3)
        xpath = '/html/body/div[1]/div[3]/div/div/div/div[2]/p'
        nome = re.search(r'\((.*?)\)', robo.title).group(1)
        resumo = WebDriverWait(robo, 10).until(
        EC.presence_of_element_located(
            (By.XPATH,xpath)
            )
        )
        resumo = resumo.text.lower() # Tratamento básico de NLP
        #print("Pegou Resumo")

        if ("universidade estadual do ceará" in resumo) or ("uece" in resumo):
            resumos[nome] = resumo
        else:
            nao_alunos.append(nome)
        
        #volta pra aba 
        robo.switch_to.window(abas[0])
        time.sleep(1)
        robo.find_element(By.ID,'idbtnfechar').click()

    time.sleep(1)
    for aba in abas[1:]:  # Ignora a primeira aba (a original)
        robo.switch_to.window(aba)  # Muda para a aba
        robo.close()  # Fecha a aba atual

    robo.switch_to.window(abas[0])
    time.sleep(1)
    robo.find_element(By.XPATH,'//*[@id="botaoBuscaFiltros"]').click()

# Convertendo o dicionário em DataFrame

df = pd.DataFrame(list(resumos.items()), columns=['Nome', 'Resumo'])
df.to_csv("resultado.csv", index=False)