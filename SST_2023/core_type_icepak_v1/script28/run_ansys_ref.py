import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()

N1 = $N1

# ====================
# Open aedt file
#oDesktop.OpenProject("Z:/ANSYS_simulation/transformer/core_type_HFTR/HFTR_2022_05_31_solid_model/ML28.aedt")
oDesktop.OpenProject("Y:/git/ML_MFT/SST_2023/core_type_icepak_v1/script28/ML_aedt/ML28.aedt")


# Make project
oProject = oDesktop.SetActiveProject("ML28")
oProject.InsertDesign("Icepak", "Icepak_ML_v$VERSION_IDX_STR", "TemperatureAndFlow", "")

oDesign = oProject.SetActiveDesign("Icepak_ML_v$VERSION_IDX_STR")
oDesign.SetSolutionType(
	[
		"NAME:SolutionTypeOption",
		"SolutionTypeOption:="	, "SteadyState",
		"ProblemOption:="	, "TemperatureAndFlow"
	])



# ====================
# Make setup
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("IcepakSteadyState", 
	[
		"NAME:Setup1",
		"Enabled:="		, True,
		"Flow Regime:="		, "Turbulent",
		"Turbulent Model Eqn:="	, "ZeroEquation",
		"Include Temperature:="	, True,
		"Include Flow:="	, True,
		"Include Gravity:="	, True,
		"Include Solar:="	, False,
		"Solution Initialization - X Velocity:=", "0m_per_sec",
		"Solution Initialization - Y Velocity:=", "0m_per_sec",
		"Solution Initialization - Z Velocity:=", "1m_per_sec",
		"Solution Initialization - Temperature:=", "AmbientTemp",
		"Solution Initialization - Turbulent Kinetic Energy:=", "1m2_per_s2",
		"Solution Initialization - Turbulent Dissipation Rate:=", "1m2_per_s3",
		"Solution Initialization - Specific Dissipation Rate:=", "1diss_per_s",
		"Solution Initialization - Use Model Based Flow Initialization:=", False,
		"Convergence Criteria - Flow:=", "0.001",
		"Convergence Criteria - Energy:=", "1e-07",
		"Convergence Criteria - Turbulent Kinetic Energy:=", "0.001",
		"Convergence Criteria - Turbulent Dissipation Rate:=", "0.001",
		"Convergence Criteria - Specific Dissipation Rate:=", "0.001",
		"Convergence Criteria - Discrete Ordinates:=", "1e-06",
		"IsEnabled:="		, False,
		"Radiation Model:="	, "Off",
		"Solar Radiation Model:=", "Solar Radiation Calculator",
		"Solar Radiation - Scattering Fraction:=", "0",
		"Solar Radiation - Day:=", 1,
		"Solar Radiation - Month:=", 1,
		"Solar Radiation - Hours:=", 0,
		"Solar Radiation - Minutes:=", 0,
		"Solar Radiation - GMT:=", "0",
		"Solar Radiation - Latitude:=", "0",
		"Solar Radiation - Latitude Direction:=", "East",
		"Solar Radiation - Longitude:=", "0",
		"Solar Radiation - Longitude Direction:=", "North",
		"Solar Radiation - Ground Reflectance:=", "0",
		"Solar Radiation - Sunshine Fraction:=", "0",
		"Solar Radiation - North X:=", "0",
		"Solar Radiation - North Y:=", "0",
		"Solar Radiation - North Z:=", "1",
		"Under-relaxation - Pressure:=", "0.3",
		"Under-relaxation - Momentum:=", "0.7",
		"Under-relaxation - Temperature:=", "1",
		"Under-relaxation - Turbulent Kinetic Energy:=", "0.8",
		"Under-relaxation - Turbulent Dissipation Rate:=", "0.8",
		"Under-relaxation - Specific Dissipation Rate:=", "0.8",
		"Discretization Scheme - Pressure:=", "Standard",
		"Discretization Scheme - Momentum:=", "First",
		"Discretization Scheme - Temperature:=", "First",
		"Secondary Gradient:="	, False,
		"Discretization Scheme - Turbulent Kinetic Energy:=", "First",
		"Discretization Scheme - Turbulent Dissipation Rate:=", "First",
		"Discretization Scheme - Specific Dissipation Rate:=", "First",
		"Discretization Scheme - Discrete Ordinates:=", "First",
		"Linear Solver Type - Pressure:=", "V",
		"Linear Solver Type - Momentum:=", "flex",
		"Linear Solver Type - Temperature:=", "F",
		"Linear Solver Type - Turbulent Kinetic Energy:=", "flex",
		"Linear Solver Type - Turbulent Dissipation Rate:=", "flex",
		"Linear Solver Type - Specific Dissipation Rate:=", "flex",
		"Linear Solver Termination Criterion - Pressure:=", "0.1",
		"Linear Solver Termination Criterion - Momentum:=", "0.1",
		"Linear Solver Termination Criterion - Temperature:=", "0.1",
		"Linear Solver Termination Criterion - Turbulent Kinetic Energy:=", "0.1",
		"Linear Solver Termination Criterion - Turbulent Dissipation Rate:=", "0.1",
		"Linear Solver Termination Criterion - Specific Dissipation Rate:=", "0.1",
		"Linear Solver Residual Reduction Tolerance - Pressure:=", "0.1",
		"Linear Solver Residual Reduction Tolerance - Momentum:=", "0.1",
		"Linear Solver Residual Reduction Tolerance - Temperature:=", "0.1",
		"Linear Solver Residual Reduction Tolerance - Turbulent Kinetic Energy:=", "0.1",
		"Linear Solver Residual Reduction Tolerance - Turbulent Dissipation Rate:=", "0.1",
		"Linear Solver Residual Reduction Tolerance - Specific Dissipation Rate:=", "0.1",
		"Linear Solver Stabilization - Pressure:=", "None",
		"Linear Solver Stabilization - Temperature:=", "None",
		"Coupled pressure-velocity formulation:=", False,
		"Frozen Flow Simulation:=", False,
		"Sequential Solve of Flow and Energy Equations:=", False,
		"Convergence Criteria - Max Iterations:=", 200
	])



# ====================
# Set material

oDefinitionManager = oProject.GetDefinitionManager()

# core material
oDefinitionManager.AddMaterial(
	[
		"NAME:ferrite_v$VERSION_IDX_STR",
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
		"permeability:="	, "1000",
		"conductivity:="	, "0.01",
		"thermal_conductivity:=", "$core_thermal_coeff", # $core_thermal_coeff
		"mass_density:="	, "4600",
		"specific_heat:="	, "750",
		"youngs_modulus:="	, "119000000000",
		"thermal_expansion_coefficient:=", "1e-05"
	])

# molding material
oDefinitionManager.AddMaterial(
	[
		"NAME:epoxy_v$VERSION_IDX_STR",
		"CoordinateSystemType:=", "Cartesian",
		"BulkOrSurfaceType:="	, 1,
		[
			"NAME:PhysicsTypes",
			"set:="			, ["Thermal"]
		],
		[
			"NAME:AttachedData",
			[
				"NAME:MatAppearanceData",
				"property_data:="	, "appearance_data",
				"Red:="			, 255,
				"Green:="		, 210,
				"Blue:="		, 80
			]
		],
		"thermal_conductivity:=", "$epoxy_thermal_coeff", # $epoxy_thermal_coeff
		"mass_density:="	, "1120",
		"specific_heat:="	, "1400",
		[
			"NAME:thermal_material_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Solid"
		],
		[
			"NAME:clarity_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Opaque"
		]
	])

# bobin material
oDefinitionManager.AddMaterial(
	[
		"NAME:bobin_epoxy_v$VERSION_IDX_STR",
		"CoordinateSystemType:=", "Cartesian",
		"BulkOrSurfaceType:="	, 1,
		[
			"NAME:PhysicsTypes",
			"set:="			, ["Thermal"]
		],
		[
			"NAME:AttachedData",
			[
				"NAME:MatAppearanceData",
				"property_data:="	, "appearance_data",
				"Red:="			, 255,
				"Green:="		, 210,
				"Blue:="		, 80
			]
		],
		"thermal_conductivity:=", "$bobin_thermal_coeff", # $bobin_thermal_coeff
		"mass_density:="	, "1120",
		"specific_heat:="	, "1400",
		[
			"NAME:thermal_material_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Solid"
		],
		[
			"NAME:clarity_type",
			"property_type:="	, "ChoiceProperty",
			"Choice:="		, "Opaque"
		]
	])


# ====================
# Set FEA variable

# Num
oDesign.ChangeProperty(
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

# air
oDesign.ChangeProperty(
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
					"Value:="		, "[300, 300, 300] mm"
				]
			]
		]
	])


# ====================
# Set variable

# N1
oDesign.ChangeProperty(
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
					"Value:="		, "$N1" # $N1
					
				]
			]
		]
	])


# w1
oDesign.ChangeProperty(
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
					"Value:="		, "$w1mm" # $w1
					
				]
			]
		]
	])


# l1
oDesign.ChangeProperty(
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
					"Value:="		, "$l1mm" # $l1
					
				]
			]
		]
	])


# l2
oDesign.ChangeProperty(
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
					"Value:="		, "$l2mm" # $l2
					
				]
			]
		]
	])


# h1
oDesign.ChangeProperty(
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
					"Value:="		, "$h1mm" # $h1
					
				]
			]
		]
	])


# space1, space2, space3, space4
oDesign.ChangeProperty(
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
					"Value:="		, "[$space1, $space2, $space3, $space4] mm" # $space1, $space2, $space3, $space4
				]
			]
		]
	])


# coil_width
oDesign.ChangeProperty(
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
					"Value:="		, "[$coil_width1, $coil_width2] mm" # $coil_width1, $coil_width2
				]
			]
		]
	])


# move
oDesign.ChangeProperty(
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
					"Value:="		, "[$move_z1, $move_z2] mm" # $move_z1, $move_z2
				]
			]
		]
	])


# offset
oDesign.ChangeProperty(
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
					"Value:="		, "[$offset_z1, $offset_z2] mm" # $offset_z1, $offset_z2
				]
			]
		]
	])


# epoxy
oDesign.ChangeProperty(
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
					"NAME:epoxy_xy",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$epoxy_x, $epoxy_y] mm" # $epoxy_x, $epoxy_y
				]
			]
		]
	])


# cold1
oDesign.ChangeProperty(
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
					"NAME:cold_xyz",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "[$cold_x1, $cold_y1, $cold_z1, $cold_x2, $cold_y2, $cold_z2] mm" # $cold_x1, $cold_y1, $cold_z1, $cold_x2, $cold_y2, $cold_z2
				]
			]
		]
	])


# fillet_core
oDesign.ChangeProperty(
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
					"NAME:fillet_core",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$fillet_coremm" # $fillet_core
					
				]
			]
		]
	])


# fillet_epoxy
oDesign.ChangeProperty(
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
					"NAME:fillet_epoxy",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$fillet_epoxymm" # $fillet_epoxy
					
				]
			]
		]
	])

# epoxy_gap
oDesign.ChangeProperty(
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
					"NAME:epoxy_gap",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$epoxy_gapmm" # $epoxy_gap
					
				]
			]
		]
	])

# bobin_thick
oDesign.ChangeProperty(
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
					"NAME:bobin_thick",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$bobin_thickmm" # $bobin_thick
					
				]
			]
		]
	])

# bobin_skirt
oDesign.ChangeProperty(
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
					"NAME:bobin_skirt",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "$bobin_skirtmm" # $bobin_skirt
					
				]
			]
		]
	])

# ====================
# Draw component


# =================================================================================================
# Make region
# =================================================================================================
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Region:CreateRegion:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:+X Padding Data",
					"Value:="		, "300"
				],
				[
					"NAME:-X Padding Data",
					"Value:="		, "300"
				],
				[
					"NAME:+Y Padding Data",
					"Value:="		, "200"
				],
				[
					"NAME:-Y Padding Data",
					"Value:="		, "200"
				],
				[
					"NAME:+Z Padding Data",
					"Value:="		, "200"
				],
				[
					"NAME:-Z Padding Data",
					"Value:="		, "200"
				]
			]
		]
	])


# =================================================================================================
# Make core
# =================================================================================================
oEditor = oDesign.SetActiveEditor("3D Modeler")
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
		"MaterialValue:="	, "\"ferrite_v$VERSION_IDX_STR\"", # ferrite_v$VERSION_IDX_STR
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
		"MaterialValue:="	, "\"ferrite_v$VERSION_IDX_STR\"", # ferrite_v$VERSION_IDX_STR
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

oEditor.Fillet(
	[
		"NAME:Selections",
		"Selections:="		, "core",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:FilletParameters",
			"Edges:="		, [42,44,46,48],
			"Vertices:="		, [],
			"Radius:="		, "fillet_core", # $fillet_core
			"Setback:="		, "0mm"
		]
	])


# =================================================================================================
# Make mold
# =================================================================================================
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-w1/2 - 0.5*2*(coil_width[0]+space[0]+epoxy_xy[0])",
		"YPosition:="		, "-l1/2 - 0.5*2*(coil_width[0]+space[1]+epoxy_xy[1])",
		"ZPosition:="		, "-h1/2",
		"XSize:="		, "w1 + 2*(coil_width[0]+space[0]+epoxy_xy[0])",
		"YSize:="		, "l1 + 2*(coil_width[0]+space[1]+epoxy_xy[1])",
		"ZSize:="		, "h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "mold",
		"Flags:="		, "",
		"Color:="		, "(255 210 80)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"epoxy_v$VERSION_IDX_STR\"", # epoxy_v$VERSION_IDX_STR
		"SurfaceMaterialValue:=", "\"steel-oxidised-surface\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.Fillet(
	[
		"NAME:Selections",
		"Selections:="		, "mold",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:Parameters",
		[
			"NAME:FilletParameters",
			"Edges:="		, [167,168,169,170],
			"Vertices:="		, [],
			"Radius:="		, "fillet_epoxy", # $fillet_epoxy
			"Setback:="		, "0mm"
		]
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-(w1+2*epoxy_gap)/2",
		"YPosition:="		, "-(l1+2*epoxy_gap)/2",
		"ZPosition:="		, "-h1/2",
		"XSize:="		, "(w1+2*epoxy_gap)",
		"YSize:="		, "(l1+2*epoxy_gap)",
		"ZSize:="		, "h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "mold_sub",
		"Flags:="		, "",
		"Color:="		, "(255 210 80)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"epoxy_v$VERSION_IDX_STR\"", # epoxy_v$VERSION_IDX_STR
		"SurfaceMaterialValue:=", "\"steel-oxidised-surface\"",
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
				"X:="			, "w1/2 + 0.5*2*(coil_width[0]+space[0])",
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
				"X:="			, "w1/2 + 0.5*2*(coil_width[0]+space[0])",
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
				"X:="			, "w1/2 + 0.5*2*(coil_width[1]+space[2])",
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
				"X:="			, "w1/2 + 0.5*2*(coil_width[1]+space[2])",
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



# =================================================================================================
# Make Rx end
# =================================================================================================


# subtract
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "mold",
		"Tool Parts:="		, "mold_sub"
	], 
	[
		"NAME:SubtractParameters",
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "mold",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "-(l1+l2)/2",
		"TranslateVectorZ:="	, "0mm"
	])

# subtract
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "mold",
		"Tool Parts:="		, "Tx_in, core"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, True
	])




# =================================================================================================
# Make bobin
# =================================================================================================
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-(w1+space[2]*2-coil_width[1]+2*bobin_skirt)/2",
		"YPosition:="		, "-(l1+space[3]*2-coil_width[1]+2*bobin_skirt)/2",
		"ZPosition:="		, "-h1/2",
		"XSize:="		, "(w1+space[2]*2-coil_width[1]+2*bobin_skirt)",
		"YSize:="		, "(l1+space[3]*2-coil_width[1]+2*bobin_skirt)",
		"ZSize:="		, "h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "bobin",
		"Flags:="		, "",
		"Color:="		, "(255 210 80)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"bobin_epoxy_v$VERSION_IDX_STR\"", # bobin_epoxy_v$VERSION_IDX_STR
		"SurfaceMaterialValue:=", "\"steel-oxidised-surface\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-(w1+space[2]*2-coil_width[1]-2*bobin_thick)/2",
		"YPosition:="		, "-(l1+space[3]*2-coil_width[1]-2*bobin_thick)/2",
		"ZPosition:="		, "-h1/2",
		"XSize:="		, "(w1+space[2]*2-coil_width[1]-2*bobin_thick)",
		"YSize:="		, "(l1+space[3]*2-coil_width[1]-2*bobin_thick)",
		"ZSize:="		, "h1"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "bobin_sub",
		"Flags:="		, "",
		"Color:="		, "(255 210 80)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"bobin_epoxy_v$VERSION_IDX_STR\"", # bobin_epoxy_v$VERSION_IDX_STR
		"SurfaceMaterialValue:=", "\"steel-oxidised-surface\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

# subtract
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "bobin",
		"Tool Parts:="		, "bobin_sub"
	], 
	[
		"NAME:SubtractParameters",
	])

oEditor.Move(
	[
		"NAME:Selections",
		"Selections:="		, "bobin",
		"NewPartsModelFlag:="	, "Model"
	], 
	[
		"NAME:TranslateParameters",
		"TranslateVectorX:="	, "0mm",
		"TranslateVectorY:="	, "(l1+l2)/2",
		"TranslateVectorZ:="	, "0mm"
	])

oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "bobin",
		"Tool Parts:="		, "core, Rx_in"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, True
	])




# =================================================================================================
# Make model end
# =================================================================================================



# ====================
# Thermal excitation

oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignOpeningBoundary(
	[
		"NAME:Opening1",
		"Faces:="		, [7,8,9,10,11,12],
		"Temperature:="		, "AmbientTemp",
		"External Rad. Temperature:=", "AmbientRadTemp",
		"Inlet Type:="		, "Pressure",
		"Total Pressure:="	, "AmbientPressure",
		"No Reverse Flow:="	, False
	])

oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Icepak",
			[
				"NAME:PropServers", 
				"Design Settings"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Ambients/Temperature",
					"Value:="		, "50cel"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Icepak",
			[
				"NAME:PropServers", 
				"Design Settings"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Ambients/Rad. Temperature",
					"Value:="		, "50cel"
				]
			]
		]
	])

oModule.AssignSourceBoundary(
	[
		"NAME:source_LV_loss",
		"Objects:="		, ["Tx_in"],
		"Thermal Condition:="	, "Total Power",
		"Total Power:="		, "$LV_lossW",
		"Surface Heat:="	, "0irrad_W_per_m2",
		"Temperature:="		, "AmbientTemp",
		[
			"NAME:Radiation",
			"Radiate:="		, False
		]
	])
oModule.AssignSourceBoundary(
	[
		"NAME:source_HV_loss",
		"Objects:="		, ["Rx_in"],
		"Thermal Condition:="	, "Total Power",
		"Total Power:="		, "$HV_lossW",
		"Surface Heat:="	, "0irrad_W_per_m2",
		"Temperature:="		, "AmbientTemp",
		[
			"NAME:Radiation",
			"Radiate:="		, False
		]
	])
oModule.AssignSourceBoundary(
	[
		"NAME:source_core_loss",
		"Objects:="		, ["core"],
		"Thermal Condition:="	, "Total Power",
		"Total Power:="		, "$core_lossW",
		"Surface Heat:="	, "0irrad_W_per_m2",
		"Temperature:="		, "AmbientTemp",
		[
			"NAME:Radiation",
			"Radiate:="		, False
		]
	])



# =================================================================================================
# Make coldplate
# =================================================================================================

oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-w1/2 - cold_xyz[0]",
		"YPosition:="		, "-(2*l1+l2-2*fillet_core)/2 - cold_xyz[1]",
		"ZPosition:="		, "(h1/2+l1) + cold_xyz[2]",
		"XSize:="		, "w1 + 2*cold_xyz[0]",
		"YSize:="		, "(2*l1+l2-2*fillet_core) + 2*cold_xyz[1]",
		"ZSize:="		, "-cold_xyz[2] - cold_xyz[5]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "cold_plate1",
		"Flags:="		, "",
		"Color:="		, "(232 232 235)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"aluminum\"",
		"SurfaceMaterialValue:=", "\"steel-oxidised-surface\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-w1/2 - cold_xyz[0] + cold_xyz[3]",
		"YPosition:="		, "-(2*l1+l2-2*fillet_core)/2 - cold_xyz[1] + cold_xyz[4]",
		"ZPosition:="		, "(h1/2+l1)",
		"XSize:="		, "w1 + 2*cold_xyz[0] - 2*cold_xyz[3]",
		"YSize:="		, "(2*l1+l2-2*fillet_core) + 2*cold_xyz[1] - 2*cold_xyz[4]",
		"ZSize:="		, "-cold_xyz[5]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "cold_plate1_sub",
		"Flags:="		, "",
		"Color:="		, "(232 232 235)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"aluminum\"",
		"SurfaceMaterialValue:=", "\"steel-oxidised-surface\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "cold_plate1",
		"Tool Parts:="		, "cold_plate1_sub"
	], 
	[
		"NAME:SubtractParameters",
	])

# coldplate 2
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-w1/2 - cold_xyz[0]",
		"YPosition:="		, "-(2*l1+l2-2*fillet_core)/2 - cold_xyz[1]",
		"ZPosition:="		, "-(h1/2+l1) - cold_xyz[2]",
		"XSize:="		, "w1 + 2*cold_xyz[0]",
		"YSize:="		, "(2*l1+l2-2*fillet_core) + 2*cold_xyz[1]",
		"ZSize:="		, "cold_xyz[2] + cold_xyz[5]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "cold_plate2",
		"Flags:="		, "",
		"Color:="		, "(232 232 235)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"aluminum\"",
		"SurfaceMaterialValue:=", "\"steel-oxidised-surface\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-w1/2 - cold_xyz[0] + cold_xyz[3]",
		"YPosition:="		, "-(2*l1+l2-2*fillet_core)/2 - cold_xyz[1] + cold_xyz[4]",
		"ZPosition:="		, "-(h1/2+l1)",
		"XSize:="		, "w1 + 2*cold_xyz[0] - 2*cold_xyz[3]",
		"YSize:="		, "(2*l1+l2-2*fillet_core) + 2*cold_xyz[1] - 2*cold_xyz[4]",
		"ZSize:="		, "cold_xyz[5]"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "cold_plate2_sub",
		"Flags:="		, "",
		"Color:="		, "(232 232 235)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMIZ:="		, "",
		"MaterialValue:="	, "\"aluminum\"",
		"SurfaceMaterialValue:=", "\"steel-oxidised-surface\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "cold_plate2",
		"Tool Parts:="		, "cold_plate2_sub"
	], 
	[
		"NAME:SubtractParameters",
	])

oModule = oDesign.GetModule("BoundarySetup")
oModule.AssignSourceBoundary(
	[
		"NAME:Source1",
		"Objects:="		, ["cold_plate1","cold_plate2"],
		"Thermal Condition:="	, "Fixed Temperature",
		"Total Power:="		, "0W",
		"Surface Heat:="	, "0irrad_W_per_m2",
		"Temperature:="		, "AmbientTemp",
		[
			"NAME:Radiation",
			"Radiate:="		, False
		]
	])



# ====================
# calculator

# LV side
oModule = oDesign.GetModule("FieldsReporter")
oModule.EnterQty("Temp")
oModule.EnterVol("Tx_in")
oModule.CalcOp("Maximum")
oModule.AddNamedExpression("LV_max_temp", "Fields")
oModule.EnterQty("Temp")
oModule.EnterVol("Tx_in")
oModule.CalcOp("Mean")
oModule.AddNamedExpression("LV_mean_temp", "Fields")

# HV side
oModule = oDesign.GetModule("FieldsReporter")
oModule.EnterQty("Temp")
oModule.EnterVol("Rx_in")
oModule.CalcOp("Maximum")
oModule.AddNamedExpression("HV_max_temp", "Fields")
oModule.EnterQty("Temp")
oModule.EnterVol("Rx_in")
oModule.CalcOp("Mean")
oModule.AddNamedExpression("HV_mean_temp", "Fields")

# core side
oModule = oDesign.GetModule("FieldsReporter")
oModule.EnterQty("Temp")
oModule.EnterVol("core")
oModule.CalcOp("Maximum")
oModule.AddNamedExpression("core_max_temp", "Fields")
oModule.EnterQty("Temp")
oModule.EnterVol("core")
oModule.CalcOp("Mean")
oModule.AddNamedExpression("core_mean_temp", "Fields")





oProject.Save()
oDesign = oProject.SetActiveDesign("Icepak_ML_v$VERSION_IDX_STR")
oDesign.Analyze("Setup1")
oModule = oDesign.GetModule("ReportSetup")
oModule.CreateReport("Calculator Expressions Table 1", "Fields", "Data Table", "Setup1 : SteadyState", [], 
	[
		"Num:="			, ["All"],
		"N1:="			, ["Nominal"],
		"w1:="			, ["Nominal"],
		"l1:="			, ["Nominal"],
		"l2:="			, ["Nominal"],
		"h1:="			, ["Nominal"],
		"fillet_core:="		, ["Nominal"],
		"fillet_epoxy:="	, ["Nominal"],
		"epoxy_gap:="		, ["Nominal"],
		"bobin_thick:="		, ["Nominal"],
		"bobin_skirt:="		, ["Nominal"]
	], 
	[
		"X Component:="		, "Num",
		"Y Component:="		, ["LV_max_temp","LV_mean_temp","HV_max_temp","HV_mean_temp","core_max_temp","core_mean_temp"]
	])
oModule.ExportToFile("Calculator Expressions Table 1", "Y:/git/ML_MFT/SST_2023/core_type_icepak_v1/script28/ML_data/temp_data_$VERSION_IDX_STR.csv", False)





oDefinitionManager.RemoveMaterial("ferrite_v$VERSION_IDX_STR", True, "", "Project")
oDefinitionManager.RemoveMaterial("epoxy_v$VERSION_IDX_STR", True, "", "Project")
oDefinitionManager.RemoveMaterial("bobin_epoxy_v$VERSION_IDX_STR", True, "", "Project")



oProject.DeleteDesign("Icepak_ML_v$VERSION_IDX_STR")