<!-- Spanish Translation: Emiliano Gonzalez (egonzalez . hiperion @ gmail . com) -->
# Hoja de ruta

## POR HACER

* [x] Soporte multilínea REPL.
* [x] Información de depuración en tiempo de ejecución.
* [x] Protección de pila API.
* [x] Soporte de operación de archivos.
* [x] Tabla hash fija (basada en ROM).
* [x] Soporte de destructor.
* [x] Compatibilidad con módulos nativos (use `import xxx` para importar un módulo).
* [x] Soporte de expresiones condicionales.
* [x] Función anónima.
* [x] Operación bit a bit.
* [x] Sentencia de asignación compuesta.
* [x] Alcance incorporado.
* [x] Función de argumentos variables.
* [x] Función nativa: `classof(obj)`.
* [ ] ~~Función nativa: `copy(obj)`~~.
* [ ] Pila de llamadas de liberación automática.
* [ ] Expresión regular.
* [x] GC optimizado para el uso de la pila (sin recursividad).
* [x] Simplifica los mensajes de error de desbordamiento de pila.
* [x] Expresión lambda.
* [x] Manejo excepcional.
* [x] Compatibilidad con archivos de bytecode.
* [x] Iterador optimizado y sentencia `for`.
* [x] Operador de conexión (redefine el operador de rango `..`).
   * [x] Conexión de cadena, por ejemplo, `'cadena' .. expr`.
   * [x] Lista de conexiones, por ejemplo, `[] .. expr`.
   * [x] Método de serialización de lista (para conexión de cadena de alto rendimiento).
* [x] Soporte de módulo completo.
   * [x] Exportación/importación del módulo de archivo de script.
   * [x] Compilación/importación del módulo de archivo de bytecode.
   * [x] Carga del módulo nativo compartido (como *.so, *.dll).
* [x] API de verificación de igualdad universal (como el operador `==` pero se usa en C).
   * [x] Coincidencia de clave de mapa completa.
   * [x] Coincidencia de valor de excepción completa.
* [ ] Compatibilidad con el depurador.
* [ ] Mecanismo completo de clases y objetos.
* [ ] Mensaje de error de soporte para la herramienta *map_build*.
* [x] Llamada sobrecargada al operador `()`.

## Versión de lanzamiento

### V0.2.0

* [ ] Documentación china completa.
* [x] Manejo excepcional.
* [x] Soporte de módulo completo.

### V0.1.0

* [x] Interfaz de sistema de archivos portátil.
* [x] Compatibilidad con objetos constantes precompilados.
* [x] Módulo constante completo precompilado.
* [ ] ~~Documentación más completa (chino)~~.
* [ ] ~~Guía de portabilidad~~.
