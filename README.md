# Простые макросы и анализ на VBA

## В папке Python scripts for excel приведены примеры скриптов на Python (генерация данных в таблицы, преобразования, фильтрация, запись в файл, подсчет формул)
----
### Первый макрос выводит "отчет" по заказу по нажатию кнопки (MsgBox)

![first](https://sun9-74.userapi.com/impg/17uS2DJrlA_PYF1uSPivFt2M_7NJmCfONmuvfw/x6rzrmMfcPo.jpg?size=1310x527&quality=96&sign=48987a0e39b55e5aa663f43b80ac09e9&type=album)

----

### Сборник макросов для последовательного исполнения


![macros](https://sun9-52.userapi.com/impg/97kh_KuZI-BgNaAPTfA6vuLIUk7zvqQLgoYxFA/L8BI0I8nPnE.jpg?size=1418x821&quality=96&sign=b6119ec841d47e0d10b785d8ef988064&type=album)

### MACROS GO 
Формирует последовательность фиббоначи (берет значение из ячейки B1), передает сформированные формулы в ячейки.

----

### 2 STEP

Формирует таблицу со столбцами H, I, J, K - если к ячейкам "аналитики" закреплены формулы, производится автоматический расчет (кроме ratetion тк нет необходимых таблиц)

----

### Средняя выручка
Вычисляет средню выручку (Сумма всей выручки на количество совершенных сделок (проданных товаров)) Сочетание клавиш: Ctrl+a или нажатие на кнопку


### Ratetion - Коффициент удержания клиентов

(Общее число пользователей за конкретный промежуток времени - новые пользователи за этот же промежуток) / общее количество пользователей за все время * 100. Сочетание клавиш: Ctrl+r или нажатие на кнопку


### CLV - Стоимость клиента на протяжении всего срока сотрудничества

Общая сумма по каждому клиенту + учитывается столбец статус с неоплаченными заказами

Итоговые вычисления

![end](https://sun9-80.userapi.com/impg/kbviP4T9xy56DzhgS2UKzBMWTmEnXho7V3u-uA/4oRkO-4M1o8.jpg?size=448x318&quality=96&sign=034cd8d9cf2413a74fcbb157ecb233b2&type=album)


```

Option Explicit
Sub Go()
    Dim intSwapCase As Integer
    intSwapCase = Range("L5").Value + 5
    
    Dim strBrickStr_full As String
    Dim strBrickStr_1 As String
    Dim strBrickStr_2 As String
    Dim strBrickStr_3 As String
    Dim strBrickStr_4 As String
    Dim strBrickStr_5 As String
    ' strBrickStr_1 = Range("D" & inSwapCase)
    strBrickStr_1 = Cells(intSwapCase, 4).Value
    strBrickStr_2 = Cells(intSwapCase, 7).Value
    strBrickStr_3 = Cells(intSwapCase, 5).Value
    strBrickStr_4 = Cells(intSwapCase, 9).Value
    strBrickStr_5 = Cells(intSwapCase, 10).Value
    strBrickStr_full = strBrickStr_1 & " заказал " & strBrickStr_2 & " шт " & strBrickStr_3
    strBrickStr_full = strBrickStr_full & vbNewLine & "Действует скидка на заказ в размере: " & strBrickStr_4 & " €"
    strBrickStr_full = strBrickStr_full & vbNewLine & "Итоговая сумма к оплате: " & strBrickStr_5 & " €"
    If intSwapCase > 15 Or intSwapCase < 6 Then
        MsgBox "Введите корректные значения!"
    Else
        MsgBox strBrickStr_full
    End If
End Sub

------

Option Explicit

Sub СР_выручка()
'
' СР_выручка Макрос
' Формула средней выручки"&chr(13)&" Сумма всей выручки на количество совершенных сделок"&chr(13)&" (проданных товаров)
'
' Сочетание клавиш: Ctrl+a
'
    Range("M3").FormulaR1C1 = _
        "=ROUND(SUM(R[-1]C[-3]:R[38]C[-3])/COUNT(R[-1]C[-3]:R[38]C[-3]), 2)"
End Sub

Sub Ratetion()
'
' Ratetion Макрос
' Коэффициент удержания клиентов
'
' Сочетание клавиш: Ctrl+r
'
    Range("H2:H16").Select
    Application.CutCopyMode = False
    Application.CutCopyMode = False
    ActiveWindow.SmallScroll Down:=-1
    Range("I4").Select
    Application.CutCopyMode = False
    Range("H2:H41").AdvancedFilter Action:=xlFilterCopy, CopyToRange:=Range( _
        "O4:O24"), Unique:=True
    Application.CutCopyMode = False
    Application.CutCopyMode = False
    Application.CutCopyMode = False
    Range("H2:H16").AdvancedFilter Action:=xlFilterCopy, CopyToRange:=Range( _
        "N4:N17"), Unique:=True
    Range("M5").Select
    ActiveCell.FormulaR1C1 = _
        "=ROUND((COUNT(R[-1]C[1]:R[9]C[1])-COUNTIF(R[-1]C[1]:R[9]C[1], R[-1]C[1]>10))/COUNT(R[-1]C[2]:R[12]C[2]) * 100, 2)"
End Sub
Sub CLV()
    Dim sum As Long, i As Integer, j As Integer
    For j = 4 To 17
        For i = 2 To 41
            If (Range("O" & j) = Range("H" & i)) And Range("K" & i) <> "Неоплачен" Then
                sum = sum + Range("J" & i)
            End If
    Next i
    Range("q" & j) = sum
    sum = 0
Next j
End Sub

------------------

Option Explicit

Sub SetData()
' Keyboard shortcut: Ctrl+Shift+R
' Заполнение таблицы
Dim max_row As Integer, max_Col As Integer
max_row = 40
max_Col = 4
Dim intId As Integer, StrDate As Date, status As String, price As Long
Dim i As Integer
Range("H1") = "id клиента"
Range("I1") = "Дата оформления"
Range("J1") = "Сумма"
Range("K1") = "Статус"
StrDate = "03.2023"
For i = 2 To max_row
    intId = Int((10 * Rnd) + 1)
    Range("H" & i) = intId
    
    If i = 38 Then
        Range("H" & i) = "11"
        Range("H" & i).Interior.Color = vbYellow
    End If
    If i = 3 Then
        Range("H" & i) = "12"
        Range("H" & i).Interior.Color = vbYellow
    End If
    If i = 8 Then
        Range("H" & i) = "13"
        Range("H" & i).Interior.Color = vbYellow
    End If
    
    Range("I" & i) = i & "04.2023"
'    If i > 31 Then
'        Range("I" & i) = (i - 30) & "04.2023"
'    Else
'        Range("I" & i) = i & StrDate
'    End If
    ' Range("I" & i) = i & StrDate
    
    price = Int((1000 * Rnd) + 100)
    Range("J" & i) = price
    
    If i = 19 Or i = 7 Or i = 33 Then
        Range("K" & i) = "Неоплачен"
        Range("K" & i).Interior.Color = vbRed
    Else
        Range("K" & i) = "Оплачен"
        Range("K" & i).Interior.Color = vbGreen
    End If
Next i

End Sub


-----

Option Explicit

Sub Fibb()
    ' Keyboard Shortcut: Ctrl+q

    Dim i As Integer
    Dim prev As Long, current As Long, temp As Long
    prev = 0
    current = 1
    Dim k As Integer
    k = Range("B1")
    For i = 1 To k
        Cells(i, 1).Value = prev
        temp = current
        current = prev + current
        prev = temp
    Next i
    
    ' Блок функкций
    Dim str As String
    str = "A1:A" & k
    Range("E1") = "=SUM(A1:A30)"
    Range("E2") = "=Average(A1:A30)"
    Range("E3") = "=Count(A1:A30)"
    Range("E4") = "=CountA(A1:A30)"
    Range("E5") = "=CountIF(A1:A30, 21)"
    Range("E6") = "=Min(A1:A30)"
    Range("E7") = "=MAX(A1:A30)"
    Range("E8") = "=Column(A1)"
    Range("E9") = "=Row(A15)"
    Range("E10") = "=Rows(A1:A30)"
    Range("E11") = "=LOWER(E11)"
    Range("E12") = "=Upper(C12)"
    Range("E13") = "=MEDIAN(A1:A30)"
    Range("E14") = "=PI()"
    Range("E15") = "=COS(A1)"
    Range("E16") = "=SIN(A1)"
    ' что не так? =ЕСЛИ(СУММ(A1:A30)=1346268;1;0)
    ' Range("E15") = "=IF(SUM(A1:A30)=1346268;1;0)"

End Sub
```

## Сводные таблицы

Интерактивные диаграммы

----

![Dashboard](https://sun9-78.userapi.com/impg/8hWktiV_iMxSrl2UtnXlcusv1KdoyHAaHF2kNQ/wo1v0gJ_etc.jpg?size=1928x1048&quality=96&sign=16a0461037be2cad5eeaff2f71563c92&type=album)

----

![Dashboard_change](https://sun9-72.userapi.com/impg/GvecE1B1-yaGehZJt1r-eTHUqwB2gMawuMDz1A/edij42VHgGI.jpg?size=1928x1048&quality=96&sign=aeb960ce1fc62133f909cf2a0aca2408&type=album)


----

## Данные сводной таблицы

![PivotTable](https://sun9-29.userapi.com/impg/6yAiQvyKi_wlb2q0UGB7B1pG-S6wuKLGhtdLag/57que2VEJfo.jpg?size=1074x766&quality=96&sign=714b1172d0363d38d56f0e411a8fbefe&type=album)
