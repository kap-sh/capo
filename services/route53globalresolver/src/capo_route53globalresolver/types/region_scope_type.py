"""Generated from Smithy shape ``com.amazonaws.route53globalresolver#RegionScopeType``."""

from typing import Literal, TypeAlias, cast

"""<p>Indicates the scope of Amazon Web Services Regions that a DNS IP address of a core network endpoint applies to. Valid values are the following:</p> <ul> <li> <p> <code>ALL</code> - The IP address applies to all Amazon Web Services Regions in which the core network endpoint is available.</p> </li> <li> <p> <code>REGIONAL</code> - The IP address applies only to the specific Amazon Web Services Regions that you identify in the <code>regions</code> field.</p> </li> </ul>"""
RegionScopeType: TypeAlias = Literal[
    "ALL",
    "REGIONAL",
]


# --- restJson1 ser/de ---
def serialize_json(value: RegionScopeType) -> str:
    return value


def deserialize_json(data: str) -> RegionScopeType:
    return cast(RegionScopeType, data)
