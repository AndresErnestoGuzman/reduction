from recipes.almahelpers import fixsyscaltimes # SACM/JAO - Fixes
__rethrow_casa_exceptions = True
context = h_init()
context.set_state('ProjectSummary', 'proposal_code', '2017.1.01355.L')
context.set_state('ProjectSummary', 'piname', 'unknown')
context.set_state('ProjectSummary', 'proposal_title', 'unknown')
context.set_state('ProjectStructure', 'ous_part_id', 'X446028809')
context.set_state('ProjectStructure', 'ous_title', 'Undefined')
context.set_state('ProjectStructure', 'ppr_file', '/opt/dared/opt/c5r1/mnt/dataproc/2017.1.01355.L_2018_04_24T20_32_27.369/SOUS_uid___A001_X1296_X123/GOUS_uid___A001_X1296_X124/MOUS_uid___A001_X1296_X12b/working/PPR_uid___A001_X1296_X12c.xml')
context.set_state('ProjectStructure', 'ps_entity_id', 'uid://A001/X1220/Xddd')
context.set_state('ProjectStructure', 'recipe_name', 'hsd_calimage')
context.set_state('ProjectStructure', 'ous_entity_id', 'uid://A001/X1220/Xdd9')
context.set_state('ProjectStructure', 'ousstatus_entity_id', 'uid://A001/X1296/X12b')
try:
    hsd_importdata(vis=['uid___A002_Xc9831a_X646c', 'uid___A002_Xc9831a_X7723', 'uid___A002_Xca0a7b_X4e0b', 'uid___A002_Xca8fbf_X707f', 'uid___A002_Xca9e6b_Xe64b', 'uid___A002_Xca9e6b_Xf5da', 'uid___A002_Xcaf094_X3588', 'uid___A002_Xcaf094_X5182', 'uid___A002_Xcb1740_X6ef4', 'uid___A002_Xcb4a8e_X549a', 'uid___A002_Xcb5bc7_X2846', 'uid___A002_Xcb8a93_Xc0cb', 'uid___A002_Xcba691_X6e74', 'uid___A002_Xcbc47c_X51de', 'uid___A002_Xcbc47c_X6495', 'uid___A002_Xcbdb2a_X13be0', 'uid___A002_Xcc10e0_X1c41', 'uid___A002_Xcc10e0_X67e5'], session=['session_1', 'session_2', 'session_3', 'session_4', 'session_5', 'session_6', 'session_7', 'session_8', 'session_9', 'session_10', 'session_11', 'session_12', 'session_13', 'session_14', 'session_14', 'session_15', 'session_16', 'session_17'])
    hsd_flagdata(pipelinemode="automatic")
    h_tsyscal(pipelinemode="automatic")
    hsd_tsysflag(pipelinemode="automatic")
    hsd_skycal(pipelinemode="automatic")
    hsd_k2jycal(pipelinemode="automatic")
    hsd_applycal(pipelinemode="automatic")
    hsd_baseline(pipelinemode="automatic")
    hsd_blflag(pipelinemode="automatic")
    hsd_baseline(pipelinemode="automatic")
    hsd_blflag(pipelinemode="automatic")
    hsd_imaging(pipelinemode="automatic")
finally:
    h_save()
