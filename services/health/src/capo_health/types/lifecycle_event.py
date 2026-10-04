"""Generated from Smithy shape ``com.amazonaws.health#LifecycleEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_health.types.impact_risk_list
    import capo_health.types.region_list
    import capo_health.types.string
    import capo_health.types.timestamp


class LifecycleEvent(TypedDict, closed=True):
    lifecycle_event_type: NotRequired["capo_health.types.string.string"]
    """<p>The type of lifecycle event (for example, end-of-support, end-of-life).</p>"""
    date: NotRequired["capo_health.types.timestamp.timestamp"]
    """<p>The date of the lifecycle event.</p>"""
    regions: NotRequired["capo_health.types.region_list.regionList"]
    """<p>The Amazon Web Services Regions affected by this lifecycle event.</p>"""
    impact_risks: NotRequired["capo_health.types.impact_risk_list.ImpactRiskList"]
    """<p>The potential impact risks associated with this lifecycle event.</p>"""
    description: NotRequired["capo_health.types.string.string"]
    """<p>A description of the lifecycle event.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LifecycleEvent) -> dict:
    out: dict = {}
    if "lifecycle_event_type" in value:
        out["lifecycleEventType"] = value["lifecycle_event_type"]
    if "date" in value:
        import capo_health.types.timestamp

        out["date"] = capo_health.types.timestamp.serialize_aws_json_1_1(value["date"])
    if "regions" in value:
        import capo_health.types.region_list

        out["regions"] = capo_health.types.region_list.serialize_aws_json_1_1(
            value["regions"]
        )
    if "impact_risks" in value:
        import capo_health.types.impact_risk_list

        out["impactRisks"] = capo_health.types.impact_risk_list.serialize_aws_json_1_1(
            value["impact_risks"]
        )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LifecycleEvent:
    out: LifecycleEvent = {}  # type: ignore[typeddict-item]
    if data.get("lifecycleEventType") is not None:
        out["lifecycle_event_type"] = data["lifecycleEventType"]
    if data.get("date") is not None:
        import capo_health.types.timestamp

        out["date"] = capo_health.types.timestamp.deserialize_aws_json_1_1(data["date"])
    if data.get("regions") is not None:
        import capo_health.types.region_list

        out["regions"] = capo_health.types.region_list.deserialize_aws_json_1_1(
            data["regions"]
        )
    if data.get("impactRisks") is not None:
        import capo_health.types.impact_risk_list

        out["impact_risks"] = (
            capo_health.types.impact_risk_list.deserialize_aws_json_1_1(
                data["impactRisks"]
            )
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
