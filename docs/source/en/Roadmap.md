# Roadmap

## TODO

* [x] REPL multi-line support.
* [x] Runtime debug information.
* [x] API stack protection.
* [x] File operation support.
* [x] Fixed (ROM based) hash table.
* [x] Destructor support.
* [x] Native module support (use `import xxx` to import a module).
* [x] Conditional expression support.
* [x] Anonymous function.
* [x] Bitwise operation.
* [x] Compound assignment statement.
* [x] Built-in scope.
* [x] Variable arguments function.
* [x] Native function: `classof(obj)`.
* [ ] ~~Native function: `copy(obj)`~~.
* [ ] Auto release call stack.
* [ ] Regular expression.
* [x] Stack usage optimized GC (no recursion).
* [x] Simplify stack overflow error messages.
* [x] Lambda expression.
* [x] Exceptional handling.
* [x] Bytecode file support.
* [x] Optimized iterator and `for` statement.
* [x] Connection operator (redefine the range operator `..`).
   * [x] String connection, e.g., `'string' .. expr`.
   * [x] List connection, e.g., `[] .. expr`.
   * [x] List serialization method (for high performance string connection).
* [x] Complete module support.
   * [x] Script file module export / import.
   * [x] Bytecode file module build / import.
   * [x] Shared native module (like *.so, *.dll) load.
* [x] Universal Equality Check API (like `==` operator but use in C).
   * [x] Complete map key matching.
   * [x] Complete exception value matching.
* [ ] Debugger support.
* [ ] Complete class and object mechanism.
* [ ] Support error message for *map_build* tool.
* [x] Overloaded call `()` operator.

## Release version

### V0.2.0

* [ ] Complete Chinese documentation.
* [x] Exceptional handling.
* [x] Complete module support.

### V0.1.0

* [x] Portable file system interface.
* [x] Precompiled constant object support.
* [x] Complete precompiled constant module.
* [ ] ~~More complete documentation (Chinese)~~.
* [ ] ~~Porting guide~~.


