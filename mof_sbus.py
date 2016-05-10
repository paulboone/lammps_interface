import networkx as nx
import numpy as np
from scipy.spatial import distance

def add_distance_matrix(graph):
    carts = []
    for j, data in sorted(graph.nodes_iter(data=True)):
        carts.append(data['cartesian_coordinates'])
    
    carts = np.array(carts)
    graph.distance_matrix = distance.cdist(carts, carts)

InorganicCluster = {
        'Cu':{'Cu Paddlewheel': nx.Graph(name='Cu Paddlewheel') # taken from doi: 10.1126/science.283.5405.1148
              },
        'Zn':{'Zn4O': nx.Graph(name='Zn4O'), # taken from doi:
              'Zn Paddlewheel': nx.Graph(name='Zn Paddlewheel') # taken from doi:
              },
        'Zr':{'Zr_UiO': nx.Graph(name='Zr_UiO') # taken from doi:
              }
        }

OrganicCluster = {
        'N':{'Thymine': nx.Graph(name='Thymine'),
             'Adenine': nx.Graph(name='Adenine')}
        }

# add entry
InorganicCluster['Cu']['Cu Paddlewheel'].add_nodes_from([
    (1, {'element':'O',
         'special_flag': 'O1_Cu_pdw',
         'cartesian_coordinates':np.array([1.755, -0.181, -1.376])
         }
        ),
    (2, {'element':'O',
         'special_flag': 'O2_Cu_pdw',
         'cartesian_coordinates':np.array([-1.755,  0.181, -1.376])
         }
        ),
    (3, {'element':'O',
         'special_flag': 'O1_Cu_pdw',
         'cartesian_coordinates':np.array([-0.181,  1.755,  1.376])
         }
        ),
    (4, {'element':'O', 
         'special_flag':'O2_Cu_pdw',
         'cartesian_coordinates':np.array([0.181, -1.755,  1.376])
         }
        ),
    (5, {'element':'O',
         'special_flag':'O1_Cu_pdw', 
         'cartesian_coordinates':np.array([-1.755,  0.181,  1.376])
         }
        ),
    (6, {'element':'O',
         'special_flag':'O2_Cu_pdw', 
         'cartesian_coordinates':np.array([1.755, -0.181,  1.376])
         }
        ),
    (7, {'element':'O',
         'special_flag':'O1_Cu_pdw',
         'cartesian_coordinates':np.array([0.181, -1.755, -1.376])
         }
        ),
    (8, {'element':'O',
         'special_flag':'O2_Cu_pdw',
         'cartesian_coordinates':np.array([-0.181,  1.755, -1.376])
         }
        ),
    (9, {'element':'Cu',
         'special_flag':'Cu_pdw', 
         'cartesian_coordinates':np.array([0.929,  0.929,  0.000])
         }
        ),
    (10, {'element':'Cu',
          'special_flag':'Cu_pdw',
          'cartesian_coordinates':np.array([-0.929, -0.929,  0.000])
          }
        ),
    (11, {'element':'C', 
          'special_flag':'C_Cu_pdw',
          'cartesian_coordinates':np.array([1.233, -1.233, -1.810])
          }
        ),
    (12, {'element':'C', 
          'special_flag':'C_Cu_pdw',
          'cartesian_coordinates':np.array([-1.233, 1.233, -1.810])
          }
        ),
    (13, {'element':'C', 
          'special_flag':'C_Cu_pdw',
          'cartesian_coordinates':np.array([-1.233, 1.233, 1.810])
          }
        ),
    (14, {'element':'C', 
          'special_flag':'C_Cu_pdw',
          'cartesian_coordinates':np.array([1.233, -1.233, 1.810])
          }
        )
    ])

InorganicCluster['Zn']['Zn Paddlewheel'].add_nodes_from([
    (1, {'element':'O',
         'special_flag': 'O1_Zn_pdw',
         'cartesian_coordinates':np.array([-1.398, -1.339, 1.417])
         }
        ),
    (2, {'element':'O',
         'special_flag': 'O2_Zn_pdw',
         'cartesian_coordinates':np.array([-1.398, 0.853, -1.417])
         }
        ),
    (3, {'element':'O',
         'special_flag': 'O1_Zn_pdw',
         'cartesian_coordinates':np.array([-1.398, 0.853, 1.417])
         }
        ),
    (4, {'element':'O', 
         'special_flag':'O2_Zn_pdw',
         'cartesian_coordinates':np.array([-1.398, -1.339, -1.417])
         }
        ),
    (5, {'element':'O',
         'special_flag':'O1_Zn_pdw', 
         'cartesian_coordinates':np.array([1.398, -1.339, -1.417])
         }
        ),
    (6, {'element':'O',
         'special_flag':'O2_Zn_pdw', 
         'cartesian_coordinates':np.array([1.398, 0.853, 1.417])
         }
        ),
    (7, {'element':'O',
         'special_flag':'O1_Zn_pdw',
         'cartesian_coordinates':np.array([1.398, 0.853, -1.417])
         }
        ),
    (8, {'element':'O',
         'special_flag':'O2_Zn_pdw',
         'cartesian_coordinates':np.array([1.398, -1.339, 1.417])
         }
        ),
    (9, {'element':'Zn',
         'special_flag':'Zn_pdw', 
         'cartesian_coordinates':np.array([0.000, -1.717, 0.000])
         }
        ),
    (10, {'element':'Zn',
          'special_flag':'Zn_pdw',
          'cartesian_coordinates':np.array([0.000, 1.230, 0.000])
          }
        ),
    (11, {'element':'C', 
          'special_flag':'C_Zn_pdw',
          'cartesian_coordinates':np.array([-1.761, -0.243, 1.837])
          }
        ),
    (12, {'element':'C', 
          'special_flag':'C_Zn_pdw',
          'cartesian_coordinates':np.array([-1.761, -0.243, -1.837])
          }
        ),
    (13, {'element':'C', 
          'special_flag':'C_Zn_pdw',
          'cartesian_coordinates':np.array([1.761, -0.243, 1.837])
          }
        ),
    (14, {'element':'C', 
          'special_flag':'C_Zn_pdw',
          'cartesian_coordinates':np.array([1.761, -0.243, -1.837])
          }
        )
    ])


InorganicCluster['Zn']['Zn4O'].add_nodes_from([
    (1, {'element':'Zn',
         'special_flag':'Zn4O',
         'cartesian_coordinates':np.array([-1.063000,-1.063000,-1.174000])
         }
       ),
    (2, {'element':'Zn',
         'special_flag':'Zn4O',
         'cartesian_coordinates':np.array([-1.062000,1.179000,1.067000])
         }
       ),
    (3, {'element':'Zn',
         'special_flag':'Zn4O',
         'cartesian_coordinates':np.array([1.179000,-1.063000,1.067000])
         }
       ),
    (4, {'element':'Zn',
         'special_flag':'Zn4O',
         'cartesian_coordinates':np.array([1.179000,1.178000,-1.175000])
         }
       ),
    (5, {'element':'O',
         'special_flag':'O_z_Zn4O',
         'cartesian_coordinates':np.array([0.058000,0.058000,-0.054000])
         }
       ),
    (6, {'element':'O',
         'special_flag':'O_c_Zn4O',
         'cartesian_coordinates':np.array([-2.939000,-0.765000,-0.876000])
         }
       ),
    (7, {'element':'O',
         'special_flag':'O_c_Zn4O',
         'cartesian_coordinates':np.array([-0.764000,0.883000,2.943000])
         }
       ),
    (8, {'element':'O',
         'special_flag':'O_c_Zn4O',
         'cartesian_coordinates':np.array([0.881000,-2.938000,0.770000])
         }
       ),
    (9, {'element':'O',
         'special_flag':'O_c_Zn4O',
         'cartesian_coordinates':np.array([-2.938000,0.883000,0.770000])
         }
       ),
    (10, {'element':'O',
          'special_flag':'O_c_Zn4O',
          'cartesian_coordinates':np.array([-0.767000,-2.938000,-0.876000])
          }
        ),
    (11, {'element':'O',
          'special_flag':'O_c_Zn4O',
          'cartesian_coordinates':np.array([0.882000,-0.764000,2.943000])
          }
        ),
    (12, {'element':'O',
          'special_flag':'O_c_Zn4O',
          'cartesian_coordinates':np.array([3.055000,-0.766000,0.769000])
          }
        ),
    (13, {'element':'O',
          'special_flag':'O_c_Zn4O',
          'cartesian_coordinates':np.array([0.881000,0.880000,-3.051000])
          }
        ),
    (14, {'element':'O',
          'special_flag':'O_c_Zn4O',
          'cartesian_coordinates':np.array([3.055000,0.880000,-0.878000])
          }
        ),
    (15, {'element':'O',
          'special_flag':'O_c_Zn4O',
          'cartesian_coordinates':np.array([-0.766000,-0.766000,-3.050000])
          }
        ),
    (16, {'element':'O',
          'special_flag':'O_c_Zn4O',
          'cartesian_coordinates':np.array([-0.764000,3.055000,0.769000])
          }
        ),
    (17, {'element':'O',
          'special_flag':'O_c_Zn4O',
          'cartesian_coordinates':np.array([0.882000,3.054000,-0.879000])
          }
        ),
    (18, {'element':'C',
          'special_flag':'C_Zn4O',
          'cartesian_coordinates':np.array([3.541000,0.057000,-0.055000])
          }
        ),
    (19, {'element':'C',
          'special_flag':'C_Zn4O',
          'cartesian_coordinates':np.array([0.059000,3.541000,-0.055000])
          }
        ),
    (20, {'element':'C',
          'special_flag':'C_Zn4O',
          'cartesian_coordinates':np.array([0.057000,0.057000,-3.550000])
          }
        ),
    (21, {'element':'C',
          'special_flag':'C_Zn4O',
          'cartesian_coordinates':np.array([-3.438000,0.059000,-0.053000])
          }
        ),
    (22, {'element':'C',
          'special_flag':'C_Zn4O',
          'cartesian_coordinates':np.array([0.057000,-3.438000,-0.053000])
          }
        ),
    (23, {'element':'C',
          'special_flag':'C_Zn4O',
          'cartesian_coordinates':np.array([0.058000,0.058000,3.429000])
          }
        )
    ])


InorganicCluster['Zr']['Zr_UiO'].add_nodes_from([
    (1, {'element':'Zr',
         'special_flag':'Zr_UiO',
         'cartesian_coordinates':np.array([-0.000000,-2.521000,0.000000])
         }
       ),
    (2, {'element':'O',
         'special_flag':'O_c_Zr_UiO',
         'cartesian_coordinates':np.array([1.973000,-3.568000,0.000000])
         }
       ),
    (3, {'element':'O',
         'special_flag':'O_c_Zr_UiO',
         'cartesian_coordinates':np.array([-1.973000,-3.568000,0.000000])
         }
       ),
    (4, {'element':'O',
         'special_flag':'O_c_Zr_UiO',
         'cartesian_coordinates':np.array([-0.000000,-2.012000,-3.529000])
         }
       ),
    (5, {'element':'O',
         'special_flag':'O_c_Zr_UiO',
         'cartesian_coordinates':np.array([-0.000000,-2.012000,3.529000])
         }
       ),
    (6, {'element':'O',
         'special_flag':'O_c_Zr_UiO',
         'cartesian_coordinates':np.array([-0.000000,-3.568000,-1.973000])
         }
       ),
    (7, {'element':'O',
         'special_flag':'O_c_Zr_UiO',
         'cartesian_coordinates':np.array([-0.000000,-3.568000,1.973000])
         }
       ),
    (8, {'element':'O',
         'special_flag':'O_c_Zr_UiO',
         'cartesian_coordinates':np.array([-3.529000,-2.012000,0.000000])
         }
       ),
    (9, {'element':'O',
         'special_flag':'O_c_Zr_UiO',
         'cartesian_coordinates':np.array([3.529000,-2.012000,0.000000])
         }
       ),
    (10, {'element':'O',
          'special_flag':'O_h_Zr_UiO',
          'cartesian_coordinates':np.array([1.161000,-1.200000,-1.161000])
          }
        ),
    (11, {'element':'O',
          'special_flag':'O_h_Zr_UiO',
          'cartesian_coordinates':np.array([-1.161000,-1.200000,1.161000])
          }
        ),
    (12, {'element':'O',
          'special_flag':'O_z_Zr_UiO',
          'cartesian_coordinates':np.array([1.161000,-1.200000,1.161000])
          }
        ),
    (13, {'element':'O',
          'special_flag':'O_z_Zr_UiO',
          'cartesian_coordinates':np.array([-1.161000,-1.200000,-1.161000])
          }
        ),
    (14, {'element':'C',
          'special_flag':'C_Zr_UiO',
          'cartesian_coordinates':np.array([-3.180000,-3.219000,0.000000])
          }
        ),
    (15, {'element':'C',
          'special_flag':'C_Zr_UiO',
          'cartesian_coordinates':np.array([3.180000,-3.219000,0.000000])
          }
        ),
    (16, {'element':'C',
          'special_flag':'C_Zr_UiO',
          'cartesian_coordinates':np.array([-0.000000,-3.219000,3.180000])
          }
        ),
    (17, {'element':'C',
          'special_flag':'C_Zr_UiO',
          'cartesian_coordinates':np.array([-0.000000,-3.219000,-3.180000])
          }
        ),
    (18, {'element':'Zr',
          'special_flag':'Zr_UiO',
          'cartesian_coordinates':np.array([2.482000,-0.039000,0.000000])
          }
        ),
    (19, {'element':'Zr',
          'special_flag':'Zr_UiO',
          'cartesian_coordinates':np.array([-2.482000,-0.039000,0.000000])
          }
        ),
    (20, {'element':'Zr',
          'special_flag':'Zr_UiO',
          'cartesian_coordinates':np.array([-0.000000,2.443000,0.000000])
          }
        ),
    (21, {'element':'Zr',
          'special_flag':'Zr_UiO',
          'cartesian_coordinates':np.array([-0.000000,-0.039000,2.482000])
          }
        ),
    (22, {'element':'Zr',
          'special_flag':'Zr_UiO',
          'cartesian_coordinates':np.array([-0.000000,-0.039000,-2.482000])
          }
        ),
    (23, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([3.529000,-0.039000,1.973000])
          }
        ),
    (24, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([-3.529000,-0.039000,1.973000])
          }
        ),
    (25, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([-3.529000,-0.039000,-1.973000])
          }
        ),
    (26, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([3.529000,-0.039000,-1.973000])
          }
        ),
    (27, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([1.973000,3.490000,0.000000])
          }
        ),
    (28, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([-1.973000,3.490000,0.000000])
          }
        ),
    (29, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([-0.000000,1.934000,3.529000])
          }
        ),
    (30, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([-0.000000,1.934000,-3.529000])
          }
        ),
    (31, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([-0.000000,3.490000,-1.973000])
          }
        ),
    (32, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([-0.000000,3.490000,1.973000])
          }
        ),
    (33, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([3.529000,1.934000,0.000000])
          }
        ),
    (34, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([-3.529000,1.934000,0.000000])
          }
        ),
    (35, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([1.973000,-0.039000,-3.529000])
          }
        ),
    (36, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([1.973000,-0.039000,3.529000])
          }
        ),
    (37, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([-1.973000,-0.039000,3.529000])
          }
        ),
    (38, {'element':'O',
          'special_flag':'O_c_Zr_UiO',
          'cartesian_coordinates':np.array([-1.973000,-0.039000,-3.529000])
          }
        ),
    (39, {'element':'O',
          'special_flag':'O_h_Zr_UiO',
          'cartesian_coordinates':np.array([-1.161000,1.122000,-1.161000])
          }
        ),
    (40, {'element':'O',
          'special_flag':'O_h_Zr_UiO',
          'cartesian_coordinates':np.array([1.161000,1.122000,1.161000])
          }
        ),
    (41, {'element':'O',
          'special_flag':'O_z_Zr_UiO',
          'cartesian_coordinates':np.array([-1.161000,1.122000,1.161000])
          }
        ),
    (42, {'element':'O',
          'special_flag':'O_z_Zr_UiO',
          'cartesian_coordinates':np.array([1.161000,1.122000,-1.161000])
          }
        ),
    (43, {'element':'C',
          'special_flag':'C_Zr_UiO',
          'cartesian_coordinates':np.array([3.180000,-0.039000,-3.180000])
          }
        ),
    (44, {'element':'C',
          'special_flag':'C_Zr_UiO',
          'cartesian_coordinates':np.array([-3.180000,-0.039000,-3.180000])
          }
        ),
    (45, {'element':'C',
          'special_flag':'C_Zr_UiO',
          'cartesian_coordinates':np.array([-3.180000,-0.039000,3.180000])
          }
        ),
    (46, {'element':'C',
          'special_flag':'C_Zr_UiO',
          'cartesian_coordinates':np.array([3.180000,-0.039000,3.180000])
          }
        ),
    (47, {'element':'C',
          'special_flag':'C_Zr_UiO',
          'cartesian_coordinates':np.array([-3.180000,3.141000,0.000000])
          }
        ),
    (48, {'element':'C',
          'special_flag':'C_Zr_UiO',
          'cartesian_coordinates':np.array([3.180000,3.141000,0.000000])
          }
        ),
    (49, {'element':'C',
          'special_flag':'C_Zr_UiO',
          'cartesian_coordinates':np.array([-0.000000,3.141000,-3.180000])
          }
        ),
    (50, {'element':'C',
          'special_flag':'C_Zr_UiO',
          'cartesian_coordinates':np.array([-0.000000,3.141000,3.180000])
          }
        ),
    (51, {'element':'H',
          'special_flag':'H_o_Zr_UiO',
          'cartesian_coordinates':np.array([1.881000,1.801000,1.666000])
          }
        ),
    (52, {'element':'H',
          'special_flag':'H_o_Zr_UiO',
          'cartesian_coordinates':np.array([-1.832000,-1.884000,1.722000])
          }
        ),
    (53, {'element':'H',
          'special_flag':'H_o_Zr_UiO',
          'cartesian_coordinates':np.array([-1.838000,1.795000,-1.728000])
          }
        ),
    (54, {'element':'H',
          'special_flag':'H_o_Zr_UiO',
          'cartesian_coordinates':np.array([1.871000,-1.866000,-1.695000])
          }
        )
    ])

OrganicCluster['N']['Adenine'].add_nodes_from([
    (1, {'element':'C',
         'special_flag':'C',
         'cartesian_coordinates':np.array([-0.108000,-0.237000,0.527000])
         }
       ),
    (2, {'element':'C',
         'special_flag':'C',
         'cartesian_coordinates':np.array([0.853000,-2.150000,0.700000])
         }
       ),
    (3, {'element':'C',
         'special_flag':'C',
         'cartesian_coordinates':np.array([0.550000,-0.540000,-0.675000])
         }
       ),
    (4, {'element':'C',
         'special_flag':'C',
         'cartesian_coordinates':np.array([-0.074000,1.419000,-1.600000])
         }
       ),
    (5, {'element':'C',
         'special_flag':'C',
         'cartesian_coordinates':np.array([-0.796000,0.992000,0.603000])
         }
       ),
    (6, {'element':'H',
         'special_flag':'Hd',
         'cartesian_coordinates':np.array([-1.914000,2.348000,1.629000])
         }
       ),
    (7, {'element':'H',
         'special_flag':'H',
         'cartesian_coordinates':np.array([-1.599000,0.804000,2.476000])
         }
       ),
    (8, {'element':'H',
         'special_flag':'H',
         'cartesian_coordinates':np.array([1.193000,-3.098000,1.104000])
         }
       ),
    (9, {'element':'H',
         'special_flag':'H',
         'cartesian_coordinates':np.array([-0.080000,2.127000,-2.431000])
         }
       ),
    (10, {'element':'N',
          'special_flag':'N',
          'cartesian_coordinates':np.array([0.121000,-1.283000,1.403000])
          }
        ),
    (11, {'element':'N',
          'special_flag':'N',
          'cartesian_coordinates':np.array([1.133000,-1.761000,-0.560000])
          }
        ),
    (12, {'element':'N',
          'special_flag':'N',
          'cartesian_coordinates':np.array([0.617000,0.283000,-1.751000])
          }
        ),
    (13, {'element':'H',
          'special_flag':'Na',
          'cartesian_coordinates':np.array([-0.763000,1.773000,-0.514000])
          }
        ),
    (14, {'element':'N',
          'special_flag':'Nd',
          'cartesian_coordinates':np.array([-1.424000,1.447000,1.691000])
          }
        )
    ])

OrganicCluster['N']['Thymine'].add_nodes_from([
    (1, {'element':'C',
         'special_flag':'C',
         'cartesian_coordinates':np.array([13.966000,16.972000,12.145000])
         }
       ),
    (2, {'element':'C',
         'special_flag':'C',
         'cartesian_coordinates':np.array([12.549000,18.380000,13.950000])
         }
       ),
    (3, {'element':'C',
         'special_flag':'C',
         'cartesian_coordinates':np.array([11.714000,19.119000,14.888000])
         }
       ),
    (4, {'element':'C',
         'special_flag':'C',
         'cartesian_coordinates':np.array([13.016000,17.103000,14.220000])
         }
       ),
    (5, {'element':'N',
         'special_flag':'Ndw',
         'cartesian_coordinates':np.array([13.714000,16.442000,13.316000])
         }
       ),
    (6, {'element':'O',
         'special_flag':'Oa2',
         'cartesian_coordinates':np.array([14.542000,16.323000,11.289000])
         }
       ),
    (7, {'element':'O',
         'special_flag':'Oaw',
         'cartesian_coordinates':np.array([12.755000,16.528000,15.269000])
         }
       ),
    (8, {'element':'H',
         'special_flag':'H',
         'cartesian_coordinates':np.array([10.864000,18.500000,15.184000])
         }
       ),
    (9, {'element':'H',
         'special_flag':'Hdw',
         'cartesian_coordinates':np.array([14.003000,15.581000,13.493000])
         }
       ),
    (10, {'element':'C',
          'special_flag':'C',
          'cartesian_coordinates':np.array([12.877000,18.890000,12.738000])
          }
        ),
    (11, {'element':'N',
          'special_flag':'Nd2',
          'cartesian_coordinates':np.array([13.557000,18.186000,11.867000])
          }
        ),
    (12, {'element':'H',
          'special_flag':'H',
          'cartesian_coordinates':np.array([12.293000,19.381000,15.776000])
          }
        ),
    (13, {'element':'H',
          'special_flag':'H',
          'cartesian_coordinates':np.array([11.316000,20.039000,14.453000])
          }
        ),
    (14, {'element':'H',
          'special_flag':'H',
          'cartesian_coordinates':np.array([12.585000,19.801000,12.470000])
          }
        ),
    (15, {'element':'H',
          'special_flag':'Hd2',
          'cartesian_coordinates':np.array([13.727000,18.544000,11.021000])
          }
        )
    ])

# compute the distance matrix
add_distance_matrix(InorganicCluster['Cu']['Cu Paddlewheel'])
add_distance_matrix(InorganicCluster['Zn']['Zn Paddlewheel'])
add_distance_matrix(InorganicCluster['Zn']['Zn4O'])
add_distance_matrix(InorganicCluster['Zr']['Zr_UiO'])
add_distance_matrix(OrganicCluster['N']['Adenine'])
add_distance_matrix(OrganicCluster['N']['Thymine'])
