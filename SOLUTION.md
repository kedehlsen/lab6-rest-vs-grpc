
|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|---	|
|   REST add	| 3.19  	| 3.60  	|  	|
|   gRPC add	| 0.84  	|  2.01 	|    	|
|   REST rawimg	|  6.14 	|  9.90 	|   	|
|   gRPC rawimg	|   10.68    |  17.00 	|   	|
|   REST dotproduct	|  3.78 	|  4.45 	|  	|
|   gRPC dotproduct	|  0.95 	| 1.45  	|    	|
|   REST jsonimg	|  30.97 	|  36.81 	|   	|
|   gRPC jsonimg	|   29.49    |  31.51 	|   	|
|   PING        |   0.046    |   0.414   |       |



You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.
