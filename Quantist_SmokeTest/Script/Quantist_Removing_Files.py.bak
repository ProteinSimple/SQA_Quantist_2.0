def Removing_CSV_Files(flag):

  main = Aliases.Quantist.MainWindowView
  treeViewItem = Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem
  Xbutton = treeViewItem.DeleteButton

  unsaved_diag = Aliases.Quantist.MainWindowView.MainViewRunCtr.UserMessageBox
  
  if (Aliases.Quantist.MainWindowView.RunTreeView.HasItems):
    i = Aliases.Quantist.MainWindowView.RunTreeView.TreeViewItem.WPFControlOrdinalNo

  while (i != 0): 
    try:
        if (Aliases.Quantist.MainWindowView.RunTreeView.HasItems):
           Log.Message("Total Number of loading items: " + aqConvert.VartoStr(i))
    
        if (Xbutton.Exists):
           Xbutton.ClickButton()
           aqUtils.Delay(ProjectSuite.Variables.Short_Delay)       
    
        if (flag == True):
           if (Aliases.Quantist.MainWindowView.MainViewRunCtr.UserMessageBox.Visible):
              main.MaxButtonOk.ClickButton()
        i -= 1
        
    except:
        Log.Message("Can not remove run file from Run Control View")
        break
        
   #finally:
   #  break
   
  Log.Message("No more run file from Run Control View")          
  
def Alternate():
  treeView = Aliases.Quantist.MainWindowView.RunTreeView
  Xbutton = treeView.TreeViewItem.delete_Button
  
  while (treeView.HasItems): 
    Xbutton.ClickButton()
    #if (aqObject.CheckProperty(treeView, "HasItems", cmpEqual, False)):
    if (not treeView.HasItems):
      break

    #  The try block lets we test a block of code for errors.
    #  The except block lets we handle the error.
    #  The else block lets we execute code when there is no error.
    #  The finally block lets you execute code, regardless of the result of the try- and except blocks.

    #  The try block will generate an exception if something goes wrong
    #  Many Exceptions
    #  We can define as many exception blocks as we want, e.g. 
    #      if one wants to execute a special block of code for a special kind of error:

    try:
      print("Hello")
    except:
      print("Something went wrong")
    else:     # We can use the else keyword to define a block of code to be executed if no errors were raised:
      print("Nothing went wrong")

    try:
      print(x)
    except:
      print("Something went wrong")
    finally:  # The finally block, if specified, will be executed regardless if the try block raises an error or not.
      print("The 'try except' is finished")

def Unsaved_diag_Wait():
  unsaved_diag = Aliases.Quantist.MainWindowView.MainViewRunCtr.UserMessageBox  
  if (unsaved_diag.WaitProperty("Exists", True, 2000)):
  #dialog is displayed
     if (unsaved_dialog.Enabled == True):
        main.MaxButtonOk.ClickButton()
           
     if (main.MaxButtonOk.WaitProperty("Exists", True, 1000)):
       main.MaxButtonOk.ClickButton()
     else:
       aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
