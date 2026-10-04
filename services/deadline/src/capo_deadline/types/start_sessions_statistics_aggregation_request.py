"""Generated from Smithy shape ``com.amazonaws.deadline#StartSessionsStatisticsAggregationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.period
    import capo_deadline.types.sessions_statistics_resources
    import capo_deadline.types.timestamp
    import capo_deadline.types.timezone
    import capo_deadline.types.usage_group_by
    import capo_deadline.types.usage_statistics


class StartSessionsStatisticsAggregationRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The identifier of the farm that contains queues or fleets to return statistics for.</p>"""
    resource_ids: (
        "capo_deadline.types.sessions_statistics_resources.SessionsStatisticsResources"
    )
    """<p>A list of fleet IDs or queue IDs to gather statistics for.</p>"""
    start_time: "capo_deadline.types.timestamp.Timestamp"
    """<p>The Linux timestamp of the date and time that the statistics start.</p>"""
    end_time: "capo_deadline.types.timestamp.Timestamp"
    """<p>The Linux timestamp of the date and time that the statistics end.</p>"""
    timezone: NotRequired["capo_deadline.types.timezone.Timezone"]
    """<p>The time zone to use for the statistics. Use UTC notation such as "UTC+8."</p>"""
    period: NotRequired["capo_deadline.types.period.Period"]
    """<p>The period to aggregate the statistics.</p>"""
    group_by: "capo_deadline.types.usage_group_by.UsageGroupBy"
    """<p>The field to use to group the statistics.</p>"""
    statistics: "capo_deadline.types.usage_statistics.UsageStatistics"
    """<p>One to four statistics to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSessionsStatisticsAggregationRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.sessions_statistics_resources

    out["resourceIds"] = (
        capo_deadline.types.sessions_statistics_resources.serialize_json(
            value["resource_ids"]
        )
    )
    import capo_deadline._protocol.serialize

    out["startTime"] = capo_deadline._protocol.serialize.fmt_date_time(
        value["start_time"]
    )
    import capo_deadline._protocol.serialize

    out["endTime"] = capo_deadline._protocol.serialize.fmt_date_time(value["end_time"])
    if "timezone" in value:
        out["timezone"] = value["timezone"]
    if "period" in value:
        import capo_deadline.types.period

        out["period"] = capo_deadline.types.period.serialize_json(value["period"])
    import capo_deadline.types.usage_group_by

    out["groupBy"] = capo_deadline.types.usage_group_by.serialize_json(
        value["group_by"]
    )
    import capo_deadline.types.usage_statistics

    out["statistics"] = capo_deadline.types.usage_statistics.serialize_json(
        value["statistics"]
    )
    return out


def deserialize_json(data: dict) -> StartSessionsStatisticsAggregationRequest:
    out: StartSessionsStatisticsAggregationRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceIds") is not None:
        import capo_deadline.types.sessions_statistics_resources

        out["resource_ids"] = (
            capo_deadline.types.sessions_statistics_resources.deserialize_json(
                data["resourceIds"]
            )
        )
    else:
        raise DeserializationError(
            "StartSessionsStatisticsAggregationRequest.resource_ids required"
        )
    if data.get("startTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["startTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError(
            "StartSessionsStatisticsAggregationRequest.start_time required"
        )
    if data.get("endTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["endTime"].replace("Z", "+00:00")
        )
    else:
        raise DeserializationError(
            "StartSessionsStatisticsAggregationRequest.end_time required"
        )
    if data.get("timezone") is not None:
        out["timezone"] = data["timezone"]
    if data.get("period") is not None:
        import capo_deadline.types.period

        out["period"] = capo_deadline.types.period.deserialize_json(data["period"])
    if data.get("groupBy") is not None:
        import capo_deadline.types.usage_group_by

        out["group_by"] = capo_deadline.types.usage_group_by.deserialize_json(
            data["groupBy"]
        )
    else:
        raise DeserializationError(
            "StartSessionsStatisticsAggregationRequest.group_by required"
        )
    if data.get("statistics") is not None:
        import capo_deadline.types.usage_statistics

        out["statistics"] = capo_deadline.types.usage_statistics.deserialize_json(
            data["statistics"]
        )
    else:
        raise DeserializationError(
            "StartSessionsStatisticsAggregationRequest.statistics required"
        )
    return out
