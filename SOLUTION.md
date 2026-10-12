
|  Method 	| Local  	| Same-Zone  	|  Different Region 	|
|---	|---	|---	|---	|---	|
|   REST add	| 3.19  	| 3.60  	|  361.55	|
|   gRPC add	| 0.84  	|  2.01 	|   183.68 	|
|   REST rawimg	|  6.14 	|  9.90 	|  1876.97 	|
|   gRPC rawimg	|   10.68    |  17.00 	|  268.14 	|
|   REST dotproduct	|  3.78 	|  4.45 	|  409.42	|
|   gRPC dotproduct	|  0.95 	| 1.45  	|  164.31  	|
|   REST jsonimg	|  30.97 	|  36.81 	|  1610.53 	|
|   gRPC jsonimg	|   29.49    |  31.51 	|  285.65 	|
|   PING        |   0.046    |   0.414   |   299.25    |


You should measure the basic latency  using the `ping` command - this can be construed to be the latency without any RPC or python overhead.

You should examine your results and provide a short paragraph with your observations of the performance difference between REST and gRPC. You should explicitly comment on the role that network latency plays -- it's useful to know that REST makes a new TCP connection for each query while gRPC makes a single TCP connection that is used for all the queries.


gRPC was faster than REST for small requests in every environment, and the gap increased with distance. REST opens a new TCP connection each query so two round trips are required for handshake and request, while gRPC keeps it a connection open and has reuse. Same-Zone results were only a few milliseconds above Local, since the network adds under a millisecond of latency, where the cross-region results were one to two times larger, with network round-trip time accounting for most of each call. For large images, gRPC had no advantage locally, but across regions it was far faster (rawimg: 268 ms vs. 1877 ms).
