def Removing_CSV_Files():
  mainWindowView = Aliases.Quantist_WPF.HwndSource_MainWindowView.MainWindowView
  Xbutton = mainWindowView.RunTreeView.TreeViewItem.Button

  for i in range(16):
    Xbutton.ClickButton()



