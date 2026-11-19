"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeploymentStatusMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.error_message

DeploymentStatusMessageList: TypeAlias = list[
    "capo_codedeploy.types.error_message.ErrorMessage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeploymentStatusMessageList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DeploymentStatusMessageList:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeploymentStatusMessageList) -> list:
    return list(value)


def deserialize_cbor(data: list) -> DeploymentStatusMessageList:
    return [item for item in data if item is not None]
