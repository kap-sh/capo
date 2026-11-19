"""Generated from Smithy shape ``com.amazonaws.codedeploy#RegistrationStatus``."""

from typing import Literal, TypeAlias, cast

RegistrationStatus: TypeAlias = Literal[
    "Registered",
    "Deregistered",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegistrationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RegistrationStatus:
    return cast(RegistrationStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegistrationStatus) -> str:
    return value


def deserialize_cbor(data: str) -> RegistrationStatus:
    return cast(RegistrationStatus, data)
