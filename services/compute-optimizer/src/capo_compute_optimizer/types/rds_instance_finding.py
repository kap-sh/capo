"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RDSInstanceFinding``."""

from typing import Literal, TypeAlias, cast

RDSInstanceFinding: TypeAlias = Literal[
    "Optimized",
    "Underprovisioned",
    "Overprovisioned",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RDSInstanceFinding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RDSInstanceFinding:
    return cast(RDSInstanceFinding, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RDSInstanceFinding) -> str:
    return value


def deserialize_cbor(data: str) -> RDSInstanceFinding:
    return cast(RDSInstanceFinding, data)
