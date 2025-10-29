import Quantist_Removing_Files
import Load_CSV_File

def Save_Changes_as_Quantist_Files():

  quantist = Aliases.Quantist
  hwndSource = quantist.MainWindowView
  hwndSource.Menu.WPFMenu.Click("File|Save All")
  button = hwndSource.MaxButtonOk
  button.ClickButton()
  button.ClickButton()
  quantist.dlgSavehmhmagWithControlsAs.btnSave.ClickButton()
  quantist.dlgSavehuCvP2As.btnSave.ClickButton()
  quantist.dlgSavelx200DataAs.btnSave.ClickButton()
  quantist.dlgSavemagpixDataAs.btnSave.ClickButton()
  quantist.dlgSavemessyPlateAs.btnSave.ClickButton()
  quantist.dlgSavemultipleCurvesAs.btnSave.ClickButton()
  quantist.dlgSaveoriginalResultsAs.btnSave.ClickButton()
  quantist.dlgSavepm6910As.btnSave.ClickButton()
  quantist.dlgSavepm8800As.btnSave.ClickButton()
  quantist.dlgSavepm8800modAs.btnSave.ClickButton()
  quantist.dlgSavequalitativeAs.btnSave.ClickButton()
  quantist.dlg.btnSave.ClickButton()
  quantist.dlgSavestandardcontrolunknownxponentAs.btnSave.ClickButton()
  quantist.dlgSavetestdataAs.btnSave.ClickButton()

     
def Test1():
  quantist = Aliases.Quantist
  hwndSource = quantist.MainWindowView
  hwndSource.LoadButton.ClickButton()
  dlgOpen = quantist.dlgOpen
  progress = dlgOpen.WorkerW.ReBarWindow32.AddressBandRoot.progress
  progress.BreadcrumbParent.toolbar.Click(506, 13)
  comboBox = progress.comboBox
  comboBox.SetText("C:\\Quantist\\SQA-Quantist\\Test_Data\\SampleQuantistFiles\\Saved_Changes")
  comboBox.ComboBox.Edit.Keys("[Enter]")
  UIItem = dlgOpen.DUIViewWndClassName.Explorer_Pane.CtrlNotifySink.ShellView.Items_View.flex_quantist
  OCR.Recognize(UIItem.Name).BlockByText("flex.quantist").Click()
  UIItem.Keys("^a")
  dlgOpen.btnOpen.ClickButton()
  treeView = hwndSource.RunTreeView
  treeView.ClickItem("|[0]|[4]")
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainView.CurvePanel.znotesView1.ztextBox1, "wText", cmpEqual, "Flex - new notes")
  treeView.ClickItem("|[1]|[4]")
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainView.CurvePanel.znotesView1.ztextBox1, "wText", cmpEqual, "flexmap data - new notes")
  treeView.ClickItem("|[2]|[4]")
  aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainView.CurvePanel.znotesView1, "wExpanded", cmpEqual, True)
  

def Save_As_Quantist():
  quantist = Aliases.Quantist
  hwndSource = quantist.MainWindowView
  hwndSource.Menu.WPFMenu.Click("File|Save All")
  dlgSavessspikedlinearityhepedtaAs = quantist.dlgSavessspikedlinearityhepedtaAs
  progress = dlgSavessspikedlinearityhepedtaAs.WorkerW.ReBarWindow32.AddressBandRoot.progress
  progress.BreadcrumbParent.toolbar.Click(518, 11)
  comboBox = progress.comboBox
  comboBox.SetText("C:\\Quantist\\SQA-Quantist\\Test_Data\\SampleQuantistFiles\\Saved_Changes")
  comboBox.ComboBox.Edit.Keys("[Enter]")
  dlgSavessspikedlinearityhepedtaAs.btnSave.ClickButton()
  hwndSource.RunTreeView.TreeViewItem.DeleteButton.ClickButton()



