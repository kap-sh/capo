"""Generated from Smithy shape ``com.amazonaws.codedeploy#ApplicationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.application_name

ApplicationsList: TypeAlias = list[
    "capo_codedeploy.types.application_name.ApplicationName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ApplicationsList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApplicationsList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> ApplicationsList:
    return [item for item in data if item is not None]
