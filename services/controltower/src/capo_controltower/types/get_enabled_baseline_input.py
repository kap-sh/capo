"""Generated from Smithy shape ``com.amazonaws.controltower#GetEnabledBaselineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn


class GetEnabledBaselineInput(TypedDict, closed=True):
    enabled_baseline_identifier: "capo_controltower.types.arn.Arn"
    """<p>Identifier of the <code>EnabledBaseline</code> resource to be retrieved, in ARN format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnabledBaselineInput) -> dict:
    out: dict = {}
    out["enabledBaselineIdentifier"] = value["enabled_baseline_identifier"]
    return out


def deserialize_json(data: dict) -> GetEnabledBaselineInput:
    out: GetEnabledBaselineInput = {}  # type: ignore[typeddict-item]
    if data.get("enabledBaselineIdentifier") is not None:
        out["enabled_baseline_identifier"] = data["enabledBaselineIdentifier"]
    else:
        out["enabled_baseline_identifier"] = ""
    return out
