"""Generated from Smithy shape ``com.amazonaws.workspaces#Compute``."""

from typing import Literal, TypeAlias, cast

Compute: TypeAlias = Literal[
    "VALUE",
    "STANDARD",
    "PERFORMANCE",
    "POWER",
    "GRAPHICS",
    "POWERPRO",
    "GENERALPURPOSE_4XLARGE",
    "GENERALPURPOSE_8XLARGE",
    "GRAPHICSPRO",
    "GRAPHICS_G4DN",
    "GRAPHICSPRO_G4DN",
    "GRAPHICS_G6_XLARGE",
    "GRAPHICS_G6_2XLARGE",
    "GRAPHICS_G6_4XLARGE",
    "GRAPHICS_G6_8XLARGE",
    "GRAPHICS_G6_16XLARGE",
    "GRAPHICS_GR6_4XLARGE",
    "GRAPHICS_GR6_8XLARGE",
    "GRAPHICS_G6F_LARGE",
    "GRAPHICS_G6F_XLARGE",
    "GRAPHICS_G6F_2XLARGE",
    "GRAPHICS_G6F_4XLARGE",
    "GRAPHICS_GR6F_4XLARGE",
    "GRAPHICS_G7_2XLARGE",
    "GRAPHICS_G7_4XLARGE",
    "GRAPHICS_G7_8XLARGE",
    "GRAPHICS_G7_12XLARGE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Compute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Compute:
    return cast(Compute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Compute) -> str:
    return value


def deserialize_cbor(data: str) -> Compute:
    return cast(Compute, data)
