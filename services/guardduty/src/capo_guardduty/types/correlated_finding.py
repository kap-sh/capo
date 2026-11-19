"""Generated from Smithy shape ``com.amazonaws.guardduty#CorrelatedFinding``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.correlation_reasons
    import capo_guardduty.types.count
    import capo_guardduty.types.finding_type
    import capo_guardduty.types.related_finding_ids
    import capo_guardduty.types.severity_score
    import capo_guardduty.types.shared_behaviors
    import capo_guardduty.types.shared_resources


class CorrelatedFinding(TypedDict, closed=True):
    finding_type: NotRequired["capo_guardduty.types.finding_type.FindingType"]
    """<p>The finding type of the group.</p>"""
    count: NotRequired["capo_guardduty.types.count.Count"]
    """<p>The number of correlated findings of this type. This value can be greater than the number of IDs in <code>FindingIds</code>.</p>"""
    severity_max: NotRequired["capo_guardduty.types.severity_score.SeverityScore"]
    """<p>The highest severity score among the findings in the group, from 0 to 10.</p>"""
    correlation_reasons: NotRequired[
        "capo_guardduty.types.correlation_reasons.CorrelationReasons"
    ]
    """<p>The reasons why GuardDuty correlated the findings. Possible values are <code>HIGH_SEVERITY</code>, <code>SAME_RESOURCE</code>, and <code>SAME_BEHAVIOR</code>. A value can appear more than once.</p>"""
    finding_ids: NotRequired[
        "capo_guardduty.types.related_finding_ids.RelatedFindingIds"
    ]
    """<p>A sample of the IDs of the findings in the group.</p>"""
    shared_resources: NotRequired[
        "capo_guardduty.types.shared_resources.SharedResources"
    ]
    """<p>The resources that the findings in the group share with the investigated activity.</p>"""
    shared_behaviors: NotRequired[
        "capo_guardduty.types.shared_behaviors.SharedBehaviors"
    ]
    """<p>The behaviors that the findings in the group share with the investigated activity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CorrelatedFinding) -> dict:
    out: dict = {}
    if "finding_type" in value:
        out["findingType"] = value["finding_type"]
    if "count" in value:
        out["count"] = value["count"]
    if "severity_max" in value:
        out["severityMax"] = (
            "NaN"
            if value["severity_max"] != value["severity_max"]
            else "Infinity"
            if value["severity_max"] == float("inf")
            else "-Infinity"
            if value["severity_max"] == float("-inf")
            else value["severity_max"]
        )
    if "correlation_reasons" in value:
        import capo_guardduty.types.correlation_reasons

        out["correlationReasons"] = (
            capo_guardduty.types.correlation_reasons.serialize_json(
                value["correlation_reasons"]
            )
        )
    if "finding_ids" in value:
        import capo_guardduty.types.related_finding_ids

        out["findingIds"] = capo_guardduty.types.related_finding_ids.serialize_json(
            value["finding_ids"]
        )
    if "shared_resources" in value:
        import capo_guardduty.types.shared_resources

        out["sharedResources"] = capo_guardduty.types.shared_resources.serialize_json(
            value["shared_resources"]
        )
    if "shared_behaviors" in value:
        import capo_guardduty.types.shared_behaviors

        out["sharedBehaviors"] = capo_guardduty.types.shared_behaviors.serialize_json(
            value["shared_behaviors"]
        )
    return out


def deserialize_json(data: dict) -> CorrelatedFinding:
    out: CorrelatedFinding = {}  # type: ignore[typeddict-item]
    if data.get("findingType") is not None:
        out["finding_type"] = data["findingType"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    if data.get("severityMax") is not None:
        out["severity_max"] = float(data["severityMax"])
    if data.get("correlationReasons") is not None:
        import capo_guardduty.types.correlation_reasons

        out["correlation_reasons"] = (
            capo_guardduty.types.correlation_reasons.deserialize_json(
                data["correlationReasons"]
            )
        )
    if data.get("findingIds") is not None:
        import capo_guardduty.types.related_finding_ids

        out["finding_ids"] = capo_guardduty.types.related_finding_ids.deserialize_json(
            data["findingIds"]
        )
    if data.get("sharedResources") is not None:
        import capo_guardduty.types.shared_resources

        out["shared_resources"] = (
            capo_guardduty.types.shared_resources.deserialize_json(
                data["sharedResources"]
            )
        )
    if data.get("sharedBehaviors") is not None:
        import capo_guardduty.types.shared_behaviors

        out["shared_behaviors"] = (
            capo_guardduty.types.shared_behaviors.deserialize_json(
                data["sharedBehaviors"]
            )
        )
    return out
