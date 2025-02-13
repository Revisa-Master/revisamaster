# Site da Empresa de Revisão Acadêmica
Este projeto consiste no desenvolvimento de um site profissional para uma empresa especializada em revisão acadêmica. O objetivo é fornecer uma plataforma intuitiva e eficiente para que os clientes possam conhecer os serviços oferecidos e entrar em contato com a empresa.

## Funcionalidades Principais
Apresentação Institucional: Seção dedicada à história, missão e valores da empresa, permitindo que os visitantes compreendam a essência e os objetivos da organização.

### Serviços Oferecidos: Descrição detalhada dos serviços de revisão acadêmica disponíveis, incluindo tipos de documentos atendidos, prazos e metodologias utilizadas.

Formulário de Contato Integrado ao SMTP: Um formulário de contato que permite aos clientes enviar mensagens diretamente pelo site. A integração com o protocolo SMTP garante que essas mensagens sejam entregues de forma segura e eficiente à equipe da empresa.

## Tecnologias Utilizadas

### Frontend:

HTML5: Estruturação semântica das páginas, garantindo acessibilidade e SEO adequados.
CSS3: Estilização responsiva e atraente, assegurando uma experiência de usuário consistente em diferentes dispositivos.
JavaScript: Implementação de interatividade e validações no lado do cliente, melhorando a usabilidade do site.
Backend:

Flask: Microframework em Python utilizado para gerenciar rotas, lógica de negócios e integração com o servidor de e-mail via SMTP.
Servidor de Aplicação:

Gunicorn: Servidor WSGI utilizado para servir a aplicação Flask em ambiente de produção, garantindo desempenho e escalabilidade.
Servidor Web:

Nginx: Configurado como proxy reverso, o Nginx direciona as requisições HTTP para o Gunicorn, além de servir arquivos estáticos e gerenciar conexões de forma eficiente.
Ambiente Virtual:

venv: Utilizado para criar um ambiente isolado para as dependências do projeto, garantindo que pacotes específicos não conflitem com outras aplicações no servidor.
