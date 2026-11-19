"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#InferredWorkloadType``."""

from typing import Literal, TypeAlias, cast

InferredWorkloadType: TypeAlias = Literal[
    "AmazonEmr",
    "ApacheCassandra",
    "ApacheHadoop",
    "Memcached",
    "Nginx",
    "PostgreSql",
    "Redis",
    "Kafka",
    "SQLServer",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferredWorkloadType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> InferredWorkloadType:
    return cast(InferredWorkloadType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InferredWorkloadType) -> str:
    return value


def deserialize_cbor(data: str) -> InferredWorkloadType:
    return cast(InferredWorkloadType, data)
