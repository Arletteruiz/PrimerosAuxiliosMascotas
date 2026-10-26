# 10 Hechos
hechos = [
    ("incluye", "botiquin_mascotas", "vendas_y_apositos"),
    ("incluye", "botiquin_mascotas", "antiseptico"),
    ("puede_reaccionar_impredeciblemente", "perro_herido"),
    ("presion_directa_controla_sangrado", "perro"),
    ("requiere_atencion_veterinaria", "fractura_sospechada_perro"),
    ("medicamentos_humanos_peligrosos", "gato"),
    ("presion_directa_controla_sangrado", "gato"),
    ("requiere_atencion_urgente", "intoxicacion_gato"),
    ("signo_de_enfermedad", "perdida_apetito", "pez"),
    ("signo_de_enfermedad", "natacion_erratica", "pez"),
]

# 5 reglas
reglas = {
    "R1": {
        "nombre": "Control de hemorragias en perros",
        "condicion": ("hemorragia", "perro"),
        "conclusion": ("aplicar_presion", "perro"),
    },
    "R2": {
        "nombre": "Prevencion de mordeduras",
        "condicion": ("perro_herido", "perro"),
        "conclusion": ("manipular_con_precaucion", "perro"),
    },
    "R3": {
        "nombre": "Intoxicaciones en gatos",
        "condicion": ("ingiere_veneno", "gato"),
        "conclusion": ("requiere_atencion_urgente", "gato"),
    },
    "R4": {
        "nombre": "Medicamentos humanos en gatos",
        "condicion": ("medicamento_humano", "gato"),
        "conclusion": (
            "no_administrar_sin_indicacion_veterinaria",
            "gato",
        ),
    },
    "R5": {
        "nombre": "Preparacion del botiquin",
        "condicion": ("preparar", "botiquin_mascotas"),
        "conclusion": (
            "incluir_materiales_basicos",
            "botiquin_mascotas",
        ),
    },
}

# Mostrar los hechos
print("=== HECHOS ===")
for hecho in hechos:
    print(hecho)

# Mostrar las reglas
print("\n=== REGLAS ===")
for identificador, regla in reglas.items():
    print(f"{identificador}: {regla['nombre']}")
    print("  SI:", regla["condicion"])
    print("  ENTONCES:", regla["conclusion"])