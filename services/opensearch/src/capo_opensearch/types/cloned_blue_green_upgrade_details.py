"""Generated from Smithy shape ``com.amazonaws.opensearch#ClonedBlueGreenUpgradeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.cloned_blue_green_scheduled_action
    import capo_opensearch.types.integer_class
    import capo_opensearch.types.traffic_percents


class ClonedBlueGreenUpgradeDetails(TypedDict, closed=True):
    traffic_split: NotRequired["capo_opensearch.types.traffic_percents.TrafficPercents"]
    """<p>The current split of search traffic between the primary and cloned clusters.</p>"""
    scheduled_action: NotRequired[
        "capo_opensearch.types.cloned_blue_green_scheduled_action.ClonedBlueGreenScheduledAction"
    ]
    """<p>The action that the service takes automatically if you don't act before the scheduled time.</p>"""
    retention_in_hours: NotRequired["capo_opensearch.types.integer_class.IntegerClass"]
    """<p>The retention period, in hours, for the cluster that you cut over from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClonedBlueGreenUpgradeDetails) -> dict:
    out: dict = {}
    if "traffic_split" in value:
        import capo_opensearch.types.traffic_percents

        out["TrafficSplit"] = capo_opensearch.types.traffic_percents.serialize_json(
            value["traffic_split"]
        )
    if "scheduled_action" in value:
        import capo_opensearch.types.cloned_blue_green_scheduled_action

        out["ScheduledAction"] = (
            capo_opensearch.types.cloned_blue_green_scheduled_action.serialize_json(
                value["scheduled_action"]
            )
        )
    if "retention_in_hours" in value:
        out["RetentionInHours"] = value["retention_in_hours"]
    return out


def deserialize_json(data: dict) -> ClonedBlueGreenUpgradeDetails:
    out: ClonedBlueGreenUpgradeDetails = {}  # type: ignore[typeddict-item]
    if data.get("TrafficSplit") is not None:
        import capo_opensearch.types.traffic_percents

        out["traffic_split"] = capo_opensearch.types.traffic_percents.deserialize_json(
            data["TrafficSplit"]
        )
    if data.get("ScheduledAction") is not None:
        import capo_opensearch.types.cloned_blue_green_scheduled_action

        out["scheduled_action"] = (
            capo_opensearch.types.cloned_blue_green_scheduled_action.deserialize_json(
                data["ScheduledAction"]
            )
        )
    if data.get("RetentionInHours") is not None:
        out["retention_in_hours"] = data["RetentionInHours"]
    return out
