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
            '1': "Clínica Médica",
            '2': "Cardiologia", 
            '3': "Endocrinologia",
            '4': "Pneumologia",
            '5': "Dermatologia",
            '6': "Psicologia"
        }
    },
    'autorizacoes': "Menu de autorizações ainda não implementado."
}

@consultorio_bp.route('/menu', methods=['GET'])
def get_menu():
    """Retorna o menu principal"""
    return jsonify({
        'titulo': 'Consultório MD',
        'opcoes': [
            {'id': '1', 'texto': 'Exames'},
            {'id': '2', 'texto': 'Consultas'},
            {'id': '3', 'texto': 'Autorizações'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/exames', methods=['GET'])
def get_exames_menu():
    """Retorna o menu de exames"""
    return jsonify({
        'titulo': 'Menu de Exames',
        'opcoes': [
            {'id': '1', 'texto': 'Laboratório'},
            {'id': '2', 'texto': 'Imagem'},
            {'id': '3', 'texto': 'Resultados'},
            {'id': '0', 'texto': 'Voltar'},
            {'id': '9', 'texto': 'Menu Principal'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/laboratorio', methods=['GET'])
def get_laboratorio_menu():
    """Retorna o menu de laboratório"""
    return jsonify({
        'titulo': 'Menu de Laboratório',
        'opcoes': [
            {'id': '1', 'texto': 'Agendar coleta domiciliar'},
            {'id': '2', 'texto': 'Exames anatomopatológicos'},
            {'id': '3', 'texto': 'Rotinas de Exames'},
            {'id': '0', 'texto': 'Voltar'},
            {'id': '9', 'texto': 'Menu Principal'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/imagem', methods=['GET'])
def get_imagem_menu():
    """Retorna o menu de imagens"""
    return jsonify({
        'titulo': 'Menu de Imagens',
        'opcoes': [
            {'id': '1', 'texto': 'Agendar Tomografia'},
            {'id': '2', 'texto': 'Agendar Ressonância'},
            {'id': '3', 'texto': 'Agendar Raio X'},
            {'id': '0', 'texto': 'Voltar'},
            {'id': '9', 'texto': 'Menu Principal'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/resultados', methods=['GET'])
def get_resultados_menu():
    """Retorna o menu de resultados"""
    return jsonify({
        'titulo': 'Menu de Resultados',
        'opcoes': [
            {'id': '1', 'texto': 'Resultado Imagens'},
            {'id': '2', 'texto': 'Resultado Laboratório'},
            {'id': '0', 'texto': 'Voltar'},
            {'id': '9', 'texto': 'Menu Principal'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/consultas', methods=['GET'])
def get_consultas_menu():
    """Retorna o menu de consultas"""
    return jsonify({
        'titulo': 'Agendamento de Consultas',
        'opcoes': [
            {'id': '1', 'texto': 'Selecionar Especialidade'},
            {'id': '2', 'texto': 'Remarcar Consulta'},
            {'id': '3', 'texto': 'Confirmar Consulta'},
            {'id': '0', 'texto': 'Voltar'},
            {'id': '9', 'texto': 'Menu Principal'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/especialidades', methods=['GET'])
def get_especialidades_menu():
    """Retorna o menu de especialidades"""
    return jsonify({
        'titulo': 'Especialidades',
        'opcoes': [
            {'id': '1', 'texto': 'Clínica Médica'},
            {'id': '2', 'texto': 'Cardiologia'},
            {'id': '3', 'texto': 'Endocrinologia'},
            {'id': '4', 'texto': 'Pneumologia'},
            {'id': '5', 'texto': 'Dermatologia'},
            {'id': '6', 'texto': 'Psicologia'},
            {'id': '0', 'texto': 'Voltar'},
            {'id': '9', 'texto': 'Menu Principal'},
            {'id': 'X', 'texto': 'Encerrar contato'}
        ]
    })

@consultorio_bp.route('/resposta', methods=['POST'])
def get_resposta():
    """Retorna a resposta baseada na navegação do usuário"""
    data = request.get_json()
    caminho = data.get('caminho', [])
    
    try:
        if len(caminho) == 1:
            # Menu principal
            opcao = caminho[0]
            if opcao == '3':
                return jsonify({'resposta': RESPOSTAS['autorizacoes']})
        
            elif len(caminho) == 3:
                if caminho[0] == '1' and caminho[1] == '1':  # Exames > Laboratório
                    opcao_lab = caminho[2]
                if opcao_lab in RESPOSTAS['exames']['laboratorio']:
                    return jsonify({'resposta': RESPOSTAS['exames']['laboratorio'][opcao_lab]})

            elif caminho[0] == '1' and caminho[1] == '2':  # Exames > Imagem
                opcao_img = caminho[2]
                if opcao_img in RESPOSTAS['exames']['imagem']:
                    return jsonify({'resposta': RESPOSTAS['exames']['imagem'][opcao_img]})

            elif caminho[0] == '1' and caminho[1] == '3':  # Exames > Resultados
                opcao_res = caminho[2]
                if opcao_res in RESPOSTAS['exames']['resultados']:
                    return jsonify({'resposta': RESPOSTAS['exames']['resultados'][opcao_res]})
        
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

