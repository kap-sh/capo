"""Generated from Smithy shape ``com.amazonaws.controltower#ResetEnabledBaselineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn


class ResetEnabledBaselineInput(TypedDict, closed=True):
    enabled_baseline_identifier: "capo_controltower.types.arn.Arn"
    """<p>Specifies the ID of the <code>EnabledBaseline</code> resource to be re-enabled, in ARN format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResetEnabledBaselineInput) -> dict:
    out: dict = {}
    out["enabledBaselineIdentifier"] = value["enabled_baseline_identifier"]
    return out


def deserialize_json(data: dict) -> ResetEnabledBaselineInput:
    out: ResetEnabledBaselineInput = {}  # type: ignore[typeddict-item]
    if data.get("enabledBaselineIdentifier") is not None:
        out["enabled_baseline_identifier"] = data["enabledBaselineIdentifier"]
    else:
        out["enabled_baseline_identifier"] = ""
    return out
