# Delete-Error-Block
Скрипт написан для обработки результатов симуляции, он принимает на вход файлы формата .dat.
Пример файла: 2.dip_pos.L.5.fl.10.fn.51.dist.0.01.dat.
Проверка идёт на длинну блоков, если блок меньше нормальной длинный (fl * fn * 2 - 1),
то он считается ошибочным и подлежит удалению, такие блоки появляются при сбоях в симуляции. 
Задачей этого скрипта является очищение файлов от неполных блоков для дальнейшей корректной работы.
