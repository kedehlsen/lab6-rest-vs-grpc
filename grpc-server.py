#!/usr/bin/env python3
import argparse
import base64
import io
from concurrent import futures

import grpc
from PIL import Image

import lab6_pb2
import lab6_pb2_grpc


class Lab6Servicer(lab6_pb2_grpc.Lab6Servicer):

    def dotProduct(self, request, context):
        total = sum(x * y for x, y in zip(request.a, request.b))
        return lab6_pb2.dotProductReply(dotproduct=total)

    def add(self, request, context):
        return lab6_pb2.addReply(sum=request.a + request.b)

    def rawImage(self, request, context):
        try:
            img = Image.open(io.BytesIO(request.img))
            return lab6_pb2.imageReply(width=img.size[0], height=img.size[1])
        except Exception:
            return lab6_pb2.imageReply(width=0, height=0)

    def jsonImage(self, request, context):
        try:
            img = Image.open(io.BytesIO(base64.b64decode(request.img)))
            return lab6_pb2.imageReply(width=img.size[0], height=img.size[1])
        except Exception:
            return lab6_pb2.imageReply(width=0, height=0)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='gRPC server')
    parser.add_argument('-p', '--port', type=int, default=50051,
                        help='Port to listen on (default: 50051)')
    args = parser.parse_args()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lab6_pb2_grpc.add_Lab6Servicer_to_server(Lab6Servicer(), server)
    server.add_insecure_port(f'[::]:{args.port}')
    server.start()
    print(f'gRPC server listening on port {args.port}')
    server.wait_for_termination()