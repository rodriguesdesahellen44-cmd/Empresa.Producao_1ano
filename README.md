#  Nexus Infinity - Análise do Setor de Produção

##  Descrição
Aplicação interativa para apresentar análise completa da empresa **Nexus Infinity**, focando no setor de **Produção**. Desenvolvida com Flask e PyWebView, apresenta 8 seções estruturadas com informações da empresa, equipe e análise detalhada.

##  Informações do Projeto

- **Empresa Analisada:** Nexus Infinity
- **Setor:** Produção
- **Entrevistadoras:** Hellen Rodrigues e Emilly Vargas
- **Gerente:** Rebeca
- **Subgerente:** Ellen
- **Dono:** Thomas

##  Estrutura de Arquivos

```
Nexus.Infinity/
├── app.py                  # Código principal da aplicação Flask
├── requirements.txt        # Dependências do projeto
├── templates/
│   └── empresa.html       # Template HTML com as 8 seções
└── static/
    └── style.css          # Estilos CSS responsivos
```

##  Como Executar

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

Ou com pip3:
```bash
pip3 install -r requirements.txt
```

### Execução

1. **No terminal, execute:**
```bash
python3 app.py
```

2. **Uma nova janela irá abrir automaticamente com a apresentação da empresa**

##  Seções da Página

A apresentação contém 8 seções estruturadas:

### 1 Apresentação da Empresa
- Nome, área de atuação, produto/serviço principal
- Público-alvo e descrição detalhada da missão, visão e valores

###  Apresentação da Equipe
- Nomes das entrevistadoras
- Gerente e subgerente do setor de produção
- Função geral do setor

###  Função do Setor Dentro da Empresa
- Para que o setor existe
- Como ajuda a empresa
- Cenários de falha
- Problemas que resolve

###  Principais Atividades do Setor
- Lista de atividades principais (5 atividades)

###  Análise da Empresa
- Como o setor aparece na prática
- Pontos positivos
- Pontos de melhoria

###  Propostas de Melhoria
- 3 sugestões de otimização para o setor

###  Histórico da Análise
- Tabela com registro de análises realizadas em cada setor

###  Conclusão da Equipe
- Resumo final com principais aprendizados

##  Recursos

- ✅ Interface responsiva (funciona em desktop, tablet e mobile)
- ✅ Design moderno com gradientes e animações
- ✅ Tabelas interativas
- ✅ Seções coloridas para melhor visualização
- ✅ Suporte a impressão (PDF)
- ✅ Código Python bem estruturado e comentado

##  Dependências

- **Flask 2.3.2** - Framework web Python
- **pywebview 5.0.4** - Visualizador web nativo multiplataforma

##  Modificações Futuras

Para adicionar mais dados ou modificar informações:

1. Edite o dicionário `DADOS_NEXUS` no arquivo `app.py`
2. As mudanças serão refletidas automaticamente na página

##  Licença

Projeto educacional - Projeto de Análise de Empresas

---

**Desenvolvido para análise do setor de Produção da Nexus Infinity**
