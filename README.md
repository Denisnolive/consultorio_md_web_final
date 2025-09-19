## Como Executar

1. **Instalar dependências com Poetry:**
   ```bash
   cd consultorio_md_web
   poetry install --no-root
   ```

2. **Executar a aplicação:**
   ```bash
   poetry run python src/main.py
   ```

3. **Acessar no navegador:**
   ```
   http://localhost:5000
   ```

## API Endpoints

### Consultório MD API

- `GET /api/consultorio/menu` - Retorna o menu principal
- `GET /api/consultorio/exames` - Retorna o menu de exames
- `GET /api/consultorio/laboratorio` - Retorna o menu de laboratório
- `GET /api/consultorio/imagem` - Retorna o menu de imagens
- `GET /api/consultorio/resultados` - Retorna o menu de resultados
- `GET /api/consultorio/consultas` - Retorna o menu de agendamento de consultas
- `GET /api/consultorio/especialidades` - Retorna o menu de especialidades
- `POST /api/consultorio/resposta` - Retorna resposta baseada no caminho de navegação
- `POST /api/consultorio/agendar` - Processa agendamento de consulta

## Respostas do Sistema

O sistema fornece as seguintes respostas automáticas:

### Laboratório
- **Agendar Coleta**: "Para agendar coleta, por favor, ligue para (XX) XXXX-XXXX ou acesse nosso site."
- **Exames anatomopatológicos**: "O resultado do exame anatomopatológico estará disponível em 15 dias úteis."
- **Rotinas de Exames**: "Rotinas: Hemograma, EAS, TGP, TGO."

### Imagem
- **Agendar Tomografia**: "Para Tomografia, tenha o pedido médico e ligue (XX) XXXX-XXXX."
- **Agendar Ressonância**: "Para Ressonância, tenha o pedido médico e ligue (XX) XXXX-XXXX."
- **Agendar Raio X**: "Para Raio X, tenha o pedido médico e ligue (XX) XXXX-XXXX."

### Resultados
- **Resultado Imagens**: "Resultados de Imagens disponíveis no portal em até 10 dias úteis."
- **Resultado Laboratório**: "Resultados de Laboratório disponíveis no portal em 5 a 7 dias úteis."

### Consultas
- **Selecionar Especialidade**: Permite selecionar uma especialidade para agendamento.
- **Remarcar Consulta**: Permite remarcar uma consulta existente.
- **Confirmar Consulta**: Permite confirmar uma consulta agendada.

### Especialidades
- **Clínica Médica**: Agendamento de consulta com clínico geral.
- **Cardiologia**: Agendamento de consulta com cardiologista.
- **Endocrinologia**: Agendamento de consulta com endocrinologista.
- **Pneumologia**: Agendamento de consulta com pneumologista.
- **Dermatologia**: Agendamento de consulta com dermatologista.
- **Psicologia**: Agendamento de consulta com psicólogo.

### Menu Principal
- **Autorizações**: "Para autorizações de procedimentos, dirija-se à nossa recepção, com a solicitação médica e carteirinha do convênio."

## Tecnologias Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Banco de Dados**: SQLite
- **Estilo**: CSS com gradientes e animações
- **Responsividade**: Media queries para dispositivos móveis

## Características da Interface

- Design moderno com gradiente azul/roxo
- Animações suaves e efeitos hover
- Breadcrumb para navegação
- Botões de voltar e início
- Layout responsivo
- Feedback visual para carregamento e erros

## Desenvolvimento

O projeto foi desenvolvido seguindo as melhores práticas:

- Separação clara entre frontend e backend
- API RESTful para comunicação
- Código modular e organizados
- Interface responsiva e acessível
- Tratamento de erros adequado

## Autor

Sistema desenvolvido para o Consultório MD como uma modernização do sistema de atendimento digital.

