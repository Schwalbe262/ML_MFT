import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

N1 = $N1

# Open aedt file
#oDesktop.OpenProject("Z:/ANSYS_simulation/transformer/core_type_HFTR/HFTR_2022_05_31_solid_model/ML28.aedt")
oDesktop.OpenProject("Y:/git/ML_MFT/shell_type/litz_model2/script28/ML_aedt/ML28.aedt")


# Make project
oProject = oDesktop.SetActiveProject("ML28")
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

oDefinitionManager = oProject.GetDefinitionManager()

oDefinitionManager.AddMaterial(
	[
		"NAME:copper_litz_Tx_script28_$VERSION_IDX_STR",
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
				"Red:="			, 242,
				"Green:="		, 140,
				"Blue:="		, 102
			]
		],
		"permeability:="	, "0.999991",
		"conductivity:="	, "58000000",
		"thermal_conductivity:=", "400",
		"mass_density:="	, "8933",
		[
			"NAME:stacking_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Litz Wire"
		],
		"specific_heat:="	, "385",
		"youngs_modulus:="	, "120000000000",
		"poissons_ratio:="	, "0.38",
		"thermal_expansion_coefficient:=", "1.77e-05",
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
			"NAME:wire_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Round"
		],
		"strand_number:="	, "$strand_Tx",
		"wire_diameter:="	, "0.1mm"
	])

oDefinitionManager.AddMaterial(
	[
		"NAME:copper_litz_Rx_script28_$VERSION_IDX_STR",
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
				"Red:="			, 242,
				"Green:="		, 140,
				"Blue:="		, 102
			]
		],
		"permeability:="	, "0.999991",
		"conductivity:="	, "58000000",
		"thermal_conductivity:=", "400",
		"mass_density:="	, "8933",
		[
			"NAME:stacking_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Litz Wire"
		],
		"specific_heat:="	, "385",
		"youngs_modulus:="	, "120000000000",
		"poissons_ratio:="	, "0.38",
		"thermal_expansion_coefficient:=", "1.77e-05",
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
			"NAME:wire_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Round"
		],
		"strand_number:="	, "$strand_Rx",
		"wire_diameter:="	, "0.1mm"
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
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "h1/2"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "h1/2"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[0]-coil_width[0]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[0]-coil_width[0]/2",
				"Y:="			, "l1+space[1]+coil_width[0]/2",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2",
				"Y:="			, "l1+space[1]+coil_width[0]/2",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]/2",
				"Y:="			, "l1+space[1]+coil_width[0]/2",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
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
		"MaterialValue:="	, "\"copper_litz_Tx_script28_$VERSION_IDX_STR\"",
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
		"TranslateVectorY:="	, "0mm",
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
				"X:="			, "w1/2+1*space[0]+coil_width[0]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[0]-coil_width[0]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[0]-coil_width[0]/2",
				"Y:="			, "l1+space[1]+coil_width[0]/2",
				"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]/2",
				"Y:="			, "l1+space[1]+coil_width[0]/2",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "-h1/2-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+2*coil_width[0]",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "-h1/2-2/2*(coil_width[0]+move_z[0])"
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
		"MaterialValue:="	, "\"copper_litz_Tx_script28_$VERSION_IDX_STR\"",
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
				"X:="			, "w1/2+space[0]+coil_width[0]",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "-h1/2-2/2*(coil_width[0]+move_z[0])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "(air[0])/2",
				"Y:="			, "-l1-space[1]-coil_width[0]/2",
				"Z:="			, "-h1/2-2/2*(coil_width[0]+move_z[0])"
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
		"MaterialValue:="	, "\"copper_litz_Tx_script28_$VERSION_IDX_STR\"",
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
		"TranslateVectorY:="	, "0mm",
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
					"X:="			, "w1/2+space[0]+coil_width[0]/2 ",
					"Y:="			, "-l1-space[1]-coil_width[0]/2",
					"Z:="			, "0mm"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2",
					"Y:="			, "-l1-space[1]-coil_width[0]/2",
					"Z:="			, "0mm"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-space[0]-coil_width[0]/2",
					"Y:="			, "-l1-space[1]-coil_width[0]/2",
					"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-space[0]-coil_width[0]/2",
					"Y:="			, "l1+space[1]+coil_width[0]/2",
					"Z:="			, "-1/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+space[0]+coil_width[0]/2",
					"Y:="			, "l1+space[1]+coil_width[0]/2",
					"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+space[0]+coil_width[0]/2",
					"Y:="			, "-l1-space[1]-coil_width[0]/2",
					"Z:="			, "-2/2*(coil_width[0]+move_z[0])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+space[0]+coil_width[0]/2 ",
					"Y:="			, "-l1-space[1]-coil_width[0]/2",
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
			"MaterialValue:="	, "\"copper_litz_Tx_script28_$VERSION_IDX_STR\"",
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
			"TranslateVectorY:="	, "0mm",
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
				"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[0]-coil_width[0]-space[2]-coil_width[1]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[0]-coil_width[0]-space[2]-coil_width[1]/2",
				"Y:="			, "l1+space[1]+coil_width[0]+space[3]+coil_width[1]/2",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2",
				"Y:="			, "l1+space[1]+coil_width[0]+space[3]+coil_width[1]/2",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]+space[2]+coil_width[1]/2",
				"Y:="			, "l1+space[1]+coil_width[0]+space[3]+coil_width[1]/2",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]+space[2]+coil_width[1]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
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
		"MaterialValue:="	, "\"copper_litz_Rx_script28_$VERSION_IDX_STR\"",
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
		"TranslateVectorY:="	, "0mm",
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
				"X:="			, "w1/2+1*space[0]+coil_width[0]+space[2]+coil_width[1]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2",
				"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
				"Z:="			, "0mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[0]-coil_width[0]-space[2]-coil_width[1]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-w1/2-space[0]-coil_width[0]-space[2]-coil_width[1]/2",
				"Y:="			, "l1+space[1]+coil_width[0]+space[3]+coil_width[1]/2",
				"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]+space[2]+coil_width[1]/2",
				"Y:="			, "l1+space[1]+coil_width[0]+space[3]+coil_width[1]/2",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]+space[2]+coil_width[1]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "w1/2+space[0]+coil_width[0]+space[2]+coil_width[1]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
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
		"MaterialValue:="	, "\"copper_litz_Rx_script28_$VERSION_IDX_STR\"",
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
				"X:="			, "w1/2+space[0]+coil_width[0]+space[2]+coil_width[1]/2",
				"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
				"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
			],
			[
				"NAME:PLPoint",
				"X:="			, "(air[0])/2",
				"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
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
		"MaterialValue:="	, "\"copper_litz_Rx_script28_$VERSION_IDX_STR\"",
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
		"TranslateVectorY:="	, "0mm",
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
					"X:="			, "w1/2+space[0]+coil_width[0]+space[2]+coil_width[1]/2",
					"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
					"Z:="			, "0mm"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2",
					"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
					"Z:="			, "0mm"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-space[0]-coil_width[0]-space[2]-coil_width[1]/2",
					"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
					"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "-w1/2-space[0]-coil_width[0]-space[2]-coil_width[1]/2",
					"Y:="			, "l1+space[1]+coil_width[0]+space[3]+coil_width[1]/2",
					"Z:="			, "-1/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+space[0]+coil_width[0]+space[2]+coil_width[1]/2",
					"Y:="			, "l1+space[1]+coil_width[0]+space[3]+coil_width[1]/2",
					"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+space[0]+coil_width[0]+space[2]+coil_width[1]/2",
					"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
					"Z:="			, "-2/2*(coil_width[1]+move_z[1])"
				],
				[
					"NAME:PLPoint",
					"X:="			, "w1/2+space[0]+coil_width[0]+space[2]+coil_width[1]/2",
					"Y:="			, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
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
			"MaterialValue:="	, "\"copper_litz_Rx_script28_$VERSION_IDX_STR\"",
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
			"TranslateVectorY:="	, "0mm",
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
		"YCenter:="		, "-l1-space[1]-coil_width[0]/2",
		"ZCenter:="		, "0mm",
		"XStart:="		, "(air[0])/2",
		"YStart:="		, "-l1-space[1]",
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
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "h1/2+(N1/2+0.25)*(coil_width[0]+move_z[0])+offset_z[0]"
	])


oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "(air[0])/2",
		"YCenter:="		, "-l1-space[1]-coil_width[0]/2",
		"ZCenter:="		, "0mm",
		"XStart:="		, "(air[0])/2",
		"YStart:="		, "-l1-space[1]-coil_width[0]/2",
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
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "-h1/2+(-N1/2+0.25)*(coil_width[0]+move_z[0])+offset_z[0]"
	])


oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "(air[0])/2",
		"YCenter:="		, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
		"ZCenter:="		, "0mm",
		"XStart:="		, "(air[0])/2",
		"YStart:="		, "-l1-space[1]-coil_width[0]-space[3]",
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
		"TranslateVectorY:="	, "0mm",
		"TranslateVectorZ:="	, "(N1/2+0.25)*(coil_width[1]+move_z[1])+offset_z[1]"
	])


oEditor.CreateRegularPolygon(
	[
		"NAME:RegularPolygonParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "(air[0])/2",
		"YCenter:="		, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
		"ZCenter:="		, "0mm",
		"XStart:="		, "(air[0])/2",
		"YStart:="		, "-l1-space[1]-coil_width[0]-space[3]-coil_width[1]/2",
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
		"TranslateVectorY:="	, "0mm",
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
		"IsSolid:="		, False,
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
		"IsSolid:="		, False,
		"Current:="		, "0A",
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


oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("magnetizing inductance", "Y:/git/ML_MFT/shell_type/litz_model2/script28/ML_data/magnetizing_inductance$VERSION_IDX_STR.csv", False)
oModule.ExportToFile("leakage inductance", "Y:/git/ML_MFT/shell_type/litz_model2/script28/ML_data/leakage_inductance$VERSION_IDX_STR.csv", False)

oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("litz loss", "EddyCurrent", "Data Table", "Setup1 : LastAdaptive", [], 
	[
		"Freq:="		, ["All"],
		"l1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"Num:="			, ["Nominal"],
		"N1:="			, ["Nominal"]
	], 
	[
		"X Component:="		, "Freq",
		"Y Component:="		, ["StrandedLoss","StrandedLossAC"]
	])

oModule.ExportToFile("litz loss", "Y:/git/ML_MFT/shell_type/litz_model2/script28/ML_data/litz_Tx_loss$VERSION_IDX_STR.csv", False)


oModule = oDesign.GetModule("BoundarySetup")
oModule.EditWindingGroup("Rx", 
	[
		"NAME:Rx",
		"Type:="		, "Current",
		"IsSolid:="		, False,
		"Current:="		, "100A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])
oModule.EditWindingGroup("Tx", 
	[
		"NAME:Tx",
		"Type:="		, "Current",
		"IsSolid:="		, False,
		"Current:="		, "0A",
		"Resistance:="		, "0ohm",
		"Inductance:="		, "0nH",
		"Voltage:="		, "0mV",
		"ParallelBranchesNum:="	, "1",
		"Phase:="		, "0deg"
	])


oProject.Save()

oDesign.Analyze("Setup1")

oModule = oDesign.GetModule("ReportSetup")
oModule.ExportToFile("litz loss", "Y:/git/ML_MFT/shell_type/litz_model2/script28/ML_data/litz_Rx_loss$VERSION_IDX_STR.csv", False)



oDefinitionManager.RemoveMaterial("copper_litz_Tx_script28_$VERSION_IDX_STR", True, "", "Project")
oDefinitionManager.RemoveMaterial("copper_litz_Rx_script28_$VERSION_IDX_STR", True, "", "Project")
oDefinitionManager.RemoveMaterial("ferrite$VERSION_IDX_STR", True, "", "Project")