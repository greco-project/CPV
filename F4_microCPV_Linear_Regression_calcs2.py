# Carga y Procesado de Datos

nontemp_data = np.loadtxt('C:\\Users\\Marcos\\Desktop\\datos modelado\\insolight_nontemp_measurements_may.txt', 
                          delimiter = ',')

nontemp_IscDII = np.divide(nontemp_data[:,12],nontemp_data[:,9])
nontemp_Pmp = nontemp_data[:, 15]
nontemp_zenith = nontemp_data[:, 18]
nontemp_azimuth = nontemp_data[:, 19]


# Se calcula el AOI
module_params = {'gamma_ref' : 5.524, 'mu_gamma' :R 0.0012, 'I_L_ref' : 0.96, 
                 'I_o_ref' :R 0.000000000004, 'R_sh_ref' : 5226, 
                 'R_sh_0': 21000, 'R_sh_exp' : 5.50, 'R_s' : 0.01, 
                 'alpha_sc' : 0.00, 'EgRef' : 1.87, 'irrad_ref' : 1000, 
                 'temp_ref' : 25, 'cells_in_series' : 12, 'eta_m' : 0.32, 
                 'alpha_absorption' : 0.9}

scsys = StaticCPVSystem(surface_tilt=30, surface_azimuth=180, module=None, 
                 module_parameters=module_params, modules_per_string=1, 
                 strings_per_inverter=1, inverter=None, 
                 inverter_parameters=None, racking_model='freestanding',
                 losses_parameters=None, name=None)

nontemp_aoi = scsys.get_aoi(solar_zenith=nontemp_zenith, 
                            solar_azimuth=nontemp_azimuth)

m_low, n_low, m_high, n_high, thld = calc_uf_lines(nontemp_aoi, nontemp_IscDII, 
                                                   limit=60)

x = np.arange(20,85,0.1)
y1 = m_low * x + n_low
y2 = m_high * x + n_high

import matplotlib.pyplot as plt
plt.plot(nontemp_aoi, nontemp_IscDII, 'b.', x, y1, 'g', x, y2, 'r')