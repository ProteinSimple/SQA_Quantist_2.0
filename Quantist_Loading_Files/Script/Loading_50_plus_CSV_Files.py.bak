import Load_CSV_File 
import Quantist_Removing_Files

def Loading_50_Plus():
  
  quantist = Aliases.Quantist
  main = Aliases.Quantist.MainWindowView
  treeView = main.RunTreeView
  
  #dialog = Aliases.Quantist.MainWindowView.MainViewRunCtr.UserMessageBox
  dialog = NameMapping.Sys.Quantist2.HwndSource_MainWindowView.MainWindowView.Grid.UserMessageBox
  
  flag = False
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
    #treeView.TreeViewItem.Button.ClickButton()
     
  if (not treeView.HasItems):
    main.LoadButton.ClickButton()
    dlgOpen = quantist.dlgOpen

    pane = dlgOpen.DUIViewWndClassName.Explorer_Pane
    tree = pane.CtrlNotifySink2.NamespaceTreeControl.tvNamespaceTreeControl
    tree.ExpandItem("|Desktop|This PC|Local Disk (C:)")
    tree.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist")
    tree.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist")
    tree.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist|Test_Data")
    tree.ClickItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist|Test_Data|67 files")
    UIItem = pane.CtrlNotifySink.ShellView.Items_View.HMHMAG_with_Controls_csv
    UIItem.Keys("^a")
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    Aliases.Quantist.dlgOpen.btnOpen.ClickButton()

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  if (dialog.WaitProperty("Enabled", True, 2000)):
     aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainViewRunCtr.UserMessageBox, "Enabled", cmpEqual, True)
     main.MaxButtonOk.ClickButton()
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)

  load_17_CSV_Files()
  edit_CSV_Files()   
  getTime()

   
def edit_CSV_Files():
  hwndSource = Aliases.Quantist.MainWindowView
  treeView = hwndSource.RunTreeView
  textBox = hwndSource.MainView.CurvePanel.znotesView1.ztextBox1

  aqUtils.Delay(ProjectSuite.Variables.Long_Delay)

#  i = 0
#  for i in range(49):
#      treeView.ClickItem("|[i]|[4]")
#      #textBox.Click(98, 31)
#      textBox.Keys("TEST")
#      aqUtils.Delay(500)
#      i += 1
  
  treeView.ClickItem("|[0]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[1]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[2]|[4]")
  textBox.Keys("TEST")
  
  treeView.ClickItem("|[3]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[4]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[5]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[6]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[7]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[8]|[4]")
  textBox.Keys("TEST")

  treeView.ClickItem("|[9]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[10]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[11]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[12]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[13]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[14]|[4]")
  textBox.Keys("TEST")
  treeView.ClickItem("|[15]|[4]")
  textBox.Keys("TEST")
  
def load_17_CSV_Files():
    
  quantist = Aliases.Quantist
  main = Aliases.Quantist.MainWindowView
  treeView = main.RunTreeView
  
  #dialog = Aliases.Quantist.MainWindowView.MainViewRunCtr.UserMessageBox
  dialog = NameMapping.Sys.Quantist2.HwndSource_MainWindowView.MainWindowView.Grid.UserMessageBox
  
  flag = False
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)
    #treeView.TreeViewItem.Button.ClickButton()
     
  if (not treeView.HasItems):
    main.LoadButton.ClickButton()
    dlgOpen = quantist.dlgOpen

    pane = dlgOpen.DUIViewWndClassName.Explorer_Pane
    tree = pane.CtrlNotifySink2.NamespaceTreeControl.tvNamespaceTreeControl
    tree.ExpandItem("|Desktop|This PC|Local Disk (C:)")
    tree.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist")
    tree.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist")
    tree.ExpandItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist|Test_Data")
    tree.ClickItem("|Desktop|This PC|Local Disk (C:)|Quantist|SQA-Quantist|Test_Data|SampleQuantistFiles") #67 files")
    UIItem = pane.CtrlNotifySink.ShellView.Items_View.HMHMAG_with_Controls_csv
    UIItem.Keys("^a")
    aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
    Aliases.Quantist.dlgOpen.btnOpen.ClickButton()

    if (dialog.WaitProperty("Enabled", True, 2000)):
     aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainViewRunCtr.UserMessageBox, "Enabled", cmpEqual, True)
     main.MaxButtonOk.ClickButton()

  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
def getTime():
  # Start a time counter
  aqPerformance.Start()

  quantist = Aliases.Quantist
  main = Aliases.Quantist.MainWindowView
  treeView = main.RunTreeView

  flag = True
  if (treeView.HasItems):
    Quantist_Removing_Files.Removing_CSV_Files(flag)  

  timeTotal = aqPerformance.__getprop__("Value") / 1000 #convert to second
  timeDialog = timeTotal / 17 # average time to display and confirm the dialog message

  # Log the elapsed time, in second
  Log.Message("Approximate time (in second) to remove CSV files with expected displayed dialogs: " + aqConvert.IntToStr(timeTotal))  
  Log.Message("Approximate time (in second) to display and confirm the message: " + aqConvert.IntToStr(timeDialog))