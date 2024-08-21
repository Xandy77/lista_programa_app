# importa biblioteca
import winapps

# lista programas   
for item in winapps.list_installed():
    print(f'Programa: {item.name}.')
    print(f'Versão: {item.version}.')
    print(f'Data da instalação: {item.install_date}.')
    print(f'Data da publicação: {item.publisher}.')
    print(f'Local de desinstalação: {item.uninstall_string}.')
    print('-'*50)