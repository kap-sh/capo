"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PublicRouterNetworkInterfaceRule``."""

from typing_extensions import TypedDict


class PublicRouterNetworkInterfaceRule(TypedDict, closed=True):
    cidr: "str"
    """<p>The CIDR block that is allowed to access the public router network interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublicRouterNetworkInterfaceRule) -> dict:
    out: dict = {}
    out["cidr"] = value["cidr"]
    return out


def deserialize_json(data: dict) -> PublicRouterNetworkInterfaceRule:
    out: PublicRouterNetworkInterfaceRule = {}  # type: ignore[typeddict-item]
    if data.get("cidr") is not None:
        out["cidr"] = data["cidr"]
    else:
        out["cidr"] = ""
    return out
