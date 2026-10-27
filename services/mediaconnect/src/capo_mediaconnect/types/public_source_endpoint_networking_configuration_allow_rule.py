"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PublicSourceEndpointNetworkingConfigurationAllowRule``."""

from typing_extensions import TypedDict


class PublicSourceEndpointNetworkingConfigurationAllowRule(TypedDict, closed=True):
    cidr: "str"
    """<p>The CIDR block that is allowed to connect to the source endpoint, in CIDR notation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublicSourceEndpointNetworkingConfigurationAllowRule) -> dict:
    out: dict = {}
    out["cidr"] = value["cidr"]
    return out


def deserialize_json(
    data: dict,
) -> PublicSourceEndpointNetworkingConfigurationAllowRule:
    out: PublicSourceEndpointNetworkingConfigurationAllowRule = {}  # type: ignore[typeddict-item]
    if data.get("cidr") is not None:
        out["cidr"] = data["cidr"]
    else:
        out["cidr"] = ""
    return out
