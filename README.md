# C_Xtr_plotter
use the eppler code velocity table to create an approximate fitting C_Xtr_plotter curve
make sure to copy the whole and only the velocity table coming from Eppler code output file.
example:
0PANEL METHOD AIRFOIL Eppler 211   CL= 0.57041, 6.75660 ALPHA0= 4.83 DEG.
1AIRFOIL Eppler 211   10.96% THICKNESS,     0.00% FLAP   0.00DEGREES DEFLECTION
 MACH=0.000                 -4.00  -2.00   0.00   2.00   4.00   6.00   8.00  10.00  12.00
   N       X          Y      V-DISTRIBUTIONS FOR THE ABOVE ANGLES OF ATTACK RELATIVE TO THE CHORD LINE     
   0  0.9966100  0.0008300  0.812  0.811  0.809  0.805  0.801  0.796  0.790  0.782  0.774
   1  0.9869800  0.0034900  0.904  0.905  0.905  0.904  0.902  0.899  0.894  0.889  0.882
   2  0.9721500  0.0079000  0.994  0.999  1.003  1.006  1.007  1.008  1.007  1.004  1.001
   3  0.9528700  0.0133700  1.054  1.062  1.069  1.074  1.078  1.081  1.082  1.082  1.081
   4  0.9292600  0.0191200  1.084  1.094  1.102  1.110  1.116  1.121  1.124  1.126  1.126
   5  0.9011500  0.0248800  1.090  1.102  1.113  1.123  1.131  1.138  1.143  1.147  1.150
   6  0.8686700  0.0307600  1.094  1.109  1.122  1.134  1.144  1.153  1.161  1.167  1.171
   7  0.8322600  0.0367600  1.100  1.117  1.132  1.146  1.159  1.170  1.180  1.188  1.195
   8  0.7923500  0.0428000  1.106  1.125  1.143  1.159  1.174  1.188  1.200  1.211  1.220
   9  0.7494500  0.0487700  1.112  1.134  1.154  1.173  1.191  1.207  1.222  1.235  1.247
  10  0.7040700  0.0545700  1.119  1.144  1.167  1.189  1.209  1.228  1.246  1.262  1.276
  11  0.6567400  0.0600800  1.127  1.154  1.181  1.206  1.229  1.251  1.271  1.290  1.307
  12  0.6080400  0.0651800  1.135  1.166  1.196  1.224  1.251  1.276  1.300  1.322  1.342
  13  0.5585400  0.0697100  1.145  1.179  1.213  1.245  1.275  1.304  1.331  1.357  1.381
  14  0.5088300  0.0735000  1.155  1.194  1.231  1.267  1.301  1.334  1.366  1.395  1.423
  15  0.4594200  0.0763300  1.163  1.207  1.249  1.289  1.328  1.366  1.401  1.435  1.467
  16  0.4107300  0.0780100  1.168  1.216  1.263  1.309  1.352  1.395  1.435  1.474  1.511
  17  0.3631700  0.0784700  1.170  1.224  1.276  1.327  1.377  1.424  1.470  1.515  1.557
  18  0.3171200  0.0776200  1.166  1.226  1.285  1.342  1.398  1.451  1.503  1.554  1.602
  19  0.2729200  0.0754700  1.157  1.224  1.290  1.354  1.416  1.477  1.536  1.593  1.648
  20  0.2308800  0.0720700  1.142  1.217  1.290  1.362  1.432  1.500  1.567  1.632  1.694
  21  0.1913600  0.0675800  1.122  1.206  1.289  1.370  1.449  1.526  1.602  1.675  1.747
  22  0.1547400  0.0621400  1.098  1.193  1.287  1.378  1.468  1.557  1.643  1.728  1.810
  23  0.1214000  0.0558500  1.066  1.174  1.281  1.386  1.490  1.591  1.691  1.788  1.884
  24  0.0916500  0.0488500  1.024  1.149  1.272  1.394  1.514  1.633  1.749  1.863  1.975
  25  0.0657600  0.0412700  0.965  1.112  1.257  1.401  1.543  1.684  1.822  1.958  2.091
  26  0.0439600  0.0332500  0.878  1.054  1.229  1.402  1.573  1.742  1.910  2.075  2.237
  27  0.0264000  0.0249700  0.748  0.966  1.184  1.400  1.614  1.827  2.037  2.244  2.449
  28  0.0044400  0.0087000  0.139  0.514  0.887  1.260  1.631  2.000  2.367  2.731  3.091
  29  0.0001800  0.0015900  0.744  0.151  0.442  1.034  1.625  2.214  2.801  3.384  3.963
  30  0.0015800 -0.0042900  1.497  0.949  0.399  0.151  0.701  1.250  1.797  2.343  2.885
  31  0.0089600 -0.0096700  1.400  1.080  0.759  0.437  0.115  0.208  0.531  0.853  1.173
  32  0.0214800 -0.0148200  1.379  1.148  0.914  0.680  0.445  0.209  0.027  0.263  0.499
  33  0.0390200 -0.0194200  1.322  1.147  0.972  0.795  0.617  0.439  0.260  0.080  0.099
  34  0.0614600 -0.0233700  1.285  1.145  1.005  0.863  0.720  0.576  0.432  0.287  0.142
  35  0.0886200 -0.0266200  1.249  1.134  1.019  0.902  0.784  0.664  0.545  0.424  0.303
  36  0.1202400 -0.0291600  1.219  1.123  1.025  0.926  0.826  0.725  0.623  0.521  0.417
  37  0.1560200 -0.0309900  1.193  1.111  1.027  0.942  0.856  0.768  0.680  0.591  0.502
  38  0.1955800 -0.0321300  1.171  1.099  1.026  0.952  0.877  0.801  0.723  0.645  0.566
  39  0.2384900 -0.0326000  1.151  1.088  1.024  0.959  0.893  0.825  0.757  0.687  0.617
  40  0.2842700 -0.0324200  1.134  1.078  1.022  0.964  0.905  0.845  0.784  0.722  0.659
  41  0.3323800 -0.0315900  1.118  1.069  1.019  0.967  0.915  0.861  0.806  0.750  0.693
  42  0.3822600 -0.0300900  1.105  1.061  1.016  0.970  0.922  0.874  0.824  0.774  0.722
  43  0.4332900 -0.0277900  1.092  1.053  1.012  0.971  0.928  0.884  0.839  0.793  0.746
  44  0.4851500 -0.0244100  1.068  1.033  0.998  0.961  0.922  0.883  0.843  0.801  0.759
  45  0.5378300 -0.0200600  1.035  1.005  0.973  0.941  0.907  0.872  0.836  0.799  0.761
  46  0.5909800 -0.0153000  1.004  0.977  0.950  0.921  0.891  0.860  0.828  0.794  0.760
  47  0.6439100 -0.0105700  0.976  0.952  0.928  0.902  0.876  0.848  0.819  0.790  0.759
  48  0.6958900 -0.0061800  0.950  0.929  0.908  0.885  0.862  0.837  0.811  0.784  0.757
  49  0.7461500 -0.0023800  0.926  0.908  0.889  0.870  0.849  0.827  0.803  0.779  0.754
  50  0.7939000  0.0006400  0.905  0.890  0.873  0.856  0.837  0.817  0.797  0.775  0.752
  51  0.8383400  0.0027800  0.885  0.872  0.858  0.842  0.826  0.808  0.790  0.771  0.750
  52  0.8787300  0.0039800  0.868  0.857  0.844  0.831  0.816  0.801  0.785  0.767  0.749
  53  0.9143200  0.0042900  0.852  0.842  0.832  0.820  0.807  0.794  0.779  0.764  0.747
  54  0.9444300  0.0038100  0.837  0.830  0.821  0.811  0.800  0.788  0.775  0.762  0.747
  55  0.9684400  0.0027700  0.822  0.816  0.809  0.801  0.792  0.782  0.771  0.760  0.747
  56  0.9858900  0.0015200  0.812  0.811  0.809  0.805  0.801  0.796  0.790  0.782  0.774
