import Quantist_Removing_Files
import Load_CSV_File 

def Load_CSV_Files():
  quantist = Aliases.Quantist
  mainWindowView = Aliases.Quantist.MainWindowView
  treeView = Aliases.Quantist.MainWindowView.RunTreeView

  flag = True
  while (treeView.HasItems):
     Quantist_Removing_Files.Removing_CSV_Files(flag)  

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  quantist.MainWindowView.LoadButton.ClickButton()    
  dlgOpen = quantist.dlgOpen
  UIItem = dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.FLEX_csv
  UIItem.Keys("^a")

  dlgOpen.btnOpen.ClickButton()
  Aliases.Quantist.MainWindowView.MaxButtonOk.ClickButton()
    
  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)
  Aliases.Quantist.MainWindowView.ToggleShareView.ClickButton(cbChecked)  

  treeView = mainWindowView.RunTreeView
  treeView.ClickItem("|[0]|[0]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[1]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[2]|[2]")
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  treeView.ClickItem("|[3]|[3]")  

  Regions.MainWin_horz_shareview.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr)
  Aliases.Quantist.MainWindowView.ToggleVerticalButton.ClickButton(cbChecked)

  ProjectSuite.Variables.Short_Delay  
  Regions.MainWin_vert_shareview.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr)

  ProjectSuite.Variables.Short_Delay
  Aliases.Quantist.MainWindowView.ToggleVerticalButton.ClickButton(cbUnChecked)

  ProjectSuite.Variables.Short_Delay
  #Regions.MainWin_horz_shareview.Check(Aliases.Quantist.MainWindowView.MainViewRunCtr)


def Max_Load_Files():
  #dialog display max number (>50)
  Aliases.Quantist.MainWindowView.MaxButtonOk.ClickButton()
