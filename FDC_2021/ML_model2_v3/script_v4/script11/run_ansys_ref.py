import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

# Open aedt file
oDesktop.OpenProject("C:/script11/ML_aedt/ML11.aedt")

# Make project
oProject = oDesktop.SetActiveProject("ML11")
oProject.InsertDesign("Maxwell", "Maxwell_ML_v$VERSION_IDX_STR", "EddyCurrent", "")
oDesign = oProject.SetActiveDesign("Maxwell_ML_v$VERSION_IDX_STR")

# core Material setup
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

# litz_tx material setup

oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.AddMaterial(
	[
		"NAME:litz_tx",
		"CoordinateSystemType:=", "Cartesian",
		"BulkOrSurfaceType:="	, 1,
		[
			"NAME:PhysicsTypes",
			"set:="			, ["Electromagnetic"]
		],
		"permeability:="	, "0.999991",
		"conductivity:="	, "58000000",
		"mass_density:="	, "8933",
		[
			"NAME:stacking_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Litz Wire"
		],
		[
			"NAME:wire_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Round"
		],
		"strand_number:="	, "$litz_num_d1",
		"wire_diameter:="	, "$litz_dia_d1mm"
	])

oDefinitionManager = oProject.GetDefinitionManager()
oDefinitionManager.AddMaterial(
	[
		"NAME:litz_rx",
		"CoordinateSystemType:=", "Cartesian",
		"BulkOrSurfaceType:="	, 1,
		[
			"NAME:PhysicsTypes",
			"set:="			, ["Electromagnetic"]
		],
		"permeability:="	, "0.999991",
		"conductivity:="	, "58000000",
		"mass_density:="	, "8933",
		[
			"NAME:stacking_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Litz Wire"
		],
		[
			"NAME:wire_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Round"
		],
		"strand_number:="	, "$litz_num_d2",
		"wire_diameter:="	, "$litz_dia_d2mm"
	])


# Make setup
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
					"Value:="		, "d1+$move_txmm"
					
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
					"Value:="		, "d2+$move_rxmm"
					
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
					"NAME:space1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "d1/2+$space1mm"
					
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
					"Value:="		, "d1/2+$space3mm"
					
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
					"NAME:airx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "w1/2+space4+30mm"
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



# Make air
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




# =================================================================================================
# Make Tx
# =================================================================================================

oEditor = oDesign.SetActiveEditor("3D Modeler")
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
		"MaterialValue:="	, "\"litz_tx\"",
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

# Tx_in
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
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3+d1/2+1mm",
				"Y:="			, "-l1-space1",
				"Z:="			, "h1/2+10mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "airx",
				"Y:="			, "-l1-space1",
				"Z:="			, "h1/2+10mm"
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
		"MaterialValue:="	, "\"litz_tx\"",
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

# Tx_out
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
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space3+d1/2+1mm",
				"Y:="			, "-l1-space1",
				"Z:="			, "-h1/2-10mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "airx",
				"Y:="			, "-l1-space1",
				"Z:="			, "-h1/2-10mm"
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
		"MaterialValue:="	, "\"litz_tx\"",
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



# =================================================================================================
# Make Rx
# =================================================================================================

oEditor = oDesign.SetActiveEditor("3D Modeler")
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
		"MaterialValue:="	, "\"litz_rx\"",
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
					"X:="			, "w1/2+space4+1mm",
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
					"X:="			, "w1/2+space4+1mm",
					"Y:="			, "-l1-space2",
					"Z:="			, "-4/4*move_rx"
				]
			]
		]
	])

# Rx_in
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
				"X:="			, "w1/2+space4+d2/2+1mm",
				"Y:="			, "-l1-space2",
				"Z:="			, "offset_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4+d2/2+1mm",
				"Y:="			, "-l1-space2",
				"Z:="			, "h1/2+d2"
			],
			[
				"NAME:PLPoint",
				"X:="			, "airx",
				"Y:="			, "-l1-space2",
				"Z:="			, "h1/2+d2"
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
		"MaterialValue:="	, "\"litz_rx\"",
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

# Rx_out
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
				"X:="			, "w1/2+space4+d2/2+1mm",
				"Y:="			, "-l1-space2",
				"Z:="			, "offset_rx-$N2*move_rx"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space4+d2/2+1mm",
				"Y:="			, "-l1-space2",
				"Z:="			, "-h1/2-d2"
			],
			[
				"NAME:PLPoint",
				"X:="			, "airx",
				"Y:="			, "-l1-space2",
				"Z:="			, "-h1/2-d2"
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
		"MaterialValue:="	, "\"litz_rx\"",
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



# maketerminal

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "airx",
		"YStart:="		, "-l1-space1-d1/2",
		"ZStart:="		, "h1/2-d1/2+10mm",
		"Width:="		, "d1",
		"Height:="		, "d1",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
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
		"XStart:="		, "airx",
		"YStart:="		, "-l1-space1-d1/2",
		"ZStart:="		, "-h1/2-d1/2-10mm",
		"Width:="		, "d1",
		"Height:="		, "d1",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle2",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
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
		"XStart:="		, "airx",
		"YStart:="		, "-l1-space2-d2/2",
		"ZStart:="		, "h1/2-d2/2+d2",
		"Width:="		, "d2",
		"Height:="		, "d2",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle3",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
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
		"XStart:="		, "airx",
		"YStart:="		, "-l1-space2-d2/2",
		"ZStart:="		, "-h1/2-d2/2-d2",
		"Width:="		, "d2",
		"Height:="		, "d2",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle4",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"ShellElement:="	, False,
		"ShellElementThickness:=", "0mm",
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignWindingGroup(
	[
		"NAME:Tx_winding",
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
		"NAME:Rx_winding",
		"Type:="		, "Current",
		"IsSolid:="		, True,
		"Current:="		, "100A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])
oModule.AssignCoilTerminal(
	[
		"NAME:CoilTerminal1",
		"Objects:="		, ["Rectangle1"],
		"ParentBndID:="		, "Tx_winding",
		"Conductor number:="	, "1",
		"Winding:="		, "Tx_winding",
		"Point out of terminal:=", False
	])
oModule.AssignCoilTerminal(
	[
		"NAME:CoilTerminal2",
		"Objects:="		, ["Rectangle2"],
		"ParentBndID:="		, "Tx_winding",
		"Conductor number:="	, "1",
		"Winding:="		, "Tx_winding",
		"Point out of terminal:=", True
	])
oModule.AssignCoilTerminal(
	[
		"NAME:CoilTerminal3",
		"Objects:="		, ["Rectangle3"],
		"ParentBndID:="		, "Rx_winding",
		"Conductor number:="	, "1",
		"Winding:="		, "Rx_winding",
		"Point out of terminal:=", True
	])
oModule.AssignCoilTerminal(
	[
		"NAME:CoilTerminal4",
		"Objects:="		, ["Rectangle4"],
		"ParentBndID:="		, "Rx_winding",
		"Conductor number:="	, "1",
		"Winding:="		, "Rx_winding",
		"Point out of terminal:=", False
	])
oModule = oDesign.GetModule("MaxwellParameterSetup")
oModule.AssignMatrix(
	[
		"NAME:Matrix1",
		[
			"NAME:MatrixEntry",
			[
				"NAME:MatrixEntry",
				"Source:="		, "Rx_winding"
			],
			[
				"NAME:MatrixEntry",
				"Source:="		, "Tx_winding"
			]
		]
	])


# simulation
oProject.Save()
oDesign.Analyze("Setup1")

# calculator
oModule = oDesign.GetModule("FieldsReporter")
oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Tx_in")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("Tx_copperloss", "Fields")
oModule.EnterQty("OhmicLoss")
oModule.EnterVol("Rx_in")
oModule.CalcOp("Integrate")
oModule.AddNamedExpression("Rx_copperloss", "Fields")


# Result

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Parameter", "EddyCurrent", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"d2:="			, ["Nominal"],
		"space2:="		, ["Nominal"],
		"space4:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"Num:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["(Matrix1.L(Tx_winding,Rx_winding) / sqrt(Matrix1.L(Tx_winding,Tx_winding)*Matrix1.L(Rx_winding,Rx_winding)))^2 * Matrix1.L(Tx_winding,Tx_winding) * 1e+3","(Matrix1.L(Tx_winding,Rx_winding) / sqrt(Matrix1.L(Tx_winding,Tx_winding)*Matrix1.L(Rx_winding,Rx_winding)))^2 * Matrix1.L(Rx_winding,Rx_winding) * 1e+3","(1 - (Matrix1.L(Tx_winding,Rx_winding) / sqrt(Matrix1.L(Tx_winding,Tx_winding)*Matrix1.L(Rx_winding,Rx_winding)))^2) * Matrix1.L(Tx_winding,Tx_winding) * 1e+6","(1 - (Matrix1.L(Tx_winding,Rx_winding) / sqrt(Matrix1.L(Tx_winding,Tx_winding)*Matrix1.L(Rx_winding,Rx_winding)))^2) * Matrix1.L(Rx_winding,Rx_winding) * 1e+6","(Matrix1.L(Tx_winding,Rx_winding) / sqrt(Matrix1.L(Tx_winding,Tx_winding)*Matrix1.L(Rx_winding,Rx_winding)))","Matrix1.L(Tx_winding,Tx_winding) * 1e+3","Matrix1.L(Rx_winding,Rx_winding) * 1e+3","Matrix1.L(Tx_winding,Rx_winding) * 1e+3","Matrix1.R(Tx_winding,Tx_winding)","Matrix1.R(Rx_winding,Rx_winding)","InputCurrent(Tx_winding)","InputCurrent(Rx_winding)","Matrix1.Z(Tx_winding,Tx_winding)","Matrix1.Z(Rx_winding,Rx_winding)","Matrix1.Z(Tx_winding,Rx_winding)"]
	])
oModule.CreateReport("loss", "Fields", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"Phase:="		, ["0deg"],
		"N1:="			, ["Nominal"],
		"N2:="			, ["Nominal"],
		"d1:="			, ["Nominal"],
		"d2:="			, ["Nominal"],
		"space2:="		, ["Nominal"],
		"space4:="		, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"Num:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["Tx_copperloss","Rx_copperloss"]
	])

# get report
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Parameter", "C:/script11/ML_data/Data1 $VERSION_IDX_STR.csv", False)
oModule.ExportToFile("loss", "C:/script11/ML_data/Data2 $VERSION_IDX_STR.csv", False)







# =================================================================================================
# continue 2
# =================================================================================================

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
					"NAME:move_tx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "d1+$X2move_txmm"
					
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
					"Value:="		, "d2+$X2move_rxmm"
					
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
					"NAME:space1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "d1/2+$X2space1mm"
					
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
					"Value:="		, "d1/2+$X2space3mm"
					
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
					"NAME:w1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X2w1mm"
					
				]
			]
		]
	])


# simulation
oProject.Save()
oDesign.Analyze("Setup1")


# get report
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Parameter", "C:/script11/ML_data/Data3 $VERSION_IDX_STR.csv", False)
oModule.ExportToFile("loss", "C:/script11/ML_data/Data4 $VERSION_IDX_STR.csv", False)



# =================================================================================================
# continue 3
# =================================================================================================

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
					"NAME:move_tx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "d1+$X3move_txmm"
					
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
					"Value:="		, "d2+$X3move_rxmm"
					
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
					"NAME:space1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "d1/2+$X3space1mm"
					
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
					"Value:="		, "d1/2+$X3space3mm"
					
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
					"NAME:w1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X3w1mm"
					
				]
			]
		]
	])


# simulation
oProject.Save()
oDesign.Analyze("Setup1")


# get report
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Parameter", "C:/script11/ML_data/Data5 $VERSION_IDX_STR.csv", False)
oModule.ExportToFile("loss", "C:/script11/ML_data/Data6 $VERSION_IDX_STR.csv", False)



# =================================================================================================
# continue 4
# =================================================================================================

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
					"NAME:move_tx",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "d1+$X4move_txmm"
					
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
					"Value:="		, "d2+$X4move_rxmm"
					
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
					"NAME:space1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "d1/2+$X4space1mm"
					
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
					"Value:="		, "d1/2+$X4space3mm"
					
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
					"NAME:w1",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$X4w1mm"
					
				]
			]
		]
	])


# simulation
oProject.Save()
oDesign.Analyze("Setup1")


# get report
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("Parameter", "C:/script11/ML_data/Data7 $VERSION_IDX_STR.csv", False)
oModule.ExportToFile("loss", "C:/script11/ML_data/Data8 $VERSION_IDX_STR.csv", False)