import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

# Open aedt file
oDesktop.OpenProject("Z:/git/ML_WPT_coil/LRT/simple_model/script6/ML_aedt/ML6.aedt")

# Make project
oProject = oDesktop.SetActiveProject("ML6")
oProject.InsertDesign("Maxwell", "Maxwell_ML_v$VERSION_IDX_STR", "EddyCurrent", "")
oDesign = oProject.SetActiveDesign("Maxwell_ML_v$VERSION_IDX_STR")

# Make setup
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("EddyCurrent", 
	[
		"NAME:Setup1",
		"EnableZ:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"MaximumPasses:="	, 5,
		"MinimumPasses:="	, 5,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"SolveFieldOnly:="	, False,
		"PercentError:="	, 1E-12,
		"SolveMatrixAtLast:="	, True,
		"PercentError:="	, 1E-12,
		"CacheSaveKinZ:="	, "Delta",
		"ConstantDelta:="	, "0s",
		"UseIterativeSolver:="	, False,
		"RelativeResidual:="	, 1E-05,
		"NonLinearResidual:="	, 0.0001,
		"SmoothBHCurve:="	, False,
		"Frequency:="		, "60e+3Hz",
		"HasSweepSetup:="	, False,
		"UseHighOrderShapeFunZ:=", False,
		"UseMuLink:="		, False
	])


# Set variable

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:air_gap",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "100mm"
					
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:move",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$move"
					
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:width",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$width0, $width1] mm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:height",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$height0, $height1] mm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:gap",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$gap0, $gap1] mm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:coil_width",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$coil0_width, $coil1_width] mm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:coil_height",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$coil0_width, $coil1_width] mm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:ferrite_thick",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[10, 10] mm"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:ferrite_x",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[1.2, 1.2]"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:ferrite_y",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[1.05, 1.05]"
				]
			]
		]
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:ter",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.2*height[0]"
					
				]
			]
		]
	])



# Make air
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-width[0]/2-1.5*ter",
		"YPosition:="		, "-height[0]/2-1.5*ter",
		"ZPosition:="		, "-150mm-air_gap/2",
		"XSize:="		, "width[0]+3*ter",
		"YSize:="		, "height[0]+3*ter",
		"ZSize:="		, "300mm+air_gap"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Air",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 1,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


# Make core

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-width[0]/2*ferrite_x[0]",
		"YPosition:="		, "-height[0]/2*ferrite_y[0]",
		"ZPosition:="		, "-air_gap/2-coil_width[0]/2",
		"XSize:="		, "width[0]*ferrite_x[0]",
		"YSize:="		, "height[0]*ferrite_y[0]",
		"ZSize:="		, "-ferrite_thick[0]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ferrite_tx",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"ferrite\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-width[1]/2*ferrite_x[1]",
		"YPosition:="		, "-height[1]/2*ferrite_y[1]-height[1]/2-height[1]*move",
		"ZPosition:="		, "air_gap/2+coil_width[1]/2",
		"XSize:="		, "width[1]*ferrite_x[1]",
		"YSize:="		, "height[1]*ferrite_y[1]",
		"ZSize:="		, "ferrite_thick[1]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ferrite_rx1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"ferrite\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-width[1]/2*ferrite_x[1]",
		"YPosition:="		, "-height[1]/2*ferrite_y[1]+height[1]/2+height[1]*move",
		"ZPosition:="		, "air_gap/2+coil_width[1]/2",
		"XSize:="		, "width[1]*ferrite_x[1]",
		"YSize:="		, "height[1]*ferrite_y[1]",
		"ZSize:="		, "ferrite_thick[1]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "ferrite_rx2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"ferrite\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])




# =================================================================================================
# Make Tx
# =================================================================================================

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "-width[0]/2",
				"Y:="			, "height[0]/2+1.5*ter",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[0]/2",
				"Y:="			, "height[0]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[0]/2",
				"Y:="			, "-height[0]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "width[0]/2",
				"Y:="			, "-height[0]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "width[0]/2",
				"Y:="			, "height[0]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[0]/2+1*gap[0]",
				"Y:="			, "height[0]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[0]/2+1*gap[0]",
				"Y:="			, "height[0]/2-1*gap[0]",
				"Z:="			, "0mm"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 1,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 2,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 3,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 4,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 5,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Rectangle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[0]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "coil_height[0]",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])



oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "-width[0]/2+1*gap[0]",
				"Y:="			, "height[0]/2+0*gap[0]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[0]/2+1*gap[0]",
				"Y:="			, "-height[0]/2+1*gap[0]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "width[0]/2-1*gap[0]",
				"Y:="			, "-height[0]/2+1*gap[0]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "width[0]/2-1*gap[0]",
				"Y:="			, "height[0]/2-1*gap[0]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[0]/2+2*gap[0]",
				"Y:="			, "height[0]/2-1*gap[0]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[0]/2+2*gap[0]",
				"Y:="			, "height[0]/2-1*gap[0]",
				"Z:="			, "coil_width[0]+5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[0]/2+2*gap[0]",
				"Y:="			, "height[0]/2+1*gap[0]",
				"Z:="			, "coil_width[0]+5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[0]/2+2*gap[0]",
				"Y:="			, "height[0]/2+1*gap[0]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[0]/2+2*gap[0]",
				"Y:="			, "height[0]/2+1.5*ter",
				"Z:="			, "0mm"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 1,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 2,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 3,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 4,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 5,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 6,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 7,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Rectangle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[0]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "coil_height[0]",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Tx1,Tx2"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])


oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "-air_gap/2"
	])





# =================================================================================================
# Make Rx
# =================================================================================================

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2",
				"Y:="			, "height[0]/2+1.5*ter-height[1]/2-height[1]*move",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2",
				"Y:="			, "height[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2",
				"Y:="			, "-height[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "width[1]/2",
				"Y:="			, "-height[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "width[1]/2",
				"Y:="			, "height[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+1*gap[1]",
				"Y:="			, "height[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+1*gap[1]",
				"Y:="			, "height[1]/2-1*gap[1]",
				"Z:="			, "0mm"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 1,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 2,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 3,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 4,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 5,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Rectangle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[1]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "coil_height[1]",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])



oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+1*gap[1]",
				"Y:="			, "height[1]/2+0*gap[1]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+1*gap[1]",
				"Y:="			, "-height[1]/2+1*gap[1]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "width[1]/2-1*gap[1]",
				"Y:="			, "-height[1]/2+1*gap[1]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "width[1]/2-1*gap[1]",
				"Y:="			, "height[1]/2-1*gap[1]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+2*gap[1]",
				"Y:="			, "height[1]/2-1*gap[1]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+2*gap[1]",
				"Y:="			, "height[1]/2-1*gap[1]",
				"Z:="			, "coil_width[1]+5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+2*gap[1]",
				"Y:="			, "height[1]/2+1*gap[1]",
				"Z:="			, "coil_width[1]+5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+2*gap[1]",
				"Y:="			, "height[1]/2+1*gap[1]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-width[1]/2+2*gap[1]",
				"Y:="			, "height[0]/2+1.5*ter-height[1]/2-height[1]*move",
				"Z:="			, "0mm"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 1,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 2,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 3,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 4,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 5,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 6,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 7,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Rectangle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[1]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "coil_height[1]",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1,Rx2"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])

oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1"
	])
oEditor.Paste()


oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "height[1]/2+height[1]*move",
		"TranslateVectorZ:="	, "-air_gap/2"
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Rx3",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "height[1]/2+height[1]*move",
		"TranslateVectorZ:="	, "-air_gap/2"
	])






oEditor.Mirror(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:MirrorParameters",
		"MirrorBaseX:="		, "0mm",
		"MirrorBaseY:="		, "0mm",
		"MirrorBaseZ:="		, "0mm",
		"MirrorNormalX:="	, "0mm",
		"MirrorNormalY:="	, "1mm",
		"MirrorNormalZ:="	, "0mm"
	])

oEditor.Mirror(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:MirrorParameters",
		"MirrorBaseX:="		, "0mm",
		"MirrorBaseY:="		, "0mm",
		"MirrorBaseZ:="		, "0mm",
		"MirrorNormalX:="	, "1mm",
		"MirrorNormalY:="	, "0mm",
		"MirrorNormalZ:="	, "0mm"
	])

oEditor.Mirror(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:MirrorParameters",
		"MirrorBaseX:="		, "0mm",
		"MirrorBaseY:="		, "0mm",
		"MirrorBaseZ:="		, "0mm",
		"MirrorNormalX:="	, "0mm",
		"MirrorNormalY:="	, "0mm",
		"MirrorNormalZ:="	, "1mm"
	])


oEditor.Mirror(
	[
		"NAME:Selections",
		"Selections:="		, "Rx3",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:MirrorParameters",
		"MirrorBaseX:="		, "0mm",
		"MirrorBaseY:="		, "0mm",
		"MirrorBaseZ:="		, "0mm",
		"MirrorNormalX:="	, "1mm",
		"MirrorNormalY:="	, "0mm",
		"MirrorNormalZ:="	, "0mm"
	])

oEditor.Mirror(
	[
		"NAME:Selections",
		"Selections:="		, "Rx3",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:MirrorParameters",
		"MirrorBaseX:="		, "0mm",
		"MirrorBaseY:="		, "0mm",
		"MirrorBaseZ:="		, "0mm",
		"MirrorNormalX:="	, "0mm",
		"MirrorNormalY:="	, "0mm",
		"MirrorNormalZ:="	, "1mm"
	])




# Tx Make sheet

oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-width[0]/2-coil_width[0]/2",
		"YStart:="		, "height[0]/2+1.5*ter",
		"ZStart:="		, "-air_gap/2-coil_width[0]/2",
		"Width:="		, "coil_width[0]",
		"Height:="		, "coil_width[0]",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_in",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-width[0]/2+2*gap[0]-coil_width[0]/2",
		"YStart:="		, "height[0]/2+1.5*ter",
		"ZStart:="		, "-air_gap/2-coil_width[0]/2",
		"Width:="		, "coil_width[0]",
		"Height:="		, "coil_width[0]",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_out",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])



# Rx Make sheet


oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "width[1]/2-coil_width[1]/2",
		"YStart:="		, "height[0]/2+1.5*ter",
		"ZStart:="		, "air_gap/2-coil_width[1]/2",
		"Width:="		, "coil_width[1]",
		"Height:="		, "coil_width[1]",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx1_out",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "width[1]/2-2*gap[1]-coil_width[1]/2",
		"YStart:="		, "height[0]/2+1.5*ter",
		"ZStart:="		, "air_gap/2-coil_width[1]/2",
		"Width:="		, "coil_width[1]",
		"Height:="		, "coil_width[1]",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx1_in",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "width[1]/2-coil_width[1]/2",
		"YStart:="		, "-height[0]/2-1.5*ter",
		"ZStart:="		, "air_gap/2-coil_width[1]/2",
		"Width:="		, "coil_width[1]",
		"Height:="		, "coil_width[1]",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx2_in",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "width[1]/2-2*gap[1]-coil_width[1]/2",
		"YStart:="		, "-height[0]/2-1.5*ter",
		"ZStart:="		, "air_gap/2-coil_width[1]/2",
		"Width:="		, "coil_width[1]",
		"Height:="		, "coil_width[1]",
		"WhichAxis:="		, "Y"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx2_out",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])



# Set coil terminal

oModule = oDesign.GetModule("BoundarySetup")

oModule.AssignCoilTerminal(
	[
		"NAME:Tx_in",
		"Objects:="		, ["Tx_in"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", False
	])

oModule.AssignCoilTerminal(
	[
		"NAME:Tx_out",
		"Objects:="		, ["Tx_out"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", True
	])


oModule.AssignCoilTerminal(
	[
		"NAME:Rx1_in",
		"Objects:="		, ["Rx1_in"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", False
	])

oModule.AssignCoilTerminal(
	[
		"NAME:Rx1_out",
		"Objects:="		, ["Rx1_out"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", True
	])

oModule.AssignCoilTerminal(
	[
		"NAME:Rx2_in",
		"Objects:="		, ["Rx2_in"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", True
	])

oModule.AssignCoilTerminal(
	[
		"NAME:Rx2_out",
		"Objects:="		, ["Rx2_out"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", False
	])



# Add winding

oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignWindingGroup(
	[
		"NAME:Tx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "100A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])

oModule.AssignWindingGroup(
	[
		"NAME:Rx1",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "100A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])

oModule.AssignWindingGroup(
	[
		"NAME:Rx2",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "100A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])


# Assign coil terminal


oModule.AddWindingTerminals("Tx", ["Tx_in", "Tx_out"])

oModule.AddWindingTerminals("Rx1", ["Rx1_in", "Rx1_out"])

oModule.AddWindingTerminals("Rx2", ["Rx2_in", "Rx2_out"])


oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignRadiation(
	[
		"NAME:Radiation1",
		"Objects:="		, ["Air"]
	])


oModule = oDesign.GetModule("MaxwellParameterSetup")
oModule.AssignMatrix(
	[
		"NAME:Matrix1",
		[
			"NAME:MatrixEntry",
			[
				"NAME:MatrixEntry",
				"Source:="		, "Rx1"
			],
			[
				"NAME:MatrixEntry",
				"Source:="		, "Rx2"
			],
			[
				"NAME:MatrixEntry",
				"Source:="		, "Tx"
			]
		]
	])


oModule = oDesign.GetModule("MeshSetup")
oModule.AssignSkinDepthOp(
	[
		"NAME:SkinDepth1",
		"Enabled:="		, True,
		"Objects:="		, ["Rx1","Rx3","Tx1"],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"SkinDepth:="		, "0.269794105765115mm",
		"SurfTriMaxLength:="	, "300mm",
		"NumLayers:="		, "2"
	])


oProject.Save()
oDesign.Analyze("Setup1")




oModule = oDesign.GetModule("FieldsReporter")

oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Tx1")
oModule.CalcOp("Integrate")
oModule.EnterScalar(1)
oModule.CalcOp("*")
oModule.AddNamedExpression("Tx_loss", "Fields")

oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Rx1")
oModule.CalcOp("Integrate")
oModule.EnterScalar(1)
oModule.CalcOp("*")
oModule.AddNamedExpression("Rx1_loss", "Fields")

oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Rx3")
oModule.CalcOp("Integrate")
oModule.EnterScalar(1)
oModule.CalcOp("*")
oModule.AddNamedExpression("Rx2_loss", "Fields")




oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("L Table 1", "EddyCurrent", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"air_gap:="		, ["Nominal"],
		"move:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Matrix1.L(Tx,Tx)","Matrix1.L(Rx1,Rx1)","Matrix1.L(Rx2,Rx2)"]
	])
oModule.ExportToFile("L Table 1", "Z:/git/ML_WPT_coil/LRT/simple_model/script6/ML_data/inductance$VERSION_IDX_STR.csv", False)



oModule.CreateReport("Coupling Coeff Table 1", "EddyCurrent", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"air_gap:="		, ["Nominal"],
		"move:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Matrix1.CplCoef(Tx,Rx1)","Matrix1.CplCoef(Tx,Rx2)","Matrix1.CplCoef(Rx1,Rx2)"]
	])
oModule.ExportToFile("Coupling Coeff Table 1", "Z:/git/ML_WPT_coil/LRT/simple_model/script6/ML_data/coupling$VERSION_IDX_STR.csv", False)

oModule.CreateReport("Calculator Expressions Table 1", "Fields", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"air_gap:="		, ["Nominal"],
		"move:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Tx_loss","Rx1_loss","Rx2_loss"]
	])
oModule.ExportToFile("Calculator Expressions Table 1", "Z:/git/ML_WPT_coil/LRT/simple_model/script6/ML_data/loss$VERSION_IDX_STR.csv", False)