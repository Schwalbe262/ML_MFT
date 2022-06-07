import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

N1 = $N1

# Open aedt file
#oDesktop.OpenProject("Z:/ANSYS_simulation/transformer/core_type_HFTR/HFTR_2022_05_31_solid_model/ML24.aedt")
oDesktop.OpenProject("Y:/git/ML_MFT/core_type/solid_model/script24/ML_aedt/ML24.aedt")


# Make project
oProject = oDesktop.SetActiveProject("ML24")
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
		"Frequency:="		, "30e+3Hz",
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
					"NAME:N1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$N1"
					
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
					"NAME:w1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$w1mm"
					
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
					"NAME:l1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$l1mm"
					
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
					"NAME:l2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$l2mm"
					
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
					"NAME:h1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$h1mm"
					
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
					"NAME:space",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$space1, $space2, $space3, $space4] mm"
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
					"Value:="		, "[$coil_width1, $coil_width2] mm"
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
					"NAME:Num",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "6"
					
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
					"NAME:move_z",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$move_z1, $move_z2] mm"
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
					"NAME:air",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$air_x, $air_y, $air_z] mm"
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
					"NAME:offset_z",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$offset_z1, $offset_z2] mm"
				]
			]
		]
	])


# Make air
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-(air[0])/2",
		"YPosition:="		, "-(air[1])/2",
		"ZPosition:="		, "-(air[2])/2",
		"XSize:="		, "(air[0])",
		"YSize:="		, "(air[1])",
		"ZSize:="		, "(air[2])"
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
		"XPosition:="		, "-(w1)/2",
		"YPosition:="		, "-(2*l1+l2)/2",
		"ZPosition:="		, "-(2*l1+h1)/2",
		"XSize:="		, "w1",
		"YSize:="		, "2*l1+l2",
		"ZSize:="		, "2*l1+h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "core",
		"Flags:="		, "",
		"Color:="		, "(0 0 0)",
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
		"XPosition:="		, "-(w1)/2",
		"YPosition:="		, "-(l2)/2",
		"ZPosition:="		, "-(h1)/2",
		"XSize:="		, "w1",
		"YSize:="		, "l2",
		"ZSize:="		, "h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "core_sub",
		"Flags:="		, "",
		"Color:="		, "(0 0 0)",
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


oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "core",
		"Tool Parts:="		, "core_sub"
	], 
	[
		"NAME:SubtractParameters",
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
				"X:="			, "(air[0])/2",
				"Y:="			, "-l1/2-space[1]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1/2-space[1]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[0]",
				"Y:="			, "-l1/2-space[1]",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[0]",
				"Y:="			, "l1/2+space[1]",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2",
				"Y:="			, "l1/2+space[1]",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]",
				"Y:="			, "l1/2+space[1]",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]",
				"Y:="			, "-l1/2-space[1]",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+0.5*space[0]",
				"Y:="			, "-l1/2-space[1]",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
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
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[0]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "Num",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_in",
		"Flags:="		, "",
		"Color:="		, "(255 0 0)",
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

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_in",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "-(l1+l2)/2",
		"TranslateVectorZ:="	, "(N1/2+0.25)*(coil_width[0]+move_z[0])"
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
				"X:="			, "w1/2+0.5*space[0]",
				"Y:="			, "-l1/2-space[1]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1/2-space[1]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[0]",
				"Y:="			, "-l1/2-space[1]",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[0]",
				"Y:="			, "l1/2+space[1]",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]",
				"Y:="			, "l1/2+space[1]",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]",
				"Y:="			, "-l1/2-space[1]",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+2*space[0]",
				"Y:="			, "-l1/2-space[1]",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
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
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[0]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "Num",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_out",
		"Flags:="		, "",
		"Color:="		, "(255 0 0)",
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
				"X:="			, "w1/2+2*space[0]",
				"Y:="			, "-l1/2-space[1]",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "(air[0])/2",
				"Y:="			, "-l1/2-space[1]",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[0]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "Num",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_out2",
		"Flags:="		, "",
		"Color:="		, "(255 0 0)",
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
	"Selections:="		, "Tx_out,Tx_out2"
], 
[
	"NAME:UniteParameters",
	"KeepOriginals:="	, False
])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_out",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "-(l1+l2)/2",
		"TranslateVectorZ:="	, "-(N1/2-1-0.25)*(coil_width[0]+move_z[0])"
	])


if N1>2 : 

	oEditor.CreatePolyline(
		[
			"NAME:PolylineParameters",
			"IsPolylineCovereZ:="	, True,
			"IsPolylineCloseZ:="	, False,
			[
				"NAME:PolylinePoints",
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+0.5*space[0]",
					"Y:="			, "-l1/2-space[1]",
					"Z:="			, "0mm"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2",
					"Y:="			, "-l1/2-space[1]",
					"Z:="			, "0mm"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-space[0]",
					"Y:="			, "-l1/2-space[1]",
					"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-space[0]",
					"Y:="			, "l1/2+space[1]",
					"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+space[0]",
					"Y:="			, "l1/2+space[1]",
					"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+space[0]",
					"Y:="			, "-l1/2-space[1]",
					"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+0.5*space[0]",
					"Y:="			, "-l1/2-space[1]",
					"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
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
				"XSectionType:="	, "Circle",
				"XSectionOrient:="	, "Auto",
				"XSectionWidth:="	, "coil_width[0]",
				"XSectionTopWidth:="	, "0mm",
				"XSectionHeight:="	, "0mm",
				"XSectionNumSegments:="	, "Num",
				"XSectionBendType:="	, "Corner"
			]
		], 
		[
			"NAME:Attributes",
			"Name:="		, "Tx1",
			"Flags:="		, "",
			"Color:="		, "(255 0 0)",
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

	oEditor.Move(
		[
			"NAME:Selections",
			"Selections:="		, "Tx1",
			"NewPartsModelFlag:="	, "Model"
		], 
		[
			"NAME:TranslateParameters",
			"TranslateVectorX:="	, "0mm",
			"TranslateVectorY:="	, "-(l1+l2)/2",
			"TranslateVectorZ:="	, "(N1/2-1+0.25)*(coil_width[0]+move_z[0])"
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
				"X:="			, "(air[0])/2",
				"Y:="			, "l1/2+space[3]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "l1/2+space[3]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[2]",
				"Y:="			, "l1/2+space[3]",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[2]",
				"Y:="			, "-l1/2-space[3]",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2",
				"Y:="			, "-l1/2-space[3]",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[2]",
				"Y:="			, "-l1/2-space[3]",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[2]",
				"Y:="			, "l1/2+space[3]",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+0.5*space[2]",
				"Y:="			, "l1/2+space[3]",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
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
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[1]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "Num",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx_in",
		"Flags:="		, "",
		"Color:="		, "(0 0 255)",
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

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Rx_in",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "(l1+l2)/2",
		"TranslateVectorZ:="	, "(N1/2+0.25)*(coil_width[1]+move_z[1])"
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
				"X:="			, "w1/2+0.5*space[2]",
				"Y:="			, "l1/2+space[3]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "l1/2+space[3]",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[2]",
				"Y:="			, "l1/2+space[3]",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[2]",
				"Y:="			, "-l1/2-space[3]",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[2]",
				"Y:="			, "-l1/2-space[3]",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[2]",
				"Y:="			, "l1/2+space[3]",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+2*space[2]",
				"Y:="			, "l1/2+space[3]",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
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
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[1]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "Num",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx_out",
		"Flags:="		, "",
		"Color:="		, "(0 0 255)",
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
				"X:="			, "w1/2+2*space[2]",
				"Y:="			, "l1/2+space[3]",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "(air[0])/2",
				"Y:="			, "l1/2+space[3]",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "Circle",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "coil_width[1]",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "Num",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx_out2",
		"Flags:="		, "",
		"Color:="		, "(0 0 255)",
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
	"Selections:="		, "Rx_out,Rx_out2"
], 
[
	"NAME:UniteParameters",
	"KeepOriginals:="	, False
])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Rx_out",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "(l1+l2)/2",
		"TranslateVectorZ:="	, "-(N1/2-1-0.25)*(coil_width[1]+move_z[1])"
	])


if N1>2 : 

	oEditor.CreatePolyline(
		[
			"NAME:PolylineParameters",
			"IsPolylineCovereZ:="	, True,
			"IsPolylineCloseZ:="	, False,
			[
				"NAME:PolylinePoints",
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+0.5*space[2]",
					"Y:="			, "l1/2+space[3]",
					"Z:="			, "0mm"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2",
					"Y:="			, "l1/2+space[3]",
					"Z:="			, "0mm"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-space[2]",
					"Y:="			, "l1/2+space[3]",
					"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-space[2]",
					"Y:="			, "-l1/2-space[3]",
					"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+space[2]",
					"Y:="			, "-l1/2-space[3]",
					"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+space[2]",
					"Y:="			, "l1/2+space[3]",
					"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+0.5*space[2]",
					"Y:="			, "l1/2+space[3]",
					"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
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
				"XSectionType:="	, "Circle",
				"XSectionOrient:="	, "Auto",
				"XSectionWidth:="	, "coil_width[1]",
				"XSectionTopWidth:="	, "0mm",
				"XSectionHeight:="	, "0mm",
				"XSectionNumSegments:="	, "Num",
				"XSectionBendType:="	, "Corner"
			]
		], 
		[
			"NAME:Attributes",
			"Name:="		, "Rx1",
			"Flags:="		, "",
			"Color:="		, "(0 0 255)",
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

	oEditor.Move(
		[
			"NAME:Selections",
			"Selections:="		, "Rx1",
			"NewPartsModelFlag:="	, "Model"
		], 
		[
			"NAME:TranslateParameters",
			"TranslateVectorX:="	, "0mm",
			"TranslateVectorY:="	, "(l1+l2)/2",
			"TranslateVectorZ:="	, "(N1/2-1+0.25)*(coil_width[1]+move_z[1])"
		])



## copy

for i in range(N1-3) : 

    selection = "Tx" + str(i+2)
    z_vector = "-" + str(i+1) + "*(coil_width[0]+move_z[0])"

    oEditor.Copy(
        [
            "NAME:Selections",
            "Selections:="		, "Tx1"
        ])
    oEditor.Paste()

    oEditor.Move(
        [
            "NAME:Selections",
            "Selections:="		, selection,
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:TranslateParameters",
            "TranslateVectorX:="	, "0mm",
            "TranslateVectorY:="	, "0mm",
            "TranslateVectorZ:="	, z_vector
        ])

for i in range(N1-3) : 

    selection = "Rx" + str(i+2)
    z_vector = "-" + str(i+1) + "*(coil_width[1]+move_z[1])"

    oEditor.Copy(
        [
            "NAME:Selections",
            "Selections:="		, "Rx1"
        ])
    oEditor.Paste()

    oEditor.Move(
        [
            "NAME:Selections",
            "Selections:="		, selection,
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:TranslateParameters",
            "TranslateVectorX:="	, "0mm",
            "TranslateVectorY:="	, "0mm",
            "TranslateVectorZ:="	, z_vector
        ])



## Unite

Tx_unite = "Tx_in,Tx_out"
Rx_unite = "Rx_in,Rx_out"

for i in range(N1-2) : 

    Tx_unite = Tx_unite + ",Tx" + str(i+1)
    Rx_unite = Rx_unite + ",Rx" + str(i+1)

oEditor.Unite(
[
	"NAME:Selections",
	"Selections:="		, Tx_unite
], 
[
	"NAME:UniteParameters",
	"KeepOriginals:="	, False
])

oEditor.Unite(
[
	"NAME:Selections",
	"Selections:="		, Rx_unite
], 
[
	"NAME:UniteParameters",
	"KeepOriginals:="	, False
])




## offset_z

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_in",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "offset_z[0]"
	])


oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Rx_in",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "offset_z[1]"
	])




## Make terminal

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "(air[0])/2",
		"YCenter:="		, "-l1/2-space[1]",
		"ZCenter:="		, "0mm",
		"XStart:="		, "(air[0])/2",
		"YStart:="		, "-l1/2-space[1]-coil_width[0]/2",
		"ZStart:="		, "0mm",
		"NumSides:="		, "Num",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_in_ter",
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

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_in_ter",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "-(l1+l2)/2",
		"TranslateVectorZ:="	, "(N1/2+0.25)*(coil_width[0]+move_z[0])+offset_z[0]"
	])


oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "(air[0])/2",
		"YCenter:="		, "-l1/2-space[1]",
		"ZCenter:="		, "0mm",
		"XStart:="		, "(air[0])/2",
		"YStart:="		, "-l1/2-space[1]",
		"ZStart:="		, "coil_width[0]/2",
		"NumSides:="		, "Num",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_out_ter",
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

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx_out_ter",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "-(l1+l2)/2",
		"TranslateVectorZ:="	, "(-N1/2+0.25)*(coil_width[0]+move_z[0])+offset_z[0]"
	])


oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "(air[0])/2",
		"YCenter:="		, "l1/2+space[3]",
		"ZCenter:="		, "0mm",
		"XStart:="		, "(air[0])/2",
		"YStart:="		, "l1/2+space[3]+coil_width[1]/2",
		"ZStart:="		, "0mm",
		"NumSides:="		, "Num",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx_in_ter",
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

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Rx_in_ter",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "(l1+l2)/2",
		"TranslateVectorZ:="	, "(N1/2+0.25)*(coil_width[1]+move_z[1])+offset_z[1]"
	])


oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "(air[0])/2",
		"YCenter:="		, "l1/2+space[3]",
		"ZCenter:="		, "0mm",
		"XStart:="		, "(air[0])/2",
		"YStart:="		, "l1/2+space[3]",
		"ZStart:="		, "coil_width[1]/2",
		"NumSides:="		, "Num",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx_out_ter",
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

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Rx_out_ter",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "(l1+l2)/2",
		"TranslateVectorZ:="	, "(-N1/2+0.25)*(coil_width[1]+move_z[1])+offset_z[1]"
	])



# Boundary setup

oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignCoilTerminal(
	[
		"NAME:Tx_in",
		"Objects:="		, ["Tx_in_ter"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", False
	])
oModule.AssignCoilTerminal(
	[
		"NAME:Tx_out",
		"Objects:="		, ["Tx_out_ter"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", True
	])
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
oModule.AddWindingTerminals("Tx", ["Tx_in", "Tx_out"])


oModule.AssignCoilTerminal(
	[
		"NAME:Rx_in",
		"Objects:="		, ["Rx_in_ter"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", False
	])
oModule.AssignCoilTerminal(
	[
		"NAME:Rx_out",
		"Objects:="		, ["Rx_out_ter"],
		"Conductor number:="	, "1",
		"Point out of terminal:=", True
	])
oModule.AssignWindingGroup(
	[
		"NAME:Rx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "100A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])
oModule.AddWindingTerminals("Rx", ["Rx_in", "Rx_out"])



## Assign

oModule = oDesign.GetModule("MaxwellParameterSetup")
oModule.AssignMatrix(
	[
		"NAME:Matrix1",
		[
			"NAME:MatrixEntry",
			[
				"NAME:MatrixEntry",
				"Source:="		, "Rx"
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
		"Objects:="		, ["Rx_in","Tx_in"],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"SkinDepth:="		, "0.381546483421347mm",
		"SurfTriMaxLength:="	, "51.7996915365222mm",
		"NumLayers:="		, "2"
	])

oProject.Save()

oDesign.Analyze("Setup1")



# Report

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("magnetizing inductance", "EddyCurrent", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"w1:="			, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Matrix1.CplCoef(Tx,Rx)^2 * Matrix1.L(Tx,Tx) * 1000","Matrix1.CplCoef(Tx,Rx)^2 * Matrix1.L(Rx,Rx) * 1000"]
	])

oModule.CreateReport("leakage inductance", "EddyCurrent", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"w1:="			, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["(1-Matrix1.CplCoef(Tx,Rx)^2) * Matrix1.L(Tx,Tx) * 1000", "(1-Matrix1.CplCoef(Tx,Rx)^2) * Matrix1.L(Rx,Rx) * 1000"]
	])



oModule = oDesign.GetModule("FieldsReporter")
oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Tx_in")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("Tx_loss", "Fields")
oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Rx_in")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("Rx_loss", "Fields")
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("copper loss", "Fields", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"w1:="			, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Tx_loss","Rx_loss"]
	])


oModule.ExportToFile("magnetizing inductance", "Y:/git/ML_MFT/core_type/solid_model/script24/ML_data/magnetizing_inductance$VERSION_IDX_STR.csv", False)
oModule.ExportToFile("leakage inductance", "Y:/git/ML_MFT/core_type/solid_model/script24/ML_data/leakage_inductance$VERSION_IDX_STR.csv", False)
oModule.ExportToFile("copper loss", "Y:/git/ML_MFT/core_type/solid_model/script24/ML_data/loss$VERSION_IDX_STR.csv", False)
