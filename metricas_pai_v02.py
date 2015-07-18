#importando pacotes
import grass.script as grass
import os

os.chdir(r'F:\data\Ju_coelho') # mudando diretrio de trabalho

arquivo=open('teste.txt','w') #criando e abrindo arquivo txt escrita ('W') para gravação de linhas
cabecalho='HEXID'',''classe'',''area M2' '\n' # criando cabeçalho
arquivo.write(cabecalho) #escrevendo linha cabeçalho
temp_2='' #declarando variaveis que serao linhas
temp_3='' #=====================================

#este for vai de 1 até o N de hexagonos
for i in range(24497):
    
    i=i+1 # incrementando o indici (i) para sair do 0
    grass.run_command('g.region', rast='union_vegHex_cer_rast',verbose=False) # definindo extensão
    frag=grass.read_command('v.db.select', flags='c', map='hex_1m_cerrado_albers_shp', column='HEXID', where="cat="+`i`) #atribuindo para variavel frag o valor da coluna (HEXID), onde cat for igual a i.Este sera usado para\
    #identificar o hexagono
    grass.run_command('v.extract', input='hex_1m_cerrado_albers_shp', output='Temp', where="cat="+`i`, overwrite=True   ) # extraindo do shp de hexago o hexagono referente ao cat=i
    grass.run_command('g.region',vect='temp') # neste comando nós limitamos nossa janela de trabalho com base na extensão do hexagono
    grass.run_command('v.to.rast',input='temp', out='temp', use="cat" , overwrite=True) #rasterizando o hexagono
    
    grass.run_command('r.mask',  input='temp',flags='o')  #criando mascara de analize utilizando o hexanogo extraido, assim todo processamento feito após a definicão da mascara será limitado a sua extensão
    grass.run_command('g.region',vect='temp') # reforçando a extensão
    temp=grass.read_command('r.stats', input='union_vegHex_cer_rast_bin_erdo_soma' ,flags='la',quiet=True,fs='comma') # extraindo para variavel tem, as informações do raster,lembrando que só será retornado o valor dentro da mascara.
   
    temp=temp.replace('*','') # substituindo * por nada ''
    temp=temp.replace('\n','cc') # substituindo '\n' por cc
    temp_2=temp.split('cc') # criando uma lista dizendo que os itens serão separados onde houver (cc)
   
    
    del temp_2[-1] # removendo o ultimo item da lista
    del temp_2[-1] # removendo o ultimo item da lista
    
    linha1=frag.replace('\n','') #substituindo na variavel frag,q contem o código identificador do hexagono,'\n' por nada.
    
    # enquanto o vetor temp_2 for maior que 1
    while len(temp_2)>1:
       
        linha2=temp_2[0] # grae na linha2 o indice 0 do vetor temp_2
        linha3=temp_2[1] # grae na linha2 o indice 0 do vetor temp_2
        
        del temp_2[0] # removendo primeiro item
        del temp_2[0] # removendo primeiro item
        arquivo.write(linha1+","+linha2+','+linha3+ '\n') #gravando no txt as linhas 
        
    
    
    grass.run_command('r.mask',  flags='r') # removendo a mascara
arquivo.close() # fechando txt
