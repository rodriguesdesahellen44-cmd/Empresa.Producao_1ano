#!/bin/bash

# Script para executar a aplicação Nexus Infinity

echo " Iniciando Nexus Infinity - Análise do Setor de Produção..."
echo ""

# Verifica se Python 3 está instalado
if ! command -v python3 &> /dev/null; then
    echo " Erro: Python 3 não está instalado"
    exit 1
fi

# Instala dependências se necessário
echo "Verificando dependências..."
pip install -r requirements.txt > /dev/null 2>&1

# Verifica se a instalação foi bem-sucedida
if [ $? -eq 0 ]; then
    echo "✅ Dependências instaladas com sucesso!"
else
    echo "  Aviso: Não foi possível instalar as dependências automaticamente"
    echo "   Execute manualmente: pip install -r requirements.txt"
fi

echo ""
echo " Abrindo aplicação na porta 5000..."
echo " A janela da aplicação será aberta automaticamente"
echo ""

# Executa a aplicação
python3 app.py

# Se a aplicação encerrar
echo ""
echo " Aplicação encerrada"
