# lough model pass 3

# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2020.1.0
# 20:04:29  7 09, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

# Open aedt file
oDesktop.OpenProject("C:/script17/ML_aedt/ML17.aedt")

# Make project
oProject = oDesktop.SetActiveProject("ML17")
oProject.InsertDesign("Maxwell", "Maxwell_ML_v$VERSION_IDX_STR", "EddyCurrent", "")
oDesign = oProject.SetActiveDesign("Maxwell_ML_v$VERSION_IDX_STR")

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

# air =====================================================
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


#

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
					"Value:="		, "$NX1/2*move_tx+$offset_txmm"
					
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
					"Value:="		, "$NX2/2*move_rx+$offset_rxmm"
					
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
					"NAME:space5",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$space5mm"
					
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
					"NAME:space6",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$space6mm"
					
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
					"NAME:airy",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "2*l1+l2+30mm"
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
					"NAME:airz",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "h1/2+2*l1+30mm"
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
		"YPosition:="		, "-airy",
		"ZPosition:="		, "-airz",
		"XSize:="		, "2*airx",
		"YSize:="		, "2*airy",
		"ZSize:="		, "2*airz"
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


# Tx inner
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
					"X:="			, "w1/2+space3+0mm",
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
				"Tx$NX1:CreatePolyline:2:Segment5"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Point2",
					"X:="			, "w1/2+space3",
					"Y:="			, "-l1-space1-space5",
					"Z:="			, "-4/4*move_tx"
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
				"Tx$NX1:CreatePolyline:2:Segment6"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Point2",
					"X:="			, "w1/2+space3-10mm",
					"Y:="			, "-l1-space1-space5",
					"Z:="			, "-4/4*move_tx"
				]
			]
		]
	])

# Tx outer

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
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "-3/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "-3/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space3-space5",
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "-3/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space3-space5",
				"Y:="			, "l1+space1+space5",
				"Z:="			, "-2/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3+space5",
				"Y:="			, "l1+space1+space5",
				"Z:="			, "-1/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3+space5",
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "-0/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "-0/3*move_tx"
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
		"Name:="		, "Tx$NY1",
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
				"Tx$NY1:CreatePolyline:1"
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
		"Selections:="		, "Tx$NY1"
	])	


$Tx2_loop

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx$NY1",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0",
		"TranslateVectorY:="	, "0",
		"TranslateVectorZ:="	, "-($NX1-1)*move_tx+offset_tx"
	 ])


# Tx last loop

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
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "-3/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "-3/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space3-space5",
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "-3/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space3-space5",
				"Y:="			, "l1+space1+space5",
				"Z:="			, "-2/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3+space5",
				"Y:="			, "l1+space1+space5",
				"Z:="			, "-1/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3+space5",
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "-0/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3",
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "-0/3*move_tx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3",
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "airz-offset_tx-5mm"
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
		"Name:="		, "Tx$N1",
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
				"Tx$N1:CreatePolyline:1"
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

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Tx$N1",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:TranslateParameters",
		"TranslateVectotx:="	, "0",
		"TranslateVectorY:="	, "0",
		"TranslateVectorZ:="	, "-(0)*move_tx+offset_tx"
	 ])


# add TX terminal

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
				"Z:="			, "airz-5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3+0mm",
				"Y:="			, "-l1-space1",
				"Z:="			, "airz"
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
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "airz-5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3",
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "airz"
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

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.InsertPolylineSegment(
	[
		"NAME:Insert Polyline Segment",
		"Selections:="		, "Tx1:CreatePolyline:1",
		"Segment Indices:="	, [0],
		"At Start:="		, True,
		"SegmentType:="		, "Line",
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
					"X:="			, "w1/2+space3+0mm",
					"Y:="			, "-l1-space1",
					"Z:="			, "airz-offset_tx-5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3+0mm",
				"Y:="			, "-l1-space1",
				"Z:="			, "0mm"
			]
		]
	])

oEditor.InsertPolylineSegment(
	[
		"NAME:Insert Polyline Segment",
		"Selections:="		, "Tx$N1:CreatePolyline:1",
		"Segment Indices:="	, [5],
		"At Start:="		, False,
		"SegmentType:="		, "Line",
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3",
				"Y:="			, "-l1-space1-space5",
				"Z:="			, "-0/3*move_tx"
			],
			[
				"NAME:PLPoint",
					"X:="			, "w1/2+space3",
					"Y:="			, "-l1-space1-space5",
					"Z:="			, "airz-offset_tx-5mm"
			]
		]
	])


oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "w1/2+space3+0mm",
		"YCenter:="		, "-l1-space1",
		"ZCenter:="		, "airz",
		"Radius:="		, "d1/2",
		"WhichAxis:="		, "Z",
		"NumSegments:="		, "Num"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_in_1",
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

oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "w1/2+space3",
		"YCenter:="		, "-l1-space1-space5",
		"ZCenter:="		, "airz",
		"Radius:="		, "d1/2",
		"WhichAxis:="		, "Z",
		"NumSegments:="		, "Num"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Tx_out_1",
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


oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignWindingGroup(
	[
		"NAME:Tx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "$I1A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])
oModule.AssignCoilTerminal(
	[
		"NAME:Tx1",
		"Objects:="		, ["Tx_in_1"],
		"ParentBndID:="		, "Tx",
		"Conductor number:="	, "1",
		"Winding:="		, "Tx",
		"Point out of terminal:=", False
	])
oModule.AssignCoilTerminal(
	[
		"NAME:Tx2",
		"Objects:="		, ["Tx_out_1"],
		"ParentBndID:="		, "Tx",
		"Conductor number:="	, "1",
		"Winding:="		, "Tx",
		"Point out of terminal:=", True
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


# Rx inner
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
					"X:="			, "w1/2+space4+0mm",
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
				"Rx$NX2:CreatePolyline:2:Segment5"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Point2",
					"X:="			, "w1/2+space4",
					"Y:="			, "-l1-space2-space6",
					"Z:="			, "-4/4*move_rx"
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
				"Rx$NX2:CreatePolyline:2:Segment6"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Point2",
					"X:="			, "w1/2+space4-10mm",
					"Y:="			, "-l1-space2-space6",
					"Z:="			, "-4/4*move_rx"
				]
			]
		]
	])

# Rx outer

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
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "-3/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "-3/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space4-space6",
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "-3/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space4-space6",
				"Y:="			, "l1+space2+space6",
				"Z:="			, "-2/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4+space6",
				"Y:="			, "l1+space2+space6",
				"Z:="			, "-1/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4+space6",
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "-0/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "-0/3*move_rx"
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
		"Name:="		, "Rx$NY2",
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
				"Rx$NY2:CreatePolyline:1"
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
		"Selections:="		, "Rx$NY2"
	])	


$Rx2_loop


	
oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Rx$NY2",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0",
		"TranslateVectorY:="	, "0",
		"TranslateVectorZ:="	, "-($NX2-1)*move_rx+offset_rx"
	 ])
	 


# last Rx loop

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
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "-3/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "-3/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space4-space6",
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "-3/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space4-space6",
				"Y:="			, "l1+space2+space6",
				"Z:="			, "-2/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4+space6",
				"Y:="			, "l1+space2+space6",
				"Z:="			, "-1/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4+space6",
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "-0/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4",
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "-0/3*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4",
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "airz-offset_rx-5mm"
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
		"Name:="		, "Rx$N2",
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
				"Rx$N2:CreatePolyline:1"
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

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "Rx$N2",
		"NewPartsModelFlag:="	, "Model"
	],
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0",
		"TranslateVectorY:="	, "0",
		"TranslateVectorZ:="	, "-(0)*move_rx+offset_rx"
	 ])




# add RX terminal

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
				"Z:="			, "airz-5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4+0mm",
				"Y:="			, "-l1-space2",
				"Z:="			, "airz"
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
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "airz-5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4",
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "airz"
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

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.InsertPolylineSegment(
	[
		"NAME:Insert Polyline Segment",
		"Selections:="		, "Rx1:CreatePolyline:1",
		"Segment Indices:="	, [0],
		"At Start:="		, True,
		"SegmentType:="		, "Line",
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
					"X:="			, "w1/2+space4+0mm",
					"Y:="			, "-l1-space2",
					"Z:="			, "airz-offset_rx-5mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4+0mm",
				"Y:="			, "-l1-space2",
				"Z:="			, "0mm"
			]
		]
	])

oEditor.InsertPolylineSegment(
	[
		"NAME:Insert Polyline Segment",
		"Selections:="		, "Rx$N2:CreatePolyline:1",
		"Segment Indices:="	, [5],
		"At Start:="		, False,
		"SegmentType:="		, "Line",
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4",
				"Y:="			, "-l1-space2-space6",
				"Z:="			, "-0/3*move_rx"
			],
			[
				"NAME:PLPoint",
					"X:="			, "w1/2+space4",
					"Y:="			, "-l1-space2-space6",
					"Z:="			, "airz-offset_rx-5mm"
			]
		]
	])

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "w1/2+space4+0mm",
		"YCenter:="		, "-l1-space2",
		"ZCenter:="		, "airz",
		"Radius:="		, "d2/2",
		"WhichAxis:="		, "Z",
		"NumSegments:="		, "Num"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx_in_1",
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

oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "w1/2+space4",
		"YCenter:="		, "-l1-space2-space6",
		"ZCenter:="		, "airz",
		"Radius:="		, "d2/2",
		"WhichAxis:="		, "Z",
		"NumSegments:="		, "Num"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rx_out_1",
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


oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignWindingGroup(
	[
		"NAME:Rx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "$I2A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])
oModule.AssignCoilTerminal(
	[
		"NAME:Rx1",
		"Objects:="		, ["Rx_in_1"],
		"ParentBndID:="		, "Rx",
		"Conductor number:="	, "1",
		"Winding:="		, "Rx",
		"Point out of terminal:=", False
	])
oModule.AssignCoilTerminal(
	[
		"NAME:Rx2",
		"Objects:="		, ["Rx_out_1"],
		"ParentBndID:="		, "Rx",
		"Conductor number:="	, "1",
		"Winding:="		, "Rx",
		"Point out of terminal:=", True
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
# Make Terminal
# ===========================================================================================

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

oProject.Save()
oDesign.Analyze("Setup1")

oModule = oDesign.GetModule("FieldsReporter")
oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Tx_in")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("Tx_copperloss", "Fields")
oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Rx_in")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("Rx_copperloss", "Fields")
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("L Table 1", "EddyCurrent", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"air:="			, ["Nominal"],
		"airx:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"d2:="			, ["Nominal"],
		"move_tx:="		, ["Nominal"],
		"move_rx:="		, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"space3:="		, ["Nominal"],
		"space4:="		, ["Nominal"],
		"space5:="		, ["Nominal"],
		"space6:="		, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["(Matrix1.L(Tx,Rx) / sqrt(Matrix1.L(Tx,Tx)*Matrix1.L(Rx,Rx)))^2 * Matrix1.L(Tx,Tx) * 1e+3","(Matrix1.L(Tx,Rx) / sqrt(Matrix1.L(Tx,Tx)*Matrix1.L(Rx,Rx)))^2 * Matrix1.L(Rx,Rx) * 1e+3","(1 - (Matrix1.L(Tx,Rx) / sqrt(Matrix1.L(Tx,Tx)*Matrix1.L(Rx,Rx)))^2) * Matrix1.L(Tx,Tx) * 1e+6","(1 - (Matrix1.L(Tx,Rx) / sqrt(Matrix1.L(Tx,Tx)*Matrix1.L(Rx,Rx)))^2) * Matrix1.L(Rx,Rx) * 1e+6","(Matrix1.L(Tx,Rx) / sqrt(Matrix1.L(Tx,Tx)*Matrix1.L(Rx,Rx)))","Matrix1.L(Tx,Tx) * 1e+3","Matrix1.L(Rx,Rx) * 1e+3","Matrix1.L(Tx,Rx) * 1e+3","Matrix1.R(Tx,Tx)","Matrix1.R(Rx,Rx)","InputCurrent(Tx)","InputCurrent(Rx)","Matrix1.Z(Tx,Tx)","Matrix1.Z(Rx,Rx)","Matrix1.Z(Tx,Rx)"]
	])
oModule.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Data Filter",
			[
				"NAME:PropServers", 
				"L Table 1:InputCurrent(Tx):Curve1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Units",
					"Value:="		, "A"
				]
			]
		]
	])
oModule.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Data Filter",
			[
				"NAME:PropServers", 
				"L Table 1:InputCurrent(Rx):Curve1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Units",
					"Value:="		, "A"
				]
			]
		]
	])
oModule.CreateReport("Calculator Expressions Table 1", "Fields", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"air:="			, ["Nominal"],
		"airx:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"d2:="			, ["Nominal"],
		"move_tx:="		, ["Nominal"],
		"move_rx:="		, ["Nominal"],
		"w1:="			, ["Nominal"],
		"space1:="		, ["Nominal"],
		"space2:="		, ["Nominal"],
		"space3:="		, ["Nominal"],
		"space4:="		, ["Nominal"],
		"space5:="		, ["Nominal"],
		"space6:="		, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Tx_copperloss","Rx_copperloss"]
	])

oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("L Table 1", "C:/script17/ML_data/Data1 $VERSION_IDX_STR.csv", False)
oModule.ExportToFile("Calculator Expressions Table 1", "C:/script17/ML_data/Data2 $VERSION_IDX_STR.csv", False)


## continue 2

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
					"Value:="		, "$NX1/2*move_tx+$X2offset_txmm"
					
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
					"Value:="		, "$NX2/2*move_rx+$X2offset_rxmm"
					
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
					"NAME:space5",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2space5mm"
					
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
					"NAME:space6",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2space6mm"
					
				]
			]
		]
	])

oModule = oDesign.GetModule("BoundarySetup")
oModule.EditWindingGroup("Tx", 
	[
		"NAME:Tx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "$X2I1A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])
oModule.EditWindingGroup("Rx", 
	[
		"NAME:Rx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "$X2I2A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])

oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("Setup1", 
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
		"UseNonLinearIterNum:="	, False,
		"CacheSaveKind:="	, "Delta",
		"ConstantDelta:="	, "0s",
		"UseCacheFor:="		, ["Pass"],
		"UseIterativeSolver:="	, False,
		"RelativeResidual:="	, 1E-05,
		"NonLinearResidual:="	, 0.0001,
		"SmoothBHCurve:="	, False,
		"Frequency:="		, "$X2freqHz",
		"HasSweepSetup:="	, False,
		"UseHighOrderShapeFunc:=", False,
		"UseMuLink:="		, False
	])

oProject.Save()
oDesign.Analyze("Setup1")

oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("L Table 1", "C:/script17/ML_data/Data3 $VERSION_IDX_STR.csv", False)
oModule.ExportToFile("Calculator Expressions Table 1", "C:/script17/ML_data/Data4 $VERSION_IDX_STR.csv", False)

## continue 3

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
					"Value:="		, "$NX1/2*move_tx+$X3offset_txmm"
					
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
					"Value:="		, "$NX2/2*move_rx+$X3offset_rxmm"
					
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
					"NAME:space5",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3space5mm"
					
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
					"NAME:space6",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3space6mm"
					
				]
			]
		]
	])

oModule = oDesign.GetModule("BoundarySetup")
oModule.EditWindingGroup("Tx", 
	[
		"NAME:Tx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "$X3I1A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])
oModule.EditWindingGroup("Rx", 
	[
		"NAME:Rx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "$X3I2A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])

oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("Setup1", 
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
		"UseNonLinearIterNum:="	, False,
		"CacheSaveKind:="	, "Delta",
		"ConstantDelta:="	, "0s",
		"UseCacheFor:="		, ["Pass"],
		"UseIterativeSolver:="	, False,
		"RelativeResidual:="	, 1E-05,
		"NonLinearResidual:="	, 0.0001,
		"SmoothBHCurve:="	, False,
		"Frequency:="		, "$X3freqHz",
		"HasSweepSetup:="	, False,
		"UseHighOrderShapeFunc:=", False,
		"UseMuLink:="		, False
	])

oProject.Save()
oDesign.Analyze("Setup1")

oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("L Table 1", "C:/script17/ML_data/Data5 $VERSION_IDX_STR.csv", False)
oModule.ExportToFile("Calculator Expressions Table 1", "C:/script17/ML_data/Data6 $VERSION_IDX_STR.csv", False)

## continue 4

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
					"Value:="		, "$NX1/2*move_tx+$X4offset_txmm"
					
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
					"Value:="		, "$NX2/2*move_rx+$X4offset_rxmm"
					
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
					"NAME:space5",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4space5mm"
					
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
					"NAME:space6",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4space6mm"
					
				]
			]
		]
	])

oModule = oDesign.GetModule("BoundarySetup")
oModule.EditWindingGroup("Tx", 
	[
		"NAME:Tx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "$X4I1A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])
oModule.EditWindingGroup("Rx", 
	[
		"NAME:Rx",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "$X4I2A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])

oModule = oDesign.GetModule("AnalysisSetup")
oModule.EditSetup("Setup1", 
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
		"UseNonLinearIterNum:="	, False,
		"CacheSaveKind:="	, "Delta",
		"ConstantDelta:="	, "0s",
		"UseCacheFor:="		, ["Pass"],
		"UseIterativeSolver:="	, False,
		"RelativeResidual:="	, 1E-05,
		"NonLinearResidual:="	, 0.0001,
		"SmoothBHCurve:="	, False,
		"Frequency:="		, "$X4freqHz",
		"HasSweepSetup:="	, False,
		"UseHighOrderShapeFunc:=", False,
		"UseMuLink:="		, False
	])

oProject.Save()
oDesign.Analyze("Setup1")

oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("L Table 1", "C:/script17/ML_data/Data7 $VERSION_IDX_STR.csv", False)
oModule.ExportToFile("Calculator Expressions Table 1", "C:/script17/ML_data/Data8 $VERSION_IDX_STR.csv", False)




oProject.DeleteDesign("Maxwell_ML_v$VERSION_IDX_STR")
#time.sleep(1)
oProject.Save()
