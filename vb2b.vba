Sub cLeanDump()
    Columns("FT:HE").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    
    Columns("DD:FR").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    
    Columns("CO:DA").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    
    Columns("AX:CM").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    
    Columns("AV:AV").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    
    Columns("AN:AS").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    
    
    Columns("AI:AJ").Select
    Application.CutCopyMode = False
    Selection.Delete Shift:=xlToLeft
    
    Columns("q:AG").Select
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
