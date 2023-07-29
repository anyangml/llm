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
                    latex: Fuel = \sum_{{j=1}}^{{n}} \frac{{P_{{rated\ j}}}}{{\eta_j}} \times \frac{{LD_j}}{{HHV_j}} \times OH_j \times 0.0036
                    display_name: Fuel Consumption
                    measurement_type: measurement_type
                    measurement_unit: m3
                    measurement_quantity: Volume
                    data_type: float
                - symbol: power
                    description: Maximum rated power for fired equipment j.
                    latex: P_{{rated\ j}}
                    display_name: Maximum rated power
                    measurement_type: measurement_type
                    measurement_unit: kW
                    measurement_quantity: Power
                    required: true
                    constraints:
                    minimum: 0
                    data_type: float
                - symbol: load_factor
                    description: Load for fired equipment j (load fraction).
                    latex: LD_j
                    display_name: Load factor
                    measurement_type: measurement_type
                    measurement_unit: fraction
                    measurement_quantity: Fraction
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
                    measurement_quantity: Time
                    required: true
                    constraints:
                    minimum: 0
                    data_type: float
                - symbol: eff
                    description: Thermal efficiency for fired equipment j.
                    latex: \eat_j
                    display_name: Thermal efficiency
                    measurement_type: measurement_type
                    measurement_unit: fraction
                    measurement_quantity: Fraction
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
                    measurement_quantity: Energy density
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
                    measurement_quantity: Conversion Factor
                    data_type: float
""",
    }
]
