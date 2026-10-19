"""Generated from Smithy shape ``com.amazonaws.controltower#UpdateEnabledBaselineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.baseline_version
    import capo_controltower.types.enabled_baseline_parameters


class UpdateEnabledBaselineInput(TypedDict, closed=True):
    baseline_version: "capo_controltower.types.baseline_version.BaselineVersion"
    """<p>Specifies the new <code>Baseline</code> version, to which the <code>EnabledBaseline</code> should be updated.</p>"""
    parameters: NotRequired[
        "capo_controltower.types.enabled_baseline_parameters.EnabledBaselineParameters"
    ]
    """<p>Parameters to apply when making an update.</p>"""
    enabled_baseline_identifier: "capo_controltower.types.arn.Arn"
    """<p>Specifies the <code>EnabledBaseline</code> resource to be updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEnabledBaselineInput) -> dict:
    out: dict = {}
    out["baselineVersion"] = value["baseline_version"]
    if "parameters" in value:
        import capo_controltower.types.enabled_baseline_parameters

        out["parameters"] = (
            capo_controltower.types.enabled_baseline_parameters.serialize_json(
                value["parameters"]
            )
        )
    out["enabledBaselineIdentifier"] = value["enabled_baseline_identifier"]
    return out


def deserialize_json(data: dict) -> UpdateEnabledBaselineInput:
    out: UpdateEnabledBaselineInput = {}  # type: ignore[typeddict-item]
    if data.get("baselineVersion") is not None:
        out["baseline_version"] = data["baselineVersion"]
    else:
        out["baseline_version"] = ""
    if data.get("parameters") is not None:
        import capo_controltower.types.enabled_baseline_parameters

        out["parameters"] = (
            capo_controltower.types.enabled_baseline_parameters.deserialize_json(
                data["parameters"]
            )
        )
    if data.get("enabledBaselineIdentifier") is not None:
        out["enabled_baseline_identifier"] = data["enabledBaselineIdentifier"]
    else:
        out["enabled_baseline_identifier"] = ""
    return out
