"""Generated from Smithy shape ``com.amazonaws.controltower#GetBaselineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.baseline_arn


class GetBaselineInput(TypedDict, closed=True):
    baseline_identifier: "capo_controltower.types.baseline_arn.BaselineArn"
    """<p>The ARN of the <code>Baseline</code> resource to be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBaselineInput) -> dict:
    out: dict = {}
    out["baselineIdentifier"] = value["baseline_identifier"]
    return out


def deserialize_json(data: dict) -> GetBaselineInput:
    out: GetBaselineInput = {}  # type: ignore[typeddict-item]
    if data.get("baselineIdentifier") is not None:
        out["baseline_identifier"] = data["baselineIdentifier"]
    else:
        out["baseline_identifier"] = ""
    return out
