"""Generated from Smithy shape ``com.amazonaws.interconnect#EnvironmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_interconnect.types.environment

EnvironmentList: TypeAlias = list["capo_interconnect.types.environment.Environment"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentList) -> list:
    import capo_interconnect.types.environment

    out: list = []
    for item in value:
        out.append(capo_interconnect.types.environment.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> EnvironmentList:
    import capo_interconnect.types.environment

    out: EnvironmentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_interconnect.types.environment.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnvironmentList) -> list:
    import capo_interconnect.types.environment

    out: list = []
    for item in value:
        out.append(capo_interconnect.types.environment.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> EnvironmentList:
    import capo_interconnect.types.environment

    out: EnvironmentList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_interconnect.types.environment.deserialize_cbor(item))
    return out
