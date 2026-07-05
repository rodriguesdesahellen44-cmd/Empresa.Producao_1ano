#!/bin/bash

# Script Simples de Execução - Nexus Infinity

cd /home/hellen/Desktop/Nexus.Infinity

source .venv/bin/activate

echo "Iniciando Nexus Infinity..."
echo " Abrindo no navegador em http://127.0.0.1:5000"
echo ""
echo "Pressione Ctrl+C para encerrar"
echo ""

python3 app.py
