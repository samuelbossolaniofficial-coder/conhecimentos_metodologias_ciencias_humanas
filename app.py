import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="A Sociedade Através do Tempo ⏳",
    page_icon="⏳",
    layout="centered"
)

# Estilização CSS com FUNDO PRETO, cores altamente contrastantes e textos super aprofundados
st.markdown("""
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #f1f5f9;
    }
    .main-title {
        font-size: 2.5rem;
        color: #00f0ff;
        text-align: center;
        font-weight: 900;
        text-shadow: 0 0 10px rgba(0, 240, 255, 0.4);
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 1.25rem;
        color: #ff007f;
        text-align: center;
        margin-bottom: 25px;
        font-weight: 700;
    }
    
    /* Cards com fundo escuro elegante e bordas de cores super vibrantes */
    .card-1950 { background-color: #121826; padding: 22px; border-radius: 16px; border-left: 8px solid #00b4d8; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(0,180,216,0.15); }
    .card-1970 { background-color: #121826; padding: 22px; border-radius: 16px; border-left: 8px solid #ffb703; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(255,183,3,0.15); }
    .card-1990 { background-color: #121826; padding: 22px; border-radius: 16px; border-left: 8px solid #9d4edd; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(157,78,221,0.15); }
    .card-2010 { background-color: #121826; padding: 22px; border-radius: 16px; border-left: 8px solid #06d6a0; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(6,214,160,0.15); }
    .card-hoje { background-color: #121826; padding: 22px; border-radius: 16px; border-left: 8px solid #ef476f; margin-bottom: 18px; box-shadow: 0 4px 12px rgba(239,71,111,0.15); }
    
    .box-instrucao {
        background-color: #1e293b;
        padding: 18px;
        border-radius: 14px;
        border: 2px dashed #ffb703;
        text-align: center;
        font-size: 1.1rem;
        color: #f8fafc;
        font-weight: bold;
        margin-bottom: 25px;
    }
    .explanation-box {
        background-color: #121826;
        padding: 22px;
        border-radius: 16px;
        border: 2px solid #00f0ff;
        margin-bottom: 20px;
        font-size: 1.05rem;
        color: #f1f5f9;
    }
    </style>
""", unsafe_allow_html=True)

# Controle de Navegação por Estado no Streamlit
if "pagina" not in st.session_state:
    st.session_state.pagina = "introducao"

# ----------------- TELA 1: INTRODUÇÃO -----------------
if st.session_state.pagina == "introducao":
    st.markdown('<p class="main-title">🌍 A Sociedade Através do Tempo ⏳</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Uma investigação histórica profunda sobre as mudanças e permanências sociais!</p>', unsafe_allow_html=True)
    
    st.info("👋 Olá, estudante e pesquisador(a)! Este recurso foi desenvolvido para analisar criticamente como a infraestrutura urbana, a tecnologia, a educação, as relações de trabalho e o cotidiano se transformaram no Brasil e no mundo ao longo de sete décadas.")
    
    st.write("""
    ### 🎯 Objetivos de Aprendizagem (Ciências Humanas):
    * **Compreender o Tempo Histórico:** Diferenciar cronologia (contagem de anos) de historicidade (o processo dinâmico de construção da sociedade humana).
    * **Analisar Mudanças e Permanências:** Identificar quais hábitos sociais foram totalmente substituídos pela industrialização e digitalização, e quais valores sociais (como a importância da família, da comunidade e da educação) permaneceram essenciais.
    * **Pensamento Crítico:** Investigar como a revolução técnico-científica-informacional moldou a nossa rotina atual.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 INICIAR A JORNADA HISTÓRICA", use_container_width=True):
            st.session_state.pagina = "linha_tempo"
            st.rerun()

# ----------------- TELA 2: LINHA DO TEMPO -----------------
elif st.session_state.pagina == "linha_tempo":
    st.markdown('<p class="main-title">⏳ Linha do Tempo Histórica e Detalhada</p>', unsafe_allow_html=True)
    st.markdown('<div class="box-instrucao">👇 Selecione abaixo o período histórico que deseja analisar com profundidade analítica:</div>', unsafe_allow_html=True)
    
    periodo = st.radio(
        "Escolha uma época para analisar:",
        ["1950", "1970", "1990", "2010", "Hoje"],
        horizontal=True
    )
    
    st.markdown("---")
    
    # Dicionário com informações históricas rigorosas e aprofundadas
    dados_eras = {
        "1950": {
            "titulo": "📻 Década de 1950 — Industrialização, Urbanização e o Rádio Valvulado",
            "desc": "Período marcado pelo pós-guerra mundial, pelo forte projeto de industrialização do Brasil (governo JK e o lema '50 anos em 5') e pelo acelerado êxodo rural, com populações migrando do campo para as cidades em expansão.",
            "estilo": "card-1950",
            "elementos": [
                ("📻 Mídia de Massa e Comunicação Analógica", "O rádio valvulado — construído em pesadas caixas de madeira com circuitos a válvula — era o centro da vida cultural doméstica. Através dele, radionovelas, programas de auditório e boletins informativos uniam o país. As comunicações à distância dependiam inteiramente de cartas manuscritas enviadas via Correios, cujos prazos de entrega duravam semanas."),
                ("🏫 O Sistema Escolar e a Rigidez Disciplinar", "As instituições de ensino primário e secundário operavam sob preceitos pedagógicos tradicionais e altamente autoritários. Os materiais didáticos exigiam caligrafia precisa feita com canetas tinteiro e tinteiros de mesa. O respeito irrestrito à autoridade do professor e à hierarquia escolar era a base da formação cívica."),
                ("⚡ Infraestrutura Doméstica Urbana", "A eletrificação urbana ainda era instável e restrita a áreas centrais. Os eletrodomésticos começavam a entrar timidamente nas residências (geladeiras de uma porta e fogões a gás de botijão), substituindo fogões a lenha e facilitando o trabalho doméstico, que recaía majoritariamente sobre as mulheres.")
            ]
        },
        "1970": {
            "titulo": "📺 Década de 1970 — A Chegada da TV Cores e a Vitalidade do Espaço Público",
            "desc": "Marcada politicamente pelo regime militar no Brasil e economicamente pelo chamado 'Milagre Econômico'. Houve forte expansão das rodovias federais, crescimento automotivo e consolidação da cultura urbana de massa.",
            "estilo": "card-1970",
            "elementos": [
                ("📺 A Revolução da Televisão Colorida", "Embora as transmissões em cores tenham começado oficialmente no Brasil em 1972 (com a Festa da Uva), foi ao longo dessa década que a televisão se consolidou como o principal vetor de unificação cultural nacional. Famílias inteiras e vizinhanças se reuniam para assistir a telenovelas diárias e grandes eventos esportivos, como a Copa do Mundo de 1970."),
                ("🚗 Expansão Automotiva e Mobilidade", "A indústria automobilística nacional (instalada no ABC Paulista com montadoras multinacionais) impulsionou a preferência pelo transporte rodoviário individual em detrimento de ferrovias. Carros como o Fusca, o Corcel e o Opala tornaram-se símbolos visuais das grandes metrópoles em adensamento."),
                ("🪀 Sociabilidade e Infância nas Ruas", "Como a oferta de entretenimento doméstico era restrita a alguns canais de TV aberta e o rádio, a infância urbana ocorria majoritariamente nas ruas, calçadas e praças públicas. Jogos coletivos tradicionais (pião, amarelinha, pular corda, taco/betes e carrinho de rolimã) estruturavam redes de solidariedade e convivência comunitária.")
            ]
        },
        "1990": {
            "titulo": "💾 Década de 1990 — Globalização, Abertura Econômica e a Era dos PCs",
            "desc": "Década de profundas transformações estruturais: estabilização da moeda com o Plano Real (1994), abertura do mercado brasileiro a produtos importados, redemocratização consolidada e o início da revolução digital comercial.",
            "estilo": "card-1990",
            "elementos": [
                ("💻 A Difusão Inicial dos Computadores Pessoais", "Os computadores de mesa (desktops) faziam sua entrada incipiente em escritórios corporativos e escolas de elite. Eram máquinas de alto custo, equipadas com monitores pesados de tubo de raios catódicos (CRT) e processadores limitados. Os dados e softwares eram armazenados fisicamente em disquetes magnéticos de 3.5 polegadas."),
                ("📞 Telecomunicações e a Pré-Internet", "A telefonia fixa era um bem escasso e de altíssimo valor de mercado (muitas vezes declarado no Imposto de Renda). Os telefones celulares iniciais eram analógicos, volumosos ('tijolões') e restritos a elites econômicas. A conexão à internet dependia de linhas discadas tradicionais, ativas majoritariamente após a meia-noite para baratear custos de pulso telefônico."),
                ("📚 Pesquisa Acadêmica e Fontes Impressas", "A pesquisa escolar e universitária apoiava-se fundamentalmente em mídias impressas. Bibliotecas físicas e coleções de enciclopédias volumosas (como a Barsa) eram as únicas fontes de consulta estruturada, exigindo leitura analítica e fichamentos manuais de verbetes.")
            ]
        },
        "2010": {
            "titulo": "📱 Década de 2010 — Smartphones, Redes Sociais e Sociedade em Rede",
            "desc": "O período testemunhou a conversão digital total da sociedade. A computação em nuvem, a expansão de redes móveis de alta velocidade (3G/4G) e a popularização dos smartphones transformaram radicalmente a economia, a política e as relações interpessoais.",
            "estilo": "card-2010",
            "elementos": [
                ("📱 A Explosão da Computação Móvel e Instantaneidade", "Com a popularização dos smartphones de baixo e médio custo, a internet deixou de ser um ponto fixo de acesso em desktops para se tornar onipresente. Aplicativos de mensagens instantâneas e redes sociais reconfiguraram a comunicação humana, eliminando barreiras espaciais e temporais no fluxo de informações."),
                ("🎒 Reformulação Digital da Educação", "As metodologias pedagógicas começaram a incorporar ambientes virtuais de aprendizagem, plataformas de videoaulas e enciclopédias abertas colaborativas (como a Wikipédia). A busca de dados passou a ser instantânea, exigindo das escolas novos papéis voltados à curadoria e ao pensamento crítico frente ao excesso de dados."),
                ("🎬 Disrupção no Entretenimento (Streaming)", "A indústria cultural sofreu uma guinada histórica com a transição da mídia física (CDs, DVDs) e da TV linear tradicional para plataformas de streaming por assinatura sob demanda, alterando os hábitos de consumo cultural de gerações inteiras.")
            ]
        },
        "Hoje": {
            "titulo": "🤖 Atualidade — Hiperconectividade, Inteligência Artificial e Desafios Globais",
            "desc": "O presente é caracterizado pela integração profunda de inteligência artificial generativa, automação de processos produtivos, algoritmos preditivos e debates cruciais sobre privacidade de dados (LGPD) e sustentabilidade ecológica.",
            "estilo": "card-hoje",
            "elementos": [
                ("🤖 Inteligência Artificial Generativa e Automação", "Sistemas avançados de inteligência artificial auxiliam desde a medicina diagnóstica e a logística urbana até a educação personalizada e a criação artística. A automação redefine o mercado de trabalho, exigindo novas competências cognitivas e letramento digital avançado."),
                ("🌐 Economia Globalizada em Tempo Real", "O trabalho remoto global, as transações financeiras digitais instantâneas e as reuniões virtuais em alta definição estruturam uma sociedade interdependente em escala planetária, onde crises locais repercutem instantaneamente em cadeias globais de suprimento."),
                ("♻️ Contradições e Desafios Socioambientais", "Apesar do altíssimo desenvolvimento tecnológico, a humanidade contemporânea enfrenta graves crises estruturais: desigualdades socioeconômicas persistentes, polarização informacional e a urgência climática global que demanda modelos sustentáveis de desenvolvimento para as próximas gerações.")
            ]
        }
    }
    
    info = dados_eras[periodo]
    st.subheader(info["titulo"])
    st.info(info["desc"])
    
    st.markdown("### 🔍 Análise Detalhada deste Período Histórico:")
    for cat, desc_cat in info["elementos"]:
        st.markdown(f"""
            <div class="{info['estilo']}">
                <strong>{cat}</strong><br><br>
                {desc_cat}
            </div>
        """, unsafe_allow_html=True)
            
    st.markdown("---")
    if st.button("🎯 IR PARA O SUPER QUIZ DE AVALIAÇÃO HISTÓRICA!", use_container_width=True):
        st.session_state.pagina = "quiz"
        st.rerun()

# ----------------- TELA 3: QUIZ / DESAFIO INTERATIVO -----------------
elif st.session_state.pagina == "quiz":
    st.markdown('<p class="main-title">🧠 Quiz Analítico de Ciências Humanas</p>', unsafe_allow_html=True)
    st.markdown('<div class="box-instrucao">Teste o seu entendimento crítico sobre os processos históricos estudados nas diferentes décadas!</div>', unsafe_allow_html=True)
    
    banco_questoes = [
        # 1950
        {
            "ano": "1950",
            "pergunta": "Qual fator socioeconômico e infraestrutural marcou de forma contundente a década de 1950 no Brasil?",
            "opcoes": ["O avanço acelerado da industrialização urbana e o intenso êxodo rural", "A universalização imediata de computadores portáteis nas escolas públicas", "O predomínio exclusivo da economia agrária de subsistência sem cidades", "A substituição completa dos meios de transporte por ferrovias elétricas subterrâneas"],
            "correta": 0,
            "dica": "O governo da época incentivou fortemente a vinda de indústrias e a construção de estradas, atraindo populações do campo para as cidades."
        },
        {
            "ano": "1950",
            "pergunta": "Qual equipamento tecnológico centrava a vida doméstica e o entretenimento das famílias na década de 1950?",
            "opcoes": ["O console de videogame em rede", "O rádio valvulado de madeira", "O smartphone com acesso à nuvem", "O projetor de holografia digital"],
            "correta": 1,
            "dica": "Era um aparelho pesado que emitia som através de válvulas e trazia radionovelas e notícias para a sala de estar."
        },
        # 1970
        {
            "ano": "1970",
            "pergunta": "Qual foi o impacto cultural da introdução da televisão em cores no Brasil na década de 1970?",
            "opcoes": ["A extinção imediata do rádio como meio de comunicação", "A consolidação da televisão como principal agente de integração cultural de massa", "A proibição de transmissões de eventos esportivos ao vivo", "A substituição de todas as salas de aula por televisores"],
            "correta": 1,
            "dica": "Com novelas diárias e a transmissão da Copa de 1970, as famílias passaram a se aglomerar em torno da telinha colorida."
        },
        {
            "ano": "1970",
            "pergunta": "Por que o espaço público da rua e da calçada desempenhava um papel central na infância dos anos 1970?",
            "opcoes": ["Porque as escolas públicas funcionavam exclusivamente nas calçadas", "Devido à escassez de telas e entretenimento digital doméstico, favorecendo brincadeiras coletivas ao ar livre", "Porque o trânsito de automóveis era totalmente proibido por lei municipal", "Porque as residências não possuíam energia elétrica em cômodo algum"],
            "correta": 1,
            "dica": "Como não existiam videogames ou celulares, as crianças utilizavam a rua como o grande quintal social de convivência."
        },
        # 1990
        {
            "ano": "1990",
            "pergunta": "Quais características estruturais definiam os computadores pessoais (desktops) no início da década de 1990?",
            "opcoes": ["Eram minúsculos relógios inteligentes de pulso com inteligência artificial", "Eram máquinas volumosas, com monitores de tubo pesados e uso de disquetes magnéticos", "Eram projetados diretamente nas paredes através de hologramas a laser", "Eram totalmente integrados a redes de satélite sem fio de alta velocidade"],
            "correta": 1,
            "dica": "Eles ocupavam grande parte das mesas e dependiam de mídias físicas magnéticas limitadas para salvar arquivos."
        },
        {
            "ano": "1990",
            "pergunta": "No contexto brasileiro da década de 1990, qual transformação macroeconômica e comercial reconfigurou o mercado interno?",
            "opcoes": ["O isolamento econômico absoluto com proibição de produtos estrangeiros", "A estabilização monetária com o Plano Real e a abertura do mercado a produtos importados", "A estatização total de todas as empresas privadas do país", "A abolição completa da moeda física em favor de trocas diretas de mercadorias"],
            "correta": 1,
            "dica": "O Plano Real em 1994 conteve a hiperinflação e permitiu a entrada de novas tecnologias estrangeiras no país."
        },
        # 2010
        {
            "ano": "2010",
            "pergunta": "Qual mudança tecnológica estrutural ocorreu com a popularização massiva dos smartphones na década de 2010?",
            "opcoes": ["A internet móvel tornou-se onipresente, descentralizando o acesso à informação e alterando as interações sociais", "O fim absoluto do uso de texto escrito na comunicação humana", "A obrigatoriedade de uso de telefones fixos a cabo em residências", "A regressão das tecnologias de comunicação para o formato postal analógico"],
            "correta": 0,
            "dica": "A rede mundial de computadores deixou de estar presa apenas aos computadores de mesa e passou a caber no bolso."
        },
        {
            "ano": "2010",
            "pergunta": "Como os serviços de streaming impactaram o consumo de mídia e entretenimento durante a década de 2010?",
            "opcoes": ["Impediram totalmente que as pessoas assistissem a vídeos na internet", "Promoveram o consumo de conteúdos sob demanda, reduzindo a dependência da programação linear tradicional", "Obrigaram o retorno exclusivo ao uso de fitas VHS e toca-discos de vinil", "Tornaram o cinema em salas físicas uma atividade extinta no mundo inteiro"],
            "correta": 1,
            "dica": "Permitiu escolher filmes e séries a qualquer momento, rompendo com os horários fixos da TV aberta."
        },
        # Hoje
        {
            "ano": "Hoje",
            "pergunta": "O que caracteriza a sociedade contemporânea na atualidade em termos de infraestrutura técnico-científica?",
            "opcoes": ["A ausência completa de conexões digitais de rede", "O uso de inteligência artificial generativa, automação avançada e hiperconectividade em tempo real", "O retorno ao padrão de comunicação exclusivo por telégrafos a cabo", "O isolamento tecnológico de continentes inteiros sem troca de dados"],
            "correta": 1,
            "dica": "Algoritmos inteligentes, nuvem e assistentes virtuais fazem parte do nosso cotidiano atual."
        },
        {
            "ano": "Hoje",
            "pergunta": "Do ponto de vista das Ciências Humanas, qual é a principal utilidade de analisar a 'mudança e a permanência' ao longo da história?",
            "opcoes": ["Decorar uma lista cronológica estática de presidentes e datas sem reflexão", "Compreender que a sociedade se transforma tecnologicamente e socialmente, mas mantém dilemas humanos, éticos e sociais fundamentais", "Provar que o passado era perfeito e o presente não tem valor algum", "Afirmar que a tecnologia destrói todas as características da cultura humana"],
            "correta": 1,
            "dica": "Mostra que a história é um processo vivo e crítico de transformações contínuas."
        }
    ]

    if "q_atual" not in st.session_state:
        st.session_state.q_atual = 0

    idx = st.session_state.q_atual
    q = banco_questoes[idx]

    st.markdown(f"### 📌 Questão {idx + 1} de {len(banco_questoes)} (Foco Histórico: {q['ano']})")
    
    st.markdown(f"""
        <div class="explanation-box">
            <strong>{q['pergunta']}</strong>
        </div>
    """, unsafe_allow_html=True)

    escolha = st.radio("Selecione a alternativa correta:", q["opcoes"], key=f"q_{idx}", index=None)

    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button("✨ Validar Resposta", use_container_width=True):
            if escolha is None:
                st.warning("⚠️ Selecione uma alternativa antes de validar!")
            else:
                idx_escolhido = q["opcoes"].index(escolha)
                if idx_escolhido == q["correta"]:
                    st.success("🎉 **Resposta Correta!** Excelente raciocínio histórico e crítico! 🌟")
                else:
                    st.error(f"❌ **Incorreto.** Contexto de apoio: *{q['dica']}*")

    st.markdown("---")
    
    col_ant, col_prox = st.columns(2)
    with col_ant:
        if idx > 0:
            if st.button("⬅️ Questão Anterior"):
                st.session_state.q_atual -= 1
                st.rerun()
    with col_prox:
        if idx < len(banco_questoes) - 1:
            if st.button("➡️ Próxima Questão"):
                st.session_state.q_atual += 1
                st.rerun()
        else:
            if st.button("🏆 Concluir e Ver Resultado Final"):
                st.session_state.pagina = "fim"
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🏠 Retornar à Linha do Tempo"):
        st.session_state.pagina = "linha_tempo"
        st.rerun()

# ----------------- TELA 4: CONCLUSÃO -----------------
elif st.session_state.pagina == "fim":
    st.markdown('<p class="main-title">🏆 Conclusão da Jornada Histórica 🎓</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Parabéns por concluir a análise crítica das Ciências Humanas!</p>', unsafe_allow_html=True)
    
    st.success("🌟 Atividade concluída com excelente aproveitamento analítico!")
    
    st.write("""
    ### 📝 Síntese Pedagógica Final:
    Ao examinar a trajetória da sociedade desde **1950 até a atualidade**, constatamos que a história humana é um processo dinâmico 
    de **rupturas e continuidades**. Enquanto a infraestrutura material, os meios de comunicação e os aparatos tecnológicos passaram por 
    metamorfoses profundas (da válvula eletrônica à inteligência artificial), as necessidades fundamentais da convivência coletiva, 
    a busca por direitos sociais e os desafios éticos da humanidade permanecem como o cerne da reflexão histórica.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    col_r1, col_r2 = st.columns(2)
    with col_r1:
        if st.button("🔄 Refazer o Quiz", use_container_width=True):
            st.session_state.q_atual = 0
            st.session_state.pagina = "quiz"
            st.rerun()
    with col_r2:
        if st.button("🏠 Voltar à Página Inicial", use_container_width=True):
            st.session_state.q_atual = 0
            st.session_state.pagina = "introducao"
            st.rerun()