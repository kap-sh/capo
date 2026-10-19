"""Generated from Smithy shape ``com.amazonaws.connect#Distribution``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.aws_region
    import capo_connect.types.percentage


class Distribution(TypedDict, closed=True):
    region: "capo_connect.types.aws_region.AwsRegion"
    """<p>The Amazon Web Services Region where the traffic is distributed.</p>"""
    percentage: "capo_connect.types.percentage.Percentage"
    """<p>The percentage of the traffic that is distributed, in increments of 10.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Distribution) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    out["Percentage"] = value.get("percentage", 0)
    return out


def deserialize_json(data: dict) -> Distribution:
    out: Distribution = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    if data.get("Percentage") is not None:
        out["percentage"] = data["Percentage"]
    else:
        out["percentage"] = 0
    return out
