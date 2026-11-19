"""Generated from Smithy shape ``com.amazonaws.appstream#ScreenResolution``."""

from typing import Literal, TypeAlias, cast

"""<p>The screen resolution for the agent streaming environment.</p> <ul> <li> <p>W_1280xH_720 - 1280 x 720 pixels.</p> </li> </ul>"""
ScreenResolution: TypeAlias = Literal["W_1280xH_720",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScreenResolution) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScreenResolution:
    return cast(ScreenResolution, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScreenResolution) -> str:
    return value


def deserialize_cbor(data: str) -> ScreenResolution:
    return cast(ScreenResolution, data)
