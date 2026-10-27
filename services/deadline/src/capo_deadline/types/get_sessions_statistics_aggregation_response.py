"""Generated from Smithy shape ``com.amazonaws.deadline#GetSessionsStatisticsAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.next_token
    import capo_deadline.types.sessions_statistics_aggregation_status
    import capo_deadline.types.statistics_list
    import capo_deadline.types.string


class GetSessionsStatisticsAggregationResponse(TypedDict, closed=True):
    statistics: NotRequired["capo_deadline.types.statistics_list.StatisticsList"]
    """The statistics for the specified fleets or queues."""
    status: "capo_deadline.types.sessions_statistics_aggregation_status.SessionsStatisticsAggregationStatus"
    """The status of the aggregated results. An aggregation may fail or time out if the results are too large. If this happens, you can call the <code>StartSessionsStatisticsAggregation</code> operation after you reduce the aggregation time frame, reduce the number of queues or fleets in the aggregation, or increase the period length. If you call the <code>StartSessionsStatisticsAggregation </code> operation when the status is <code>IN_PROGRESS</code>, you will receive a <code>ThrottlingException</code>."""
    status_message: NotRequired["capo_deadline.types.string.String"]
    """A message that describes the status."""
    next_token: NotRequired["capo_deadline.types.next_token.NextToken"]
    """If Deadline Cloud returns <code>nextToken</code>, then there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. To retrieve the next page, call the operation again using the returned token. Keep all other arguments unchanged. If no results remain, then <code>nextToken</code> is set to <code>null</code>. Each pagination token expires after 24 hours. If you provide a token that isn't valid, then you receive an HTTP 400 <code>ValidationException</code> error."""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionsStatisticsAggregationResponse) -> dict:
    out: dict = {}
    if "statistics" in value:
        import capo_deadline.types.statistics_list

        out["statistics"] = capo_deadline.types.statistics_list.serialize_json(
            value["statistics"]
        )
    import capo_deadline.types.sessions_statistics_aggregation_status

    out["status"] = (
        capo_deadline.types.sessions_statistics_aggregation_status.serialize_json(
            value["status"]
        )
    )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetSessionsStatisticsAggregationResponse:
    out: GetSessionsStatisticsAggregationResponse = {}  # type: ignore[typeddict-item]
    if data.get("statistics") is not None:
        import capo_deadline.types.statistics_list

        out["statistics"] = capo_deadline.types.statistics_list.deserialize_json(
            data["statistics"]
        )
    if data.get("status") is not None:
        import capo_deadline.types.sessions_statistics_aggregation_status

        out["status"] = (
            capo_deadline.types.sessions_statistics_aggregation_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_deadline.types.sessions_statistics_aggregation_status.SessionsStatisticsAggregationStatus",
            "",
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
