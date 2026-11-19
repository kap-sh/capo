"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#AmdSevSnpEnum``."""

from typing import Literal, TypeAlias, cast

AmdSevSnpEnum: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AmdSevSnpEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AmdSevSnpEnum:
    return cast(AmdSevSnpEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AmdSevSnpEnum) -> str:
    return value


def deserialize_cbor(data: str) -> AmdSevSnpEnum:
    return cast(AmdSevSnpEnum, data)
