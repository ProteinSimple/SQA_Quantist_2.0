
def NotePad_SaveToFile(fileName):

    TestedApps.notepad.Run(1, True)
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    
    notepad = Aliases.notepad
    wndNotepad = notepad.wndNotepad
  
    richEditD2DPT = wndNotepad.NotepadTextBox.RichEditD2DPT
    richEditD2DPT.Keys("^v")

    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    richEditD2DPT.Keys("^s")
        
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

    dlgSaveAs = notepad.dlgSaveAs
    dlgSaveAs.DUIViewWndClassName.Explorer_Pane.FloatNotifySink.ComboBox.SetText(Project.Variables.OutputFolder + fileName)

    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    dlgSaveAs.btnSave.ClickButton()
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
    notepad.dlgConfirmSaveAs.Confirm_Save_As.CtrlNotifySink.btnYes.ClickButton()

    notepad.Close()