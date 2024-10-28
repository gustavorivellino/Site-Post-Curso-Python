O projeto é um site de postagem que permite aos usuários criar, 
visualizar e excluir posts. Ele foi desenvolvido utilizando o Flask, um framework web em Python, que facilita a construção de aplicações web.

Abaixo estão as principais tecnologias e funcionalidades envolvidas no projeto.

Tecnologias Usadas

Flask:
Framework web que fornece uma estrutura leve e flexível para construir aplicações web em Python.

SQLAlchemy:
ORM (Object-Relational Mapping) que permite interagir com bancos de dados de forma simples e intuitiva, facilitando a manipulação de dados.

Flask-Login:
Extensão que gerencia sessões de usuário, oferecendo funcionalidades como login, logout e proteção de rotas para usuários autenticados.

HTML/CSS:
Linguagens de marcação e estilo utilizadas para a construção da interface do usuário, garantindo uma apresentação agradável e responsiva.

Funcionamento do Projeto

Autenticação de Usuários:
O site requer que os usuários se registrem e façam login. O uso do Flask-Login garante que apenas usuários autenticados possam interagir com determinadas funcionalidades, como a exclusão de posts.

Gerenciamento de Posts:
Os usuários podem criar novos posts, visualizar posts existentes e excluir seus próprios posts. A exclusão de um post é controlada por uma verificação que garante que apenas o autor do post possa removê-lo.

Feedback ao Usuário:
O site utiliza mensagens flash para informar os usuários sobre ações bem-sucedidas, como a exclusão de um post, melhorando a experiência do usuário.

Interface Intuitiva:
A interface é construída em HTML e estilizada com CSS, proporcionando uma navegação fácil e acessível.

Conclusão
Este projeto de site de postagem exemplifica uma aplicação web funcional e segura, utilizando tecnologias modernas de desenvolvimento. Com um foco em autenticação e controle de acesso, ele oferece uma experiência de usuário robusta e eficiente. 
Se você quiser adicionar mais recursos ou funcionalidades, como comentários ou categorias de posts, há muitas possibilidades de expansão!
