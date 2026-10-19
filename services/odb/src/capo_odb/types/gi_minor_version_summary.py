"""Generated from Smithy shape ``com.amazonaws.odb#GiMinorVersionSummary``."""

from typing_extensions import NotRequired, TypedDict


class GiMinorVersionSummary(TypedDict, closed=True):
    version: "str"
    """<p>The GI minor version.</p>"""
    grid_image_id: NotRequired["str"]
    """<p>The Grid Infrastructure software image ID for this minor version.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GiMinorVersionSummary) -> dict:
    out: dict = {}
    out["version"] = value["version"]
    if "grid_image_id" in value:
        out["gridImageId"] = value["grid_image_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GiMinorVersionSummary:
    out: GiMinorVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("gridImageId") is not None:
        out["grid_image_id"] = data["gridImageId"]
    return out
