# AllForOne
Projeto da disciplina de Sistemas Distribuídos usando Django. Vaquinha online possibilitando o encontro doador e quem precisa de ajuda.

## Guia de uso
Faça o download do repositório remoto na pasta de preferência:
```
git clone https://github.com/filipealvesrr/AllForOne.git
```

Entre na pasta do projeto:
  ```
  cd AllForOne
  ```

Abra a pasta com o com o VsCode ou digite no terminal:
  ```
  code .
  ```

Instale o ambiente virtual do próprio VSC no terminal:
  ```
  python3 -m venv venv
  ```

Em seguida, faça a atualização do pip
  ```
  pip install pip setuptools wheel --upgrade` (atualizações pendentes)
  ```
  

Feito isso, ative o ambiente virtual;
  ```
  . venv/bin/activate` (para ativar o ambiente virtual no linux, ver como é no windows)
  ```

Fazer a instalação das dependências, gerar as migrações e iniciar o servidor.
  ```
  pip install -r requirements.txt` (instalação das dependências)
  ```
  
  ```
  python manage.py migrate` (gerando as migrações)
  ```

  ```
  python manage.py runserver` (para iniciar o servidor do django)
  ```

A aplicação django pode ser acessada no seguinte endereço: http://127.0.0.1:8000/
