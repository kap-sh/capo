"""Generated from Smithy shape ``com.amazonaws.workspaces#Application``."""

from typing import Literal, TypeAlias, cast

Application: TypeAlias = Literal[
    "Microsoft_Office_2016",
    "Microsoft_Office_2019",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Application) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Application:
    return cast(Application, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Application) -> str:
    return value


def deserialize_cbor(data: str) -> Application:
    return cast(Application, data)
