#!/bin/bash

show_menu() {
    echo "=============================="
    echo "   Gestor de Sistema Web"
    echo "=============================="
    echo "[1] Setup/Build"
    echo "[2] Iniciar Site"
    echo "[3] Parar Site"
    echo "[4] Monitorizar Logs"
    echo "[5] Limpeza Total"
    echo "[0] Sair"
    echo -n "Escolha uma opção: "
}

setup() {
    echo "[SETUP] A verificar pastas..."
    mkdir -p html
    echo "[SETUP] A construir imagens..."
    docker compose build
}

start_site() {
    echo "[START] A iniciar contentores..."
    docker compose up -d
}

stop_site() {
    echo "[STOP] A parar contentores..."
    docker compose down
}

logs() {
    echo "[LOGS] A mostrar logs..."
    docker compose logs -f
}

clean_all() {
    echo "[CLEAN] A remover pasta html..."
    rm -rf html
    echo "[CLEAN] A remover contentores e imagens..."
    docker compose down --rmi all --volumes --remove-orphans
}

while true; do
    show_menu
    read opt
    case $opt in
        1) setup ;;
        2) start_site ;;
        3) stop_site ;;
        4) logs ;;
        5) clean_all ;;
        0) exit ;;
        *) echo "Opção inválida!" ;;
    esac
done
