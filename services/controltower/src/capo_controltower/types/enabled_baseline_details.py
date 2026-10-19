"""Generated from Smithy shape ``com.amazonaws.controltower#EnabledBaselineDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_controltower.errors import DeserializationError

if TYPE_CHECKING:
    import capo_controltower.types.arn
    import capo_controltower.types.enabled_baseline_drift_status_summary
    import capo_controltower.types.enabled_baseline_parameter_summaries
    import capo_controltower.types.enablement_status_summary


class EnabledBaselineDetails(TypedDict, closed=True):
    arn: "capo_controltower.types.arn.Arn"
    """<p>The ARN of the <code>EnabledBaseline</code> resource.</p>"""
    baseline_identifier: "str"
    """<p>The specific <code>Baseline</code> enabled as part of the <code>EnabledBaseline</code> resource.</p>"""
    baseline_version: NotRequired["str"]
    """<p>The enabled version of the <code>Baseline</code>.</p>"""
    drift_status_summary: NotRequired[
        "capo_controltower.types.enabled_baseline_drift_status_summary.EnabledBaselineDriftStatusSummary"
    ]
    """<p>The drift status of the enabled baseline.</p>"""
    target_identifier: "str"
    """<p>The target on which to enable the <code>Baseline</code>.</p>"""
    parent_identifier: NotRequired["capo_controltower.types.arn.Arn"]
    """<p>An ARN that represents the parent <code>EnabledBaseline</code> at the Organizational Unit (OU) level, from which the child <code>EnabledBaseline</code> inherits its configuration. The value is returned by <code>GetEnabledBaseline</code>.</p>"""
    status_summary: (
        "capo_controltower.types.enablement_status_summary.EnablementStatusSummary"
    )
    parameters: NotRequired[
        "capo_controltower.types.enabled_baseline_parameter_summaries.EnabledBaselineParameterSummaries"
    ]
    """<p>Shows the parameters that are applied when enabling this <code>Baseline</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnabledBaselineDetails) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["baselineIdentifier"] = value["baseline_identifier"]
    if "baseline_version" in value:
        out["baselineVersion"] = value["baseline_version"]
    if "drift_status_summary" in value:
        import capo_controltower.types.enabled_baseline_drift_status_summary

        out["driftStatusSummary"] = (
            capo_controltower.types.enabled_baseline_drift_status_summary.serialize_json(
                value["drift_status_summary"]
            )
        )
    out["targetIdentifier"] = value["target_identifier"]
    if "parent_identifier" in value:
        out["parentIdentifier"] = value["parent_identifier"]
    import capo_controltower.types.enablement_status_summary

    out["statusSummary"] = (
        capo_controltower.types.enablement_status_summary.serialize_json(
            value["status_summary"]
        )
    )
    if "parameters" in value:
        import capo_controltower.types.enabled_baseline_parameter_summaries

        out["parameters"] = (
            capo_controltower.types.enabled_baseline_parameter_summaries.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnabledBaselineDetails:
    out: EnabledBaselineDetails = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("baselineIdentifier") is not None:
        out["baseline_identifier"] = data["baselineIdentifier"]
    else:
        out["baseline_identifier"] = ""
    if data.get("baselineVersion") is not None:
        out["baseline_version"] = data["baselineVersion"]
    if data.get("driftStatusSummary") is not None:
        import capo_controltower.types.enabled_baseline_drift_status_summary

        out["drift_status_summary"] = (
            capo_controltower.types.enabled_baseline_drift_status_summary.deserialize_json(
                data["driftStatusSummary"]
            )
        )
    if data.get("targetIdentifier") is not None:
        out["target_identifier"] = data["targetIdentifier"]
    else:
        out["target_identifier"] = ""
    if data.get("parentIdentifier") is not None:
        out["parent_identifier"] = data["parentIdentifier"]
    if data.get("statusSummary") is not None:
        import capo_controltower.types.enablement_status_summary

        out["status_summary"] = (
            capo_controltower.types.enablement_status_summary.deserialize_json(
                data["statusSummary"]
            )
        )
    else:
        raise DeserializationError("EnabledBaselineDetails.status_summary required")
    if data.get("parameters") is not None:
        import capo_controltower.types.enabled_baseline_parameter_summaries

        out["parameters"] = (
            capo_controltower.types.enabled_baseline_parameter_summaries.deserialize_json(
                data["parameters"]
            )
        )
    return out
