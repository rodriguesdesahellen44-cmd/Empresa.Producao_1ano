#!/bin/bash

# Script de Setup Completo - Nexus Infinity

echo "Iniciando setup da Nexus Infinity..."
echo ""

# Vai para a pasta do projeto
cd /home/hellen/Desktop/Nexus.Infinity

echo " Pasta do projeto: $(pwd)"
echo ""

# Ativa o ambiente virtual
echo " Ativando ambiente virtual..."
source .venv/bin/activate

echo " Ambiente virtual ativado!"
echo ""

# Instala as dependências
echo " Instalando dependências..."
python3 -m pip install --upgrade pip -q
python3 -m pip install -r requirements.txt -q

echo "✅ Dependências instaladas!"
echo ""

# Verifica se Flask foi instalado
if python3 -c "import flask" 2>/dev/null; then
    echo "✅ Flask encontrado!"
else
    echo "❌ Erro ao instalar Flask"
    exit 1
fi

# Verifica se PyWebView foi instalado
if python3 -c "import webview" 2>/dev/null; then
    echo "✅ PyWebView encontrado!"
else
    echo "❌ Erro ao instalar PyWebView"
    exit 1
fi

echo ""
echo " Iniciando aplicação..."
echo " A janela abrirá em poucos segundos..."
echo ""

# Executa a aplicação
python3 app.py
