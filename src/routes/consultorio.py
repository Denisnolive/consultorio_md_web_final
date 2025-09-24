from flask import Blueprint, jsonify, request
from flask_cors import CORS

consultorio_bp = Blueprint('consultorio', __name__)
CORS(consultorio_bp)

# Respostas do chatbot expandidas
RESPOSTAS = {
    'exames': {
        'laboratorio': {
            '1': "Agendamento coleta domiciliar: ligue para (XX) XXXX-XXXX ou acesse nosso site.",
            '2': "Resultado anatomopatológico disponível em até 15 dias úteis.",
            '3': "Rotinas: Hemograma, EAS, TGP, TGO."
        },
        'imagem': {
            '1': "Para Tomografia, tenha o pedido médico e ligue (XX) XXXX-XXXX.",
            '2': "Para Ressonância, tenha o pedido médico e ligue (XX) XXXX-XXXX.",
            '3': "Para Raio X, tenha o pedido médico e ligue (XX) XXXX-XXXX."
        },
        'resultados': {
            '1': "Resultados de Imagens disponíveis no portal em até 10 dias úteis.",
            '2': "Resultados de Laboratório disponíveis no portal em 5 a 7 dias úteis."
        }
    },
    'consultas': {
        'especialidades': {
            '1': "Clínica Médica - Dr. João Silva",
            '2': "Cardiologia - Dra. Maria Santos", 
            '3': "Endocrinologia - Dr. Pedro Costa",
            '4': "Pneumologia - Dra. Ana Oliveira",
            '5': "Dermatologia - Dr. Carlos Lima",
            '6': "Psicologia - Dra. Juliana Rocha"
        },
        'remarcar': "Para remarcar consulta, ligue para (XX) XXXX-XXXX com 24h de antecedência.",
        'confirmar': "Confirmação automática por SMS 48h antes da consulta."
    },
    'autorizacoes': {
        '1': "Autorização para Exames de Imagem: enviada para operadora, prazo de 72h.",
        '2': "Autorização para Exames de Laboratório: liberada automaticamente.", 
        '3': "Autorização para Mamografia: enviada para operadora, prazo de 48h.",
        '4': "Autorização para MAPA/HOLTER: necessita avaliação cardiologista.",
        '5': "Autorização para Ultrassonografia: liberada em 24h.",
        '6': "Autorização para Densitometria: enviada para operadora, prazo de 72h."
    },
}

@consultorio_bp.route('/menu', methods=['GET'])
def get_menu():
    """Retorna o menu principal"""
    return jsonify({
        'titulo': 'Bem vindo(a) ao Consultório MD. Selecione uma opção:',
        'opcoes': [
            {'id': '1', 'texto': 'Exames', 'rota': '/exames'},
            {'id': '2', 'texto': 'Consultas', 'rota': '/consultas'},
            {'id': '3', 'texto': 'Autorizações', 'rota': '/autorizacoes'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/exames', methods=['GET'])
def get_exames_menu():
    """Retorna o menu de exames"""
    return jsonify({
        'titulo': 'Menu de Exames - Selecione uma opção:',
        'opcoes': [
            {'id': '1', 'texto': 'Laboratório', 'rota': '/laboratorio'},
            {'id': '2', 'texto': 'Imagem', 'rota': '/imagem'},
            {'id': '3', 'texto': 'Resultados', 'rota': '/resultados'},
            {'id': '0', 'texto': 'Voltar', 'rota': '/menu'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/laboratorio', methods=['GET'])
def get_laboratorio_menu():
    """Retorna o menu de laboratório"""
    return jsonify({
        'titulo': 'Laboratório - Selecione uma opção:',
        'opcoes': [
            {'id': '1', 'texto': 'Agendar coleta domiciliar'},
            {'id': '2', 'texto': 'Exames anatomopatológicos'},
            {'id': '3', 'texto': 'Rotinas de Exames'},
            {'id': '0', 'texto': 'Voltar', 'rota': '/exames'},
            {'id': '9', 'texto': 'Menu Principal', 'rota': '/menu'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/imagem', methods=['GET'])
def get_imagem_menu():
    """Retorna o menu de imagens"""
    return jsonify({
        'titulo': 'Exames de Imagem - Selecione uma opção:',
        'opcoes': [
            {'id': '1', 'texto': 'Agendar Tomografia'},
            {'id': '2', 'texto': 'Agendar Ressonância'},
            {'id': '3', 'texto': 'Agendar Raio X'},
            {'id': '0', 'texto': 'Voltar', 'rota': '/exames'},
            {'id': '9', 'texto': 'Menu Principal', 'rota': '/menu'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/resultados', methods=['GET'])
def get_resultados_menu():
    """Retorna o menu de resultados"""
    return jsonify({
        'titulo': 'Resultados - Selecione uma opção:',
        'opcoes': [
            {'id': '1', 'texto': 'Resultado Imagens'},
            {'id': '2', 'texto': 'Resultado Laboratório'},
            {'id': '0', 'texto': 'Voltar', 'rota': '/exames'},
            {'id': '9', 'texto': 'Menu Principal', 'rota': '/menu'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/consultas', methods=['GET'])
def get_consultas_menu():
    """Retorna o menu de consultas"""
    return jsonify({
        'titulo': 'Agendamento de Consultas - Selecione uma opção:',
        'opcoes': [
            {'id': '1', 'texto': 'Selecionar Especialidade', 'rota': '/especialidades'},
            {'id': '2', 'texto': 'Remarcar Consulta'},
            {'id': '3', 'texto': 'Confirmar Consulta'},
            {'id': '0', 'texto': 'Voltar', 'rota': '/menu'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/especialidades', methods=['GET'])
def get_especialidades_menu():
    """Retorna o menu de especialidades"""
    return jsonify({
        'titulo': 'Especialidades Disponíveis - Selecione uma:',
        'opcoes': [
            {'id': '1', 'texto': 'Clínica Médica - Dr. João Silva'},
            {'id': '2', 'texto': 'Cardiologia - Dra. Maria Santos'},
            {'id': '3', 'texto': 'Endocrinologia - Dr. Pedro Costa'},
            {'id': '4', 'texto': 'Pneumologia - Dra. Ana Oliveira'},
            {'id': '5', 'texto': 'Dermatologia - Dr. Carlos Lima'},
            {'id': '6', 'texto': 'Psicologia - Dra. Juliana Rocha'},
            {'id': '0', 'texto': 'Voltar', 'rota': '/consultas'},
            {'id': '9', 'texto': 'Menu Principal', 'rota': '/menu'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/autorizacoes', methods=['GET'])
def get_autorizacoes_menu():
    """Retorna o menu de autorizações - NOVA ROTA ADICIONADA"""
    return jsonify({
        'titulo': 'Autorizações - Selecione o exame:',
        'opcoes': [
            {'id': '1', 'texto': 'Exames de Imagem'},
            {'id': '2', 'texto': 'Exames de Laboratório'},
            {'id': '3', 'texto': 'Mamografia'},
            {'id': '4', 'texto': 'MAPA - HOLTER'},
            {'id': '5', 'texto': 'Ultrassonografia'},
            {'id': '6', 'texto': 'Densitometria'},
            {'id': '0', 'texto': 'Voltar', 'rota': '/menu'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/resposta', methods=['POST'])
def get_resposta():
    """Retorna a resposta baseada na navegação do usuário - CORRIGIDA"""
    data = request.get_json()
    caminho = data.get('caminho', [])
    
    try:
        # Menu principal
        if len(caminho) == 1:
            opcao = caminho[0]
            if opcao == '3':  # Autorizações no menu principal
                return jsonify({'resposta': 'Selecione uma opção do menu de autorizações'})
        
        # Submenus (2 níveis)
        elif len(caminho) == 2:
            categoria = caminho[0]
            subcategoria = caminho[1]
            
            if categoria == '1':  # Exames
                if subcategoria == '1':  # Laboratório
                    return jsonify({'resposta': 'Selecione uma opção do laboratório'})
                elif subcategoria == '2':  # Imagem
                    return jsonify({'resposta': 'Selecione uma opção de exames de imagem'})
                elif subcategoria == '3':  # Resultados
                    return jsonify({'resposta': 'Selecione uma opção de resultados'})
            
            elif categoria == '2':  # Consultas
                if subcategoria == '1':  # Especialidades
                    return jsonify({'resposta': 'Selecione uma especialidade'})
                elif subcategoria == '2':  # Remarcar
                    return jsonify({'resposta': RESPOSTAS['consultas']['remarcar']})
                elif subcategoria == '3':  # Confirmar
                    return jsonify({'resposta': RESPOSTAS['consultas']['confirmar']})
            
            elif categoria == '3':  # Autorizações
                if subcategoria in RESPOSTAS['autorizacoes']:
                    return jsonify({'resposta': RESPOSTAS['autorizacoes'][subcategoria]})
        
        # Opções específicas (3 níveis)
        elif len(caminho) == 3:
            categoria = caminho[0]
            subcategoria = caminho[1]
            opcao = caminho[2]
            
            if categoria == '1':  # Exames
                if subcategoria == '1' and opcao in RESPOSTAS['exames']['laboratorio']:  # Laboratório
                    return jsonify({'resposta': RESPOSTAS['exames']['laboratorio'][opcao]})
                elif subcategoria == '2' and opcao in RESPOSTAS['exames']['imagem']:  # Imagem
                    return jsonify({'resposta': RESPOSTAS['exames']['imagem'][opcao]})
                elif subcategoria == '3' and opcao in RESPOSTAS['exames']['resultados']:  # Resultados
                    return jsonify({'resposta': RESPOSTAS['exames']['resultados'][opcao]})
            
            elif categoria == '2' and subcategoria == '1':  # Consultas > Especialidades
                if opcao in RESPOSTAS['consultas']['especialidades']:
                    return jsonify({'resposta': f"Especialidade selecionada: {RESPOSTAS['consultas']['especialidades'][opcao]}. Para agendar, ligue (XX) XXXX-XXXX."})
        
        return jsonify({'erro': 'Opção não encontrada'}), 404
    
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@consultorio_bp.route('/agendar', methods=['POST'])
def agendar_consulta():
    """Processa agendamento de consulta"""
    data = request.get_json()
    nome = data.get('nome', '')
    nascimento = data.get('nascimento', '')
    especialidade_id = data.get('especialidade', '')
    acao = data.get('acao', 'agendar')  # agendar, remarcar, confirmar
    
    if not nome or not nascimento or not especialidade_id:
        return jsonify({'erro': 'Dados incompletos'}), 400
    
    especialidade = RESPOSTAS['consultas']['especialidades'].get(especialidade_id, 'Especialidade não encontrada')
    
    if acao == 'agendar':
        resposta = f"Consulta de {nome} (nasc: {nascimento}) marcada com sucesso na especialidade {especialidade}!"
    elif acao == 'remarcar':
        nova_data = data.get('nova_data', '')
        resposta = f"Consulta de {nome} (nasc: {nascimento}) remarcada para {nova_data} na especialidade {especialidade}."
    elif acao == 'confirmar':
        data_consulta = data.get('data_consulta', '')
        resposta = f"Consulta de {nome} (nasc: {nascimento}) confirmada para {data_consulta} na especialidade {especialidade}."
    else:
        return jsonify({'erro': 'Ação inválida'}), 400
    
    return jsonify({'resposta': resposta})

