def app_icon():

  Aliases.explorer.wndShell_TrayWnd.TrayDummySearchControl.btn.ClickButton()
  windows_UI_Core_CoreWindow = Aliases.Microsoft_Windows_Search.Search
  windows_UI_Core_CoreWindow.Search_box.Keys("q")
  
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  Regions.Quantist_App_icon.Check(Regions.CreateRegionInfo(Aliases.Microsoft_Windows_Search.Search, 461, 70, 206, 156, False))
  windows_UI_Core_CoreWindow.Click(748, 24)
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

def file_icon():
  TestedApps.explorer.Run()

  tvNamespaceTreeControl = Aliases.explorer.wndCabinetWClass2.ShellTabWindowClass.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.NamespaceTreeControl.tvNamespaceTreeControl
  tvNamespaceTreeControl.ExpandItem("|Desktop|This PC|Local Disk (C:)")
  tvNamespaceTreeControl.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist")
  tvNamespaceTreeControl.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist")
  tvNamespaceTreeControl.ClickItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist|Test_Data|Quantist Files")

  aqUtils.Delay(1000)

  Regions.Quantist_File_Icon.Check(Regions.CreateRegionInfo(Aliases.explorer.wndCabinetWClass.ShellTabWindowClass.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View, 7, 24, 236, 104, False))

def file_icon_bk():
    
  NameMapping.Sys.Keys("[Hold][Win]r[Release]")
  dlgRun = Aliases.explorer.dlgRun
  dlgRun.cbxOpen.SetText("explorer c:\\quantist\\sqa-quantist\\Test_Data\\Quantist Files")
  dlgRun.btnOK.ClickButton()
  Regions.Quantist_File_Icon2.Check(Aliases.explorer.wndCabinetWClass.ShellTabWindowClass.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View)

