"""Generated from Smithy shape ``com.amazonaws.directconnect#RouteFilterPrefix``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.cidr


class RouteFilterPrefix(TypedDict, closed=True):
    cidr: NotRequired["capo_direct_connect.types.cidr.CIDR"]
    """<p>The CIDR block for the advertised route. Separate multiple routes using commas. An IPv6 CIDR must use /64 or shorter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RouteFilterPrefix) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RouteFilterPrefix:
    out: RouteFilterPrefix = {}  # type: ignore[typeddict-item]
    if data.get("cidr") is not None:
        out["cidr"] = data["cidr"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RouteFilterPrefix) -> dict:
    out: dict = {}
    if "cidr" in value:
        out["cidr"] = value["cidr"]
    return out


def deserialize_cbor(data: dict) -> RouteFilterPrefix:
    out: RouteFilterPrefix = {}  # type: ignore[typeddict-item]
    if data.get("cidr") is not None:
        out["cidr"] = data["cidr"]
    return out
