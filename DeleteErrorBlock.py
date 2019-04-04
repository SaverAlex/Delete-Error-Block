# coding: utf - 8
import glob
import os
import sys

logFile = open("File summary information.log", 'w')  # Запись результатов обработки
for nameFile in glob.glob("*.dat"):  # Обход по всем файлам типа .dat
    print("Work in progress: " + nameFile)
    # Выцепляем из названия файла длину блока
    fl = nameFile[nameFile.find("fl") + 3: nameFile.find("fn") - 1]
    fn = nameFile[nameFile.find("fn") + 3: nameFile.find("dist") - 1]
    iterationAmount = int(fl) * int(fn) * 2 - 1
    originalFile = open(nameFile, 'r+')

    numLines = sum(1 for line in open(nameFile))  # Общее количество строк
    currentNumLines = 0  # Текущая строка, с помощью которой мы вичисляем проценты
    percent = 0
    barLength = 10  # Длинна прогрес бара

    arrayOfStrings = []  # Массив с всеми верными блоками
    numberOfLinesInBlock = 0  # Количство строк в блоке
    erroneousBlock = 0  # Количество блоков с ошибками
    rightBlock = 0  # Количество блоков без ошибок
    pointer = "-1 0 0 0 0 0 0"  # Разделитель блоков
    for currentLine in originalFile:  # Идём по строкам файла

        # Блок работы с процентами
        currentNumLines = currentNumLines + 1
        # Проверяем на целочисленный переход к следующему проценту
        if (float(currentNumLines) / numLines * 100) >= percent:
            block = int(round(barLength * (float(currentNumLines) / numLines)))
            if percent == 100:
                status = "Done"
            else:
                status = "..."
            text = "\rPercent: [{0}] {1}% {2}".format("#" * block + "-" * (barLength - block), percent, status)
            sys.stdout.write(text)
            percent = percent + 1
        # Конец блока работы с процентами

        currentLine = currentLine.rstrip()  # Удаляем знаки переноса строки
        if currentLine == "":
            continue
        arrayOfStrings.append(currentLine)
        # Блок работы с данными после встречи разделителя
        if currentLine == pointer:
            if numberOfLinesInBlock < iterationAmount:
                numberOfLinesInBlock = numberOfLinesInBlock + 1
                erroneousBlock = erroneousBlock + 1
                while numberOfLinesInBlock > 0:
                    arrayOfStrings.pop()
                    numberOfLinesInBlock = numberOfLinesInBlock - 1
            else:
                rightBlock = rightBlock + 1
            numberOfLinesInBlock = 0
            continue
        numberOfLinesInBlock = numberOfLinesInBlock + 1
    originalFile.close()
    # Блок записи результатов и вывод информации
    print ("")
    print("Checking the block length - completed")
    os.remove(nameFile)
    print("Number of lines: " + str(len(arrayOfStrings)))
    summaryFile = open(nameFile, 'w')
    sys.stdout.write("Writing to file - in the process")
    for line in arrayOfStrings:
        summaryFile.write(line + "\n")
    sys.stdout.write("\r" + "Writing to file - Сompleted successfully")
    print ("")
    summaryFile.close()
    logFile.write("Right block: " + str(rightBlock) + "\n")
    logFile.write("Erroneous blocks: " + str(erroneousBlock) + "\n")
    logFile.write("File Completed: " + nameFile + "\n")
    logFile.write("________________________________________________" + "\n")
