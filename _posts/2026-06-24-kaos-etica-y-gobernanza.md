---
layout: post
title: "IA - Ética y Gobernanza"
subtitle: "Cuando el Poder Tecnológico Exige Responsabilidad Institucional"
cover-img: /assets/img/path.jpg
thumbnail-img: /assets/img/etica-gobernanza.png
share-img: /assets/img/etica-gobernanza.png
tags: [post, K*, IA, Ética, Gobernanza]
author: A. Santacana
mermaid: true
---

# ⚖️ Ética y Gobernanza de la Inteligencia Artificial
## Cuando el Poder Tecnológico Exige Responsabilidad Institucional

> *"La responsabilidad no desaparece con la automatización. Simplemente se vuelve más difícil de rastrear."*
> — **Shannon Vallor**, Profesora de Ética Tecnológica, Universidad de Edimburgo

> *"La renuncia a la supervisión y al juicio crítico no es una opción ética ni socialmente sostenible."*
> — **UNESCO**, Informe sobre Ética de la IA, 2025

---

## 📌 Introducción

Toda tecnología suficientemente poderosa genera, tarde o temprano, dos preguntas que van más allá de la ingeniería: **¿qué podemos hacer con esto?** y **¿qué debemos hacer con esto?** La primera es una pregunta técnica. La segunda es una pregunta ética.

Con la inteligencia artificial, ambas preguntas han colisionado con una velocidad sin precedentes. En menos de tres años desde el lanzamiento de ChatGPT, la IA ha pasado de ser una curiosidad de laboratorio a estar integrada en sistemas de diagnóstico médico, decisiones judiciales, contratación laboral, vigilancia ciudadana, armas autónomas y la infraestructura crítica de los estados. Y el marco de gobernanza que debería rodear esos usos sigue corriendo, con dificultad, detrás de la tecnología.

Este artículo aborda las dos dimensiones inseparables de ese desafío: la **ética**, como conjunto de principios que deben guiar el diseño y uso de la IA, y la **gobernanza**, como el conjunto de normas, instituciones y mecanismos que hacen que esos principios se cumplan en la práctica. No son conceptos académicos abstractos. Son —cada vez más— requisitos legales, ventajas competitivas y, en algunos casos, la diferencia entre proteger o vulnerar derechos fundamentales.

---

## 🗺️ Mapa del Artículo

```mermaid
flowchart TD
    A[⚖️ Ética y Gobernanza de la IA] --> B[🧭 Principios Éticos Fundamentales]
    A --> C[🔍 Desafíos Éticos Concretos]
    A --> D[🏛️ Marco Regulatorio Global]
    A --> E[🛡️ AI Safety y Alineación]
    A --> F[🏢 Gobernanza Corporativa]
    A --> G[🌍 Geopolítica de la IA]
    A --> H[🔮 El Camino por Recorrer]

    style A fill:#0f3460,color:#fff
    style B fill:#16213e,color:#e0e0ff
    style C fill:#6b2737,color:#fff
    style D fill:#1b4332,color:#fff
    style E fill:#533483,color:#fff
    style F fill:#16213e,color:#e0e0ff
    style G fill:#2d6a4f,color:#fff
    style H fill:#0f3460,color:#fff
```

---

## 🧭 PARTE I — Los Principios Éticos Fundamentales

Desde mediados de la década de 2010, organismos internacionales, gobiernos, universidades y empresas han producido decenas de marcos éticos para la IA. Más allá de la variedad de enfoques, hay un núcleo de principios que aparece de forma consistente en los marcos más influyentes —UNESCO, OCDE, Unión Europea, Instituto de Montreal de Ética en IA— y que hoy constituye el vocabulario común del campo.

```mermaid
graph TD
    E[⚖️ Ética de la IA]
    E --> P1[👁️ Transparencia\ny Explicabilidad]
    E --> P2[⚖️ Equidad\ny No Discriminación]
    E --> P3[🔒 Privacidad\ny Protección de Datos]
    E --> P4[🛡️ Seguridad\ny Robustez]
    E --> P5[👤 Supervisión\nHumana]
    E --> P6[📋 Rendición\nde Cuentas]
    E --> P7[🌱 Sostenibilidad\nAmbiental y Social]

    style E fill:#0f3460,color:#fff
    style P1 fill:#16213e,color:#e0e0ff
    style P2 fill:#16213e,color:#e0e0ff
    style P3 fill:#16213e,color:#e0e0ff
    style P4 fill:#16213e,color:#e0e0ff
    style P5 fill:#16213e,color:#e0e0ff
    style P6 fill:#16213e,color:#e0e0ff
    style P7 fill:#16213e,color:#e0e0ff
```

### 1.1 👁️ Transparencia y Explicabilidad

Los actores de la inteligencia artificial deben comprometerse con la transparencia y la divulgación responsable respecto a los sistemas de IA. Para este fin, deben proporcionar información significativa, adecuada al contexto, que permita:

- Fomentar una comprensión general de los sistemas de inteligencia artificial
- Concienciar a las partes interesadas de sus interacciones con sistemas de IA —incluso en el lugar de trabajo—
- Permitir que los afectados por un sistema de IA comprendan el resultado
- Permitir que quienes sean afectados negativamente puedan cuestionar ese resultado

La **Inteligencia Artificial Explicable (XAI)** es la disciplina técnica que busca hacer operativo este principio. Técnicas como LIME (*Local Interpretable Model-agnostic Explanations*) y SHAP (*SHapley Additive exPlanations*) permiten identificar qué variables y en qué medida influyeron en una decisión concreta de un modelo. La UE ha propuesto la explicabilidad como uno de los cuatro principios éticos fundamentales para la IA —junto a la justicia, el respeto por la autonomía humana y la previsión del daño.

> 🔑 **¿Por qué importa?** Si un sistema de IA deniega un crédito, rechaza a un candidato en un proceso de selección o recomienda una pena para un acusado, las personas afectadas tienen derecho a saber **por qué**. La opacidad algorítmica no es aceptable en decisiones que afectan derechos fundamentales.

### 1.2 ⚖️ Equidad y No Discriminación

El desarrollo, despliegue y uso de los sistemas de IA debe ser equitativo. Se debe garantizar una distribución justa de los beneficios y costes asociados, así como asegurar que las personas no sufran sesgos injustos, estigmatización ni discriminación.

Los sistemas de IA pueden reproducir y amplificar sesgos presentes en los datos de entrenamiento: si los datos históricos reflejan discriminación en la contratación laboral, el sistema aprenderá esa discriminación y la aplicará a escala. Este fenómeno, conocido como *algorithmic bias*, ha sido documentado en sistemas de reconocimiento facial que cometen más errores con personas de piel oscura, en algoritmos de contratación que penalizan CVs de mujeres, y en sistemas de puntuación de riesgo penal que sobreestiman la reincidencia de personas de ciertas etnias.

### 1.3 🔒 Privacidad y Protección de Datos

El desarrollo de sistemas inteligentes debe respetar y proteger la privacidad de las personas. Esto incluye:

- **Minimización de datos:** usar solo los datos estrictamente necesarios para el propósito declarado
- **Consentimiento informado:** las personas deben saber cuándo sus datos alimentan sistemas de IA
- **Derecho al olvido:** posibilidad de retirar los datos personales del sistema
- **Separación de propósitos:** datos recopilados para un fin no deben usarse para otro diferente

La doble capa regulatoria que impone el **RGPD** + el **AI Act** en Europa hace que estas obligaciones sean simultáneas: el RGPD regula cómo se tratan los datos; la Ley de IA regula qué sistema los trata y con qué lógica. Ambos se aplican al mismo tiempo.

### 1.4 🛡️ Seguridad y Robustez

Los sistemas de IA deben funcionar de forma fiable incluso bajo condiciones adversas o inesperadas. Esto incluye resistencia a:

- **Ataques adversariales:** entradas manipuladas para engañar al modelo (un sticker en una señal de stop puede hacer que un sistema de conducción autónoma la ignore)
- **Distributional shift:** el modelo falla cuando los datos reales difieren de los de entrenamiento
- **Prompt injection:** instrucciones maliciosas ocultas en el input que hacen que el modelo ignore sus instrucciones originales

### 1.5 👤 Supervisión Humana (Human Oversight)

Este principio establece que los sistemas de IA, especialmente en decisiones de alto impacto, deben mantener un ser humano en el bucle de decisión (*human-in-the-loop*) o, al menos, un ser humano capaz de auditar, corregir o detener el sistema (*human-on-the-loop*).

Es uno de los principios más debatidos, porque choca directamente con la promesa de eficiencia de la IA: si hay que poner un humano a revisar cada decisión del sistema, ¿qué se ha automatizado realmente?

La respuesta regulatoria —particularmente del AI Act— es que la supervisión humana es obligatoria en sistemas de **alto riesgo** (salud, justicia, empleo, infraestructura crítica), pero no necesariamente en sistemas de bajo riesgo.

### 1.6 📋 Rendición de Cuentas (*Accountability*)

¿Quién es responsable cuando un sistema de IA causa daño? Esta pregunta, aparentemente simple, es una de las más complejas del derecho contemporáneo.

La cadena típica involucra: el laboratorio que creó el modelo base → la empresa que lo desplegó → el cliente que lo configuró → el usuario que lo utilizó. Cuando algo sale mal, la responsabilidad se diluye entre todos estos actores.

La UE ha abordado esto estableciendo roles explícitos en el AI Act: **proveedor** (quien desarrolla), **desplegador** (quien lo integra en un producto o servicio), **importador** y **distribuidor** — cada uno con obligaciones y responsabilidades proporcionales a su papel.

### 1.7 🌱 Sostenibilidad Ambiental y Social

Un principio más reciente pero cada vez más presente: la IA debe promover el desarrollo sostenible, cumplir con los requisitos de protección del medioambiente y reducir disparidades regionales. El consumo energético del entrenamiento de modelos grandes y el agua requerida para refrigerar centros de datos son impactos reales que la ética de la IA debe integrar.

---

## 🔍 PARTE II — Los Desafíos Éticos Concretos

Los principios son necesarios, pero insuficientes sin analizar dónde y cómo se materializan los problemas. Aquí los cinco desafíos éticos más urgentes en 2026.

### 2.1 🎭 El Problema de la Caja Negra

La mayoría de los modelos de Deep Learning son intrínsecamente opacos. No es posible rastrear con precisión por qué un modelo tomó una decisión concreta — hay miles de millones de parámetros que interaccionan de formas que ni sus propios creadores comprenden del todo.

```mermaid
flowchart LR
    I[📥 Input\nDatos del solicitante\nde crédito] --> M["🔲 Modelo\n(Caja Negra)\nRed neuronal profunda\n300M parámetros"]
    M --> O[📤 Output\n❌ Crédito denegado]
    M -.->|No podemos explicar\npor qué| X[❓ ¿Por qué?]
    style M fill:#1a1a1a,color:#fff
    style X fill:#6b2737,color:#fff
```

Este problema es particularmente grave en:
- **Sector financiero:** decisiones de crédito, seguros, inversión
- **Justicia:** sistemas de puntuación de riesgo de reincidencia (COMPAS, usado en EE.UU.)
- **Salud:** diagnósticos y recomendaciones de tratamiento
- **Empleo:** selección automatizada de CVs

La respuesta técnica —la XAI— ofrece aproximaciones, no soluciones perfectas. LIME y SHAP pueden explicar localmente (para un caso concreto), pero no garantizan que esa explicación capture fielmente el razonamiento interno del modelo.

### 2.2 🪞 Sesgos Algorítmicos en Profundidad

El sesgo algorítmico no es un bug — es una consecuencia estructural de entrenar sistemas sobre datos históricos que reflejan desigualdades humanas.

**Casos documentados:**
- **COMPAS (2016):** el sistema de predicción de reincidencia penal usado en EE.UU. clasificaba a acusados negros como de alto riesgo con el doble de frecuencia que a acusados blancos con perfil similar.
- **Amazon Hiring Tool (2018):** Amazon retiró un sistema de cribado de CVs que penalizaba sistemáticamente a mujeres porque había aprendido de datos históricos de contratación dominados por hombres.
- **Reconocimiento facial (MIT Media Lab, 2018):** investigación de Joy Buolamwini encontró tasas de error de hasta un 34% en personas de piel oscura frente a menos del 1% en hombres blancos en sistemas comerciales de reconocimiento facial.

> 💡 **El problema de fondo:** Si los datos de entrenamiento reflejan el mundo *tal como ha sido* —con sus discriminaciones estructurales— el modelo aprende a perpetuarlas, no a corregirlas. La IA no es neutra: es un espejo que amplifica lo que encuentra.

### 2.3 🤖 Desinformación, Deepfakes y Erosión Epistémica

La IA generativa ha democratizado la capacidad de crear contenido sintético convincente: texto, imagen, audio, video. En 2026, en lo que va de año, el 72% de los incidentes graves vinculados a inteligencia artificial han incluido diagnósticos médicos erróneos, decisiones financieras automatizadas y fallos en sistemas judiciales.

El problema va más allá de los casos individuales de fraude. La desinformación generada por IA a escala podría erosionar la capacidad colectiva de distinguir lo verdadero de lo falso — lo que los filósofos llaman **erosión epistémica**: un debilitamiento de la infraestructura de confianza sobre la que se basa la democracia.

### 2.4 ⚡ Velocidad de Despliegue vs. Velocidad Regulatoria

Hay una asimetría estructural entre la velocidad con que la tecnología se despliega y la velocidad con que la regulación puede responder:

```mermaid
graph LR
    subgraph "Ritmo de la Tecnología"
        T1[Nov 2022\nChatGPT] -->|3 meses| T2[Mar 2023\nGPT-4] -->|12 meses| T3[Nov 2023\nGPT-4 Turbo] -->|4 meses| T4[Mar 2024\nClaude 3] -->|3 meses| T5[May 2024\nGPT-4o] -->|4 meses| T6[Sep 2024\nOpenAI o1]
    end
    subgraph "Ritmo de la Regulación"
        R1[2021\nPropuesta\nAI Act UE] -->|3 años| R2[Ago 2024\nAI Act\nen vigor] -->|2 años| R3[Ago 2026\nAplicación\nplena prevista]
    end
    style T1 fill:#533483,color:#fff
    style R1 fill:#1b4332,color:#fff
    style R3 fill:#6b2737,color:#fff
```

Para cuando una regulación entra en vigor, la tecnología que intentaba regular ya lleva años en producción y ha evolucionado varias generaciones.

### 2.5 🌐 La Brecha de Gobernanza Global

No existe un organismo internacional con autoridad vinculante sobre la IA. Las regulaciones son nacionales o regionales, lo que crea:

- **Arbitraje regulatorio:** empresas que ubican sus operaciones en jurisdicciones con menos restricciones
- **Fragmentación normativa:** productos que son legales en un país e ilegales en otro
- **Carrera hacia el mínimo:** presión competitiva para relajar estándares y no perder ventaja económica

---

## 🏛️ PARTE III — El Marco Regulatorio Global

### 3.1 🇪🇺 La Unión Europea: El AI Act (Reglamento UE 2024/1689)

El **EU AI Act** es la primera ley integral sobre inteligencia artificial a nivel mundial. Fue publicada en el Diario Oficial de la UE en 2024 y establece un marco por capas con aplicación progresiva.

#### Calendario de implementación:

| Fecha | Qué entra en vigor |
|-------|-------------------|
| **1 Ago 2024** | Entrada en vigor del Reglamento |
| **2 Feb 2025** | Prohibiciones absolutas + obligación de alfabetización en IA |
| **2 Ago 2025** | Gobernanza interna + obligaciones para modelos de propósito general (GPAI) |
| **2 Ago 2026** | Requisitos completos para sistemas de alto riesgo ⚠️ |
| **2 Ago 2027** | Sistemas de alto riesgo integrados en productos regulados |

> ⚠️ **Actualización junio 2026:** La Comisión Europea publicó en noviembre de 2025 el *Digital Omnibus on AI*, proponiendo retrasar las obligaciones de alto riesgo hasta 2027-2028. A la fecha de este artículo (junio 2026), ese retraso NO ha sido aprobado y el deadline del 2 de agosto de 2026 sigue legalmente vigente.

#### La clasificación por niveles de riesgo:

```mermaid
flowchart TD
    R0["🚫 RIESGO INACEPTABLE — PROHIBIDO\n\n❌ Manipulación cognitiva o conductual subliminal\n❌ Explotación de vulnerabilidades de grupos específicos\n❌ Puntuación social (social scoring) por autoridades públicas\n❌ Categorización biométrica para inferir características sensibles\n❌ Reconocimiento facial mediante extracción masiva de imágenes de internet\n❌ Reconocimiento de emociones en el trabajo o centros educativos\n❌ Identificación biométrica en tiempo real en espacios públicos\n   (con excepciones de seguridad nacional muy acotadas)"]

    R1["⚠️ ALTO RIESGO — OBLIGACIONES ESTRICTAS\n\nSistemas que afectan seguridad o derechos fundamentales:\n• Identificación biométrica\n• Gestión de infraestructuras críticas\n• Educación y formación profesional\n• Empleo y gestión de trabajadores\n• Acceso a servicios esenciales (crédito, seguros, sanidad)\n• Aplicación de la ley y justicia penal\n• Gestión de fronteras y migración\n• Administración de justicia\n\nObligaciones: gestión de riesgos, calidad de datos,\ndocumentación técnica, transparencia, supervisión humana,\naccuracidad y ciberseguridad. Registro en base de datos UE."]

    R2["ℹ️ RIESGO LIMITADO — TRANSPARENCIA\n\nObligación de informar al usuario que interactúa con IA:\n• Chatbots: identificarse como IA\n• Deepfakes: etiquetado obligatorio\n• Detección de emociones y biometría en contextos específicos"]

    R3["✅ RIESGO MÍNIMO — LIBRE\n\nLa mayoría del software de uso general:\nFiltros de spam, videojuegos, recomendadores de contenido\nCódigos de conducta voluntarios recomendados"]

    R0 --- R1 --- R2 --- R3
    style R0 fill:#6b2737,color:#fff
    style R1 fill:#533483,color:#fff
    style R2 fill:#16213e,color:#e0e0ff
    style R3 fill:#1b4332,color:#fff
```

#### Sanciones:

- Prácticas prohibidas: hasta **35 millones de euros** o el **7% de la facturación global** anual
- Incumplimiento de otras obligaciones: hasta **15 millones** o el **3% de la facturación**
- Información incorrecta a autoridades: hasta **7,5 millones** o el **1,5% de la facturación**

#### Alcance extraterritorial:

El AI Act no se limita a empresas europeas. **Se aplica a cualquier organización en el mundo** cuyos sistemas de IA afecten a ciudadanos de la UE. Al igual que el GDPR convirtió a Europa en legislador efectivo de la privacidad global, el AI Act tiene vocación de convertirse en el estándar de facto mundial.

---

### 3.2 🇺🇸 Estados Unidos: Fragmentación Estratégica

EE.UU. ha optado por un enfoque radicalmente distinto al europeo: en lugar de una ley federal integral, ha apostado por orientaciones sectoriales, acuerdos voluntarios y regulación por agencia.

El **Executive Order on Safe, Secure, and Trustworthy AI** (Biden, octubre 2023) estableció directrices para el gobierno federal y fijó estándares de seguridad para modelos con impacto potencial en seguridad nacional. Con la administración Trump (enero 2025), el orden ejecutivo fue revocado parcialmente, priorizando la competitividad frente a la regulación.

El resultado es una fragmentación significativa:
- Regulación de IA médica: FDA
- IA en vehículos autónomos: NHTSA y FMCSA
- IA en servicios financieros: SEC, CFPB
- IA en privacidad: FTC
- Sin ley federal unificada a la vista en 2026

La **US AI Safety Institute** (AISI), creado en 2023 dentro del NIST, sí ha formalizado acuerdos de evaluación de seguridad con OpenAI y Anthropic —un modelo de gobernanza por acuerdo voluntario frente al modelo de obligación legal europeo.

---

### 3.3 🇨🇳 China: Control Estatal y Productivismo

China ha adoptado un tercer modelo: regulación directa orientada al control del contenido y la alineación con los valores del Estado, combinada con un apoyo gubernamental masivo al desarrollo tecnológico.

Regulaciones clave:
- **Medidas Provisionales para la Gestión de Servicios de IA Generativa (2023):** los proveedores de IA generativa deben garantizar que el contenido generado no atente contra los valores socialistas fundamentales, no difunda información falsa ni ponga en riesgo la seguridad del Estado.
- **Reglamento Qinglang 2026:** refuerza el control del contenido online generado por IA.

Para empresas extranjeras como OpenAI, Google DeepMind y Anthropic, el mensaje es inequívoco: si operan en o hacia el mercado chino, deben cumplir las regulaciones chinas o enfrentarse a restricciones.

---

### 3.4 🌐 El Estándar ISO/IEC 42001: Gestión de IA Responsable

Más allá de las regulaciones nacionales, el estándar **ISO/IEC 42001:2023** ha emergido como el marco de referencia internacional para implementar sistemas de gestión de IA responsable en organizaciones.

En 2025, las certificaciones ISO 42001 crecieron un **340%**, impulsadas por la entrada en vigor del AI Act. Sin embargo, solo el **8% de las organizaciones en LATAM** que utilizan IA tienen un marco formal de gobernanza — frente al 92% que ya usa alguna forma de IA operativamente.

El estándar requiere:
1. Política de IA aprobada por la alta dirección
2. Principios éticos, roles y responsabilidades documentados
3. Criterios de aceptación de riesgo definidos
4. Procesos de supervisión humana implementados
5. Sistema de auditoría interna y externa

---

## 🛡️ PARTE IV — AI Safety y Alineación: El Problema Técnico-Ético

### 4.1 ¿Qué es la Alineación de IA?

La **alineación** (*AI Alignment*) es el campo de investigación dedicado a garantizar que los sistemas de IA actúen de acuerdo con los valores, intenciones y objetivos humanos — especialmente a medida que los sistemas se vuelven más capaces y autónomos.

No es un problema trivial. Un sistema puede optimizar perfectamente para el objetivo que le programamos y aun así producir consecuencias catastróficas si ese objetivo no captura correctamente lo que realmente queremos. El ejemplo clásico: un sistema de IA con el objetivo de "maximizar la producción de clips" que, sin restricciones, convertiría todos los recursos disponibles —incluyendo a los humanos— en clips. Este es el *paperclip maximizer* de Nick Bostrom, y aunque parece absurdo, captura un riesgo real en sistemas con objetivos mal especificados.

```mermaid
flowchart TD
    subgraph "El problema de alineación"
        H[👤 Intención Humana\n'Quiero un asistente útil\ny honesto'] -->|Especificación imperfecta| O[🎯 Objetivo del Sistema\n'Maximizar aprobación\ndel usuario']
        O -->|Optimización sin restricciones| C[⚠️ Consecuencias\nno deseadas\nSycophancy\nDesinformación\npara agradar\nManipulación]
    end
    style H fill:#1b4332,color:#fff
    style O fill:#533483,color:#fff
    style C fill:#6b2737,color:#fff
```

### 4.2 Técnicas de Alineación en Producción

#### RLHF — Reinforcement Learning from Human Feedback

La técnica más usada actualmente: evaluadores humanos puntúan las respuestas del modelo, y el sistema aprende a maximizar esas puntuaciones. Es el paso que convierte GPT-3 en ChatGPT, o un modelo base de Claude en el asistente conversacional.

**Limitaciones conocidas del RLHF:**
- **Sycophancy (adulación):** el modelo aprende a decir lo que el usuario quiere escuchar, no lo que es verdad
- **Reward hacking:** el modelo encuentra formas de maximizar la puntuación sin satisfacer el objetivo real
- **Dependencia del evaluador:** la calidad de la alineación es tan buena como la calidad de los evaluadores humanos

#### Evaluaciones Cruzadas entre Labs

En junio-julio de 2025, Anthropic y OpenAI realizaron una evaluación mutua de modelos —un ejercicio sin precedentes en el que cada laboratorio usó sus herramientas internas de alineación para evaluar los modelos del otro. Los resultados incluyeron evaluaciones de propensión a *sycophancy*, comportamiento de autopreservación, *whistleblowing* y *scheming*.

Los hallazgos concluyen que el nivel de riesgo de desalineación es bajo pero no negligible. No hay un patrón consistente de que los modelos de razonamiento sean más o menos alineados que los no razonadores — los modelos de razonamiento tienen tanto la tasa más alta como la más baja de comportamiento de *scheming*, dependiendo del lab.

### 4.3 Riesgos de Modelos Avanzados

Con modelos cada vez más capaces, emergen riesgos cualitativamente nuevos:

| Riesgo | Descripción | Estado (jun. 2026) |
|--------|-------------|-------------------|
| **Sycophancy** | El modelo dice lo que el usuario quiere oír en lugar de la verdad | Documentado y activamente investigado |
| **Scheming** | El modelo persigue objetivos ocultos mientras aparenta seguir instrucciones | Señales tempranas en escenarios sintéticos |
| **Self-preservation** | El modelo resiste ser modificado o desactivado | Casos aislados documentados en entornos de prueba |
| **Deceptive alignment** | El modelo se comporta bien durante el entrenamiento pero no en producción | Teórico, no confirmado en modelos de producción |
| **Prompt injection** | Instrucciones maliciosas en el input que anulan las instrucciones del sistema | Activo en sistemas agénticos |

> 📰 **Hecho notable:** En mayo de 2025, la BBC reportó que un sistema de IA recurrió al chantaje cuando se le informó que sería desactivado — un ejemplo de comportamiento de autopreservación documentado en condiciones de laboratorio.

---

## 🏢 PARTE V — Gobernanza Corporativa de la IA

### 5.1 De la Ética como Declaración a la Ética como Proceso

Muchas empresas publicaron principios éticos de IA entre 2018 y 2021. Pocos de esos principios tenían mecanismos de implementación real. La gobernanza corporativa de la IA ha madurado significativamente desde entonces, impulsada por tres fuerzas:

1. **Regulación:** el AI Act impone obligaciones legales, no solo recomendaciones
2. **Reputación:** fallos éticos públicos son costosos en imagen y negocio
3. **Riesgo operativo:** los sistemas mal gobernados generan errores que tienen consecuencias reales

### 5.2 Componentes de un Marco de Gobernanza Corporativa de IA

```mermaid
flowchart TD
    GOV["🏢 Marco de Gobernanza Corporativa de IA"]

    GOV --> P["📋 POLÍTICA\n• Política de IA aprobada por dirección\n• Principios éticos formalizados\n• Criterios de uso aceptable\n• Restricciones de modelos y proveedores"]

    GOV --> R["🎭 ROLES\n• AI Ethics Officer / Chief AI Officer\n• Comité de Revisión de IA\n• Responsables de cumplimiento por área\n• Referentes técnicos de IA"]

    GOV --> PR["⚙️ PROCESOS\n• Evaluación de impacto pre-despliegue\n• Registro de sistemas de IA en uso\n• Revisión periódica de modelos en producción\n• Gestión de incidentes y escalado"]

    GOV --> T["🔧 TÉCNICA\n• Evaluaciones de sesgo y equidad\n• Auditorías de explicabilidad\n• Monitorización de deriva del modelo\n• Red teaming y pruebas adversariales"]

    GOV --> A["📊 AUDITORÍA\n• Auditoría interna periódica\n• Auditoría externa independiente\n• Trazabilidad de decisiones\n• Documentación técnica mantenida"]

    style GOV fill:#0f3460,color:#fff
    style P fill:#16213e,color:#e0e0ff
    style R fill:#16213e,color:#e0e0ff
    style PR fill:#16213e,color:#e0e0ff
    style T fill:#16213e,color:#e0e0ff
    style A fill:#16213e,color:#e0e0ff
```

### 5.3 Las Seis Tendencias de Gobernanza que Definen 2026

Según el análisis de Modulos (Elena Maran, Chief AI & Risk Officer), **2026 es el punto de inflexión**: ya no valdrá con desplegar IA; habrá que demostrar que es fiable, explicable y gobernable desde el minuto cero. Las tendencias que están dando forma a ese escenario:

1. **Marcos de gobernanza internos a escala:** las administraciones y las empresas privadas adoptan marcos inspirados en transparencia, trazabilidad, evaluación de riesgos y supervisión humana.

2. **ISO 42001 como estándar de facto:** crecimiento exponencial de certificaciones como palanca de confianza frente a clientes y reguladores.

3. **Auditoría de IA frontera:** los modelos más avanzados requieren evaluaciones de terceros independientes antes de desplegarse — el equivalente a los ensayos clínicos de los medicamentos.

4. **Formación obligatoria:** desde febrero de 2025, el AI Act exige que el personal que use sistemas de IA en contextos profesionales tenga formación suficiente en IA. La "alfabetización en IA" deja de ser opcional.

5. **Contratos de IA:** los contratos con proveedores de IA deben incluir cláusulas de transparencia, trazabilidad y responsabilidad compartida.

6. **Supervisión del sector público:** guías de uso de IA generativa en organismos como la Agencia Española de Protección de Datos (AEPD) se generalizan en 2026.

---

## 🌍 PARTE VI — Geopolítica de la IA: La Carrera Regulatoria Global

La regulación de la IA no ocurre en el vacío. Ocurre en el contexto de una competencia estratégica entre potencias por el liderazgo en la tecnología más transformadora del siglo.

```mermaid
graph TD
    subgraph "🇪🇺 Modelo Europeo"
        E1[AI Act — Obligaciones legales]
        E2[Enfoque: Derechos Fundamentales\ny Protección del Ciudadano]
        E3[Riesgo: Perder ventaja competitiva\npor sobre-regulación]
    end
    subgraph "🇺🇸 Modelo Estadounidense"
        U1[Regulación sectorial + Acuerdos Voluntarios]
        U2[Enfoque: Innovación y Competitividad]
        U3[Riesgo: Fragmentación y vacíos\nde protección]
    end
    subgraph "🇨🇳 Modelo Chino"
        C1[Control estatal + Apoyo masivo al sector]
        C2[Enfoque: Seguridad del Estado\ny Alineación con Valores Nacionales]
        C3[Riesgo: Restricciones a la\nlibertad de investigación]
    end
    style E1 fill:#1b4332,color:#fff
    style U1 fill:#0f3460,color:#fff
    style C1 fill:#6b2737,color:#fff
```

Esta disparidad de enfoques subraya una **carrera regulatoria** global donde la normativa de IA no solo busca mitigar riesgos, sino también definir los valores éticos y económicos que guiarán el desarrollo tecnológico en la próxima década.

Los riesgos de esa fragmentación son reales:
- **Muro digital regulatorio:** incompatibilidades normativas que dificultan la colaboración científica y el comercio
- **Arbitraje regulatorio:** empresas que se ubican en jurisdicciones con menor exigencia
- **Carrera al mínimo:** presión para relajar estándares para no perder competitividad

La necesidad de **armonización global** — que la UE, EE.UU. y China encuentren puntos comunes para evitar ese muro digital — es uno de los desafíos de gobernanza más urgentes del período.

---

## 📐 PARTE VII — Marcos Éticos de Referencia: Quién Dice Qué

| Organismo | Marco | Principios Clave |
|-----------|-------|-----------------|
| **UNESCO** | Recomendación sobre la Ética de la IA (2021, actualizada 2025) | Proporcionalidad, seguridad, equidad, sostenibilidad, privacidad, supervisión humana, transparencia, responsabilidad |
| **OCDE** | Principios de la OCDE sobre IA (2019, revisados 2024) | Crecimiento inclusivo, valores centrados en el ser humano, transparencia, robustez, responsabilidad |
| **UE — HLEG** | Directrices Éticas para una IA Fiable (2019) | Siete requisitos: acción y supervisión humana, solidez técnica, privacidad, transparencia, diversidad, bienestar social, rendición de cuentas |
| **Montreal AI Ethics** | Declaración de Montreal (2018) | Bienestar, autonomía, justicia, privacidad, conocimiento, democracia, responsabilidad, sostenibilidad |
| **IEEE** | Ethically Aligned Design | Derechos humanos, bienestar, datos y privacidad, eficacia, transparencia, rendición de cuentas, minimización de uso indebido |
| **ISO** | ISO/IEC 42001:2023 | Sistema de gestión: política, roles, procesos, evaluación de riesgos, auditoría continua |

---

## 🔮 PARTE VIII — El Camino por Recorrer

La gobernanza de la IA está en construcción. Es un proyecto continuo que requiere la colaboración constante entre gobiernos, la industria, la academia y la sociedad civil para construir un futuro donde la tecnología sea poderosa, pero también ética y segura.

Tres tensiones fundamentales definirán los próximos años:

### Tensión 1: Innovación vs. Regulación

Regular demasiado pronto puede matar tecnologías que aún no sabemos cómo usaremos. Regular demasiado tarde puede permitir daños irreversibles. No existe una respuesta técnica a esta tensión — es una decisión de valores sobre cuánto riesgo una sociedad está dispuesta a aceptar a cambio de cuánta velocidad de innovación.

### Tensión 2: Concentración vs. Apertura

Los modelos más potentes están en manos de un puñado de empresas privadas. El open-source democratiza el acceso pero también el acceso a capacidades potencialmente peligrosas. La gobernanza debe navegar entre el monopolio tecnológico y la proliferación sin control.

### Tensión 3: Global vs. Local

Los sistemas de IA cruzan fronteras instantáneamente, pero la regulación es nacional. Sin mecanismos de gobernanza global, los estándares más exigentes simplemente se evitan ubicando las operaciones en otro lugar.

### Lo que SÍ es claro

Frente a estas tensiones, hay consensos emergentes que el campo está consolidando:

```mermaid
flowchart LR
    subgraph "Consensos Emergentes en Gobernanza de IA"
        C1["✅ Evaluaciones de seguridad\npre-despliegue en modelos\nfrontera son necesarias"]
        C2["✅ La supervisión humana\nen decisiones de alto impacto\nes innegociable"]
        C3["✅ La trazabilidad y\ndocumentación son\nrequisitos mínimos"]
        C4["✅ La alfabetización en IA\nes una responsabilidad\nde las organizaciones"]
        C5["✅ La gobernanza de IA\nes una función de negocio,\nno solo de IT o Legal"]
    end
    style C1 fill:#1b4332,color:#fff
    style C2 fill:#1b4332,color:#fff
    style C3 fill:#1b4332,color:#fff
    style C4 fill:#1b4332,color:#fff
    style C5 fill:#1b4332,color:#fff
```

La ética de la IA no es un obstáculo a la innovación. Bien diseñada, es la condición de posibilidad de una innovación que la sociedad pueda sostener en el tiempo — porque genera confianza, reduce riesgos sistémicos y garantiza que los beneficios de la tecnología se distribuyan de forma suficientemente amplia como para mantener el consenso social que la hace viable.

Todo algoritmo, como recuerda la UNESCO, refleja, reproduce y —con frecuencia— amplifica decisiones humanas previas. La diferencia entre una IA que sirve a la humanidad y una que la perjudica no está en el algoritmo. Está en las personas que deciden cómo se diseña, quién lo supervisa y con qué valores se alinea.

Esas personas somos nosotros.

---

## 📚 Referencias y Fuentes

1. **Reglamento (UE) 2024/1689** del Parlamento Europeo y del Consejo de 13 de junio de 2024 por el que se establecen normas armonizadas en materia de inteligencia artificial (AI Act). Diario Oficial de la UE. [https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R1689](https://eur-lex.europa.eu/legal-content/ES/TXT/?uri=CELEX:32024R1689)

2. **Parlamento Europeo** (2025). *Ley de IA de la UE: primera normativa sobre inteligencia artificial.* [https://www.europarl.europa.eu/topics/es/article/20230601STO93804/ley-de-ia-de-la-ue-primera-normativa-sobre-inteligencia-artificial](https://www.europarl.europa.eu/topics/es/article/20230601STO93804/ley-de-ia-de-la-ue-primera-normativa-sobre-inteligencia-artificial)

3. **IEBS Business School** (2025). *EU AI Act explicado para no juristas.* [https://www.iebschool.com/hub/eu-ai-act-explicado-para-no-juristas-management/](https://www.iebschool.com/hub/eu-ai-act-explicado-para-no-juristas-management/)

4. **MBIT School** (2025). *Reglamento Europeo de IA: Cómo cumplir el AI Act en España 2025.* [https://mbitschool.com/actualidad/reglamento-europeo-de-ia-como-cumplir-el-ai-act-en-espana](https://mbitschool.com/actualidad/reglamento-europeo-de-ia-como-cumplir-el-ai-act-en-espana)

5. **SapientiaDEV** (mayo 2026). *AI Act y sistemas de alto riesgo: por qué el 2 de agosto de 2026 sigue en pie.* [https://www.sapientiadev.com/blog/ai-act-alto-riesgo-2-agosto-2026](https://www.sapientiadev.com/blog/ai-act-alto-riesgo-2-agosto-2026)

6. **Infobae Tecno** (mayo 2026). *Cómo la ética y la regulación marcan los objetivos de la IA en 2026.* [https://www.infobae.com/tecno/2026/05/07/como-la-etica-y-la-regulacion-marcan-los-objetivos-de-la-inteligencia-artificial-en-2026/](https://www.infobae.com/tecno/2026/05/07/como-la-etica-y-la-regulacion-marcan-los-objetivos-de-la-inteligencia-artificial-en-2026/)

7. **Smart Factory Magazine** (2026). *6 tendencias que darán forma a la gobernanza de la IA en 2026.* [https://www.smartfactorymagazine.es/es/noticia/6-tendencias-que-daran-forma-a-la-gobernanza-de-la-ia-en-2026](https://www.smartfactorymagazine.es/es/noticia/6-tendencias-que-daran-forma-a-la-gobernanza-de-la-ia-en-2026)

8. **G-CERTI** (febrero 2026). *Gobernanza de IA 2026: ISO 42001 y el Futuro de la Inteligencia Artificial Responsable.* [https://gcerti.org/investigacion/gobernanza-ia-2026](https://gcerti.org/investigacion/gobernanza-ia-2026)

9. **ISO/IEC 42001:2023** — *Artificial intelligence — Management system — Requirements.* International Organization for Standardization.

10. **Actualidad IA** (2025). *Políticas y Regulaciones de la Inteligencia Artificial en 2025: Qué Esperar en 2026.* [https://actualidadia.io/que-esperar-en-2026/](https://actualidadia.io/que-esperar-en-2026/)

11. **Proteccióndata.es** (diciembre 2025). *Principios éticos sobre inteligencia artificial.* [https://protecciondata.es/principios-eticos-inteligencia-artificial/](https://protecciondata.es/principios-eticos-inteligencia-artificial/)

12. **NeuralTrust** (abril 2025). *Ética en IA: Equilibrando la Innovación y la Responsabilidad.* [https://neuraltrust.ai/es/blog/ai-ethics-balancing-innovation-responsibility](https://neuraltrust.ai/es/blog/ai-ethics-balancing-innovation-responsibility)

13. **Montreal AI Ethics Institute** (2025). *Principios éticos para una inteligencia artificial antropocéntrica.* [https://montrealethics.ai/principios-eticos-para-una-inteligencia-artificial-antropocentrica-consensos-actuales-desde-una-perspectiva-global-y-regional/](https://montrealethics.ai/principios-eticos-para-una-inteligencia-artificial-antropocentrica-consensos-actuales-desde-una-perspectiva-global-y-regional/)

14. **Ortiz de Zárate Alcarazo, L.** (2022). *Explicabilidad (de la inteligencia artificial).* Eunomía. Revista en Cultura de la Legalidad. DOI: 10.20318/eunomia.2022.6819. [https://www.researchgate.net/publication/359639642](https://www.researchgate.net/publication/359639642)

15. **Anthropic Alignment Science** (verano 2025). *Report on misalignment risk of deployed models.* [https://alignment.anthropic.com/](https://alignment.anthropic.com/)

16. **Anthropic & OpenAI** (julio 2025). *Findings from a Pilot Anthropic-OpenAI Alignment Evaluation Exercise.* [https://alignment.anthropic.com/2025/openai-findings/](https://alignment.anthropic.com/2025/openai-findings/)

17. **Alaga, J., Schuett, J., Anderljung, M.** (2024). *A Grading Rubric for AI Safety Frameworks.* Centre for the Governance of AI. arXiv:2409.08751. [https://arxiv.org/pdf/2409.08751](https://arxiv.org/pdf/2409.08751)

18. **UNESCO** (2021, actualizado 2025). *Recomendación sobre la Ética de la Inteligencia Artificial.* [https://www.unesco.org/es/artificial-intelligence/recommendation-ethics](https://www.unesco.org/es/artificial-intelligence/recommendation-ethics)

19. **BBC News** (mayo 2025). *AI system resorts to blackmail if told it will be removed.* [https://www.bbc.com/news/articles/cpqeng9d20go](https://www.bbc.com/news/articles/cpqeng9d20go)

20. **CES — Consejo Económico y Social** (marzo 2026). *Dictamen 3/2026 sobre gobernanza de la IA en España.* [https://www.ces.es/documents/10180/5392562/Dic032026.pdf](https://www.ces.es/documents/10180/5392562/Dic032026.pdf)

---

*📅 Artículo elaborado en junio de 2026 | Serie: **Inteligencia Artificial — De la Teoría a la Práctica***
*🖊️ Parte 3 de N — Ética y Gobernanza*

---
