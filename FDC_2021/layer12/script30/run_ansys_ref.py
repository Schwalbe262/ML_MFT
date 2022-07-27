N1 = int($N1)
N2 = int($N2)
NX1 = int($NX1)
NX2 = int($NX2)


import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()


oDesktop.OpenProject("Y:/git/ML_MFT/FDC_2021/layer12/script30/ML_aedt/ML30.aedt")



oProject = oDesktop.SetActiveProject("ML30")
oProject.InsertDesign("Maxwell", "Maxwell_ML_v$VERSION_IDX_STR", "EddyCurrent", "")
oDesign = oProject.SetActiveDesign("Maxwell_ML_v$VERSION_IDX_STR")



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
		"Frequency:="		, "40e+3Hz",
		"HasSweepSetup:="	, False,
		"UseHighOrderShapeFunZ:=", False,
		"UseMuLink:="		, False
	])





# Set variable

oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.AddMaterial(
	[
		"NAME:ferrite$VERSION_IDX_STR",
		"CoordinateSystemType:=", "Cartesian",
		"BulkOrSurfaceType:="	, 1,
		[
			"NAME:PhysicsTypes",
			"set:="			, ["Electromagnetic","Thermal","Structural"]
		],
		[
			"NAME:AttachedData",
			[
				"NAME:MatAppearanceData",
				"property_data:="	, "appearance_data",
				"Red:="			, 89,
				"Green:="		, 94,
				"Blue:="		, 107
			]
		],
		"permittivity:="	, "12",
		"permeability:="	, "$per",
		"conductivity:="	, "0.01",
		"thermal_conductivity:=", "4",
		"mass_density:="	, "4600",
		"specific_heat:="	, "750",
		"youngs_modulus:="	, "119000000000",
		"thermal_expansion_coefficient:=", "1e-05"
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
					"NAME:N2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$N2"
					
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
					"Value:="		, "[$space1, $space2, $space3, $space4, $space5, $space6] mm"
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
		"YPosition:="		, "-(4*l1+2*l2)/2",
		"ZPosition:="		, "-(2*l1+h1)/2",
		"XSize:="		, "w1",
		"YSize:="		, "4*l1+2*l2",
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
		"MaterialValue:="	, "\"ferrite$VERSION_IDX_STR\"",
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
		"YPosition:="		, "(l1)",
		"ZPosition:="		, "-(h1)/2",
		"XSize:="		, "w1",
		"YSize:="		, "l2",
		"ZSize:="		, "h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "core_sub1",
		"Flags:="		, "",
		"Color:="		, "(0 0 0)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"ferrite$VERSION_IDX_STR\"",
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
		"YPosition:="		, "-(l1)",
		"ZPosition:="		, "-(h1)/2",
		"XSize:="		, "w1",
		"YSize:="		, "-l2",
		"ZSize:="		, "h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "core_sub2",
		"Flags:="		, "",
		"Color:="		, "(0 0 0)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"ferrite$VERSION_IDX_STR\"",
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
		"Tool Parts:="		, "core_sub1,core_sub2"
	], 
	[
		"NAME:SubtractParameters",
	])





# =================================================================================================
# Make Tx
# =================================================================================================

#Tx in
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
				"X:="			, "air[0]/2",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "l1+h1/2+5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2+space[0]",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "l1+h1/2+5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2+space[0]",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "l1+h1/2"
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


# Tx inner 1
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2+space[0]",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "l1+h1/2-offset_z[0]-(N1/2)*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2+space[0]",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "-0/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "-0/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-coil_width[0]/2-space[0]",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "-0/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-coil_width[0]/2-space[0]",
				"Y:="			, "l1+coil_width[0]/2+space[1]",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2+space[0]",
				"Y:="			, "l1+coil_width[0]/2+space[1]",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2+space[0]",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
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


# Tx inner 2
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
					"X:="			, "w1/2+coil_width[0]/2+space[0]",
					"Y:="			, "-l1-coil_width[0]/2-space[1]",
					"Z:="			, "-0/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+coil_width[0]/2",
					"Y:="			, "-l1-coil_width[0]/2-space[1]",
					"Z:="			, "-0/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-coil_width[0]/2-space[0]",
					"Y:="			, "-l1-coil_width[0]/2-space[1]",
					"Z:="			, "-0/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-coil_width[0]/2-space[0]",
					"Y:="			, "l1+coil_width[0]/2+space[1]",
					"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+coil_width[0]/2+space[0]",
					"Y:="			, "l1+coil_width[0]/2+space[1]",
					"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+coil_width[0]/2+space[0]",
					"Y:="			, "-l1-coil_width[0]/2-space[1]",
					"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+coil_width[0]/2",
					"Y:="			, "-l1-coil_width[0]/2-space[1]",
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
			"Name:="		, "Tx2",
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


# Tx inner copy
for i in range(N1-3) : 

    selection = "Tx" + str(i+3)
    z_vector = "-" + str(i+2) + "*(coil_width[0]+move_z[0])"

    oEditor.Copy(
        [
            "NAME:Selections",
            "Selections:="		, "Tx2"
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

oEditor.Move(
        [
            "NAME:Selections",
            "Selections:="		, "Tx2",
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:TranslateParameters",
            "TranslateVectorX:="	, "0mm",
            "TranslateVectorY:="	, "0mm",
            "TranslateVectorZ:="	, "-1*(coil_width[0]+move_z[0])"
        ])


# Tx inner end

name_temp = "Tx" + str(N1)
move_temp = "-" + str(N1-1) + "*(coil_width[0]+move_z[0])"

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2+space[0]",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "-0/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "-0/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-coil_width[0]/2-space[0]",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "-0/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-coil_width[0]/2-space[0]",
				"Y:="			, "l1+coil_width[0]/2+space[1]",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2+space[0]",
				"Y:="			, "l1+coil_width[0]/2+space[1]",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2+space[0]",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2+space[0]",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "-l1-h1/2-offset_z[0]-(N1/2)*coil_width[0]-(N1/2)*move_z[0]+10*(coil_width[0]+move_z[0])"
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
		"Name:="		, name_temp,
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
            "Selections:="		, name_temp,
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:TranslateParameters",
            "TranslateVectorX:="	, "0mm",
            "TranslateVectorY:="	, "0mm",
            "TranslateVectorZ:="	, move_temp 
        ])


#Tx out

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
				"X:="			, "air[0]/2",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "-l1-h1/2-5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2+space[0]",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "-l1-h1/2-5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+coil_width[0]/2+space[0]",
				"Y:="			, "-l1-coil_width[0]/2-space[1]",
				"Z:="			, "-l1-h1/2"
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


## Tx Unite

Tx_unite = "Tx1"

for i in range(N1-1) : 	
    Tx_unite = Tx_unite + ",Tx" + str(i+2)

oEditor.Unite(
[
	"NAME:Selections",
	"Selections:="		, Tx_unite
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
            "TranslateVectorZ:="	, "offset_z[0]+(N1/2)*coil_width[0]+(N1/2)*move_z[0]"
        ])

oEditor.Unite(
[
	"NAME:Selections",
	"Selections:="		, "Tx1,Tx_in,Tx_out"
], 
[
	"NAME:UniteParameters",
	"KeepOriginals:="	, False
])






# =================================================================================================
# Make Rx
# =================================================================================================

#Rx in
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
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
				"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
				"Z:="			, "air[2]/2-5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
				"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
				"Z:="			, "air[2]/2"
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


# Rx inner 1
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
				"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
				"Z:="			, "air[2]/2-5mm-offset_z[1]-(N2/4)*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
				"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
				"Z:="			, "-0/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]",
				"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
				"Z:="			, "-0/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-1*coil_width[0]-1/2*coil_width[1]-space[0]-space[2]",
				"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
				"Z:="			, "-0/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-1*coil_width[0]-1/2*coil_width[1]-space[0]-space[2]",
				"Y:="			, "l1+1*coil_width[0]+1/2*coil_width[1]+space[1]+space[2]",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
				"Y:="			, "l1+1*coil_width[0]+1/2*coil_width[1]+space[1]+space[2]",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
				"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]",
				"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
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


# Rx inner 2
if NX2>2 :
	oEditor.CreatePolyline(
		[
			"NAME:PolylineParameters",
			"IsPolylineCovereZ:="	, True,
			"IsPolylineCloseZ:="	, False,
			[
				"NAME:PolylinePoints",
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
					"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
					"Z:="			, "-0/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]",
					"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
					"Z:="			, "-0/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-1*coil_width[0]-1/2*coil_width[1]-space[0]-space[2]",
					"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
					"Z:="			, "-0/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-1*coil_width[0]-1/2*coil_width[1]-space[0]-space[2]",
					"Y:="			, "l1+1*coil_width[0]+1/2*coil_width[1]+space[1]+space[2]",
					"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
					"Y:="			, "l1+1*coil_width[0]+1/2*coil_width[1]+space[1]+space[2]",
					"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
					"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
					"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]",
					"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
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
			"Name:="		, "Rx2",
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


# Rx inner copy
for i in range(NX2-3) : 

    selection = "Rx" + str(i+3)
    z_vector = "-" + str(i+2) + "*(coil_width[1]+move_z[1])"

    oEditor.Copy(
        [
            "NAME:Selections",
            "Selections:="		, "Rx2"
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

oEditor.Move(
        [
            "NAME:Selections",
            "Selections:="		, "Rx2",
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:TranslateParameters",
            "TranslateVectorX:="	, "0mm",
            "TranslateVectorY:="	, "0mm",
            "TranslateVectorZ:="	, "-1*(coil_width[1]+move_z[1])"
        ])


# Rx inner end

name_temp = "Rx" + str(NX2)
move_temp = "-" + str(NX2-1) + "*(coil_width[1]+move_z[1])"

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
				"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
				"Z:="			, "-0/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]",
				"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
				"Z:="			, "-0/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-1*coil_width[0]-1/2*coil_width[1]-space[0]-space[2]",
				"Y:="			, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
				"Z:="			, "-0/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-1*coil_width[0]-1/2*coil_width[1]-space[0]-space[2]",
				"Y:="			, "l1+1*coil_width[0]+1/2*coil_width[1]+space[1]+space[2]",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
				"Y:="			, "l1+1*coil_width[0]+1/2*coil_width[1]+space[1]+space[2]",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
				"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]",
				"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
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
		"Name:="		, name_temp,
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
            "Selections:="		, name_temp,
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:TranslateParameters",
            "TranslateVectorX:="	, "0mm",
            "TranslateVectorY:="	, "0mm",
            "TranslateVectorZ:="	, move_temp 
        ])


# Rx outer 1

name_temp = "Rx" + str(NX2+1)
move_temp = "-" + str(NX2) + "*(coil_width[1]+move_z[1])"

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovereZ:="	, True,
		"IsPolylineCloseZ:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[1]+space[2]",
				"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
				"Z:="			, "0/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]",
				"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
				"Z:="			, "0/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-3/2*5/2*coil_width[1]-space[0]-space[2]-space[5]",
				"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
				"Z:="			, "0/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-3/2*5/2*coil_width[1]-space[0]-space[2]-space[5]",
				"Y:="			, "l1+1*coil_width[0]+3/2*coil_width[1]+space[1]+space[2]+space[5]",
				"Z:="			, "1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+3/2*5/2*coil_width[1]+space[0]+space[2]+space[5]",
				"Y:="			, "l1+1*coil_width[0]+3/2*coil_width[1]+space[1]+space[2]+space[5]",
				"Z:="			, "1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+3/2*5/2*coil_width[1]+space[0]+space[2]+space[5]",
				"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
				"Z:="			, "2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]",
				"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
				"Z:="			, "2/2*(coil_width[1]+move_z[1])"
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
		"Name:="		, name_temp,
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
            "Selections:="		, name_temp,
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:TranslateParameters",
            "TranslateVectorX:="	, "0mm",
            "TranslateVectorY:="	, "0mm",
            "TranslateVectorZ:="	, move_temp 
        ])


# Rx outer 2

name_temp = "Rx" + str(NX2+2)
move_temp = "-" + str(NX2-1) + "*(coil_width[1]+move_z[1])"	

if NX2>2 :
	oEditor.CreatePolyline(
		[
			"NAME:PolylineParameters",
			"IsPolylineCovereZ:="	, True,
			"IsPolylineCloseZ:="	, False,
			[
				"NAME:PolylinePoints",
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+3/2*5/2*coil_width[1]+space[0]+space[2]+space[5]",
					"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
					"Z:="			, "0/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]",
					"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
					"Z:="			, "0/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-3/2*5/2*coil_width[1]-space[0]-space[2]-space[5]",
					"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
					"Z:="			, "0/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-3/2*5/2*coil_width[1]-space[0]-space[2]-space[5]",
					"Y:="			, "l1+1*coil_width[0]+3/2*coil_width[1]+space[1]+space[2]+space[5]",
					"Z:="			, "1/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+3/2*5/2*coil_width[1]+space[0]+space[2]+space[5]",
					"Y:="			, "l1+1*coil_width[0]+3/2*coil_width[1]+space[1]+space[2]+space[5]",
					"Z:="			, "1/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+3/2*5/2*coil_width[1]+space[0]+space[2]+space[5]",
					"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
					"Z:="			, "2/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]",
					"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
					"Z:="			, "2/2*(coil_width[1]+move_z[1])"
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
			"Name:="		, name_temp,
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

	
# Rx outer copy

name_temp = "Rx" + str(NX2+2)
move_temp = "-" + str(NX2-1) + "*(coil_width[1]+move_z[1])"	

for i in range(NX2-3) : 

    selection = "Rx" + str(NX2+i+3)
    z_vector = "-" + str(NX2-2-i) + "*(coil_width[1]+move_z[1])"

    oEditor.Copy(
        [
            "NAME:Selections",
            "Selections:="		, name_temp
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

oEditor.Move(
        [
            "NAME:Selections",
            "Selections:="		, name_temp,
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:TranslateParameters",
            "TranslateVectorX:="	, "0mm",
            "TranslateVectorY:="	, "0mm",
            "TranslateVectorZ:="	, move_temp
        ])


# Rx outer end

name_temp = "Rx" + str(N2)
move_temp = "-1*(coil_width[1]+move_z[1])"	

oEditor.CreatePolyline(
		[
			"NAME:PolylineParameters",
			"IsPolylineCovereZ:="	, True,
			"IsPolylineCloseZ:="	, False,
			[
				"NAME:PolylinePoints",
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+3/2*5/2*coil_width[1]+space[0]+space[2]+space[5]",
					"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
					"Z:="			, "0/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]",
					"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
					"Z:="			, "0/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-3/2*5/2*coil_width[1]-space[0]-space[2]-space[5]",
					"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
					"Z:="			, "0/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-3/2*5/2*coil_width[1]-space[0]-space[2]-space[5]",
					"Y:="			, "l1+1*coil_width[0]+3/2*coil_width[1]+space[1]+space[2]+space[5]",
					"Z:="			, "1/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+3/2*5/2*coil_width[1]+space[0]+space[2]+space[5]",
					"Y:="			, "l1+1*coil_width[0]+3/2*coil_width[1]+space[1]+space[2]+space[5]",
					"Z:="			, "1/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+3/2*5/2*coil_width[1]+space[0]+space[2]+space[5]",
					"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
					"Z:="			, "2/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
					"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
					"Z:="			, "2/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
					"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
					"Z:="			, "air[2]/2+(coil_width[1]+move_z[1])-5mm-offset_z[1]-(N2/4)*(coil_width[1]+move_z[1])"
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
			"Name:="		, name_temp,
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
            "Selections:="		, name_temp,
            "NewPartsModelFlag:="	, "Model"
        ], 
        [
            "NAME:TranslateParameters",
            "TranslateVectorX:="	, "0mm",
            "TranslateVectorY:="	, "0mm",
            "TranslateVectorZ:="	, move_temp
        ])


#Rx out

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
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
				"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
				"Z:="			, "air[2]/2-5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
				"Y:="			, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
				"Z:="			, "air[2]/2"
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


## Rx Unite

Rx_unite = "Rx1"

for i in range(N2-1) : 	
    Rx_unite = Rx_unite + ",Rx" + str(i+2)

oEditor.Unite(
[
	"NAME:Selections",
	"Selections:="		, Rx_unite
], 
[
	"NAME:UniteParameters",
	"KeepOriginals:="	, False
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
            "TranslateVectorY:="	, "0mm",
            "TranslateVectorZ:="	, "offset_z[1]+(N2/4)*coil_width[1]+(N2/4)*move_z[1]"
        ])

oEditor.Unite(
[
	"NAME:Selections",
	"Selections:="		, "Rx1,Rx_in,Rx_out"
], 
[
	"NAME:UniteParameters",
	"KeepOriginals:="	, False
])







## Make terminal

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "air[0]/2",
		"YCenter:="		, "-l1-coil_width[0]/2-space[1]",
		"ZCenter:="		, "l1+h1/2+5mm",
		"XStart:="		, "air[0]/2",
		"YStart:="		, "-l1-coil_width[0]-space[1]",
		"ZStart:="		, "l1+h1/2+5mm",
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


oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "air[0]/2",
		"YCenter:="		, "-l1-coil_width[0]/2-space[1]",
		"ZCenter:="		, "-l1-h1/2-5mm",
		"XStart:="		, "air[0]/2",
		"YStart:="		, "-l1-coil_width[0]-space[1]",
		"ZStart:="		, "-l1-h1/2-5mm",
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


oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
		"YCenter:="		, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
		"ZCenter:="		, "air[2]/2",
		"XStart:="		, "w1/2+1*coil_width[0]+2/2*coil_width[1]+space[0]+space[2]",
		"YStart:="		, "-l1-1*coil_width[0]-1/2*coil_width[1]-space[1]-space[2]",
		"ZStart:="		, "air[2]/2",
		"NumSides:="		, "Num",
		"WhichAxis:="		, "Z"
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


oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "w1/2+1*coil_width[0]+1/2*coil_width[1]+space[0]+space[2]",
		"YCenter:="		, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
		"ZCenter:="		, "air[2]/2",
		"XStart:="		, "w1/2+1*coil_width[0]+2/2*coil_width[1]+space[0]+space[2]",
		"YStart:="		, "-l1-1*coil_width[0]-3/2*coil_width[1]-space[1]-space[2]-space[5]",
		"ZStart:="		, "air[2]/2",
		"NumSides:="		, "Num",
		"WhichAxis:="		, "Z"
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



# Mesh

oModule = oDesign.GetModule("MeshSetup")
oModule.AssignSkinDepthOp(
	[
		"NAME:SkinDepth1",
		"Enabled:="		, True,
		"Objects:="		, ["Rx1","Tx1"],
		"RestrictElem:="	, False,
		"NumMaxElem:="		, "1000",
		"SkinDepth:="		, "0.330428947367505mm",
		"SurfTriMaxLength:="	, "52.9999513585811mm",
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
		"Y Component:="		, ["Matrix1.CplCoef(Tx,Rx)^2 * Matrix1.L(Tx,Tx)","Matrix1.CplCoef(Tx,Rx)^2 * Matrix1.L(Rx,Rx)"]
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
		"Y Component:="		, ["(1-Matrix1.CplCoef(Tx,Rx)^2) * Matrix1.L(Tx,Tx)", "(1-Matrix1.CplCoef(Tx,Rx)^2) * Matrix1.L(Rx,Rx)"]
	])

oModule = oDesign.GetModule("FieldsReporter")
oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Tx1")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("Tx_loss", "Fields")
oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Rx1")
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


oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("magnetizing inductance", "Y:/git/ML_MFT/FDC_2021/layer12/script30/ML_data/magnetizing_inductance$VERSION_IDX_STR.csv", False)
oModule.ExportToFile("leakage inductance", "Y:/git/ML_MFT/FDC_2021/layer12/script30/ML_data/leakage_inductance$VERSION_IDX_STR.csv", False)
oModule.ExportToFile("copper loss", "Y:/git/ML_MFT/FDC_2021/layer12/script30/ML_data/loss$VERSION_IDX_STR.csv", False)


oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.RemoveMaterial("ferrite$VERSION_IDX_STR", True, "", "Project")















