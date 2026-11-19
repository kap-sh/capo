"""Generated from Smithy shape ``com.amazonaws.gamelift#UDPEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.positive_integer


class UDPEndpoint(TypedDict, closed=True):
    domain: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>The domain name of the UDP endpoint.</p>"""
    port: NotRequired["capo_gamelift.types.positive_integer.PositiveInteger"]
    """<p>The port number of the UDP endpoint. For Amazon GameLift Servers ping beacons, this is typically port 7770.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UDPEndpoint) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "port" in value:
        out["Port"] = value["port"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UDPEndpoint:
    out: UDPEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UDPEndpoint) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "port" in value:
        out["Port"] = value["port"]
    return out


def deserialize_cbor(data: dict) -> UDPEndpoint:
    out: UDPEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    return out
