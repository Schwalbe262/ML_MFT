# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2021.1.0
# 22:03:00  8 07, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("ML1")
oDesign = oProject.SetActiveDesign("Maxwell_ML_v1")
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
		"Frequency:="		, "24kHz",
		"HasSweepSetup:="	, False,
		"UseHighOrderShapeFunc:=", False,
		"UseMuLink:="		, False
	])
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("L Table 1", "C:/script1/ML_data/Data3 1.csv", False)
oModule.ExportToFile("Calculator Expressions Table 1", "C:/script1/ML_data/Data4 1.csv", False)
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
		"permeability:="	, "4430",
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
					"UserDef:="		, True,
					"Value:="		, "393mm"
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
					"UserDef:="		, True,
					"Value:="		, "182.6mm"
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
					"UserDef:="		, True,
					"Value:="		, "52mm"
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
					"UserDef:="		, True,
					"Value:="		, "98mm"
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
					"UserDef:="		, True,
					"Value:="		, "239mm"
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
					"UserDef:="		, True,
					"Value:="		, "7.33mm"
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
					"UserDef:="		, True,
					"Value:="		, "9.15mm"
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
					"UserDef:="		, True,
					"Value:="		, "10.86mm"
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
					"UserDef:="		, True,
					"Value:="		, "11.27mm"
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
					"UserDef:="		, True,
					"Value:="		, "9/2*move_tx+-28.0mm"
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
					"UserDef:="		, True,
					"Value:="		, "7/2*move_rx+30.5mm"
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
					"UserDef:="		, True,
					"Value:="		, "215mm"
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
					"UserDef:="		, True,
					"Value:="		, "8.66mm"
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
					"UserDef:="		, True,
					"Value:="		, "56.06mm"
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
					"UserDef:="		, True,
					"Value:="		, "8.27mm"
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
					"UserDef:="		, True,
					"Value:="		, "45.1mm"
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
					"UserDef:="		, True,
					"Value:="		, "16.81mm"
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
					"UserDef:="		, True,
					"Value:="		, "20.6mm"
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
		"Current:="		, "46.6915555555556A",
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
		"Current:="		, "56A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])
oProject.Save()
oDesign.Analyze("Setup1")
oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("L Table 1", "C:/script1/ML_data/Data5 1.csv", False)
oModule.ExportToFile("Calculator Expressions Table 1", "C:/script1/ML_data/Data6 1.csv", False)
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
		"permeability:="	, "5014",
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
					"UserDef:="		, True,
					"Value:="		, "378mm"
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
					"UserDef:="		, True,
					"Value:="		, "200.11mm"
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
					"UserDef:="		, True,
					"Value:="		, "42mm"
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
					"UserDef:="		, True,
					"Value:="		, "88mm"
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
					"UserDef:="		, True,
					"Value:="		, "244mm"
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
					"UserDef:="		, True,
					"Value:="		, "2.88mm"
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
					"UserDef:="		, True,
					"Value:="		, "6.16mm"
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
					"UserDef:="		, True,
					"Value:="		, "4.23mm"
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
					"UserDef:="		, True,
					"Value:="		, "12.94mm"
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
					"UserDef:="		, True,
					"Value:="		, "9/2*move_tx+-76.0mm"
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
					"UserDef:="		, True,
					"Value:="		, "7/2*move_rx+32.5mm"
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
					"UserDef:="		, True,
					"Value:="		, "241mm"
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
					"UserDef:="		, True,
					"Value:="		, "5.97mm"
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
					"UserDef:="		, True,
					"Value:="		, "48.37mm"
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
					"UserDef:="		, True,
					"Value:="		, "5.03mm"
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
					"UserDef:="		, True,
					"Value:="		, "49.61mm"
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
					"UserDef:="		, True,
					"Value:="		, "15.82mm"
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
					"UserDef:="		, True,
					"Value:="		, "10.81mm"
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
		"Current:="		, "55.5286666666667A",
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
		"Current:="		, "73A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])
oProject.Save()
oDesign.Analyze("Setup1")
