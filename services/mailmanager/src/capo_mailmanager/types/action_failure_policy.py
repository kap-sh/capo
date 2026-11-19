"""Generated from Smithy shape ``com.amazonaws.mailmanager#ActionFailurePolicy``."""

from typing import Literal, TypeAlias, cast

ActionFailurePolicy: TypeAlias = Literal[
    "CONTINUE",
    "DROP",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionFailurePolicy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ActionFailurePolicy:
    return cast(ActionFailurePolicy, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionFailurePolicy) -> str:
    return value


def deserialize_cbor(data: str) -> ActionFailurePolicy:
    return cast(ActionFailurePolicy, data)
