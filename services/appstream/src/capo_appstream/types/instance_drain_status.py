"""Generated from Smithy shape ``com.amazonaws.appstream#InstanceDrainStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>Possible values for the drain status of a streaming instance.</p>"""
InstanceDrainStatus: TypeAlias = Literal[
    "ACTIVE",
    "DRAINING",
    "NOT_APPLICABLE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceDrainStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InstanceDrainStatus:
    return cast(InstanceDrainStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InstanceDrainStatus) -> str:
    return value


def deserialize_cbor(data: str) -> InstanceDrainStatus:
    return cast(InstanceDrainStatus, data)
