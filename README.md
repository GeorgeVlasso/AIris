# AIris
The Artificial Iris dataset

We provide a data generation program that simulates 128 x 128 artificial flower images according to 5 continuous parameters:

*Petal Length
*Petal Width
*Sepal Length
*Sepal Width
*Color (mixing parameter interpolating between red and magenta)

The primary use of this dataset is evaluation of explanation methods since one can create classes in terms of the latent parameters (define a ground truth).
The dataset can also be used for evaluating disentaglement of regularized generative models. 
This dataset comes as supplementary material for the paper "Explaining predictions by Approximating the local Decision Boundary", Georgios Vlassopoulos, Tim van Erven, Henry Brighton, Vlado Menkovski, 2020.
The latest version of the paper has been submitted in the ML journal track of ECML/PKDD 2021 and is under evaluation. 
This repository will not be updated upon decision.
For more details see the paper. 

Please consider citing us when using the dataset in your research. 

Python 3, matplotlib 3.2.2, PIL 7.0.0, 
