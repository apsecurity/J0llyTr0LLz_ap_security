# J0llyTr0LLz
automation for primary binary analysis

### REMEMBER

INSTALL MODES___.TTF

### ABOUT

J0llyTr0LLz: Программа для первичного анализа бинарных файлов

У большинства исследователей программного обеспечения первые шаги одинаковые. Речь идет о первичном анализе бинарного файла. Каждый раз повторятся один и тот же алгоритм: 

1. Узнать что за файл
2. Узнать какой у него хеш
3. Какие защиты стоят (Canary, PIE, NX, RELRO)

В данной статье будет рассмотрена утилита для реверс-инжиниринга и бинарной эксплуатации бинарного файла под названием J0llyTroLLz, написанная сотрудником нашего отдела разработки.

J0llyTr0LLz shows a number of characteristics of the executable file, ELF FORMAT ONLY.

1.  File type
2.  File size
3.  Endianness
4.  Architecture
5.  Binary Type (ELF, PE, Mach-O)
6.  HEX-view
7.  Hashes
8.  Information about ELF
9.  Protection types
10. ROPGadgets and find gadgets
11. strings
12. seccomp-tool dump

### J0llyTroLLz contains:

1. readelf -h programm
2. file
3. checksec (pwntool)
4. ROPGadget
5. HEX-View
6. Hashes
7. strings
8. seccomp-tool dump

### INSTALL

RUN setuptools.sh
