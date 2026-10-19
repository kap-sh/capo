"""Generated from Smithy shape ``com.amazonaws.internetmonitor#HealthEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_internetmonitor.types.arn
    import capo_internetmonitor.types.health_event_impact_type
    import capo_internetmonitor.types.health_event_name
    import capo_internetmonitor.types.health_event_status
    import capo_internetmonitor.types.impacted_locations_list
    import capo_internetmonitor.types.percentage


class HealthEvent(TypedDict, closed=True):
    event_arn: "capo_internetmonitor.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the event.</p>"""
    event_id: "capo_internetmonitor.types.health_event_name.HealthEventName"
    """<p>The internally-generated identifier of a specific network traffic impairment health event.</p>"""
    started_at: "datetime.datetime"
    """<p>When a health event started.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time when a health event ended. If the health event is still active, then the end time is not set.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>When the health event was created.</p>"""
    last_updated_at: "datetime.datetime"
    """<p>When the health event was last updated.</p>"""
    impacted_locations: (
        "capo_internetmonitor.types.impacted_locations_list.ImpactedLocationsList"
    )
    """<p>The locations impacted by the health event.</p>"""
    status: "capo_internetmonitor.types.health_event_status.HealthEventStatus"
    """<p>The status of a health event.</p>"""
    percent_of_total_traffic_impacted: NotRequired["float"]
    """<p>The impact on total traffic that a health event has, in increased latency or reduced availability. This is the percentage of how much latency has increased or availability has decreased during the event, compared to what is typical for traffic from this client location to the Amazon Web Services location using this client network.</p>"""
    impact_type: (
        "capo_internetmonitor.types.health_event_impact_type.HealthEventImpactType"
    )
    """<p>The type of impairment for a health event.</p>"""
    health_score_threshold: "capo_internetmonitor.types.percentage.Percentage"
    """<p>The value of the threshold percentage for performance or availability that was configured when Amazon CloudWatch Internet Monitor created the health event.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HealthEvent) -> dict:
    out: dict = {}
    out["EventArn"] = value["event_arn"]
    out["EventId"] = value["event_id"]
    import capo_internetmonitor._protocol.serialize

    out["StartedAt"] = capo_internetmonitor._protocol.serialize.fmt_date_time(
        value["started_at"]
    )
    if "ended_at" in value:
        import capo_internetmonitor._protocol.serialize

        out["EndedAt"] = capo_internetmonitor._protocol.serialize.fmt_date_time(
            value["ended_at"]
        )
    if "created_at" in value:
        import capo_internetmonitor._protocol.serialize

        out["CreatedAt"] = capo_internetmonitor._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    import capo_internetmonitor._protocol.serialize

    out["LastUpdatedAt"] = capo_internetmonitor._protocol.serialize.fmt_date_time(
        value["last_updated_at"]
    )
    import capo_internetmonitor.types.impacted_locations_list

    out["ImpactedLocations"] = (
        capo_internetmonitor.types.impacted_locations_list.serialize_json(
            value["impacted_locations"]
        )
    )
    out["Status"] = value["status"]
    if "percent_of_total_traffic_impacted" in value:
        out["PercentOfTotalTrafficImpacted"] = (
            "NaN"
            if value["percent_of_total_traffic_impacted"]
            != value["percent_of_total_traffic_impacted"]
            else "Infinity"
            if value["percent_of_total_traffic_impacted"] == float("inf")
            else "-Infinity"
            if value["percent_of_total_traffic_impacted"] == float("-inf")
            else value["percent_of_total_traffic_impacted"]
        )
    out["ImpactType"] = value["impact_type"]
    out["HealthScoreThreshold"] = (
        "NaN"
        if value.get("health_score_threshold", 0)
        != value.get("health_score_threshold", 0)
        else "Infinity"
        if value.get("health_score_threshold", 0) == float("inf")
        else "-Infinity"
        if value.get("health_score_threshold", 0) == float("-inf")
        else value.get("health_score_threshold", 0)
    )
    return out


def deserialize_json(data: dict) -> HealthEvent:
    out: HealthEvent = {}  # type: ignore[typeddict-item]
    if data.get("EventArn") is not None:
        out["event_arn"] = data["EventArn"]
    else:
        out["event_arn"] = ""
    if data.get("EventId") is not None:
        out["event_id"] = data["EventId"]
    else:
        out["event_id"] = ""
    if data.get("StartedAt") is not None:
        import datetime

        out["started_at"] = datetime.datetime.fromisoformat(
            data["StartedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndedAt") is not None:
        import datetime

        out["ended_at"] = datetime.datetime.fromisoformat(
            data["EndedAt"].replace("Z", "+00:00")
        )
    if data.get("CreatedAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["CreatedAt"].replace("Z", "+00:00")
        )
    if data.get("LastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["LastUpdatedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ImpactedLocations") is not None:
        import capo_internetmonitor.types.impacted_locations_list

        out["impacted_locations"] = (
            capo_internetmonitor.types.impacted_locations_list.deserialize_json(
                data["ImpactedLocations"]
            )
        )
    else:
        out["impacted_locations"] = []
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("PercentOfTotalTrafficImpacted") is not None:
        out["percent_of_total_traffic_impacted"] = float(
            data["PercentOfTotalTrafficImpacted"]
        )
    if data.get("ImpactType") is not None:
        out["impact_type"] = data["ImpactType"]
    else:
        out["impact_type"] = ""
    if data.get("HealthScoreThreshold") is not None:
        out["health_score_threshold"] = float(data["HealthScoreThreshold"])
    else:
        out["health_score_threshold"] = 0
    return out
