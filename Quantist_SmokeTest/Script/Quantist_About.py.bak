def About():
  
  #BuiltIn.ShowMessage("Temporary display view")
  Aliases.Quantist.MainWindowView.Menu.WPFMenu.Click("Help|About")
  Regions.Quantist_AboutView.Check(Aliases.Quantist.About)
  #Aliases.Quantist.MainWindowView.MaxButtonOk.ClickButton()  
  #aqObject.CheckProperty(Aliases.Quantist.MainWindowView.MainViewRunCtr.Version, "Text", cmpEqual, "Version: 1.0.0.1")
  #aqObject.CheckProperty(Aliases.Quantist.About.AboutView.Label1001.WPFControlText, "Text", cmpEqual, "1.0.0.1")
  
  #OCR.Recognize(Aliases.Quantist.About.AboutView.Label1001).CheckText("*2.0.0.1010*")
  #aqObject.CheckProperty(Aliases.Quantist.About.AboutView.WPFObject("Grid", "", 1).WPFObject("Label", "2.0.0.1010", 3).WPFControlText, cmpEqual, "2.0.0.1010")
  aqObject.CheckProperty(Aliases.Quantist.About.AboutView.Label2001010, "WPFControlText", cmpEqual, "2.0.0.1010")

  #Aliases.Quantist.MainWindowView.Menu.WPFMenu.Click("Help|About")
  aqObject.CheckProperty(Aliases.Quantist.About, "WndCaption", cmpEqual, "About")
  #aqObject.CheckProperty(Aliases.Quantist.About.AboutView.Version, "Enabled", cmpEqual, True)  
  
  aqUtils.Delay(ProjectSuite.Variables.Short_Delay)
  
  Aliases.Quantist.About.Close()  
  #verify Quantist TM top left corner
  Regions.Quantist_TM.Check(Regions.CreateRegionInfo(Aliases.Quantist.MainWindowView, 30, 9, 64, 21, False), False, False, 89, 17)
  
  #verify Quantist splash view
  #Regions.QuantistSplashView.Check(Aliases.Quantist.MainWindowView.MainView.Grid)
  Regions.QuantistSplashScreen.Check(Aliases.Quantist.MainWindowView.MainView.Grid.Image)  

  
def Main_Menu():
  quantist = Aliases.Quantist
  main = Aliases.Quantist.MainWindowView
  menu = main.Menu
  #menu.WPFMenu.Click("Help|User Guide")
  #button = main.MaxButtonOk
  #button.ClickButton()
  #menu.WPFMenu.Click("Help|Save Diagnostic")
  #button.ClickButton()
  menu.WPFMenu.Click("Help|About")
  
  #button.ClickButton()
  #menu.WPFMenu.Click("File|Open Runs")
  aqObject.CheckProperty(Aliases.Quantist.HwndSource_AboutView, "WndCaption", cmpEqual, "About")
  quantist.HwndSource_AboutView.Close()


def Test1():
  aqObject.CheckProperty(Aliases.Quantist.About.AboutView.Label1001, "Enabled", cmpEqual, True)

def Test2():
  OCR.Recognize(Aliases.Quantist.About.AboutView.Label1001).CheckText("*1.0.0.1*")

def Test3():
  aqObject.CheckProperty(Aliases.Quantist.About.AboutView.Label2001010, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(Aliases.Quantist.About.AboutView.Label2001010, "WPFControlText", cmpEqual, "2.0.0.1010")
