"""Generated from Smithy shape ``aws.iam#SdfPartition``."""

from typing import Literal, TypeAlias, cast

"""An AWS partition name."""
SdfPartition: TypeAlias = Literal[
    "pre-prod",
    "aws",
    "aws-cn",
    "aws-us-gov",
    "aws-iso",
    "aws-iso-b",
    "aws-iso-e",
    "aws-iso-f",
    "aws-eusc",
    "aws-iso-g",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SdfPartition) -> str:
    return value


def deserialize_cbor(data: str) -> SdfPartition:
    return cast(SdfPartition, data)
