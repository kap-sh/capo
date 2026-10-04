"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationV2Item``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string
    import capo_securityhub.types.remediation_guidance
    import capo_securityhub.types.remediation_outcome
    import capo_securityhub.types.remediation_priority
    import capo_securityhub.types.remediation_resource
    import capo_securityhub.types.remediation_status
    import capo_securityhub.types.remediation_summary_detail
    import capo_securityhub.types.remediation_trait
    import capo_securityhub.types.timestamp


class RemediationV2Item(TypedDict, closed=True):
    target_uid: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The unique identifier (ID) of the remediation target.</p>"""
    outcome: NotRequired[
        "capo_securityhub.types.remediation_outcome.RemediationOutcome"
    ]
    """<p>The outcome of the remediation target's resolution.</p>"""
    priority: NotRequired[
        "capo_securityhub.types.remediation_priority.RemediationPriority"
    ]
    """<p>The remediation target's priority. Valid values are <code>Critical</code>, <code>High</code>, <code>Medium</code>, and <code>Low</code>.</p>"""
    remediation_summary: NotRequired[
        "capo_securityhub.types.remediation_summary_detail.RemediationSummaryDetail"
    ]
    """<p>A summary of the remediation target.</p>"""
    resource: NotRequired[
        "capo_securityhub.types.remediation_resource.RemediationResource"
    ]
    """<p>The remediation target's associated resource.</p>"""
    status: NotRequired["capo_securityhub.types.remediation_status.RemediationStatus"]
    """<p>The current status of the remediation target.</p> <ul> <li> <p> <code>New</code> specifies that the remediation target was newly identified.</p> </li> <li> <p> <code>Updated</code> specifies that the remediation target changed after it was identified.</p> </li> <li> <p> <code>Resolved</code> specifies that the remediation target is no longer present.</p> </li> </ul>"""
    trait: NotRequired["capo_securityhub.types.remediation_trait.RemediationTrait"]
    """<p>The trait associated with the remediation target.</p>"""
    guidance: NotRequired[
        "capo_securityhub.types.remediation_guidance.RemediationGuidance"
    ]
    """<p>The remediation target's guidance. Returned only when <code>ShowGuidance</code> is <code>true</code> in the request.</p>"""
    updated_at: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>The remediation target's last updated timestamp.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationV2Item) -> dict:
    out: dict = {}
    if "target_uid" in value:
        out["TargetUid"] = value["target_uid"]
    if "outcome" in value:
        import capo_securityhub.types.remediation_outcome

        out["Outcome"] = capo_securityhub.types.remediation_outcome.serialize_json(
            value["outcome"]
        )
    if "priority" in value:
        import capo_securityhub.types.remediation_priority

        out["Priority"] = capo_securityhub.types.remediation_priority.serialize_json(
            value["priority"]
        )
    if "remediation_summary" in value:
        import capo_securityhub.types.remediation_summary_detail

        out["RemediationSummary"] = (
            capo_securityhub.types.remediation_summary_detail.serialize_json(
                value["remediation_summary"]
            )
        )
    if "resource" in value:
        import capo_securityhub.types.remediation_resource

        out["Resource"] = capo_securityhub.types.remediation_resource.serialize_json(
            value["resource"]
        )
    if "status" in value:
        import capo_securityhub.types.remediation_status

        out["Status"] = capo_securityhub.types.remediation_status.serialize_json(
            value["status"]
        )
    if "trait" in value:
        import capo_securityhub.types.remediation_trait

        out["Trait"] = capo_securityhub.types.remediation_trait.serialize_json(
            value["trait"]
        )
    if "guidance" in value:
        import capo_securityhub.types.remediation_guidance

        out["Guidance"] = capo_securityhub.types.remediation_guidance.serialize_json(
            value["guidance"]
        )
    if "updated_at" in value:
        import capo_securityhub.types.timestamp

        out["UpdatedAt"] = capo_securityhub.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> RemediationV2Item:
    out: RemediationV2Item = {}  # type: ignore[typeddict-item]
    if data.get("TargetUid") is not None:
        out["target_uid"] = data["TargetUid"]
    if data.get("Outcome") is not None:
        import capo_securityhub.types.remediation_outcome

        out["outcome"] = capo_securityhub.types.remediation_outcome.deserialize_json(
            data["Outcome"]
        )
    if data.get("Priority") is not None:
        import capo_securityhub.types.remediation_priority

        out["priority"] = capo_securityhub.types.remediation_priority.deserialize_json(
            data["Priority"]
        )
    if data.get("RemediationSummary") is not None:
        import capo_securityhub.types.remediation_summary_detail

        out["remediation_summary"] = (
            capo_securityhub.types.remediation_summary_detail.deserialize_json(
                data["RemediationSummary"]
            )
        )
    if data.get("Resource") is not None:
        import capo_securityhub.types.remediation_resource

        out["resource"] = capo_securityhub.types.remediation_resource.deserialize_json(
            data["Resource"]
        )
    if data.get("Status") is not None:
        import capo_securityhub.types.remediation_status

        out["status"] = capo_securityhub.types.remediation_status.deserialize_json(
            data["Status"]
        )
    if data.get("Trait") is not None:
        import capo_securityhub.types.remediation_trait

        out["trait"] = capo_securityhub.types.remediation_trait.deserialize_json(
            data["Trait"]
        )
    if data.get("Guidance") is not None:
        import capo_securityhub.types.remediation_guidance

        out["guidance"] = capo_securityhub.types.remediation_guidance.deserialize_json(
            data["Guidance"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_securityhub.types.timestamp

        out["updated_at"] = capo_securityhub.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
