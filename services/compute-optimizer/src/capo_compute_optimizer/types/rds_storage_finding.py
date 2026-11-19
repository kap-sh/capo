"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSStorageFinding``."""

from typing import Literal, TypeAlias, cast

RDSStorageFinding: TypeAlias = Literal[
    "Optimized",
    "Underprovisioned",
    "Overprovisioned",
    "NotOptimized",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSStorageFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSStorageFinding:
    return cast(RDSStorageFinding, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RDSStorageFinding) -> str:
    return value


def deserialize_cbor(data: str) -> RDSStorageFinding:
    return cast(RDSStorageFinding, data)
