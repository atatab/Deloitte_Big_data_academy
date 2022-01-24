# Backend Cronos Agency
Desafio tecnico de backend feito para Big Data Academy (Gama/Deloitte)

## Table of contents
  - [General info](#general-info)
  - [Technologies](#technologies)
  - [Setup](#setup)

## General info
A Agência Cronos, que presta serviços de tecnologia (desenvolvimento, marketing e UX design), contratou você para o desenvolvimento de uma API para gerenciamento do conteúdo do site institucional.
Faça um CRUD de Serviços, Posts e Integrantes da Equipe, permitindo que o administrador do site consiga criar, editar, deletar e visualizar os dados através de um painel administrativo.
O gerenciamento dos dados deve ser feito com uma API REST conectada ao banco de dados relacional.

##### REQUISITOS MÍNIMOS BACK-END
###### 1. Todos os códigos deverão estar em um repositório no Github com README.md descrevendo tecnologias utilizadas no projeto.
    github: https://github.com/atatab/Deloitte_Big_data_academy
    README: https://github.com/atatab/Deloitte_Big_data_academy/blob/master/README.md

###### 2. API:
###### a. CRUD (Criar, ler, atualizar e deletar) de Serviços
   CRUD de Serviços só pode ser utilizado com authenticação(Basic ou Token)
   https://backend-cronos-agency.herokuapp.com/api/v1/service/
   https://backend-cronos-agency.herokuapp.com/api/v1/service/create/
   https://backend-cronos-agency.herokuapp.com/api/v1/service/update/<int:pk>/
   https://backend-cronos-agency.herokuapp.com/api/v1/service/delete/<int:pk>/

###### b. CRUD (Criar, ler, atualizar e deletar) de Posts
   CRUD de Posts pode ser utilizado sem authenticação
   https://backend-cronos-agency.herokuapp.com/api/v1/blog_post/
   https://backend-cronos-agency.herokuapp.com/api/v1/blog_post/create/
   https://backend-cronos-agency.herokuapp.com/api/v1/blog_post/update/<int:pk>/
   https://backend-cronos-agency.herokuapp.com/api/v1/blog_post/delete/<int:pk>/

###### c. CRUD (Criar, ler, atualizar e deletar) de Integrantes da Equipe
   CRUD de Integrantes da Equipe quando não autenticado(Basic ou Token) entra em modo de Leitura.
   https://backend-cronos-agency.herokuapp.com/api/v1/team_member/
   https://backend-cronos-agency.herokuapp.com/api/v1/team_member/create/
   https://backend-cronos-agency.herokuapp.com/api/v1/team_member/update/<int:pk>/
   https://backend-cronos-agency.herokuapp.com/api/v1/team_member/delete/<int:pk>/

###### 3. Banco de dados:
###### a. Utilizar banco de dados relacional
    Utilizado SQLite.
###### b. Adicionar dados para teste
    Dados adicionados podem ser checados no admin ou pelo endpoint de leitura

##### OPCIONAIS BACK-END
###### 5. Autenticação de administrador para gerenciamento do conteúdo
    Endpoint de admin criado em https://backend-cronos-agency.herokuapp.com/admin/
    user: content_manager
    pass: content_chronos

###### 6. Documentação da API
   Documentação basica pode ser visualizada acessando o endpoint pelo browser e acessando o botão "Options"
###### 7. Testes automatizados
###### 8. Deploy da aplicação
    Deploy feito no Heroku: https://backend-cronos-agency.herokuapp.com/admin/
	
## Technologies
This project was created with:
* [Python](https://www.python.org): 3.10.2
* [Django](https://www.djangoproject.com/): 4.0.1
* [django_restframework](www.django-rest-framework.org/): 3.13.1
	
## Setup
* If you wish to run your own build, first ensure you have Python globally installed in your computer. 
* Confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* #### Steps
    1. Create and fire up your virtual environment inside your cloned repository:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    4. Run migrations
        ```bash
            $ python manage.py makemigrations
            $ python manage.py migrate
            $ python manage.py createsuperuser
        ```
    5. Run the server
    ```bash
        $ python manage.py runserver
    ```
    6. Test it Locally
        Endpoints:
            http://localhost:8000/admin/
            http://localhost:8000/api/v1/service/
            http://localhost:8000/api/v1/team_member/
            http://localhost:8000/api/v1/blog_post/
            