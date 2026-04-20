import math

class Flow:
    def __init__(self, pressure, nozzle_diameter, time_or_frequency, fluid, density=None, viscosity=None):
        """
        density [g/cm^3]
        pressure [psi]
        nozzleDiameter ['0.xxmm']
        timeOrFrequency [s] or [Hz]
            used in sample app as frequency [Hz]
            used in development as time [s]
        """
        density_table = {
            "Water": {"density": 1, "fluid_correction_factor": 1.0},
            "Methanol": {"density": 0.792, "fluid_correction_factor": 1.0},
            "Acetone": {"density": 0.784, "fluid_correction_factor": 1.0},
            "2-Butanol": {"density": 0.810, "fluid_correction_factor": 1.0},
            'n-Hexane': {"density": 0.655, "fluid_correction_factor": 1.0},
            'Pentane': {"density": 0.6209, "fluid_correction_factor": 1.0},
            'Cyclohexane': {"density": 0.779, "fluid_correction_factor": 1.0},
            'Carbon Tetrachloride': {"density": 1.589, "fluid_correction_factor": 1.0},
            'Toluene': {"density": 0.867, "fluid_correction_factor": 1.0},
            'Chloroform': {"density": 1.49, "fluid_correction_factor": 1.0},
            'Dichloromethane': {"density": 1.33, "fluid_correction_factor": 1.0},
            'Diethyl ether': {"density": 0.713, "fluid_correction_factor": 1.0},
            'Ethyl acetate': {"density": 0.902, "fluid_correction_factor": 1.0},
            'Ethanol': {"density": 0.789, "fluid_correction_factor": 1.0},
            'Pyridine': {"density": 0.982, "fluid_correction_factor": 1.0},
        }
        if fluid != 'Specific':
            fluid_properties = density_table[fluid]
            self.density = fluid_properties["density"]
            self.fluid_correction_factor = fluid_properties["fluid_correction_factor"]
        else:
            self.density = float(density)
            self.fluid_correction_factor = 1.0  # Default correction factor for specific fluids
            viscosity = float(viscosity)

        self.pressure = pressure
        self.timeOrFrequency = time_or_frequency
        
        if nozzle_diameter == '0.25':
            self.nozzle_lohms = 7500
            self.nozzle_correction_factor = 1
        elif nozzle_diameter == '0.19':
            self.nozzle_lohms = 15400
            self.nozzle_correction_factor = 1
        elif nozzle_diameter == '0.13':
            self.nozzle_lohms = 35000
            self.nozzle_correction_factor = 1
        elif nozzle_diameter == '0.10':
            self.nozzle_lohms = 60000
            self.nozzle_correction_factor = 1
        elif nozzle_diameter == '0.08':
            self.nozzle_lohms = 125000
            self.nozzle_correction_factor = 1
        elif nozzle_diameter == '0.05':
            self.nozzle_lohms = 280000
            self.nozzle_correction_factor = 1
        elif nozzle_diameter == 'atomizer 22k':
            self.nozzle_lohms = 22000
            self.nozzle_correction_factor = 1
        elif nozzle_diameter == 'atomizer 67k':
            self.nozzle_lohms = 67000
            self.nozzle_correction_factor = 1

    def calcFlow(self):
        """
        flowRateI [ul/s]
        """
        unit_conversion_constant_k = 75700
        lohms = math.sqrt(self.nozzle_lohms ** 2 + 4750 ** 2 + 2100 ** 2 + 700 ** 2)

        # empirically determined correction factor
        correction_factor = self.pressure/40

        # flow rate in ul per s
        flow_rate_i = correction_factor * unit_conversion_constant_k / lohms * math.sqrt(
            self.pressure / self.density) / 60 * 1000 * self.nozzle_correction_factor * self.fluid_correction_factor
        return flow_rate_i

    def calcVolumeFrequency(self):
        """
        calculates the volume for one opening of the valve
        volume [ul] (SampleApp)
        """
        volume = self.calcFlow() * (0.5 / self.timeOrFrequency)
        return volume

    def calcVolumeTime(self):
        """
        calculates the volume for the valve opened for a duration of time
        (development)
        """
        volume = self.calcFlow() * self.timeOrFrequency
        return volume

class FlowAS:
    def __init__(self, pressure, nozzle_diameter, time_or_frequency, fluid, density=None, viscosity=None):
        """
        density [g/cm^3]
        pressure [psi]
        nozzleDiameter ['0.xxmm']
        timeOrFrequency [s] or [Hz]
            used in sample app as frequency [Hz]
            used in development as time [s]
        """
        if nozzle_diameter == '0.13':
            density_table = {
                "Water": {"density": 1, "flowrate": 20},
                "Methanol": {"density": 0.792, "flowrate": 23},
                "Acetone": {"density": 0.784, "flowrate": 24},
                "Acetonitrile": {"density": 0.784, "flowrate": 24},
                "2-Butanol": {"density": 0.810, "flowrate": 26},
                'Ethyl acetate': {"density": 0.902, "flowrate": 18},
                'Ethanol': {"density": 0.789, "flowrate": 21},
                "2-Propanol": {"density": 0.786, "flowrate": 27},
                "Cyclohexane": {"density": 0.784, "flowrate": 0.0019*time_or_frequency+22},  #final
                "Toluene": {"density": 0.784, "flowrate": 0.006*time_or_frequency+16},#final
            }
        elif nozzle_diameter == '0.10':
            density_table = {
                "Water": {"density": 1, "flowrate": 0.0415*time_or_frequency+31.5},
                "Methanol": {"density": 0.792, "flowrate": 23},
                "Acetone": {"density": 0.784, "flowrate": 24},
                "Acetonitrile": {"density": 0.784, "flowrate": 24},
                "2-Butanol": {"density": 0.810, "flowrate": 26},
                'Ethyl acetate': {"density": 0.902, "flowrate": 18},
                'Ethanol': {"density": 0.789, "flowrate": 21},
                "2-Propanol": {"density": 0.786, "flowrate": 27},
                "Cyclohexane": {"density": 0.784, "flowrate": 0.0098*time_or_frequency+14},#final
                "Toluene": {"density": 0.784, "flowrate": 0.009*time_or_frequency+11.5},#final
            }
        elif nozzle_diameter == '0.08':
            density_table = {
                "Water": {"density": 1, "flowrate": 0.011*time_or_frequency+11.7},#final
                "Methanol": {"density": 0.792, "flowrate": 0.013*time_or_frequency+16.52},#final
                "Acetone": {"density": 0.784, "flowrate": 0.022*time_or_frequency+4.5},#final
                "Acetonitrile": {"density": 0.784, "flowrate": 0.0075*time_or_frequency+17.7},#final
                "2-Butanol": {"density": 0.810, "flowrate": 26},
                'Ethyl acetate': {"density": 0.902, "flowrate": 0.016*time_or_frequency+9.3},#final
                'Ethanol': {"density": 0.789, "flowrate": 0.022*time_or_frequency+5.0},#final
                "2-Propanol": {"density": 0.786, "flowrate": 0.017*time_or_frequency+8.97},#final
                "Cyclohexane": {"density": 0.784, "flowrate": 0.015*time_or_frequency+8.5},#final
                "Toluene": {"density": 0.784, "flowrate": 0.0124*time_or_frequency+7.75}, #final
            }
        
        fluid_properties = density_table[fluid]
        self.density = fluid_properties["density"]
        self.flowrate = fluid_properties["flowrate"]

        self.pressure = 5.0
        self.timeOrFrequency = time_or_frequency
        
        if nozzle_diameter == '0.25':
            self.nozzle_lohms = 7500
            self.nozzle_correction_factor = 1
        elif nozzle_diameter == '0.19':
            self.nozzle_lohms = 15400
            self.nozzle_correction_factor = 1
        elif nozzle_diameter == '0.13':
            self.nozzle_lohms = 35000
            self.nozzle_correction_factor = 0.58959066
        elif nozzle_diameter == '0.10':
            self.nozzle_lohms = 60000
            self.nozzle_correction_factor = 0.864860354
        elif nozzle_diameter == '0.08':
            self.nozzle_lohms = 125000
            self.nozzle_correction_factor = 1.252220554
        elif nozzle_diameter == '0.05':
            self.nozzle_lohms = 280000
            self.nozzle_correction_factor = 1
        elif nozzle_diameter == 'atomizer 22k':
            self.nozzle_lohms = 22000
            self.nozzle_correction_factor = 1
        elif nozzle_diameter == 'atomizer 67k':
            self.nozzle_lohms = 67000
            self.nozzle_correction_factor = 0.761582999

    def calcFlow(self):
        """
        flowRateI [ul/s]
        """
        #unit_conversion_constant_k = 75700
        #lohms = math.sqrt(self.nozzle_lohms ** 2 + 4750 ** 2 + 2100 ** 2 + 700 ** 2)

        # flow rate in ul per s
        flow_rate_i = self.flowrate
        #print(flow_rate_i)
        return flow_rate_i

    def calcVolumeFrequency(self):
        """
        calculates the volume for one opening of the valve
        volume [ul] (SampleApp)
        """
        volume = self.calcFlow() * (0.5/ self.timeOrFrequency)
        return volume
