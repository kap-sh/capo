"""Generated from Smithy shape ``com.amazonaws.connect#GetMetricDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.filters
    import capo_connect.types.groupings
    import capo_connect.types.historical_metrics
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.next_token
    import capo_connect.types.timestamp


class GetMetricDataRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    start_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp, in UNIX Epoch time format, at which to start the reporting interval for the retrieval of historical metrics data. The time must be specified using a multiple of 5 minutes, such as 10:05, 10:10, 10:15.</p> <p>The start time cannot be earlier than 24 hours before the time of the request. Historical metrics are available only for 24 hours.</p>"""
    end_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp, in UNIX Epoch time format, at which to end the reporting interval for the retrieval of historical metrics data. The time must be specified using an interval of 5 minutes, such as 11:00, 11:05, 11:10, and must be later than the start time timestamp.</p> <p>The time range between the start and end time must be less than 24 hours.</p>"""
    filters: "capo_connect.types.filters.Filters"
    """<p>The queues, up to 100, or channels, to use to filter the metrics returned. Metric data is retrieved only for the resources associated with the queues or channels included in the filter. You can include both queue IDs and queue ARNs in the same request. VOICE, CHAT, and TASK channels are supported.</p> <p>RoutingStepExpression is not a valid filter for GetMetricData and we recommend switching to GetMetricDataV2 for more up-to-date features.</p> <note> <p>To filter by <code>Queues</code>, enter the queue ID/ARN, not the name of the queue.</p> </note>"""
    groupings: NotRequired["capo_connect.types.groupings.Groupings"]
    """<p>The grouping applied to the metrics returned. For example, when results are grouped by queue, the metrics returned are grouped by queue. The values returned apply to the metrics for each queue rather than aggregated for all queues.</p> <p>If no grouping is specified, a summary of metrics for all queues is returned.</p> <p>RoutingStepExpression is not a valid filter for GetMetricData and we recommend switching to GetMetricDataV2 for more up-to-date features.</p>"""
    historical_metrics: "capo_connect.types.historical_metrics.HistoricalMetrics"
    """<p>The metrics to retrieve. Specify the name, unit, and statistic for each metric. The following historical metrics are available. For a description of each metric, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html">Metrics definition</a> in the <i>Connect Customer Administrator Guide</i>.</p> <note> <p>This API does not support a contacts incoming metric (there's no CONTACTS_INCOMING metric missing from the documented list). </p> </note> <dl> <dt>ABANDON_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-queue-abandon-time">Average queue abandon time</a> </p> </dd> <dt>AFTER_CONTACT_WORK_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#after-contact-work-time">After contact work time</a> </p> </dd> <dt>API_CONTACTS_HANDLED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#api-contacts-handled">API contacts handled</a> </p> </dd> <dt>AVG_HOLD_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-customer-hold-time">Average customer hold time</a> </p> </dd> <dt>CALLBACK_CONTACTS_HANDLED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#callback-contacts-handled">Callback contacts handled</a> </p> </dd> <dt>CONTACTS_ABANDONED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-abandoned">Contacts abandoned</a> </p> </dd> <dt>CONTACTS_AGENT_HUNG_UP_FIRST</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-agent-hung-up-first">Contacts agent hung up first</a> </p> </dd> <dt>CONTACTS_CONSULTED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-consulted">Contacts consulted</a> </p> </dd> <dt>CONTACTS_HANDLED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled">Contacts handled</a> </p> </dd> <dt>CONTACTS_HANDLED_INCOMING</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled-incoming">Contacts handled incoming</a> </p> </dd> <dt>CONTACTS_HANDLED_OUTBOUND</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-handled-outbound">Contacts handled outbound</a> </p> </dd> <dt>CONTACTS_HOLD_ABANDONS</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-hold-disconnect">Contacts hold disconnect</a> </p> </dd> <dt>CONTACTS_MISSED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#agent-non-response">AGENT_NON_RESPONSE</a> </p> </dd> <dt>CONTACTS_QUEUED</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-queued">Contacts queued</a> </p> </dd> <dt>CONTACTS_TRANSFERRED_IN</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-in">Contacts transferred in</a> </p> </dd> <dt>CONTACTS_TRANSFERRED_IN_FROM_QUEUE</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-queue">Contacts transferred out queue</a> </p> </dd> <dt>CONTACTS_TRANSFERRED_OUT</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out">Contacts transferred out</a> </p> </dd> <dt>CONTACTS_TRANSFERRED_OUT_FROM_QUEUE</dt> <dd> <p>Unit: COUNT</p> <p>Statistic: SUM</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#contacts-transferred-out-queue">Contacts transferred out queue</a> </p> </dd> <dt>HANDLE_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-handle-time">Average handle time</a> </p> </dd> <dt>INTERACTION_AND_HOLD_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-agent-interaction-and-customer-hold-time">Average agent interaction and customer hold time</a> </p> </dd> <dt>INTERACTION_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#aaverage-agent-interaction-time">Average agent interaction time</a> </p> </dd> <dt>OCCUPANCY</dt> <dd> <p>Unit: PERCENT</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#occupancy">Occupancy</a> </p> </dd> <dt>QUEUE_ANSWER_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: AVG</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html##average-queue-answer-time">Average queue answer time</a> </p> </dd> <dt>QUEUED_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>Statistic: MAX</p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#minimum-flow-time">Minimum flow time</a> </p> </dd> <dt>SERVICE_LEVEL</dt> <dd> <p>You can include up to 20 SERVICE_LEVEL metrics in a request.</p> <p>Unit: PERCENT</p> <p>Statistic: AVG</p> <p>Threshold: For <code>ThresholdValue</code>, enter any whole number from 1 to 604800 (inclusive), in seconds. For <code>Comparison</code>, you must enter <code>LT</code> (for "Less than"). </p> <p>UI name: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#average-queue-abandon-time">Average queue abandon time</a> </p> </dd> </dl>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMetricDataRequest) -> dict:
    out: dict = {}
    import capo_connect.types.timestamp

    out["StartTime"] = capo_connect.types.timestamp.serialize_json(value["start_time"])
    import capo_connect.types.timestamp

    out["EndTime"] = capo_connect.types.timestamp.serialize_json(value["end_time"])
    import capo_connect.types.filters

    out["Filters"] = capo_connect.types.filters.serialize_json(value["filters"])
    if "groupings" in value:
        import capo_connect.types.groupings

        out["Groupings"] = capo_connect.types.groupings.serialize_json(
            value["groupings"]
        )
    import capo_connect.types.historical_metrics

    out["HistoricalMetrics"] = capo_connect.types.historical_metrics.serialize_json(
        value["historical_metrics"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetMetricDataRequest:
    out: GetMetricDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_connect.types.timestamp

        out["start_time"] = capo_connect.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        raise DeserializationError("GetMetricDataRequest.start_time required")
    if data.get("EndTime") is not None:
        import capo_connect.types.timestamp

        out["end_time"] = capo_connect.types.timestamp.deserialize_json(data["EndTime"])
    else:
        raise DeserializationError("GetMetricDataRequest.end_time required")
    if data.get("Filters") is not None:
        import capo_connect.types.filters

        out["filters"] = capo_connect.types.filters.deserialize_json(data["Filters"])
    else:
        raise DeserializationError("GetMetricDataRequest.filters required")
    if data.get("Groupings") is not None:
        import capo_connect.types.groupings

        out["groupings"] = capo_connect.types.groupings.deserialize_json(
            data["Groupings"]
        )
    if data.get("HistoricalMetrics") is not None:
        import capo_connect.types.historical_metrics

        out["historical_metrics"] = (
            capo_connect.types.historical_metrics.deserialize_json(
                data["HistoricalMetrics"]
            )
        )
    else:
        raise DeserializationError("GetMetricDataRequest.historical_metrics required")
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
