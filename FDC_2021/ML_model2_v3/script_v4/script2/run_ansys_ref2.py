# lough model pass 3

# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2020.1.0
# 20:04:29  7 09, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

# Open aedt file
oDesktop.OpenProject("C:/script1/ML_aedt/ML1.aedt")

# Make project
oProject = oDesktop.SetActiveProject("ML1")
oProject.InsertDesign("Maxwell", "Maxwell_ML_v$VERSION_IDX_STR", "EddyCurrent", "")
oDesign = oProject.SetActiveDesign("Maxwell_ML_v$VERSION_IDX_STR")
#oDesign.RenameDesignInstance("HFSSDesign1", "HFSS_name") # project name

# Material setup
oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.EditMaterial("ferrite_LP3", 
	[
		"NAME:ferrite_LP3",
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
		[
			"NAME:ModifierData",
			[
				"NAME:ThermalModifierData",
				"modifier_data:="	, "thermal_modifier_data",
				[
					"NAME:all_thermal_modifiers"
				]
			]
		],
		"permittivity:="	, "12",
		"permeability:="	, "$per",
		"conductivity:="	, "0.2",
		"dielectric_loss_tangent:=", "0",
		"magnetic_loss_tangent:=", "0.046",
		[
			"NAME:magnetic_coercivity",
			"property_type:="	, "VectorProperty",
			"Magnitude:="		, "12A_per_meter",
			"DirComp1:="		, "1",
			"DirComp2:="		, "0",
			"DirComp3:="		, "0"
		],
		"thermal_conductivity:=", "4",
		"delta_H:="		, "0A_per_meter",
		[
			"NAME:core_loss_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Power Ferrite"
		],
		"core_loss_cm:="	, "7.36",
		"core_loss_x:="		, "1.26",
		"core_loss_y:="		, "2.07",
		"core_loss_kdc:="	, "5",
		"mass_density:="	, "4800",
		"specific_heat:="	, "750",
		"youngs_modulus:="	, "119000000000",
		"thermal_expansion_coefficient:=", "1e-05",
		[
			"NAME:magnetostriction",
			"property_type:="	, "CustomProperty",
			"PropertyModelType:="	, 0,
			"Dir1ModelType:="	, 0,
			"Dir2ModelType:="	, 0,
			"IsoCoeff:="		, "0",
			"IsoHMax:="		, "0A_per_meter",
			"IsoHMin:="		, "0A_per_meter",
			"Dir1Coeff:="		, "0",
			"Dir1HMax:="		, "0A_per_meter",
			"Dir1HMin:="		, "0A_per_meter",
			"Dir1VecX:="		, "1",
			"Dir1VecY:="		, "0",
			"Dir1VecZ:="		, "0",
			"Dir2Coeff:="		, "0",
			"Dir2HMax:="		, "0A_per_meter",
			"Dir2HMin:="		, "0A_per_meter",
			[
				"NAME:Magnetostriction",
				[
					"NAME:Isotropic",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "Lambda-H curves versus Stress"
					]
				],
				[
					"NAME:Direction1",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "Lambda-H curves versus Stress"
					]
				],
				[
					"NAME:Direction2",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "Lambda-H curves versus Stress"
					]
				],
				"SelectedDatasetMapsName:=", "Lambda-H curves versus Stress"
			]
		],
		[
			"NAME:inverse_magnetostriction",
			"property_type:="	, "CustomProperty",
			"PropertyModelType:="	, 0,
			"Dir1ModelType:="	, 0,
			"IsoCoeff:="		, "0",
			"IsoSigmaMax:="		, "0megPascal",
			"IsoSigmaMin:="		, "0megPascal",
			"Dir1Coeff:="		, "0",
			"Dir1SigmaMax:="	, "0megPascal",
			"Dir1SigmaMin:="	, "0megPascal",
			"Dir1VecX:="		, "1",
			"Dir1VecY:="		, "0",
			"Dir1VecZ:="		, "0",
			[
				"NAME:Magnetostriction",
				[
					"NAME:Isotropic",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-H curves versus Stress"
					],
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-Sigma curves versus H"
					]
				],
				[
					"NAME:Direction1",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-H curves versus Stress"
					],
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-Sigma curves versus H"
					]
				],
				[
					"NAME:Direction2"
				],
				"SelectedDatasetMapsName:=", "B-H curves versus Stress"
			]
		],
		"core_loss_equiv_cut_depth:=", "0.001meter"
	])

# Make setup
#oDesign.SetSolutionType("DrivenTerminal", False)
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("EddyCurrent", 
	[
		"NAME:Setup1",
		"Enabled:="		, True,
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
		"CacheSaveKind:="	, "Delta",
		"ConstantDelta:="	, "0s",
		"UseIterativeSolver:="	, False,
		"RelativeResidual:="	, 1E-05,
		"NonLinearResidual:="	, 0.0001,
		"SmoothBHCurve:="	, False,
		"Frequency:="		, "$freqHz",
		"HasSweepSetup:="	, False,
		"UseHighOrderShapeFunc:=", False,
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
					"NAME:air",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$airmm"
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
					"NAME:airx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$xairmm"
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
					"NAME:l3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "l1"
					
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
					"NAME:d1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$d1mm"
					
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
					"NAME:d2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$d2mm"
					
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
					"NAME:move_tx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$move_txmm"
					
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
					"NAME:move_rx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$move_rxmm"
					
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
					"NAME:offset_tx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$N1/2*move_tx+$offset_txmm"
					
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
					"NAME:offset_rx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$N2/2*move_rx+$offset_rxmm"
					
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
					"NAME:space1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$space1mm"
					
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
					"NAME:space2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$space2mm"
					
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
					"NAME:space3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$space3mm"
					
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
					"NAME:space4",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$space4mm"
					
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

# Make boundary
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-airx",
		"YPosition:="		, "-air",
		"ZPosition:="		, "-air",
		"XSize:="		, "2*airx",
		"YSize:="		, "2*air",
		"ZSize:="		, "2*air"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Air",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 1,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["Air"],
		"IsFssReference:="	, False,
		"IsForPML:="		, False
	])

# Make core
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-w1/2",
		"YPosition:="		, "-2*l1-l2",
		"ZPosition:="		, "-l3-h1/2",
		"XSize:="		, "w1",
		"YSize:="		, "4*l1+2*l2",
		"ZSize:="		, "2*l3+h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Core",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"ferrite_LP3\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-w1/2",
		"YPosition:="		, "-l1",
		"ZPosition:="		, "-h1/2",
		"XSize:="		, "w1",
		"YSize:="		, "-l2",
		"ZSize:="		, "h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Core_sub1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"ferrite_LP3\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-w1/2",
		"YPosition:="		, "l1",
		"ZPosition:="		, "-h1/2",
		"XSize:="		, "w1",
		"YSize:="		, "l2",
		"ZSize:="		, "h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Core_sub2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"ferrite_LP3\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Core",
		"Tool Parts:="		, "Core_sub1,Core_sub2"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])


# Tx
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3",
				"Y:="			, "-l1-space1",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space1",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space3",
				"Y:="			, "-l1-space1",
				"Z:="			, "-0*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space3",
				"Y:="			, "l1+space1",
				"Z:="			, "-1/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3",
				"Y:="			, "l1+space1",
				"Z:="			, "-2/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3",
				"Y:="			, "-l1",
				"Z:="			, "-3/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3",
				"Y:="			, "-l1-space1",
				"Z:="			, "-3/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space1",
				"Z:="			, "-3/3*move_tx"
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
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
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
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Tx1:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Circle"
				],
				[
					"NAME:Number of Segments",
					"Value:="		, "Num"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "d1"
				]
			]
		]
	])

oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "Tx1"
	])	

$Tx_loop

	
oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0",
		"TranslateVectorY:="	, "0",
		"TranslateVectorZ:="	, "offset_tx"
	])


oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DPolylineTab",
			[
				"NAME:PropServers", 
				"Tx1:CreatePolyline:2:Segment0"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Point1",
					"X:="			, "w1/2+space3+1mm",
					"Y:="			, "-l1-space1",
					"Z:="			, "0mm"
				]
			]
		]
	])


oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DPolylineTab",
			[
				"NAME:PropServers", 
				"Tx$N1:CreatePolyline:2:Segment6"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Point2",
					"X:="			, "w1/2+space3+1mm",
					"Y:="			, "-l1-space1",
					"Z:="			, "-4/4*move_tx"
				]
			]
		]
	])

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3+0mm",
				"Y:="			, "-l1-space1",
				"Z:="			, "offset_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3+d1/2+1mm",
				"Y:="			, "-l1-space1",
				"Z:="			, "offset_tx"
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
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
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
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Tx_in:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "d1"
				],
				[
					"NAME:Height",
					"Value:="		, "d1"
				]
			]
		]
	])

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3+0mm",
				"Y:="			, "-l1-space1",
				"Z:="			, "offset_tx-$N1*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3+d1/2+1mm",
				"Y:="			, "-l1-space1",
				"Z:="			, "offset_tx-$N1*move_tx"
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
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
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
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Tx_out:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "d1"
				],
				[
					"NAME:Height",
					"Value:="		, "d1"
				]
			]
		]
	])

oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "$str_tx"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])


# Rx
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4",
				"Y:="			, "-l1-space2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space4",
				"Y:="			, "-l1-space2",
				"Z:="			, "-0*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space4",
				"Y:="			, "l1+space2",
				"Z:="			, "-1/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4",
				"Y:="			, "l1+space2",
				"Z:="			, "-2/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4",
				"Y:="			, "-l1",
				"Z:="			, "-3/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4",
				"Y:="			, "-l1-space2",
				"Z:="			, "-3/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space2",
				"Z:="			, "-3/3*move_rx"
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
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
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
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rx1:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Circle"
				],
				[
					"NAME:Number of Segments",
					"Value:="		, "Num"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "d2"
				]
			]
		]
	])

oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1"
	])
	

$Rx_loop

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Rx1",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0",
		"TranslateVectorY:="	, "0",
		"TranslateVectorZ:="	, "offset_rx"
	])


oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DPolylineTab",
			[
				"NAME:PropServers", 
				"Rx1:CreatePolyline:2:Segment0"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Point1",
					"X:="			, "w1/2+space4+5mm",
					"Y:="			, "-l1-space2",
					"Z:="			, "0mm"
				]
			]
		]
	])


oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DPolylineTab",
			[
				"NAME:PropServers", 
				"Rx$N2:CreatePolyline:2:Segment6"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Point2",
					"X:="			, "w1/2+space4+3mm",
					"Y:="			, "-l1-space2",
					"Z:="			, "-4/4*move_rx"
				]
			]
		]
	])

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4+0mm",
				"Y:="			, "-l1-space2",
				"Z:="			, "offset_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4+5mm",
				"Y:="			, "-l1-space2",
				"Z:="			, "offset_rx"
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
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx_in",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rx_in:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "d2"
				],
				[
					"NAME:Height",
					"Value:="		, "d2"
				]
			]
		]
	])

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4+0mm",
				"Y:="			, "-l1-space2",
				"Z:="			, "offset_rx-$N2*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4+5mm",
				"Y:="			, "-l1-space2",
				"Z:="			, "offset_rx-$N2*move_rx"
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
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx_out",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rx_out:CreatePolyline:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Type",
					"Value:="		, "Rectangle"
				],
				[
					"NAME:Width/Diameter",
					"Value:="		, "d2"
				],
				[
					"NAME:Height",
					"Value:="		, "d2"
				]
			]
		]
	])

oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "$str_rx"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])



# ===========================================================================================
# Make Sheet
# ===========================================================================================

# 
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "w1/2+space3+d1/2+1mm",
		"YStart:="		, "-l1-space1-d1/2",
		"ZStart:="		, "offset_tx-d1/2",
		"Width:="		, "d1",
		"Height:="		, "-$N1*move_tx+d1",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Ter1_Rec1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "w1/2+space4+5mm",
		"YStart:="		, "-l1-space2-d2/2",
		"ZStart:="		, "offset_rx-d2/2",
		"Width:="		, "d2",
		"Height:="		, "-$N2*move_rx+d2",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Ter2_Rec1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "w1/2+space3+d1/2+1mm",
		"YStart:="		, "-l1-space1-d1/2",
		"ZStart:="		, "offset_tx-d1/2",
		"Width:="		, "d1",
		"Height:="		, "-1mm",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Ter1_Rec2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "w1/2+space4+5mm",
		"YStart:="		, "-l1-space2-d2/2",
		"ZStart:="		, "offset_rx-d2/2",
		"Width:="		, "d2",
		"Height:="		, "-1mm",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Ter2_Rec2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"copper\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

# ===========================================================================================
# Make Circle
# ===========================================================================================
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space1",
				"Z:="			, "offset_tx+d1/2+0.5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space1+d1/2+0.5mm",
				"Z:="			, "offset_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space1",
				"Z:="			, "offset_tx-d1/2-0.5mm"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "AngularArc",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 3,
				"NoOfSegments:="	, "0",
				"ArcAngle:="		, "-180deg",
				"ArcCenterX:="		, "w1/2",
				"ArcCenterY:="		, "-l1-space1",
				"ArcCenterZ:="		, "offset_tx",
				"ArcPlane:="		, "YZ"
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Polyline1",
		"Flags:="		, "NonModel#",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline1"
	])
oEditor.Paste()
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DPolylineTab",
			[
				"NAME:PropServers", 
				"Polyline2:CreatePolyline:2:Segment0"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Angle",
					"Value:="		, "180deg"
				]
			]
		]
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline1,Polyline2"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])

# ======== Rx ========

oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, False,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space2",
				"Z:="			, "offset_rx+d2/2+0.5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space2+d2/2+0.5mm",
				"Z:="			, "offset_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space2",
				"Z:="			, "offset_rx-d2/2-0.5mm"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "AngularArc",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 3,
				"NoOfSegments:="	, "0",
				"ArcAngle:="		, "-180deg",
				"ArcCenterX:="		, "w1/2",
				"ArcCenterY:="		, "-l1-space2",
				"ArcCenterZ:="		, "offset_rx",
				"ArcPlane:="		, "YZ"
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Polyline3",
		"Flags:="		, "NonModel#",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])


oEditor.Copy(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline3"
	])
oEditor.Paste()
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DPolylineTab",
			[
				"NAME:PropServers", 
				"Polyline4:CreatePolyline:2:Segment0"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Angle",
					"Value:="		, "180deg"
				]
			]
		]
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Polyline3,Polyline4"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])

# ===========================================================================================
# Make Terminal
# ===========================================================================================


oModule = oDesign.GetModule("BoundarySetup")

oEditor = oDesign.SetActiveEditor("3D Modeler")
oFaceIDs1 = oEditor.GetFaceIDs("Ter1_Rec1")
oFaceIDs2 = oEditor.GetFaceIDs("Ter1_Rec2")
oFaceIDs3 = oEditor.GetFaceIDs("Ter2_Rec1")
oFaceIDs4 = oEditor.GetFaceIDs("Ter2_Rec2")

oModule.AutoIdentifyPorts(
	[
		"NAME:Faces", 
		oFaceIDs1[0]
	], False, 
	[
		"NAME:ReferenceConductors", 
		"Tx_in"
	], "1", True)
oModule.AssignTerminal(
	[
		"NAME:Ter1",
		"Objects:="		, ["Ter1_Rec2"],
		"ParentBndID:="		, "1",
		"TerminalResistance:="	, "50ohm"
	])
oModule.AutoIdentifyPorts(
	[
		"NAME:Faces", 
		oFaceIDs3[0]
	], False, 
	[
		"NAME:ReferenceConductors", 
		"Rx_in"
	], "2", True)
oModule.AssignTerminal(
	[
		"NAME:Ter2",
		"Objects:="		, ["Ter2_Rec2"],
		"ParentBndID:="		, "2",
		"TerminalResistance:="	, "50ohm"
	])

oModule = oDesign.GetModule("Solutions")
oModule.EditSources(
	[
		[
			"UseIncidentVoltage:="	, False,
			"IncludePortPostProcessing:=", False,
			"SpecifySystemPower:="	, False
		],
		[
			"Name:="		, "Ter1",
			"Terminated:="		, False,
			"Magnitude:="		, "$V1V",
			"Phase:="		, "0deg"
		],
		[
			"Name:="		, "Ter2",
			"Terminated:="		, True,
			"Magnitude:="		, "$R2ohm",
			"Phase:="		, "0deg"
		]
	])

oModule = oDesign.GetModule("Solutions")
oModule.EditSources(
	[
		[
			"UseIncidentVoltage:="	, False,
			"IncludePortPostProcessing:=", False,
			"SpecifySystemPower:="	, False
		],
		[
			"Name:="		, "Ter1",
			"Terminated:="		, False,
			"Magnitude:="		, "$V1V",
			"Phase:="		, "0deg"
		],
		[
			"Name:="		, "Ter2",
			"Terminated:="		, True,
			"Resistance:="		, "$R2ohm",
			"Reactance:="		, "0ohm"
		]
	])

oModule = oDesign.GetModule("ReportSetup")

oProject.Save()
oDesign.Analyze("Setup1")

oModule.CreateReport(" Table 1", "Terminal Solution Data", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"air:="			, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"l3:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["(im(Zt(Ter1,Ter2))/2/pi/freq / sqrt(im(Zt(Ter1,Ter1))/2/pi/freq*im(Zt(Ter2,Ter2))/2/pi/freq))^2 * im(Zt(Ter1,Ter1))/2/pi/freq * 1e+3"]
	])
oModule.AddTraces(" Table 1", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"air:="			, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"l3:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["(im(Zt(Ter1,Ter2))/2/pi/freq / sqrt(im(Zt(Ter1,Ter1))/2/pi/freq*im(Zt(Ter2,Ter2))/2/pi/freq))^2 * im(Zt(Ter2,Ter2))/2/pi/freq * 1e+3"]
	])
oModule.AddTraces(" Table 1", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"air:="			, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"l3:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["(1 - (im(Zt(Ter1,Ter2))/2/pi/freq / sqrt(im(Zt(Ter1,Ter1))/2/pi/freq*im(Zt(Ter2,Ter2))/2/pi/freq))^2) * im(Zt(Ter1,Ter1))/2/pi/freq * 1e+6"]
	])
oModule.AddTraces(" Table 1", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"air:="			, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"l3:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["re(Zt(Ter1,Ter1))"]
	])
oModule.AddTraces(" Table 1", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"air:="			, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"l3:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["re(Zt(Ter2,Ter2))"]
	])


oModule = oDesign.GetModule("FieldsReporter")
oModule.EnterQty("H")
oModule.CalcOp("Real")
oModule.EnterLine("Polyline1")
oModule.CalcOp("TangentComponent")
oModule.CalcOp("Integrate")

oModule.AddNamedExpression("I1r", "Fields")
oModule.CalcStack("clear")

oModule.EnterQty("H")
oModule.CalcOp("Imag")
oModule.EnterLine("Polyline1")
oModule.CalcOp("TangentComponent")
oModule.CalcOp("Integrate")

oModule.AddNamedExpression("I1i", "Fields")
oModule.CalcStack("clear")

oModule.EnterQty("H")
oModule.CalcOp("Real")
oModule.EnterLine("Polyline3")
oModule.CalcOp("TangentComponent")
oModule.CalcOp("Integrate")

oModule.AddNamedExpression("I2r", "Fields")
oModule.CalcStack("clear")

oModule.EnterQty("H")
oModule.CalcOp("Imag")
oModule.EnterLine("Polyline3")
oModule.CalcOp("TangentComponent")
oModule.CalcOp("Integrate")

oModule.AddNamedExpression("I2i", "Fields")

oModule = oDesign.GetModule("FieldsReporter")
oModule.EnterQty("VolumeLossDensity")
oModule.EnterVol("Tx_in")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("copperloss_Tx", "Fields")
oModule.EnterQty("VolumeLossDensity")
oModule.EnterVol("Rx_in")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("copperloss_Rx", "Fields")
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport(" Table 2", "Fields", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"air:="			, ["Nominal"],
		"airx:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["sqrt(I1r^2+I1i^2)"]
	])
oModule.AddTraces(" Table 2", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"air:="			, ["Nominal"],
		"airx:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["sqrt(I2r^2+I2i^2)"]
	])
oModule.AddTraces(" Table 2", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"air:="			, ["Nominal"],
		"airx:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["copperloss_Tx"]
	])
oModule.AddTraces(" Table 2", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"air:="			, ["Nominal"],
		"airx:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["copperloss_Rx"]
	])
oModule.AddTraces(" Table 2", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"air:="			, ["Nominal"],
		"airx:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["copperloss_Tx+copperloss_Rx"]
	])
oModule.AddTraces(" Table 2", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"air:="			, ["Nominal"],
		"airx:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["I1r"]
	])
oModule.AddTraces(" Table 2", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"air:="			, ["Nominal"],
		"airx:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["I1i"]
	])
oModule.AddTraces(" Table 2", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"air:="			, ["Nominal"],
		"airx:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["I2r"]
	])
oModule.AddTraces(" Table 2", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"air:="			, ["Nominal"],
		"airx:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["I2i"]
	])



oModule = oDesign.GetModule("ReportSetup")
oProject.Save()
oDesign.Analyze("Setup1")
oModule.ExportToFile(" Table 1", "D:/script2/ML_v4_data/Data $VERSION_IDX_STR.csv", False)
oModule.ExportToFile(" Table 2", "D:/script2/ML_v4_data/Data2 $VERSION_IDX_STR.csv", False)
#time.sleep(1)

# Material setup
oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.EditMaterial("ferrite_LP3", 
	[
		"NAME:ferrite_LP3",
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
		[
			"NAME:ModifierData",
			[
				"NAME:ThermalModifierData",
				"modifier_data:="	, "thermal_modifier_data",
				[
					"NAME:all_thermal_modifiers"
				]
			]
		],
		"permittivity:="	, "12",
		"permeability:="	, "$X2per",
		"conductivity:="	, "0.2",
		"dielectric_loss_tangent:=", "0",
		"magnetic_loss_tangent:=", "0.046",
		[
			"NAME:magnetic_coercivity",
			"property_type:="	, "VectorProperty",
			"Magnitude:="		, "12A_per_meter",
			"DirComp1:="		, "1",
			"DirComp2:="		, "0",
			"DirComp3:="		, "0"
		],
		"thermal_conductivity:=", "4",
		"delta_H:="		, "0A_per_meter",
		[
			"NAME:core_loss_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Power Ferrite"
		],
		"core_loss_cm:="	, "7.36",
		"core_loss_x:="		, "1.26",
		"core_loss_y:="		, "2.07",
		"core_loss_kdc:="	, "5",
		"mass_density:="	, "4800",
		"specific_heat:="	, "750",
		"youngs_modulus:="	, "119000000000",
		"thermal_expansion_coefficient:=", "1e-05",
		[
			"NAME:magnetostriction",
			"property_type:="	, "CustomProperty",
			"PropertyModelType:="	, 0,
			"Dir1ModelType:="	, 0,
			"Dir2ModelType:="	, 0,
			"IsoCoeff:="		, "0",
			"IsoHMax:="		, "0A_per_meter",
			"IsoHMin:="		, "0A_per_meter",
			"Dir1Coeff:="		, "0",
			"Dir1HMax:="		, "0A_per_meter",
			"Dir1HMin:="		, "0A_per_meter",
			"Dir1VecX:="		, "1",
			"Dir1VecY:="		, "0",
			"Dir1VecZ:="		, "0",
			"Dir2Coeff:="		, "0",
			"Dir2HMax:="		, "0A_per_meter",
			"Dir2HMin:="		, "0A_per_meter",
			[
				"NAME:Magnetostriction",
				[
					"NAME:Isotropic",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "Lambda-H curves versus Stress"
					]
				],
				[
					"NAME:Direction1",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "Lambda-H curves versus Stress"
					]
				],
				[
					"NAME:Direction2",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "Lambda-H curves versus Stress"
					]
				],
				"SelectedDatasetMapsName:=", "Lambda-H curves versus Stress"
			]
		],
		[
			"NAME:inverse_magnetostriction",
			"property_type:="	, "CustomProperty",
			"PropertyModelType:="	, 0,
			"Dir1ModelType:="	, 0,
			"IsoCoeff:="		, "0",
			"IsoSigmaMax:="		, "0megPascal",
			"IsoSigmaMin:="		, "0megPascal",
			"Dir1Coeff:="		, "0",
			"Dir1SigmaMax:="	, "0megPascal",
			"Dir1SigmaMin:="	, "0megPascal",
			"Dir1VecX:="		, "1",
			"Dir1VecY:="		, "0",
			"Dir1VecZ:="		, "0",
			[
				"NAME:Magnetostriction",
				[
					"NAME:Isotropic",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-H curves versus Stress"
					],
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-Sigma curves versus H"
					]
				],
				[
					"NAME:Direction1",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-H curves versus Stress"
					],
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-Sigma curves versus H"
					]
				],
				[
					"NAME:Direction2"
				],
				"SelectedDatasetMapsName:=", "B-H curves versus Stress"
			]
		],
		"core_loss_equiv_cut_depth:=", "0.001meter"
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
				"NAME:ChangedProps",
				[
					"NAME:air",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2airmm"
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
				"NAME:ChangedProps",
				[
					"NAME:airx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2xairmm"
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
				"NAME:ChangedProps",
				[
					"NAME:l1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2l1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:l2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2l2mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:l3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "l1"
					
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
				"NAME:ChangedProps",
				[
					"NAME:h1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2h1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:d1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2d1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:d2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2d2mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:move_tx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2move_txmm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:move_rx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2move_rxmm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:offset_tx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$N1/2*move_tx+$X2offset_txmm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:offset_rx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$N2/2*move_rx+$X2offset_rxmm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:w1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2w1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:space1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2space1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:space2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2space2mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:space3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2space3mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:space4",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2space4mm"
					
				]
			]
		]
	])

oModule = oDesign.GetModule("Solutions")
oModule.EditSources(
	[
		[
			"UseIncidentVoltage:="	, False,
			"IncludePortPostProcessing:=", False,
			"SpecifySystemPower:="	, False
		],
		[
			"Name:="		, "Ter1",
			"Terminated:="		, False,
			"Magnitude:="		, "$X2V1V",
			"Phase:="		, "0deg"
		],
		[
			"Name:="		, "Ter2",
			"Terminated:="		, True,
			"Resistance:="		, "$X2R2ohm",
			"Reactance:="		, "0ohm"
		]
	])

# Make setup
#oDesign.SetSolutionType("DrivenTerminal", False)
oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("Setup1", 
	[
		"NAME:Setup1",
		"AdaptMultipleFreqs:="	, False,
		"Frequency:="		, "$X2freqHz",
		"MaxDeltaE:="		, 0.1,
		"MaximumPasses:="	, 5,
		"MinimumPasses:="	, 5,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 0,
		"DoLambdaRefine:="	, False,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced"
	])

oProject.Save()
oDesign.Analyze("Setup1")

oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile(" Table 1", "D:/script2/ML_v4_data/Data3 $VERSION_IDX_STR.csv", False)
oModule.ExportToFile(" Table 2", "D:/script2/ML_v4_data/Data4 $VERSION_IDX_STR.csv", False)

# Material setup
oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.EditMaterial("ferrite_LP3", 
	[
		"NAME:ferrite_LP3",
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
		[
			"NAME:ModifierData",
			[
				"NAME:ThermalModifierData",
				"modifier_data:="	, "thermal_modifier_data",
				[
					"NAME:all_thermal_modifiers"
				]
			]
		],
		"permittivity:="	, "12",
		"permeability:="	, "$X3per",
		"conductivity:="	, "0.2",
		"dielectric_loss_tangent:=", "0",
		"magnetic_loss_tangent:=", "0.046",
		[
			"NAME:magnetic_coercivity",
			"property_type:="	, "VectorProperty",
			"Magnitude:="		, "12A_per_meter",
			"DirComp1:="		, "1",
			"DirComp2:="		, "0",
			"DirComp3:="		, "0"
		],
		"thermal_conductivity:=", "4",
		"delta_H:="		, "0A_per_meter",
		[
			"NAME:core_loss_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Power Ferrite"
		],
		"core_loss_cm:="	, "7.36",
		"core_loss_x:="		, "1.26",
		"core_loss_y:="		, "2.07",
		"core_loss_kdc:="	, "5",
		"mass_density:="	, "4800",
		"specific_heat:="	, "750",
		"youngs_modulus:="	, "119000000000",
		"thermal_expansion_coefficient:=", "1e-05",
		[
			"NAME:magnetostriction",
			"property_type:="	, "CustomProperty",
			"PropertyModelType:="	, 0,
			"Dir1ModelType:="	, 0,
			"Dir2ModelType:="	, 0,
			"IsoCoeff:="		, "0",
			"IsoHMax:="		, "0A_per_meter",
			"IsoHMin:="		, "0A_per_meter",
			"Dir1Coeff:="		, "0",
			"Dir1HMax:="		, "0A_per_meter",
			"Dir1HMin:="		, "0A_per_meter",
			"Dir1VecX:="		, "1",
			"Dir1VecY:="		, "0",
			"Dir1VecZ:="		, "0",
			"Dir2Coeff:="		, "0",
			"Dir2HMax:="		, "0A_per_meter",
			"Dir2HMin:="		, "0A_per_meter",
			[
				"NAME:Magnetostriction",
				[
					"NAME:Isotropic",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "Lambda-H curves versus Stress"
					]
				],
				[
					"NAME:Direction1",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "Lambda-H curves versus Stress"
					]
				],
				[
					"NAME:Direction2",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "Lambda-H curves versus Stress"
					]
				],
				"SelectedDatasetMapsName:=", "Lambda-H curves versus Stress"
			]
		],
		[
			"NAME:inverse_magnetostriction",
			"property_type:="	, "CustomProperty",
			"PropertyModelType:="	, 0,
			"Dir1ModelType:="	, 0,
			"IsoCoeff:="		, "0",
			"IsoSigmaMax:="		, "0megPascal",
			"IsoSigmaMin:="		, "0megPascal",
			"Dir1Coeff:="		, "0",
			"Dir1SigmaMax:="	, "0megPascal",
			"Dir1SigmaMin:="	, "0megPascal",
			"Dir1VecX:="		, "1",
			"Dir1VecY:="		, "0",
			"Dir1VecZ:="		, "0",
			[
				"NAME:Magnetostriction",
				[
					"NAME:Isotropic",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-H curves versus Stress"
					],
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-Sigma curves versus H"
					]
				],
				[
					"NAME:Direction1",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-H curves versus Stress"
					],
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-Sigma curves versus H"
					]
				],
				[
					"NAME:Direction2"
				],
				"SelectedDatasetMapsName:=", "B-H curves versus Stress"
			]
		],
		"core_loss_equiv_cut_depth:=", "0.001meter"
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
				"NAME:ChangedProps",
				[
					"NAME:air",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3airmm"
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
				"NAME:ChangedProps",
				[
					"NAME:airx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3xairmm"
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
				"NAME:ChangedProps",
				[
					"NAME:l1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3l1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:l2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3l2mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:l3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "l1"
					
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
				"NAME:ChangedProps",
				[
					"NAME:h1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3h1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:d1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3d1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:d2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3d2mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:move_tx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3move_txmm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:move_rx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3move_rxmm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:offset_tx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$N1/2*move_tx+$X3offset_txmm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:offset_rx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$N2/2*move_rx+$X3offset_rxmm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:w1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3w1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:space1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3space1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:space2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3space2mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:space3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3space3mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:space4",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3space4mm"
					
				]
			]
		]
	])

oModule = oDesign.GetModule("Solutions")
oModule.EditSources(
	[
		[
			"UseIncidentVoltage:="	, False,
			"IncludePortPostProcessing:=", False,
			"SpecifySystemPower:="	, False
		],
		[
			"Name:="		, "Ter1",
			"Terminated:="		, False,
			"Magnitude:="		, "$X3V1V",
			"Phase:="		, "0deg"
		],
		[
			"Name:="		, "Ter2",
			"Terminated:="		, True,
			"Resistance:="		, "$X3R2ohm",
			"Reactance:="		, "0ohm"
		]
	])

# Make setup
#oDesign.SetSolutionType("DrivenTerminal", False)
oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("Setup1", 
	[
		"NAME:Setup1",
		"AdaptMultipleFreqs:="	, False,
		"Frequency:="		, "$X3freqHz",
		"MaxDeltaE:="		, 0.1,
		"MaximumPasses:="	, 5,
		"MinimumPasses:="	, 5,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 0,
		"DoLambdaRefine:="	, False,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced"
	])

oProject.Save()
oDesign.Analyze("Setup1")

oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile(" Table 1", "D:/script2/ML_v4_data/Data5 $VERSION_IDX_STR.csv", False)
oModule.ExportToFile(" Table 2", "D:/script2/ML_v4_data/Data6 $VERSION_IDX_STR.csv", False)

# Material setup
oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.EditMaterial("ferrite_LP3", 
	[
		"NAME:ferrite_LP3",
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
		[
			"NAME:ModifierData",
			[
				"NAME:ThermalModifierData",
				"modifier_data:="	, "thermal_modifier_data",
				[
					"NAME:all_thermal_modifiers"
				]
			]
		],
		"permittivity:="	, "12",
		"permeability:="	, "$X4per",
		"conductivity:="	, "0.2",
		"dielectric_loss_tangent:=", "0",
		"magnetic_loss_tangent:=", "0.046",
		[
			"NAME:magnetic_coercivity",
			"property_type:="	, "VectorProperty",
			"Magnitude:="		, "12A_per_meter",
			"DirComp1:="		, "1",
			"DirComp2:="		, "0",
			"DirComp3:="		, "0"
		],
		"thermal_conductivity:=", "4",
		"delta_H:="		, "0A_per_meter",
		[
			"NAME:core_loss_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Power Ferrite"
		],
		"core_loss_cm:="	, "7.36",
		"core_loss_x:="		, "1.26",
		"core_loss_y:="		, "2.07",
		"core_loss_kdc:="	, "5",
		"mass_density:="	, "4800",
		"specific_heat:="	, "750",
		"youngs_modulus:="	, "119000000000",
		"thermal_expansion_coefficient:=", "1e-05",
		[
			"NAME:magnetostriction",
			"property_type:="	, "CustomProperty",
			"PropertyModelType:="	, 0,
			"Dir1ModelType:="	, 0,
			"Dir2ModelType:="	, 0,
			"IsoCoeff:="		, "0",
			"IsoHMax:="		, "0A_per_meter",
			"IsoHMin:="		, "0A_per_meter",
			"Dir1Coeff:="		, "0",
			"Dir1HMax:="		, "0A_per_meter",
			"Dir1HMin:="		, "0A_per_meter",
			"Dir1VecX:="		, "1",
			"Dir1VecY:="		, "0",
			"Dir1VecZ:="		, "0",
			"Dir2Coeff:="		, "0",
			"Dir2HMax:="		, "0A_per_meter",
			"Dir2HMin:="		, "0A_per_meter",
			[
				"NAME:Magnetostriction",
				[
					"NAME:Isotropic",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "Lambda-H curves versus Stress"
					]
				],
				[
					"NAME:Direction1",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "Lambda-H curves versus Stress"
					]
				],
				[
					"NAME:Direction2",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "Lambda-H curves versus Stress"
					]
				],
				"SelectedDatasetMapsName:=", "Lambda-H curves versus Stress"
			]
		],
		[
			"NAME:inverse_magnetostriction",
			"property_type:="	, "CustomProperty",
			"PropertyModelType:="	, 0,
			"Dir1ModelType:="	, 0,
			"IsoCoeff:="		, "0",
			"IsoSigmaMax:="		, "0megPascal",
			"IsoSigmaMin:="		, "0megPascal",
			"Dir1Coeff:="		, "0",
			"Dir1SigmaMax:="	, "0megPascal",
			"Dir1SigmaMin:="	, "0megPascal",
			"Dir1VecX:="		, "1",
			"Dir1VecY:="		, "0",
			"Dir1VecZ:="		, "0",
			[
				"NAME:Magnetostriction",
				[
					"NAME:Isotropic",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-H curves versus Stress"
					],
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-Sigma curves versus H"
					]
				],
				[
					"NAME:Direction1",
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-H curves versus Stress"
					],
					[
						"NAME:OneVariation",
						"DatasetMapsName:="	, "B-Sigma curves versus H"
					]
				],
				[
					"NAME:Direction2"
				],
				"SelectedDatasetMapsName:=", "B-H curves versus Stress"
			]
		],
		"core_loss_equiv_cut_depth:=", "0.001meter"
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
				"NAME:ChangedProps",
				[
					"NAME:air",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4airmm"
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
				"NAME:ChangedProps",
				[
					"NAME:airx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4xairmm"
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
				"NAME:ChangedProps",
				[
					"NAME:l1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4l1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:l2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4l2mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:l3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "l1"
					
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
				"NAME:ChangedProps",
				[
					"NAME:h1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4h1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:d1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4d1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:d2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4d2mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:move_tx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4move_txmm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:move_rx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4move_rxmm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:offset_tx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$N1/2*move_tx+$X4offset_txmm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:offset_rx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$N2/2*move_rx+$X4offset_rxmm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:w1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4w1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:space1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4space1mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:space2",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4space2mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:space3",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4space3mm"
					
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
				"NAME:ChangedProps",
				[
					"NAME:space4",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4space4mm"
					
				]
			]
		]
	])

oModule = oDesign.GetModule("Solutions")
oModule.EditSources(
	[
		[
			"UseIncidentVoltage:="	, False,
			"IncludePortPostProcessing:=", False,
			"SpecifySystemPower:="	, False
		],
		[
			"Name:="		, "Ter1",
			"Terminated:="		, False,
			"Magnitude:="		, "$X4V1V",
			"Phase:="		, "0deg"
		],
		[
			"Name:="		, "Ter2",
			"Terminated:="		, True,
			"Resistance:="		, "$X4R2ohm",
			"Reactance:="		, "0ohm"
		]
	])

# Make setup
#oDesign.SetSolutionType("DrivenTerminal", False)
oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("Setup1", 
	[
		"NAME:Setup1",
		"AdaptMultipleFreqs:="	, False,
		"Frequency:="		, "$X4freqHz",
		"MaxDeltaE:="		, 0.1,
		"MaximumPasses:="	, 5,
		"MinimumPasses:="	, 5,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		[
			"NAME:MeshLink",
			"ImportMesh:="		, False
		],
		"BasisOrder:="		, 0,
		"DoLambdaRefine:="	, False,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"IE Solver Accuracy:="	, "Balanced"
	])

oProject.Save()
oDesign.Analyze("Setup1")

oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile(" Table 1", "D:/script2/ML_v4_data/Data7 $VERSION_IDX_STR.csv", False)
oModule.ExportToFile(" Table 2", "D:/script2/ML_v4_data/Data8 $VERSION_IDX_STR.csv", False)


#oEditor.Delete(
#	[
#		"NAME:Selections",
#		"Selections:="		, "Core,Tx_in,Rx_in,Tx_in_ObjectFromEdge1,Rx_in_ObjectFromEdge1"
#	])
#oModule = oDesign.GetModule("BoundarySetup")
#oModule.DeleteBoundaries(["Rad1"])
#oModule = oDesign.GetModule("AnalysisSetup")
#oModule.DeleteSetups(["Setup1"])

#oProject.Save()


#oProject.DeleteDesign("Maxwell_ML_v$VERSION_IDX_STR")
#time.sleep(1)
oProject.Save()
