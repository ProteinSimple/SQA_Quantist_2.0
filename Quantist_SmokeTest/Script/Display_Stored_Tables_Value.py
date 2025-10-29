def Print_Table_values(tbl, x, y):
  #MyVar = Project.Variables.MyTableVar
  #MyVar = Project.Variables.VariableByName["B7_H1_Analyte_Standards"]
  
  for rowIdx in range(0, x):
    for colIdx in range (0, y):
      Log.Message(tbl.Values[rowIdx,colIdx])
      #Log.Message(", ")
    Log.Message("\n")
    
def Results_values():
  Print_Table_values(test)  

def test_HoverMouse():
  Aliases.Quantist.MainWindowView.Border2.WPFObject()
  Aliases.Quantist.MainWindowView.Border2.WPFObject("ContentControl", "", 1).WPFObject("ContentListView", "", 1).WPFObject("DynamicGridControl", "", 1).WPFObject("CurveBuilderViewModel_a77b66372dcc4fb390147ec1de4dbc39").WPFObject("userControl").WPFObject("Grid", "", 1).WPFObject("Grid", "", 1).WPFObject("_curveView1").WPFObject("Grid", "", 1).WPFObject("_chart").WPFObject("_diagram").WPFObject("Pane", "", 1).HoverMouse(10,10)
  ProjectSuite.Variables.Long_Delay
  Aliases.Quantist.MainWindowView.Border2.WPFObject("ContentControl", "", 1).WPFObject("ContentListView", "", 1).WPFObject("DynamicGridControl", "", 1).WPFObject("CurveBuilderViewModel_a77b66372dcc4fb390147ec1de4dbc39").WPFObject("userControl").WPFObject("Grid", "", 1).WPFObject("Grid", "", 1).WPFObject("_curveView1").WPFObject("Grid", "", 1).WPFObject("_chart").WPFObject("_diagram").WPFObject("Pane", "", 1).HoverMouse(100,100)


