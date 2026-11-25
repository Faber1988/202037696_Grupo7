# ESCENARIO 5: Controlador de Carga Solar Fotovoltaica (Módulo Phocos MPPT) Refactorizado
mppt_phocos = {
    # SECCIÓN 1: Registro de Entrada Solar (0x10)
    # Define la fuente de voltaje proveniente de los paneles solares, estableciendo un límite máximo de 150.0 V y activando la bandera del sistema para su monitoreo.
    "0x10": {
        "hardware_source": "PV_ARRAY",
        "max_safe_value": 150.0,
        "system_flag": True,
    },
    # SECCIÓN 2: Registro de Salida a Batería (0x11)
    # Gestiona la corriente de carga hacia el banco de baterías, limitando el flujo seguro a un máximo de 60.0 A con la bandera del sistema activa.
    "0x11": {
        "hardware_source": "BATTERY",
        "max_safe_value": 60.0,
        "system_flag": True,
    },
    # SECCIÓN 3: Registro del Relevador de Carga Directa (0x15)
    # Controla el relevador de salida de consumo (Load Relay), fijando un límite de corriente de 20.0 A y manteniendo la bandera del sistema desactivada (OFF).
    "0x15": {
        "hardware_source": "LOAD_RELAY",
        "max_safe_value": 20.0,
        "system_flag": False,
    },
}
