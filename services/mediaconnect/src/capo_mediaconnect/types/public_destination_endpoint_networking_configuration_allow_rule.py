"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PublicDestinationEndpointNetworkingConfigurationAllowRule``."""

from typing_extensions import TypedDict


class PublicDestinationEndpointNetworkingConfigurationAllowRule(TypedDict, closed=True):
    cidr: "str"
    """<p>The CIDR block that is allowed to connect to the destination endpoint, in CIDR notation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: PublicDestinationEndpointNetworkingConfigurationAllowRule,
) -> dict:
    out: dict = {}
    out["cidr"] = value["cidr"]
    return out


def deserialize_json(
    data: dict,
) -> PublicDestinationEndpointNetworkingConfigurationAllowRule:
    out: PublicDestinationEndpointNetworkingConfigurationAllowRule = {}  # type: ignore[typeddict-item]
    if data.get("cidr") is not None:
        out["cidr"] = data["cidr"]
    else:
        out["cidr"] = ""
    return out
