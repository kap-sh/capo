"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledControlDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.control_identifier
    import capo_controltower.types.drift_status_summary
    import capo_controltower.types.enabled_control_parameter_summaries
    import capo_controltower.types.enablement_status_summary
    import capo_controltower.types.parent_identifier
    import capo_controltower.types.target_identifier
    import capo_controltower.types.target_regions


class EnabledControlDetails(TypedDict, closed=True):
    arn: NotRequired["capo_controltower.types.arn.Arn"]
    """<p>The ARN of the enabled control.</p>"""
    control_identifier: NotRequired[
        "capo_controltower.types.control_identifier.ControlIdentifier"
    ]
    """<p>The control identifier of the enabled control. For information on how to find the <code>controlIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>"""
    target_identifier: NotRequired[
        "capo_controltower.types.target_identifier.TargetIdentifier"
    ]
    """<p>The ARN of the organizational unit. For information on how to find the <code>targetIdentifier</code>, see <a href="https://docs.aws.amazon.com/controltower/latest/APIReference/Welcome.html">the overview page</a>.</p>"""
    status_summary: NotRequired[
        "capo_controltower.types.enablement_status_summary.EnablementStatusSummary"
    ]
    """<p>The deployment summary of the enabled control.</p>"""
    drift_status_summary: NotRequired[
        "capo_controltower.types.drift_status_summary.DriftStatusSummary"
    ]
    """<p>The drift status of the enabled control.</p>"""
    parent_identifier: NotRequired[
        "capo_controltower.types.parent_identifier.ParentIdentifier"
    ]
    """<p>The ARN of the parent enabled control from which this control inherits its configuration, if applicable.</p>"""
    target_regions: NotRequired["capo_controltower.types.target_regions.TargetRegions"]
    """<p>Target Amazon Web Services Regions for the enabled control.</p>"""
    parameters: NotRequired[
        "capo_controltower.types.enabled_control_parameter_summaries.EnabledControlParameterSummaries"
    ]
    """<p>Array of <code>EnabledControlParameter</code> objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledControlDetails) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "control_identifier" in value:
        out["controlIdentifier"] = value["control_identifier"]
    if "target_identifier" in value:
        out["targetIdentifier"] = value["target_identifier"]
    if "status_summary" in value:
        import capo_controltower.types.enablement_status_summary

        out["statusSummary"] = (
            capo_controltower.types.enablement_status_summary.serialize_json(
                value["status_summary"]
            )
        )
    if "drift_status_summary" in value:
        import capo_controltower.types.drift_status_summary

        out["driftStatusSummary"] = (
            capo_controltower.types.drift_status_summary.serialize_json(
                value["drift_status_summary"]
            )
        )
    if "parent_identifier" in value:
        out["parentIdentifier"] = value["parent_identifier"]
    if "target_regions" in value:
        import capo_controltower.types.target_regions

        out["targetRegions"] = capo_controltower.types.target_regions.serialize_json(
            value["target_regions"]
        )
    if "parameters" in value:
        import capo_controltower.types.enabled_control_parameter_summaries

        out["parameters"] = (
            capo_controltower.types.enabled_control_parameter_summaries.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnabledControlDetails:
    out: EnabledControlDetails = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("controlIdentifier") is not None:
        out["control_identifier"] = data["controlIdentifier"]
    if data.get("targetIdentifier") is not None:
        out["target_identifier"] = data["targetIdentifier"]
    if data.get("statusSummary") is not None:
        import capo_controltower.types.enablement_status_summary

        out["status_summary"] = (
            capo_controltower.types.enablement_status_summary.deserialize_json(
                data["statusSummary"]
            )
        )
    if data.get("driftStatusSummary") is not None:
        import capo_controltower.types.drift_status_summary

        out["drift_status_summary"] = (
            capo_controltower.types.drift_status_summary.deserialize_json(
                data["driftStatusSummary"]
            )
        )
    if data.get("parentIdentifier") is not None:
        out["parent_identifier"] = data["parentIdentifier"]
    if data.get("targetRegions") is not None:
        import capo_controltower.types.target_regions

        out["target_regions"] = capo_controltower.types.target_regions.deserialize_json(
            data["targetRegions"]
        )
    if data.get("parameters") is not None:
        import capo_controltower.types.enabled_control_parameter_summaries

        out["parameters"] = (
            capo_controltower.types.enabled_control_parameter_summaries.deserialize_json(
                data["parameters"]
            )
        )
    return out
