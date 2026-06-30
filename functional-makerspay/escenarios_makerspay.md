# Plan de Pruebas Funcionales - MakersPay (Billetera Digital)

## 1. Estrategia de Pruebas
Para garantizar la calidad del módulo de transferencias, se ha definido la siguiente estrategia:

### Tipos de Pruebas:
- **Pruebas Funcionales (Caja Negra):** Validación de los requisitos del negocio sin acceso al código fuente.
- **Pruebas Negativas:** Intentar forzar errores mediante ingresos de datos inválidos o que violen las reglas de negocio.
- **Pruebas de Integración:** Verificar la correcta actualización de saldos entre el remitente y el destinatario.

### Técnicas de Diseño de Pruebas:
1. **Análisis de Valores Límite (BVA):** Pruebas en los bordes de $5.000 y $2.000.000.
2. **Partición de Equivalencia (EP):** Clasificación de montos en rangos válidos e inválidos.
3. **Matriz de Transición de Estados:** Para validar el flujo del saldo (Saldo inicial -> Transacción -> Saldo final).

---

## 2. Casos de Prueba (Test Cases)

| ID | Título | Precondición | Pasos | Resultado Esperado |
|:---|:---|:---|:---|:---|
| **TC-01** | Transferencia exitosa dentro del rango | Usuario A con saldo de $50.000 y Usuario B registrado. | 1. Ingresar celular de B.<br>2. Monto: $10.000.<br>3. Confirmar. | Saldo A: $40.000.<br>Saldo B: +$10.000.<br>Registro en ambos historiales. |
| **TC-02** | Validación de monto mínimo (Límite inferior) | Usuario con saldo suficiente. | 1. Ingresar celular destino.<br>2. Monto: $4.999.<br>3. Confirmar. | Mensaje de error: "El monto mínimo por transacción es $5.000 COP". No hay descuento de saldo. |
| **TC-03** | Validación de monto máximo (Límite superior) | Usuario con saldo suficiente. | 1. Ingresar celular destino.<br>2. Monto: $2.000.001.<br>3. Confirmar. | Mensaje de error: "El monto máximo por transacción es $2.000.000 COP". No hay descuento de saldo. |
| **TC-04** | Validación de saldo insuficiente | Usuario A con saldo de $10.000. | 1. Ingresar celular destino.<br>2. Monto: $15.000.<br>3. Confirmar. | Mensaje de error: "Saldo insuficiente para realizar la transacción". El saldo se mantiene en $10.000. |
| **TC-05** | Restricción de auto-envío | Usuario autenticado. | 1. Ingresar su propio número de celular.<br>2. Monto: $5.000.<br>3. Confirmar. | Mensaje de error: "No se permiten envíos a su mismo número de celular". |
| **TC-06** | Integridad de saldo en falla de red | Conexión interrumpida durante el proceso. | 1. Iniciar transferencia.<br>2. Simular caída de red.<br>3. Reingresar al sistema. | El saldo no debe verse afectado (atomicidad de la transacción). |

---

## 3. Técnicas de Pruebas Utilizadas (Justificación)
- Se utilizó **Análisis de Valores Límite** para asegurar que los desarrolladores no hayan usado comparadores incorrectos (ej. usar `>` en lugar de `>=`).
- Se aplicó **Partición de Equivalencia** para reducir el número de pruebas, asumiendo que si el sistema falla con $2.500.000, fallará con cualquier monto superior.