import grass.script as grass
import os

os.chdir(r'F:\data\Ju_coelho')

arquivo=open('teste.txt','w')
cabecalho='HEXID'',''classe'',''area M2' '\n'
arquivo.write(cabecalho)
temp_2=''
temp_3=''
for i in range(24497):
    i=i+1
    grass.run_command('g.region', rast='union_vegHex_cer_rast',verbose=False)
    frag=grass.read_command('v.db.select', flags='c', map='hex_1m_cerrado_albers_shp', column='HEXID', where="cat="+`i`)
    
    grass.run_command('v.extract', input='hex_1m_cerrado_albers_shp', output='Temp', where="cat="+`i`, overwrite=True   )
    grass.run_command('g.region',vect='temp')
    grass.run_command('v.to.rast',input='temp', out='temp', use="cat" , overwrite=True)
    
    grass.run_command('r.mask',  input='temp',flags='o') 
    grass.run_command('g.region',vect='temp')
    temp=grass.read_command('r.stats', input='union_vegHex_cer_rast_bin_erdo_soma' ,flags='la',quiet=True,fs='comma')
   
    temp=temp.replace('*','')
    temp=temp.replace('\n','cc')
    temp_2=temp.split('cc')
   
    
    del temp_2[-1]
    del temp_2[-1]
    frag.replace('\n','')
    linha1=frag.replace('\n','')
    
    
    while len(temp_2)>1:
       
        linha2=temp_2[0]
        linha3=temp_2[1]
        
        del temp_2[0]
        del temp_2[0]
        arquivo.write(linha1+","+linha2+','+linha3+ '\n')
        
    
    
    grass.run_command('r.mask',  flags='r') 
arquivo.close()
