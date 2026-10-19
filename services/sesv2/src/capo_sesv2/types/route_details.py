"""Generated from Smithy shape ``com.amazonaws.sesv2#RouteDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.region


class RouteDetails(TypedDict, closed=True):
    region: "capo_sesv2.types.region.Region"
    """<p>The name of an AWS-Region to be a secondary region for the multi-region endpoint (global-endpoint).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteDetails) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> RouteDetails:
    out: RouteDetails = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    return out
