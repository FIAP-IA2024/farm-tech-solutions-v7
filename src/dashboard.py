import streamlit as st
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import importlib.util
import subprocess
import tempfile
import math
import time
import requests
import json
from datetime import datetime
from pathlib import Path

# Add project root to path for proper imports
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

# Paths to phase modules
PHASE1_PATH = Path(__file__).parent / 'phases' / 'v1'
PHASE2_PATH = Path(__file__).parent / 'phases' / 'v2'
PHASE3_PATH = Path(__file__).parent / 'phases' / 'v3'
PHASE6_PATH = Path(__file__).parent / 'phases' / 'v6'

# Import modules dynamically
def import_module_from_file(module_name, file_path):
    try:
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None:
            return None
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        st.error(f"Error importing {module_name} from {file_path}: {e}")
        return None

# Configure page
st.set_page_config(
    page_title="FarmTech System - Dashboard Integrado",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add sidebar for navigation
st.sidebar.title("FarmTech System")
st.sidebar.subheader("Dashboard Integrado")
st.sidebar.markdown("---")

# Inicializar a sessão state para a página selecionada se não existir
if 'selected_page' not in st.session_state:
    st.session_state.selected_page = 'Home'

# Função para mudar a página quando um botão é clicado
def change_page(page):
    st.session_state.selected_page = page
    
# Adicionar CSS personalizado para melhorar aparência dos botões
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
        border: 2px solid #e0e0e0;
        padding: 12px 20px;
        text-align: left;
        background-color: transparent;
        color: #FAFAFA;
        border-radius: 5px;
        margin-bottom: 12px;
        font-weight: normal;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
    }
    div.stButton > button:focus:not(:active) {
        border-color: #ff4b4b;
        box-shadow: none;
    }
    /* Estilo para o botão ativo */
    .stButton > [data-testid*="primary"] {
        border: 2px solid #ff4b4b !important;
        background-color: rgba(255, 75, 75, 0.1) !important;
        color: #ff4b4b !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True
)

# Definir os ícones e páginas no menu de navegação
st.sidebar.markdown("### Navegação")

# Botão Home
if st.sidebar.button("🏛 Home", key="home_btn", use_container_width=True, type="primary" if st.session_state.selected_page == "Home" else "secondary"):
    change_page("Home")
    st.rerun()

# Botão Fase 1
if st.sidebar.button("🌱 Fase 1: Plantio & Clima", key="fase1_btn", use_container_width=True, type="primary" if st.session_state.selected_page == "Fase 1: Plantio & Clima" else "secondary"):
    change_page("Fase 1: Plantio & Clima")
    st.rerun()
    
# Botão Fase 2
if st.sidebar.button("📊 Fase 2: Banco de Dados", key="fase2_btn", use_container_width=True, type="primary" if st.session_state.selected_page == "Fase 2: Banco de Dados" else "secondary"):
    change_page("Fase 2: Banco de Dados")
    st.rerun()
    
# Botão Fase 3
if st.sidebar.button("💧 Fase 3: Irrigação IoT", key="fase3_btn", use_container_width=True, type="primary" if st.session_state.selected_page == "Fase 3: Irrigação IoT" else "secondary"):
    change_page("Fase 3: Irrigação IoT")
    st.rerun()
    
# Botão Fase 6
if st.sidebar.button("📷 Fase 6: Visão Computacional", key="fase6_btn", use_container_width=True, type="primary" if st.session_state.selected_page == "Fase 6: Visão Computacional" else "secondary"):
    change_page("Fase 6: Visão Computacional")
    st.rerun()

# Botão Alertas (Sistema de alertas AWS)
if st.sidebar.button("🔔 Alertas", key="alertas_btn", use_container_width=True, type="primary" if st.session_state.selected_page == "Alertas" else "secondary"):
    change_page("Alertas")
    st.rerun()

# Adicionar separação após os botões
st.sidebar.markdown("---")

# Usar a página selecionada da session_state
selected_page = st.session_state.selected_page

# Conteúdo principal baseado na página selecionada

# Página inicial
if selected_page == "Home":
    st.title("🌱 FarmTech System - Dashboard Integrado")
    
    # Exibir introdução do projeto
    st.markdown(
        """
        ## Bem-vindo ao Dashboard Integrado FarmTech System!
        
        Este dashboard integra as principais fases do projeto FarmTech Solutions, consolidando ferramentas e funcionalidades
        desenvolvidas ao longo do curso em uma única interface intuitiva.
        
        ### Sobre o Projeto
        
        O FarmTech Solutions é um sistema de gestão agrícola que utiliza tecnologias modernas para otimizar o manejo de culturas
        e recursos, melhorando a produtividade e sustentabilidade na agricultura.
        
        ### Funcionalidades Integradas
        
        Este dashboard reúne as seguintes fases do projeto:
        
        - **Fase 1: Plantio & Clima**
          Cálculo de áreas de plantio, gerenciamento de culturas e consulta de dados meteorológicos.
        
        - **Fase 2: Banco de Dados**
          Estrutura relacional para armazenamento e gestão de informações agrícolas.
        
        - **Fase 3: Irrigação IoT**
          Simulação de dispositivos IoT para monitoramento e controle de sistemas de irrigação.
        
        - **Fase 6: Visão Computacional**
          Implementação de técnicas de detecção de objetos usando o framework YOLO.
        
        ### Como Usar
        
        Utilize o menu de navegação na barra lateral para acessar as diferentes fases do projeto.
        Cada fase possui suas próprias funcionalidades e interfaces específicas.
        
        ### Desenvolvido por:
        Alunos da FIAP - Curso de Pós-Graduação em Inteligência Artificial e Machine Learning
        """
    )
    
    # Adicionar imagem ou card para cada fase na página inicial
    st.subheader("Acesso Rápido")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Fase 1: Plantio & Clima**\n\nCálculo de áreas de plantio e dados meteorológicos.")
        st.info("**Fase 2: Banco de Dados**\n\nModelos relacionais e estrutura de dados.")
    
    with col2:
        st.info("**Fase 3: Irrigação IoT**\n\nMonitoramento e controle de sistemas de irrigação.")
        st.info("**Fase 6: Visão Computacional**\n\nDetecção de objetos usando YOLO.")

# Fase 1: Planting area calculation and weather data
elif selected_page == "Fase 1: Plantio & Clima":
    st.header("Fase 1: Cálculo de Área de Plantio e Dados Meteorológicos")
    st.markdown(
        """
        Esta fase permite calcular áreas de plantio, gerenciar culturas e obter dados meteorológicos atuais.
        """
    )
    
    # Import modules from Phase 1
    sys.path.append(str(PHASE1_PATH))
    
    try:
        # Import the main_streamlit module (without executing the main function)
        phase1_module_spec = importlib.util.spec_from_file_location(
            "main_streamlit", os.path.join(project_root, "src", "phases", "v1", "main_streamlit.py")
        )
        phase1_module = importlib.util.module_from_spec(phase1_module_spec)
        phase1_module_spec.loader.exec_module(phase1_module)
        
        # Now we can access the functions from Phase 1
        # Tab for Phase 1
        phase1_tab1, phase1_tab2 = st.tabs(["Gerenciamento de Culturas", "Dados Meteorológicos"])
        
        # Tab 1: Crop Management - using functions from Phase 1
        with phase1_tab1:
            st.subheader("Manage Crop Data")
            
            # Load existing data
            df = phase1_module.load_from_csv()
            
            # Form for adding new data
            with st.form("crop_data_form"):
                st.write("Add New Crop Data")
                
                # Input fields
                crop = st.selectbox("Select Crop:", phase1_module.VALID_CROPS)
                col1, col2 = st.columns(2)
                
                with col1:
                    if crop == "Corn":
                        length = st.number_input("Length (m):", min_value=0.1, value=1.0, step=0.1)
                    else:
                        length = st.number_input("Radius (m):", min_value=0.1, value=1.0, step=0.1)
                
                with col2:
                    if crop == "Corn":
                        width = st.number_input("Width (m):", min_value=0.1, value=1.0, step=0.1)
                    else:
                        width = st.number_input("Width (not used for Coffee):", min_value=0.1, value=1.0, step=0.1, disabled=True)
                
                # Calculate button
                submitted = st.form_submit_button("Calculate and Add")
                
                if submitted:
                    # Calculate area based on crop type
                    if crop == "Corn":
                        area = phase1_module.calculate_rectangle_area(length, width)
                    else:  # Coffee
                        area = phase1_module.calculate_circle_area(length)
                    
                    # Calculate inputs needed
                    input_needed = phase1_module.calculate_inputs(crop, area)
                    
                    # Add to dataframe
                    new_row = pd.DataFrame({"Crop": [crop], "Area": [area], "Input Needed": [input_needed]})
                    df = pd.concat([df, new_row], ignore_index=True)
                    
                    # Save to CSV
                    phase1_module.save_to_csv(df)
                    
                    st.success(f"Added new {crop} data with area {area:.2f} and input needed {input_needed:.2f}")
                    st.rerun()
            
            # Display existing data
            if not df.empty:
                st.subheader("Existing Crop Data")
                
                # Format the dataframe for display
                display_df = df.copy()
                display_df["Area"] = display_df["Area"].apply(lambda x: f"{x:.2f}")
                display_df["Input Needed"] = display_df["Input Needed"].apply(lambda x: f"{x:.2f}")
                
                # Add an index column for row selection
                display_df.insert(0, "#", range(1, len(display_df) + 1))
                
                st.dataframe(display_df, use_container_width=True)
                
                # Actions for selected rows
                col1, col2 = st.columns(2)
                
                with col1:
                    # Delete selected rows
                    rows_to_delete = st.multiselect(
                        "Select rows to delete:", 
                        options=list(range(1, len(df) + 1)),
                        format_func=lambda x: f"Row {x}"
                    )
                    
                    if st.button("Delete Selected", type="primary", use_container_width=True):
                        if rows_to_delete:
                            # Convert 1-based index to 0-based index
                            indices = [i-1 for i in rows_to_delete]
                            df = df.drop(indices).reset_index(drop=True)
                            phase1_module.save_to_csv(df)
                            st.success(f"Deleted {len(rows_to_delete)} row(s)")
                            st.rerun()
                            
                with col2:
                    # Update row
                    if not df.empty:
                        row_to_update = st.selectbox(
                            "Select a row to update:",
                            options=list(range(1, len(df) + 1)),
                            format_func=lambda x: f"Row {x}: {df.iloc[x-1]['Crop']}"
                        )
                        
                        if st.button("Edit Selected Row", type="secondary", use_container_width=True):
                            st.session_state.edit_row = row_to_update - 1  # Store 0-based index
                
                # Edit form appears when a row is selected for editing
                if "edit_row" in st.session_state and len(df) > 0:
                    row_idx = st.session_state.edit_row
                    if row_idx < len(df):
                        row_data = df.iloc[row_idx]
                        
                        st.subheader(f"Edit Row {row_idx + 1}")
                        
                        with st.form("edit_form"):
                            edit_crop = st.selectbox(
                                "Crop:", phase1_module.VALID_CROPS, 
                                index=phase1_module.VALID_CROPS.index(row_data["Crop"])
                            )
                            
                            col1, col2 = st.columns(2)
                            with col1:
                                if edit_crop == "Corn":
                                    # For rectangle, we need to reverse-calculate length and width
                                    # Since we only store area, we'll assume square (length = width) for simplicity
                                    old_length = math.sqrt(row_data["Area"]) if edit_crop == "Corn" else row_data["Area"] / math.pi
                                    edit_length = st.number_input(
                                        "Length (m):", min_value=0.1, value=float(old_length), step=0.1
                                    )
                                else:
                                    # For circle, we need to reverse-calculate radius
                                    old_radius = math.sqrt(row_data["Area"] / math.pi)
                                    edit_length = st.number_input(
                                        "Radius (m):", min_value=0.1, value=float(old_radius), step=0.1
                                    )
                            
                            with col2:
                                if edit_crop == "Corn":
                                    edit_width = st.number_input(
                                        "Width (m):", min_value=0.1, value=float(old_length), step=0.1
                                    )
                                else:
                                    edit_width = st.number_input(
                                        "Width (not used for Coffee):", min_value=0.1, value=1.0, step=0.1, disabled=True
                                    )
                            
                            # Use colunas para os botões ficarem lado a lado
                            btn_col1, btn_col2 = st.columns(2)
                            with btn_col1:
                                update_submitted = st.form_submit_button("Update", use_container_width=True)
                            with btn_col2:
                                cancel = st.form_submit_button("Cancel", use_container_width=True)
                            
                            if update_submitted:
                                # Calculate new area and input needed
                                if edit_crop == "Corn":
                                    new_area = phase1_module.calculate_rectangle_area(edit_length, edit_width)
                                else:
                                    new_area = phase1_module.calculate_circle_area(edit_length)
                                
                                new_input = phase1_module.calculate_inputs(edit_crop, new_area)
                                
                                # Update the dataframe
                                df.at[row_idx, "Crop"] = edit_crop
                                df.at[row_idx, "Area"] = new_area
                                df.at[row_idx, "Input Needed"] = new_input
                                
                                # Save changes
                                phase1_module.save_to_csv(df)
                                
                                # Clear edit state and refresh
                                del st.session_state.edit_row
                                st.success("Row updated successfully!")
                                st.rerun()
                            
                            if cancel:
                                del st.session_state.edit_row
                                st.rerun()
            else:
                st.info("No crop data available. Add some data using the form above.")
        
        # Tab 2: Weather Data
        with phase1_tab2:
            st.subheader("Weather Data")
            st.write("Get current weather information for any city.")
            
            city = st.text_input("Enter city name:", "Sao Paulo", key="phase1_weather_input")
            
            if st.button("Get Weather Data", key="phase1_weather_button"):
                weather_data = phase1_module.get_weather_data(city)
                
                if weather_data:
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.metric("Temperature", f"{weather_data['temperature']}°C")
                        st.metric("Humidity", f"{weather_data['humidity']}%")
                    
                    with col2:
                        st.metric("Wind Speed", f"{weather_data['wind_speed']} m/s")
                        st.metric("Conditions", weather_data['description'].capitalize())
                    
                    st.success(f"Current weather data for {city} retrieved successfully!")
                else:
                    st.error(f"Failed to retrieve weather data for {city}. Please check the city name and your API key.")
    except Exception as e:
        st.error(f"Error integrating Phase 1: {e}")
        st.info("Alternatively, you can run Phase 1 directly with the following command:")
        main_script = os.path.join(project_root, "src", "phases", "v1", "main_streamlit.py")
        st.code(f"{sys.executable} -m streamlit run {main_script}", language="bash")


# Phase 2: Database Structure
# Fase 2: Database Structure
elif selected_page == "Fase 2: Banco de Dados":
    st.header("Fase 2: Estrutura de Banco de Dados")
    st.markdown(
        """
        Esta fase fornece a estrutura de banco de dados relacional para gerenciar insumos agrícolas.
        """
    )
    
    # Display the database diagram
    st.subheader("Diagrama Entidade-Relacionamento")
    diagram_path = PHASE2_PATH / "diagram.png"
    if diagram_path.exists():
        st.image(str(diagram_path), caption="Diagrama Entidade-Relacionamento do Banco de Dados")
    else:
        st.warning("Diagrama do banco de dados não encontrado.")
    
    # Show SQL Schema
    st.subheader("Esquema SQL")
    sql_path = PHASE2_PATH / "data-model.sql"
    if sql_path.exists():
        with open(sql_path, 'r') as f:
            sql_content = f.read()
        st.code(sql_content, language="sql")
    else:
        st.warning("Arquivo de esquema SQL não encontrado.")

# Phase 3: IoT Irrigation
# Fase 3: IoT Irrigation
elif selected_page == "Fase 3: Irrigação IoT":
    st.header("Fase 3: Lógica de Irrigação IoT")
    st.markdown(
        """
        Esta fase simula dispositivos IoT para monitoramento e controle de sistemas de irrigação.
        """
    )
    
    # Import the necessary modules from Phase 3
    try:
        # Add Phase 3 to path
        sys.path.append(str(PHASE3_PATH / "app"))
        
        # Try to import the modules
        weather_module = import_module_from_file("weather", str(PHASE3_PATH / "app" / "weather.py"))
        database_module = import_module_from_file("database", str(PHASE3_PATH / "app" / "database.py"))
        
        if weather_module and database_module:
            # Weather data
            st.subheader("Dados Meteorológicos")
            city = st.text_input("Digite o nome da cidade:", "Sao Paulo", key="phase3_city_input")
            
            if st.button("Obter Dados Meteorológicos", key="run_phase3_weather"):
                try:
                    weather_data = weather_module.get_weather_data(city)
                    if weather_data:
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Temperatura (°C)", weather_data["temperature"])
                        with col2:
                            st.metric("Umidade (%)", weather_data["humidity"])
                        st.write(f"Descrição: {weather_data['description'].capitalize()}")
                    else:
                        st.warning("Não foi possível obter dados meteorológicos. Verifique o nome da cidade.")
                except Exception as e:
                    st.error(f"Erro ao obter dados meteorológicos: {e}")
            
            # Sensor data
            st.subheader("Dados dos Sensores")
            if st.button("Carregar Dados dos Sensores", key="run_phase3_sensors"):
                try:
                    sensor_data = database_module.fetch_sensor_data()
                    if not sensor_data.empty:
                        st.dataframe(sensor_data)
                        
                        # Display some visualizations
                        st.subheader("Visualizações dos Dados dos Sensores")
                        
                        # Group by month
                        monthly_data = sensor_data.groupby("month").mean().reset_index()
                        
                        # Humidity chart
                        fig, ax = plt.subplots(figsize=(10, 4))
                        ax.plot(monthly_data["month"].astype(str), monthly_data["humidity"], marker="o")
                        ax.set_xlabel("Mês")
                        ax.set_ylabel("Umidade Média (%)")
                        ax.set_title("Umidade Média Mensal")
                        st.pyplot(fig)
                    else:
                        st.warning("Nenhum dado de sensor disponível.")
                except Exception as e:
                    st.error(f"Erro ao carregar dados dos sensores: {e}")
        else:
            st.warning("Não foi possível carregar os módulos necessários da Fase 3.")
    except Exception as e:
        st.error(f"Erro ao inicializar os componentes da Fase 3: {e}")

# Phase 6: Computer Vision
# Fase 6: Computer Vision
elif selected_page == "Fase 6: Visão Computacional":
    st.header("Fase 6: Visão Computacional para Agricultura")
    st.markdown(
        """
        Esta fase implementa visão computacional usando YOLO para detecção de objetos em aplicações agrícolas.
        """
    )
    
    # Usar tabs em vez de colunas para organizar melhor o conteúdo
    train_tab, results_tab = st.tabs(["Executar Detecção de Objetos", "Visualizar Resultados"])
    
    with train_tab:
        st.subheader("Executar Detecção de Objetos")
        epochs = st.slider("Número de épocas", min_value=10, max_value=100, value=30, step=10)
        batch_size = st.slider("Tamanho do lote (batch size)", min_value=4, max_value=32, value=16, step=4)
        
        # Adicionar log viewer para mostrar logs em tempo real
        if 'running_phase6' not in st.session_state:
            st.session_state.running_phase6 = False
            
        if 'phase6_log' not in st.session_state:
            st.session_state.phase6_log = []
        
        if st.button("Iniciar Treinamento de Detecção de Objetos", key="run_phase6"):
            try:
                # Marcar como running para mostrar progresso
                st.session_state.running_phase6 = True
                st.session_state.phase6_log = []
                
                # Inicializar o arquivo de log
                log_file_path = os.path.join(project_root, "yolo_training.log")
                if os.path.exists(log_file_path):
                    os.remove(log_file_path)
                    
                # Adicionar uma mensagem inicial ao log
                with open(log_file_path, 'w') as f:
                    f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Iniciando treinamento YOLO com {epochs} épocas e batch size {batch_size}\n")
                
                # Execute the Python script from Phase 6 in background
                cv_script = os.path.join(project_root, "src", "phases", "v6", "notebooks", "GabrielRibeiro_rm560173_pbl_fase6.py")
                
                # Rerun para atualizar a UI
                st.rerun()
                
            except Exception as e:
                st.error(f"Erro ao iniciar detecção de objetos: {e}")
                st.session_state.running_phase6 = False
        
        # Mostrar progresso e logs quando estiver rodando
        if st.session_state.running_phase6:
            # Spinner e mensagem de progresso
            with st.spinner("Treinamento de detecção de objetos em andamento... Isso pode levar vários minutos."):
                # Verificar se o processo já está rodando, se não, iniciar
                if not hasattr(st.session_state, 'phase6_process') or st.session_state.phase6_process is None:
                    # Iniciar o processo
                    cv_script = os.path.join(project_root, "src", "phases", "v6", "notebooks", "GabrielRibeiro_rm560173_pbl_fase6.py")
                    process = subprocess.Popen(
                        [
                            sys.executable, 
                            cv_script,
                            "--epochs", str(epochs),
                            "--batch-size", str(batch_size)
                        ],
                        cwd=str(project_root),
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    st.session_state.phase6_process = process
                    
                # Verificar status do processo
                process = st.session_state.phase6_process
                if process.poll() is not None:
                    # Processo terminou
                    stdout, stderr = process.communicate()
                    if process.returncode == 0:
                        st.success("Treinamento de detecção de objetos concluído com sucesso!")
                        # Adicionar o output final ao log
                        with open(os.path.join(project_root, "yolo_training.log"), 'a') as f:
                            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Treinamento concluído com sucesso!\n")
                    else:
                        st.error(f"Erro ao executar a detecção de objetos: {stderr}")
                        # Adicionar o erro ao log
                        with open(os.path.join(project_root, "yolo_training.log"), 'a') as f:
                            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Erro no treinamento: {stderr}\n")
                    
                    # Limpar o processo
                    st.session_state.phase6_process = None
                    st.session_state.running_phase6 = False
                    
                    # Rerun para atualizar a UI
                    time.sleep(1)  # Pequena pausa para permitir que o usuário veja a mensagem
                    st.rerun()
            
            # Mostrar logs em tempo real
            log_file_path = os.path.join(project_root, "yolo_training.log")
            if os.path.exists(log_file_path):
                with open(log_file_path, 'r') as f:
                    log_content = f.read()
                    
                if log_content:
                    st.subheader("Log do Treinamento (Tempo Real)")
                    
                    # Usar st.code em vez de st.text_area para mostrar logs de forma não editável
                    st.code(log_content, language="bash")
                    
                    # Adicionar indicação animada de processo em execução
                    if process.poll() is None:  # Se o processo ainda estiver rodando
                        # Criar um efeito de loading com pontos
                        import time
                        animation_chars = [".  ", ".. ", "...", "   "]
                        idx = int(time.time() * 2) % len(animation_chars)  # Atualiza a cada 0.5 segundos
                        loading_msg = f"Processo em execução {animation_chars[idx]}"
                        st.caption(loading_msg)
                    
            # Botão para cancelar o treinamento
            if st.button("Cancelar Treinamento", key="cancel_phase6"):
                if hasattr(st.session_state, 'phase6_process') and st.session_state.phase6_process is not None:
                    try:
                        st.session_state.phase6_process.terminate()
                        st.session_state.phase6_process = None
                        st.session_state.running_phase6 = False
                        st.success("Treinamento cancelado pelo usuário.")
                        
                        # Adicionar ao log
                        with open(os.path.join(project_root, "yolo_training.log"), 'a') as f:
                            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Treinamento cancelado pelo usuário.\n")
                            
                        time.sleep(1)  # Pequena pausa para permitir que o usuário veja a mensagem
                        st.rerun()
                    except Exception as e:
                        st.error(f"Erro ao cancelar o treinamento: {e}")
    
    with results_tab:
        st.subheader("Visualizar Resultados")
        st.markdown(
            """
            Após a execução da detecção de objetos, os resultados são salvos nos diretórios de resultados.
            Você pode encontrar:
            - Métricas de treinamento
            - Resultados de validação
            - Predições de teste
            - Análise de desempenho
            """
        )
        
        # Verificar resultados em ambos os diretórios: src/phases/v6/results e /results
        phase6_results_dir = os.path.join(project_root, "src", "phases", "v6", "results")
        root_results_dir = os.path.join(project_root, "results")
        
        # Criar o diretório de resultados na raiz se não existir
        if not os.path.exists(root_results_dir):
            os.makedirs(root_results_dir)
        
        # Combinar resultados de ambos os diretórios
        all_result_paths = []
        all_result_names = []
        
        # Adicionar resultados do diretório phase6_results_dir
        if os.path.exists(phase6_results_dir) and os.path.isdir(phase6_results_dir):
            phase6_results_path = Path(phase6_results_dir)
            for folder in phase6_results_path.iterdir():
                # Excluir o diretório 'comparison' da lista de resultados
                if folder.is_dir() and folder.name != 'comparison':
                    all_result_paths.append(folder)
                    all_result_names.append(f"v6/{folder.name}")
        
        # Adicionar resultados do diretório root_results_dir
        if os.path.exists(root_results_dir) and os.path.isdir(root_results_dir):
            root_results_path = Path(root_results_dir)
            for folder in root_results_path.iterdir():
                if folder.is_dir():
                    all_result_paths.append(folder)
                    all_result_names.append(f"root/{folder.name}")
        
        if all_result_paths:
            selected_result_idx = st.selectbox(
                "Selecione um resultado para visualizar:",
                options=all_result_names,
                index=0
            )
            
            # Extrair o índice do resultado selecionado
            selected_idx = all_result_names.index(selected_result_idx)
            selected_path = all_result_paths[selected_idx]
            
            # Exibir informações sobre o resultado selecionado
            st.info(f"Diretório do resultado: {selected_path}")
            
            # Encontrar imagens e arquivos de texto no diretório selecionado
            image_files = list(selected_path.glob("*.png")) + list(selected_path.glob("*.jpg"))
            text_files = list(selected_path.glob("*.txt")) + list(selected_path.glob("*.log")) + list(selected_path.glob("*.csv"))
            other_files = list(selected_path.glob("*.json")) + list(selected_path.glob("*.yaml"))
            
            # Criar tabs para diferentes tipos de arquivos
            if image_files or text_files or other_files:
                tabs = []
                if image_files:
                    tabs.append("Imagens")
                if text_files:
                    tabs.append("Arquivos de Texto")
                if other_files:
                    tabs.append("Outros Arquivos")
                
                # Criar as tabs dinamicamente com base nos tipos de arquivos encontrados
                result_tabs = st.tabs(tabs)
                
                tab_idx = 0
                
                # Tab de imagens
                if image_files:
                    with result_tabs[tab_idx]:
                        st.subheader("Imagens")
                        
                        # Criar galeria de imagens
                        selected_image = st.selectbox(
                            "Selecione uma imagem para visualizar:",
                            options=[img.name for img in image_files],
                            index=0
                        )
                        
                        # Encontrar a imagem selecionada
                        selected_img_path = next((img for img in image_files if img.name == selected_image), None)
                        
                        if selected_img_path:
                            st.image(
                                str(selected_img_path),
                                caption=selected_image,
                                use_container_width=True
                            )
                            
                            # Opção para baixar a imagem
                            with open(selected_img_path, "rb") as file:
                                st.download_button(
                                    label="Baixar Imagem",
                                    data=file,
                                    file_name=selected_image,
                                    mime="image/png" if selected_image.endswith(".png") else "image/jpeg"
                                )
                    tab_idx += 1
                
                # Tab de arquivos de texto
                if text_files:
                    with result_tabs[tab_idx]:
                        st.subheader("Arquivos de Texto")
                        
                        selected_text = st.selectbox(
                            "Selecione um arquivo de texto para visualizar:",
                            options=[txt.name for txt in text_files],
                            index=0
                        )
                        
                        # Encontrar o arquivo de texto selecionado
                        selected_txt_path = next((txt for txt in text_files if txt.name == selected_text), None)
                        
                        if selected_txt_path:
                            try:
                                with open(selected_txt_path, "r") as file:
                                    content = file.read()
                                
                                # Mostrar conteúdo com base na extensão do arquivo
                                if selected_text.endswith(".csv"):
                                    try:
                                        df = pd.read_csv(selected_txt_path)
                                        st.dataframe(df)
                                    except:
                                        st.text_area("Conteúdo do Arquivo", content, height=400)
                                else:
                                    st.text_area("Conteúdo do Arquivo", content, height=400)
                                
                                # Opção para baixar o arquivo
                                st.download_button(
                                    label="Baixar Arquivo",
                                    data=content,
                                    file_name=selected_text,
                                    mime="text/plain"
                                )
                            except Exception as e:
                                st.error(f"Erro ao ler o arquivo: {e}")
                    tab_idx += 1
                
                # Tab de outros arquivos
                if other_files:
                    with result_tabs[tab_idx]:
                        st.subheader("Outros Arquivos")
                        
                        selected_file = st.selectbox(
                            "Selecione um arquivo para visualizar:",
                            options=[f.name for f in other_files],
                            index=0
                        )
                        
                        # Encontrar o arquivo selecionado
                        selected_file_path = next((f for f in other_files if f.name == selected_file), None)
                        
                        if selected_file_path:
                            try:
                                with open(selected_file_path, "r") as file:
                                    content = file.read()
                                
                                # Exibir conteúdo JSON ou YAML formatado
                                if selected_file.endswith(".json"):
                                    import json
                                    try:
                                        json_data = json.loads(content)
                                        st.json(json_data)
                                    except:
                                        st.text_area("Conteúdo do Arquivo", content, height=400)
                                else:
                                    st.text_area("Conteúdo do Arquivo", content, height=400)
                                
                                # Opção para baixar o arquivo
                                st.download_button(
                                    label="Baixar Arquivo",
                                    data=content,
                                    file_name=selected_file,
                                    mime="application/json" if selected_file.endswith(".json") else "text/plain"
                                )
                            except Exception as e:
                                st.error(f"Erro ao ler o arquivo: {e}")
            else:
                st.info("Não foram encontrados arquivos de resultados neste diretório.")
        else:
            st.info("Nenhum resultado disponível. Execute o treinamento de detecção de objetos primeiro.")

# Página de Alertas
elif selected_page == "Alertas":
    st.header("🔔 Sistema de Alertas")
    
    st.markdown(
        """
        Este módulo permite enviar alertas para a equipe de campo quando problemas são detectados nas culturas.
        Os alertas são processados por uma função AWS Lambda e enviados por email através do Amazon SNS.
        """
    )
    
    # Criar colunas para o layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Enviar um Novo Alerta")
        
        # Criar formulário para envio de alertas
        with st.form(key='alert_form'):
            # Lista de culturas comuns para seleção
            culturas_comuns = [
                "Selecione uma cultura",
                "Milho", 
                "Soja", 
                "Café", 
                "Algodão", 
                "Cana-de-açúcar", 
                "Trigo", 
                "Feijão",
                "Outra (especificar)"
            ]
            
            # Problemas pré-definidos
            problemas_comuns = [
                "Selecione um problema",
                "Umidade do solo baixa", 
                "Possível infestação de pragas", 
                "Deficiência nutricional", 
                "Sinais de doença", 
                "Irrigação insuficiente", 
                "Irrigação excessiva",
                "Outro (especificar)"
            ]
            
            # Seleção da cultura
            cultura_selecionada = st.selectbox(
                "Cultura:",
                culturas_comuns
            )
            
            # Se 'Outra' for selecionada, permitir entrada de texto
            if cultura_selecionada == "Outra (especificar)":
                cultura_personalizada = st.text_input("Especifique a cultura:")
            
            # Seleção do problema
            problema_selecionado = st.selectbox(
                "Problema:",
                problemas_comuns
            )
            
            # Se 'Outro' for selecionado, permitir entrada de texto
            if problema_selecionado == "Outro (especificar)":
                problema_personalizado = st.text_input("Especifique o problema:")
            
            # Campo para descrição detalhada
            descricao = st.text_area("Descrição detalhada (opcional):", height=100)
            
            # Seleção de prioridade
            prioridade = st.select_slider(
                "Prioridade:",
                options=["Baixa", "Média", "Alta"],
                value="Média"
            )
            
            # Botão de envio
            submit_button = st.form_submit_button(label="Enviar Alerta")
            
            if submit_button:
                # Determinar a cultura final (selecionada ou personalizada)
                if cultura_selecionada == "Outra (especificar)":
                    cultura_final = cultura_personalizada
                elif cultura_selecionada == "Selecione uma cultura":
                    st.error("Por favor, selecione uma cultura.")
                    cultura_final = None
                else:
                    cultura_final = cultura_selecionada
                
                # Determinar o problema final (selecionado ou personalizado)
                if problema_selecionado == "Outro (especificar)":
                    problema_final = problema_personalizado
                elif problema_selecionado == "Selecione um problema":
                    st.error("Por favor, selecione um problema.")
                    problema_final = None
                else:
                    problema_final = problema_selecionado
                
                # Formatar a mensagem de alerta completa
                if cultura_final and problema_final:
                    # Adicionar a descrição se fornecida
                    mensagem_completa = f"{problema_final}"
                    if descricao:
                        mensagem_completa += f" - {descricao}"
                    
                    # Adicionar a prioridade
                    mensagem_completa += f" [Prioridade: {prioridade}]"
                    
                    try:
                        # Enviar o alerta
                        payload = {
                            "crop": cultura_final,
                            "issue": mensagem_completa
                        }
                        
                        # Fazer a requisição POST para a API Lambda
                        response = requests.post(
                            "https://wuu3yuphjl.execute-api.us-east-1.amazonaws.com/pedidos",
                            data=json.dumps(payload),
                            headers={"Content-Type": "application/json"}
                        )
                        
                        # Verificar a resposta
                        if response.status_code == 200:
                            st.success("✅ Alerta enviado com sucesso!")
                            st.balloons()
                        else:
                            st.error(f"❌ Erro ao enviar o alerta: {response.status_code}")
                            st.write("Detalhes:", response.text)
                    
                    except Exception as e:
                        st.error(f"❌ Erro ao processar o alerta: {str(e)}")
    
    with col2:
        st.subheader("Informações do Sistema")
        
        # Card explicativo sobre o sistema de alertas
        st.info(
            """
            ### Como Funciona
            
            1. **Detecção de Problemas**: Problemas podem ser identificados manualmente ou automaticamente pelos sensores IoT e sistema de visão computacional.
            
            2. **Processamento de Alertas**: Os alertas são processados por uma função AWS Lambda.
            
            3. **Notificação**: Alertas são enviados via email para a equipe de campo através do Amazon SNS.
            
            4. **Ação**: A equipe de campo toma as medidas corretivas necessárias com base nas instruções recebidas.
            """
        )
        
        st.markdown("### Exemplos de Alertas")
        
        # Exemplos de alertas em cards coloridos
        st.error(
            """
            **Alerta: Umidade do solo baixa**
            
            * **Cultura**: Milho
            * **Local**: Setor B-12
            * **Ação Requerida**: Ativar sistema de irrigação por 45 minutos
            * **Prioridade**: Alta
            """
        )
        
        st.warning(
            """
            **Alerta: Possível infestação de pragas**
            
            * **Cultura**: Soja
            * **Local**: Zona 3
            * **Ação Requerida**: Inspeção manual e aplicar pesticidas orgânicos se confirmado
            * **Prioridade**: Média
            """
        )
        
        st.info(
            """
            **Alerta: Previsão de geada**
            
            * **Culturas Afetadas**: Todas
            * **Período**: Madrugada de amanhã
            * **Ação Requerida**: Ativar sistema de proteção térmica nas culturas sensíveis
            * **Prioridade**: Alta
            """
        )

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
    <p>FarmTech System - Dashboard Integrado 2025</p>
    <p>Desenvolvido por: Gabriel Ribeiro, Jonas Felipe, Marcos Trazzini, Edimilson Ribeiro</p>
    </div>
    """, unsafe_allow_html=True
)
