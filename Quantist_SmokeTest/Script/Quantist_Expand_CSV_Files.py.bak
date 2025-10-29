def Expanding_CSV_Files():
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  Aliases.Quantist.MainWindowView.CollapseButton.ClickButton()
  i = Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.WPFControlOrdinalNo
  Log.Message("Total Number of loading items: " + aqConvert.VartoStr(i))

  Regions.RunTreeView_Collapse.Check(Aliases.Quantist.MainWindowView.RunTreeView)
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)  
  Aliases.Quantist.MainWindowView.ExpandingButton.ClickButton()
  Regions.RunTreeView_Expanse.Check(Aliases.Quantist.MainWindowView.RunTreeView)

  count=1
  j = Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.ChildCount

  while (count < 6):  #maximum 6 expanding items in the tree
    if (Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.WPFObject("TreeViewItem", "", count).Exists):
      Log.Message("Visible? " + aqConvert.VarToStr(Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.WPFObject("TreeViewItem", "", count).Visible))
      Log.Message("Item: " + aqConvert.VarToStr(count) + " is in the tree view") 
    else:
      Log.Message("Visible? " + aqConvert.VarToStr(Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.WPFObject("TreeViewItem", "", count).Visible))
    count += 1
  Log.Message("Total Number of expanding items: " + aqConvert.VartoStr(j))
 