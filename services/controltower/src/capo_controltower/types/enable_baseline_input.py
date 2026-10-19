"""Generated from Smithy shape ``com.amazonaws.controltower#EnableBaselineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.baseline_version
    import capo_controltower.types.enabled_baseline_parameters
    import capo_controltower.types.tag_map


class EnableBaselineInput(TypedDict, closed=True):
    baseline_version: "capo_controltower.types.baseline_version.BaselineVersion"
    """<p>The specific version to be enabled of the specified baseline.</p>"""
    parameters: NotRequired[
        "capo_controltower.types.enabled_baseline_parameters.EnabledBaselineParameters"
    ]
    """<p>A list of <code>key-value</code> objects that specify enablement parameters, where <code>key</code> is a string and <code>value</code> is a document of any type.</p>"""
    baseline_identifier: "capo_controltower.types.arn.Arn"
    """<p>The ARN of the baseline to be enabled.</p>"""
    target_identifier: "capo_controltower.types.arn.Arn"
    """<p>The ARN of the target on which the baseline will be enabled. Only OUs are supported as targets.</p>"""
    tags: NotRequired["capo_controltower.types.tag_map.TagMap"]
    """<p>Tags associated with input to <code>EnableBaseline</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableBaselineInput) -> dict:
    out: dict = {}
    out["baselineVersion"] = value["baseline_version"]
    if "parameters" in value:
        import capo_controltower.types.enabled_baseline_parameters

        out["parameters"] = (
            capo_controltower.types.enabled_baseline_parameters.serialize_json(
                value["parameters"]
            )
        )
    out["baselineIdentifier"] = value["baseline_identifier"]
    out["targetIdentifier"] = value["target_identifier"]
    if "tags" in value:
        import capo_controltower.types.tag_map

        out["tags"] = capo_controltower.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> EnableBaselineInput:
    out: EnableBaselineInput = {}  # type: ignore[typeddict-item]
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
    if data.get("baselineIdentifier") is not None:
        out["baseline_identifier"] = data["baselineIdentifier"]
    else:
        out["baseline_identifier"] = ""
    if data.get("targetIdentifier") is not None:
        out["target_identifier"] = data["targetIdentifier"]
    else:
        out["target_identifier"] = ""
    if data.get("tags") is not None:
        import capo_controltower.types.tag_map

        out["tags"] = capo_controltower.types.tag_map.deserialize_json(data["tags"])
    return out
