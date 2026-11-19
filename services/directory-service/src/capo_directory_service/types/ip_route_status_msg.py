"""Generated from Smithy shape ``com.amazonaws.directoryservice#IpRouteStatusMsg``."""

from typing import Literal, TypeAlias, cast

IpRouteStatusMsg: TypeAlias = Literal[
    "Adding",
    "Added",
    "Removing",
    "Removed",
    "AddFailed",
    "RemoveFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRouteStatusMsg) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IpRouteStatusMsg:
    return cast(IpRouteStatusMsg, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IpRouteStatusMsg) -> str:
    return value


def deserialize_cbor(data: str) -> IpRouteStatusMsg:
    return cast(IpRouteStatusMsg, data)
