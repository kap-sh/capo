"""Generated from Smithy shape ``com.amazonaws.acmpca#ActionType``."""

from typing import Literal, TypeAlias, cast

ActionType: TypeAlias = Literal[
    "IssueCertificate",
    "GetCertificate",
    "ListPermissions",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionType:
    return cast(ActionType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionType) -> str:
    return value


def deserialize_cbor(data: str) -> ActionType:
    return cast(ActionType, data)
