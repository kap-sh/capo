"""Generated from Smithy shape ``com.amazonaws.connect#SignInDistribution``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.aws_region
    import capo_connect.types.boolean


class SignInDistribution(TypedDict, closed=True):
    region: "capo_connect.types.aws_region.AwsRegion"
    """<p>The Amazon Web Services Region of the sign in distribution.</p>"""
    enabled: "capo_connect.types.boolean.Boolean"
    """<p>Whether sign in distribution is enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignInDistribution) -> dict:
    out: dict = {}
    out["Region"] = value["region"]
    out["Enabled"] = value.get("enabled", False)
    return out


def deserialize_json(data: dict) -> SignInDistribution:
    out: SignInDistribution = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    return out
