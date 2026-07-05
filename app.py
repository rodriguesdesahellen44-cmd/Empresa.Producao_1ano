from flask import Flask, render_template
import webbrowser
import threading
import time

app = Flask(__name__)

# DADOS EXCLUSIVOS DO SETOR DE PRODUÇÃO DA NEXUS INFINITY
DADOS_NEXUS = {
    "apresentacao": {
        "nome": "Nexus Infinity",
        "dono": "Thomas",
        "area_atuacao": "Jogos e Brinquedos",
        "setor": "Produção",
        "gerente": "Rebeca",
        "subgerente": "Ellen",
        "entrevistadoras": "Hellen Rodrigues e Emilly Vargas",
        "produto_principal": "Fazer brinquedos e jogos com produtos recicláveis, que possa criar jogos envolventes e inovadores que proporcionem experiências únicas, despertem emoções e conectem pessoas, transformando ideias em diversão e qualidade.",
        "publico_alvo": "Pessoas de todas as idades (acima de 8 anos)",
        "descricao": "Nexus Infinity quer reunir três fatores principais: Jogos, reciclagem e valores. A missão é criar jogos envolventes e inovadores que proporcionem experiências únicas, despertem emoções e conectem pessoas, transformando ideias em diversão e qualidade. A empresa possui uma visão de ser referência global da criação de jogos reconhecida pela criatividade, qualidade e impacto positivo na vida de pessoas e nas indústrias."
    },
    "equipe": {
        "integrantes": ["Rebecca", "Guilherme", "Davi", "Nikolas", "Bryan", "Ellen"],
        "entrevistadoras": ["Hellen Rodrigues", "Emilly Vargas"],
        "setor_analisado": "Produção",
        "funcao_geral": "Produzir e criar jogos e brinquedos com materiais recicláveis."
    },
    "funcao_setor": {
        "existencia": "Existe para transformar materiais recicláveis descartados em brinquedos e jogos criativos de alta qualidade.",
        "ajuda": "Ajuda a empresa reduzindo drasticamente o custo de matéria-prima e viabilizando o propósito ecológico e sustentável da marca.",
        "se_nao_funcionasse": "Se a produção falhasse, a empresa não teria produtos para vender, gerando atrasos nas entregas e comprometendo a reputação da marca.",
        "problemas_resolvidos": "Ajuda a resolver o problema do desperdício de resíduos sólidos e a falta de opções de entretenimento sustentável no mercado."
    },
    "atividades": [
        "Organizar a criação do produto ou serviço (jogos ecológicos)",
        "Controlar materiais (estoque de recicláveis coletados)",
        "Definir etapas de trabalho na linha de montagem",
        "Verificar a qualidade e segurança dos brinquedos",
        "Cumprir prazos de fabricação e entrega"
    ],
    "analise": {
        "organizacao": "O setor de produção da Nexus Infinity foca na eficiência da triagem e higienização dos materiais. O processo criativo funciona muito bem, mas a escala de fabricação manual precisa ser otimizada.",
        "funciona_bem": "A equipe consegue criar protótipos excelentes rapidamente a partir de papelão e plásticos reaproveitados.",
        "pode_melhorar": "A escalabilidade da produção manual e a organização do estoque de recicláveis."
    },
    "melhorias": [
        "Organizar melhor as etapas de produção e separação de materiais",
        "Criar um checklist rígido de controle de qualidade para os brinquedos",
        "Reduzir desperdícios durante o corte e moldagem dos insumos"
    ],
    "historico": [
        {"data": "22/06/2026", "setor": "Marketing", "descricao": "Análise das redes sociais da empresa"},
        {"data": "22/06/2026", "setor": "Financeiro", "descricao": "Levantamento dos possíveis custos"},
        {"data": "22/06/2026", "setor": "Produção", "descricao": "Estudo do processo de entrega e fabricação do produto"},
        {"data": "22/06/2026", "setor": "RH", "descricao": "Análise da organização das funções da equipe de produção"}
    ],
    "conclusao": "Concluímos que o setor de Produção é o coração da Nexus Infinity, essencial para entregar jogos de qualidade. A principal melhoria sugerida foi a implementação de um checklist técnico para evitar falhas manuais e atrasos."
}

@app.route('/')
def index():
    return render_template('empresa.html', dados=DADOS_NEXUS)

def iniciar_servidor():
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    # Inicia o servidor local Flask em uma thread separada
    servidor = threading.Thread(target=iniciar_servidor, daemon=True)
    servidor.start()
    
    # Aguarda o servidor iniciar
    time.sleep(2)
    
    # Abre o navegador automaticamente
    print("🌐 Abrindo navegador...")
    webbrowser.open('http://127.0.0.1:5000')
    
    # Mantém o servidor rodando
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n✅ Servidor encerrado")
