import pycycle.api as pyc


def print_perf(prob, ptName):
    print('Altd  ', prob[ptName+'.fc.alt'])
    print('Mach  ', prob[ptName+'.fc.MN']); print()

    print('ṁ      ', prob[ptName+'.balance.W']) # Mass Flowrate
    print('Fg     ', prob[ptName+'.perf.Fg']) #uninstalled gross thrust
    print('Fnet   ', prob[ptName+'.perf.Fn']) #uninstalled net thrust
    print('SFC    ', prob[ptName+'.perf.TSFC'])

    print('BPR    ', prob[ptName+'.balance.BPR'])
    print('ER     ', prob[ptName+'.mixer.ER']); print()

    print('OPR    ', prob[ptName+'.fan.PR']*prob[ptName+'.hpc.PR']) # OPR = pi_f * pi_hpc (since no LPC)
    print('Fan PR ', prob[ptName+'.fan.PR'])
    print('HPC PR ', prob[ptName+'.hpc.PR']); print()
    print('HPT PR ', prob[ptName+'.hpt.PR'])
    print('LPT PR ', prob[ptName+'.lpt.PR'])


def page_viewer(prob, point):
    flow_stations = ['fc.Fl_O', 'inlet.Fl_O', 'inlet_duct.Fl_O', 'fan.Fl_O', 'bypass_duct.Fl_O',
                     'splitter.Fl_O2', 'splitter.Fl_O1', 'splitter_core_duct.Fl_O',
                     'hpc.Fl_O', 'bld3.Fl_O', 'burner.Fl_O', #OG: had 'lpc.Fl_O', 'lpc_duct.Fl_O' before hpc.Fl_O
                     'hpt.Fl_O', 'hpt_duct.Fl_O', 'lpt_duct.Fl_O',
                     'mixer.Fl_O', 'mixer_duct.Fl_O', 'afterburner.Fl_O', 'mixed_nozz.Fl_O']

    compressors = ['fan', 'hpc'] #OG: lpc after hpc
    burners = ['burner', 'afterburner']
    turbines = ['hpt', 'lpt']
    shafts = ['hp_shaft', 'lp_shaft']

    print('*'*60)
    print('* ' + ' '*10 + point)
    print('*'*60)
    print_perf(prob, point)

    pyc.print_flow_station(prob, [point+"."+fl for fl in flow_stations])
    pyc.print_compressor(prob, [point+"."+c for c in compressors])
    # print_splitter(prob,[point+ ".splitter" ])
    pyc.print_burner(prob, [point+"."+b for b in burners])
    pyc.print_turbine(prob, [point+"."+turb for turb in turbines])
    pyc.print_mixer(prob, [point+'.mixer'])
    pyc.print_nozzle(prob, [point+'.mixed_nozz'])
    pyc.print_shaft(prob, [point+"."+s for s in shafts])
    pyc.print_bleed(prob, [point+'.hpc', point+'.bld3'])
