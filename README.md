# AllForOne
Projeto da disciplina de Sistemas Distribuídos usando Django. Vaquinha online possibilitando o encontro doador e quem precisa de ajuda.

## Padrões do projeto
- Nomes de classes: PascalCase
- Nomes de métodos e variáveis: snake_case

## Setup de instalação
Faça o download do repositório remoto na pasta de preferência:
```
git clone https://github.com/filipealvesrr/AllForOne.git
```

Feito isto, entre na pasta do projeto:
  ```
  cd AllForOne
  ```

Feito isto, abra o projeto no seu VSC:
  ```
  code .
  ```

Instale o ambiente virtual do próprio VSC no terminal:
  ```
  python3 -m venv venv
  ```

Em seguida, faça a atualização do pip e instalação do django:
  ```
  pip install pip setuptools wheel --upgrade` (atualizações pendentes)
  ```
  ```
  pip install django` (instalação do django no venv)
  ```

Feito isso, ative o ambiente virtual e inicie o servidor;
  ```
  . venv/bin/activate` (para ativar o ambiente virtual)
  ```
  ```
  python manage.py runserver` (para iniciar o servidor do django)
  ```

Obs: fechar o terminal vai matar o processo do servidor e consequentemente ele vai parar, por isso é recomendável deixar em outro terminal.

Feito isso, você já deve poder acessar a aplicação django no seguinte endereço: http://127.0.0.1:8000/
