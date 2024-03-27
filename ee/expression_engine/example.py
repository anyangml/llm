examples = [
    {
        "latex": """F u e l=\\sum_{{j=1}}^{{n}}{{\\frac{{P_{{r a e d j}}}}{{\\eta_{{j}}}}}}\\times{{\\frac{{L D_{{j}}}}{{H H V_{{j}}}}}}\\times O H_{{j}}\\times0.0036 \n
                Fuel = Annual theoretical volume of liquid fuel combusted by fired equipment j
                (m
                3/year).
                Prated j = Maximum rated power for fired equipment j (kW).
                LD j  = Load for fired equipment j (load fraction).
                OH j  = Annual operating hours for fired equipment j (hours/year).
                ηj  = Thermal efficiency for fired equipment j.
                HHV j  = High heat value of the liquid fuel combusted by fired equipment j (GJ/m3).
                n = quantity of fired equipment units,
                0.0036          = conversion factor between kWh and GJ.""",

        "yaml": """version: 1
                equation: power * load_factor * hour / (eff * hhv) * conversion_factor
                inputs:
                  - power
                  - load_factor
                  - hour
                  - eff
                  - hhv
                output: fuel
                terms:
                  - symbol: fuel
                    description: Theoretical volume of liquid fuel combusted by fired equipment j.
                    latex: Fuel
                    display_name: Volume Fuel Consumed
                    measurement_type: measurement_type
                    measurement_unit: m3
                    measurement_quantity: volume
                    data_type: float
                  - symbol: power
                    description: Maximum rated power for fired equipment j.
                    latex: P_{{rated\ j}}
                    display_name: Maximum rated power
                    measurement_type: measurement_type
                    measurement_unit: kW
                    measurement_quantity: power
                    required: true
                    constraints:
                      minimum: 0
                    data_type: float
                  - symbol: load_factor
                    description: Load for fired equipment j (load fraction).
                    latex: LD_j
                    display_name: Load factor
                    measurement_type: measurement_type
                    measurement_unit: unitless
                    measurement_quantity: ratio
                    required: true
                    constraints:
                      minimum: 0
                      maximum: 1
                    data_type: float
                  - symbol: hour
                    description: Total operating hours for fired equipment j.
                    latex: OH_j
                    display_name: Operating hours
                    measurement_type: measurement_type
                    measurement_unit: h
                    measurement_quantity: time
                    required: true
                    constraints:
                      minimum: 0
                    data_type: float
                  - symbol: eff
                    description: Thermal efficiency for fired equipment j.
                    latex: \eat_j
                    display_name: Thermal efficiency
                    measurement_type: measurement_type
                    measurement_unit: unitless
                    measurement_quantity: ratio
                    required: true
                    constraints:
                      minimum: 0
                      maximum: 1
                    data_type: float
                  - symbol: hhv
                    description: High heat value of the liquid fuel combusted by fired equipment j.
                    latex: HHV_j
                    display_name: High heat value
                    measurement_type: measurement_type
                    measurement_unit: GJ/m3
                    measurement_quantity: energy_density
                    required: true
                    constraints:
                      minimum: 0
                    data_type: float
                  - symbol: conversion_factor
                    description: Energy conversion factor
                    latex: 0.0036
                    constant_value: 0.0036
                    display_name: Mass conversion factor (GJ/kWh)
                    measurement_type: measurement_type
                    measurement_unit: GJ/kWh
                    measurement_quantity: ratio
                    data_type: float
""",
    },
    {
        "latex": """C O_{{2}}=\sum_{{i=1}}^{{n}}\ {{3.664\times F u e l_{{i}}\times C C_{{i}}\times0.001  \n
                CO, 一 Annual CO, mass emissions from combustion of the specific gaseous fuel
                (tonnes).
                n Number of required carbon content determinations for the year, as specified in
                WCI.25.
                Fuel 一 Fuel combusted in period “i” a day or month, as applicable) (volume of the
                gaseous fuel in Rm at reference temperature and pressure conditions as used by
                the facility, or mass of the gaseous fuel in kg if a mass flow meter is used)
                CC 一 Average carbon content of the gaseous fuel, from the fuel analysis results for the
                period i(day or month, as applicable) (kg per Rm' or kg C per kg of fuel if a
                mass flow meter is used)
                3.664 Ratio of molecular weights, CO to carbon.
                0.001 Conversion factor from kg to tonnes.""",

        "yaml": """version: 1
                equation: mw_ratio * fuel * cc * conversion_factor
                inputs:
                  - fuel
                  - cc
                output: mass_co2
                terms:
                  - symbol: mass_co2
                    description: Annual CO2 mass emissions from combustion of the specific gaseous fuel.
                    latex: CO_2
                    display_name: CO2 Emissions
                    measurement_type: measurement_type
                    measurement_unit: tonnes
                    measurement_quantity: mass
                    data_type: float
                  - symbol: mw_ratio
                    description: Ratio of molecular weights, CO2 to carbon.
                    latex: 3.664
                    constant_value: 3.664
                    display_name: CO2 to carbon MW ratio
                    measurement_type: measurement_type
                    measurement_unit: unitless
                    measurement_quantity: ratio
                    data_type: float
                  - symbol: fuel
                    description: Fuel combusted in period "i" (volume of the gaseous fuel in Rm at reference temperature and pressure conditions as used by the facility, or mass of the gaseous fuel in kg if a mass flow meter is used).
                    latex: Fuel_i
                    display_name: Fuel Combusted
                    measurement_type: measurement_type
                    measurement_unit: m3
                    measurement_quantity: volume
                    required: true
                    constraints:
                      minimum: 0
                    data_type: float
                  - symbol: cc
                    description: Average carbon content of the gaseous fuel, from the fuel analysis results for the period "i" (kg per Rm' or kg C per kg of fuel if a mass flow meter is used).
                    latex: CC_i
                    display_name: Carbon Content
                    measurement_type: measurement_type
                    measurement_unit: kg/Rm or kg C/kg
                    measurement_quantity: Mass per Volume or Mass per Mass
                    required: true
                    constraints:
                      minimum: 0
                    data_type: float
                  - symbol: conversion_factor
                    description: Conversion factor from kg to tonnes.
                    latex: 0.001
                    constant_value: 0.001
                    display_name: Mass Conversion Factor (kg/tonnes)
                    measurement_type: measurement_type
                    measurement_unit: kg/tonnes
                    measurement_quantity: ratio
                    data_type: float
""",
    },
        {
        "latex": """C O_{{2}}=Product_{{i}} * EF_{{i}} * \%Vol_{{i}}\n
                CO, 一 Annual CO2 emissions that would result from the complete combustion or oxidation of each petroleum product “i” (metric tons).
                Product i - Annual volume of each petroleum product “i” produced, imported, or exported by the reporting party (barrels). For refiners, this volume only includes products ex refinery gate.
                EF i Petroleum product-specific CO2 emission factor (metric tons CO2 per barrel) from Table MM–1 of this subpart.
                Vol i Percent volume of product “i” that is petroleum-based, not including any denaturant that may be present in any ethanol product, expressed as a fraction (e.g., 75% would be expressed as 0.75 in the above equation).
                """,

        "yaml": """version: 1
                   equation: product_vol * ef * volume_fraction
                   inputs:
                     - product_vol
                     - ef
                     - volume_fraction
                   output: mass_co2
                   terms:
                     - symbol: mass_co2
                       description: Annual CO2 emissions that would result from the complete combustion or oxidation of each petroleum product "i".
                       latex: CO_2i
                       display_name: CO2 Emissions
                       measurement_type: measurement_type
                       measurement_unit: tonnes
                       measurement_quantity: mass
                       data_type: float
                     - symbol: product_vol
                       description: Annual volume of each petroleum product "i" produced, imported, or exported by the reporting party.
                       latex: Product_i
                       display_name: Annual Volume of Petroleum Product
                       measurement_type: measurement_type
                       measurement_unit: bbl
                       measurement_quantity: volume
                       required: true
                       constraints:
                         minimum: 0
                       data_type: float
                     - symbol: ef
                       description: Petroleum product-specific CO2 emission factor from Table MM-1.
                       latex: EF_i
                       display_name: CO2 Emission Factor
                       measurement_type: measurement_type
                       measurement_unit: tonnes/bbl
                       measurement_quantity: density
                       required: true
                       constraints:
                         minimum: 0
                       data_type: float
                     - symbol: volume_fraction
                       description: Percent volume of product "i" that is petroleum-based, not including any denaturant that may be present in any ethanol product, expressed as a fraction.
                       latex: \%Vol_i
                       display_name: Volume Fraction
                       measurement_type: measurement_type
                       measurement_unit: unitless
                       measurement_quantity: ratio
                       required: true
                       constraints:
                         minimum: 0
                         maximum: 1
                       data_type: float
""",
    }
]
