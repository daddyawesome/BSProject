Sub cLeanDump()
    Columns("GB:HE").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    
    Columns("DF:FQ").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    
    Columns("CO:CS").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    
    Columns("AX:CM").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    
    Columns("A:G").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    
    Range("A2:T2").Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    
    Sheets("RAW (2)").Select
    Range("A2").Select
    Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
        :=False, Transpose:=False
    ActiveWindow.SmallScroll Down:=-12
    Columns("A:A").Select
    Application.CutCopyMode = False
    Selection.NumberFormat = "m/d/yy;@"
    
    Sheets("Dump").Select
    ActiveWindow.SelectedSheets.Visible = False
    Sheets("RAW (2)").Select
    Range("A2").Select
End Sub
