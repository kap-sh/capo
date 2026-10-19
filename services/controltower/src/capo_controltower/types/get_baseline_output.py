"""Generated from Smithy shape ``com.amazonaws.controltower#GetBaselineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.baseline_arn


class GetBaselineOutput(TypedDict, closed=True):
    arn: "capo_controltower.types.baseline_arn.BaselineArn"
    """<p>The baseline ARN.</p>"""
    name: "str"
    """<p>A user-friendly name for the baseline.</p>"""
    description: NotRequired["str"]
    """<p>A description of the baseline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBaselineOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> GetBaselineOutput:
    out: GetBaselineOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
