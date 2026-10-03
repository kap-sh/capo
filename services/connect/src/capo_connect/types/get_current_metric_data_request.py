"""Generated from Smithy shape ``com.amazonaws.connect#GetCurrentMetricDataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.current_metric_sort_criteria_max_one
    import capo_connect.types.current_metrics
    import capo_connect.types.filters
    import capo_connect.types.groupings
    import capo_connect.types.instance_id
    import capo_connect.types.max_result100
    import capo_connect.types.next_token


class GetCurrentMetricDataRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    filters: "capo_connect.types.filters.Filters"
    """<p>The filters to apply to returned metrics. You can filter up to the following limits:</p> <ul> <li> <p>Queues: 100</p> </li> <li> <p>Routing profiles: 100</p> </li> <li> <p>Channels: 3 (VOICE, CHAT, and TASK channels are supported.)</p> </li> <li> <p>RoutingStepExpressions: 50</p> </li> <li> <p>AgentStatuses: 50</p> </li> <li> <p>Subtypes: 10</p> </li> <li> <p>ValidationTestTypes: 10</p> </li> </ul> <p>Metric data is retrieved only for the resources associated with the queues or routing profiles, and by any channels included in the filter. (You cannot filter by both queue AND routing profile.) You can include both resource IDs and resource ARNs in the same request.</p> <p>When using <code>AgentStatuses</code> as filter make sure Queues is added as primary filter.</p> <p>When using <code>Subtypes</code> as filter make sure Queues is added as primary filter.</p> <p>When using <code>ValidationTestTypes</code> as filter make sure Queues is added as primary filter.</p> <p>When using the <code>RoutingStepExpression</code> filter, you need to pass exactly one <code>QueueId</code>. The filter is also case sensitive so when using the <code>RoutingStepExpression</code> filter, grouping by <code>ROUTING_STEP_EXPRESSION</code> is required.</p> <p>Currently tagging is only supported on the resources that are passed in the filter.</p>"""
    groupings: NotRequired["capo_connect.types.groupings.Groupings"]
    """<p>Defines the level of aggregation for metrics data by a dimension(s). Its similar to sorting items into buckets based on a common characteristic, then counting or calculating something for each bucket. For example, when grouped by <code>QUEUE</code>, the metrics returned apply to each queue rather than aggregated for all queues. </p> <p>The grouping list is an ordered list, with the first item in the list defined as the primary grouping. If no grouping is included in the request, the aggregation happens at the instance-level.</p> <ul> <li> <p>If you group by <code>CHANNEL</code>, you should include a Channels filter. VOICE, CHAT, and TASK channels are supported.</p> </li> <li> <p>If you group by <code>AGENT_STATUS</code>, you must include the <code>QUEUE</code> as the primary grouping and use queue filter. When you group by <code>AGENT_STATUS</code>, the only metric available is the <code>AGENTS_ONLINE</code> metric.</p> </li> <li> <p>If you group by <code>SUBTYPE</code> or <code>VALIDATION_TEST_TYPE</code> as secondary grouping then you must include <code>QUEUE</code> as primary grouping and use Queue as filter</p> </li> <li> <p>If you group by <code>ROUTING_PROFILE</code>, you must include either a queue or routing profile filter. In addition, a routing profile filter is required for metrics <code>CONTACTS_SCHEDULED</code>, <code>CONTACTS_IN_QUEUE</code>, and <code> OLDEST_CONTACT_AGE</code>.</p> </li> <li> <p>When using the <code>RoutingStepExpression</code> filter, group by <code>ROUTING_STEP_EXPRESSION</code> is required.</p> </li> </ul>"""
    current_metrics: "capo_connect.types.current_metrics.CurrentMetrics"
    """<p>The metrics to retrieve. Specify the name or metricId, and unit for each metric. The following metrics are available. For a description of all the metrics, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html">Metrics definitions</a> in the <i>Connect Customer Administrator Guide</i>.</p> <note> <p> MetricId should be used to reference custom metrics or out of the box metrics as Arn. If using MetricId, the limit is 10 MetricId per request.</p> </note> <dl> <dt>AGENTS_AFTER_CONTACT_WORK</dt> <dd> <p>Unit: COUNT</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#aftercallwork-real-time">ACW</a> </p> </dd> <dt>AGENTS_AVAILABLE</dt> <dd> <p>Unit: COUNT</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#available-real-time">Available</a> </p> </dd> <dt>AGENTS_ERROR</dt> <dd> <p>Unit: COUNT</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#error-real-time">Error</a> </p> </dd> <dt>AGENTS_NON_PRODUCTIVE</dt> <dd> <p>Unit: COUNT</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#non-productive-time-real-time">NPT (Non-Productive Time)</a> </p> </dd> <dt>AGENTS_ON_CALL</dt> <dd> <p>Unit: COUNT</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#on-call-real-time">On contact</a> </p> </dd> <dt>AGENTS_ON_CONTACT</dt> <dd> <p>Unit: COUNT</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#on-call-real-time">On contact</a> </p> </dd> <dt>AGENTS_ONLINE</dt> <dd> <p>Unit: COUNT</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#online-real-time">Online</a> </p> </dd> <dt>AGENTS_STAFFED</dt> <dd> <p>Unit: COUNT</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#staffed-real-time">Staffed</a> </p> </dd> <dt>CONTACTS_IN_QUEUE</dt> <dd> <p>Unit: COUNT</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#in-queue-real-time">In queue</a> </p> </dd> <dt>CONTACTS_SCHEDULED</dt> <dd> <p>Unit: COUNT</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#scheduled-real-time">Scheduled</a> </p> </dd> <dt>ESTIMATED_WAIT_TIME</dt> <dd> <p>Unit: SECONDS</p> <p>This metric supports filter and grouping combination only used for core routing purpose. Valid filter and grouping use cases: </p> <ul> <li> <p>Filter by a list of [Queues] and a list of [Channels], group by [“QUEUE”, “CHANNEL”]</p> </li> <li> <p>Filter by a singleton list of [Queue], a singleton list of [Channel], a list of [RoutingStepExpression], group by [“ROUTING_STEP_EXPRESSION”].</p> </li> </ul> </dd> <dt>OLDEST_CONTACT_AGE</dt> <dd> <p>Unit: SECONDS</p> <p>When you use groupings, Unit says SECONDS and the Value is returned in SECONDS. </p> <p>When you do not use groupings, Unit says SECONDS but the Value is returned in MILLISECONDS. For example, if you get a response like this:</p> <p> <code>{ "Metric": { "Name": "OLDEST_CONTACT_AGE", "Unit": "SECONDS" }, "Value": 24113.0 </code>}</p> <p>The actual OLDEST_CONTACT_AGE is 24 seconds.</p> <p>When the filter <code>RoutingStepExpression</code> is used, this metric is still calculated from enqueue time. For example, if a contact that has been queued under <code><Expression 1></code> for 10 seconds has expired and <code><Expression 2></code> becomes active, then <code>OLDEST_CONTACT_AGE</code> for this queue will be counted starting from 10, not 0.</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#oldest-real-time">Oldest</a> </p> </dd> <dt>SLOTS_ACTIVE</dt> <dd> <p>Unit: COUNT</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#active-real-time">Active</a> </p> </dd> <dt>SLOTS_AVAILABLE</dt> <dd> <p>Unit: COUNT</p> <p>Name in real-time metrics report: <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#availability-real-time">Availability</a> </p> </dd> </dl>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p> <p>The token expires after 5 minutes from the time it is created. Subsequent requests that use the token must use the same request parameters as the request that generated the token.</p>"""
    max_results: NotRequired["capo_connect.types.max_result100.MaxResult100"]
    """<p>The maximum number of results to return per page.</p>"""
    sort_criteria: NotRequired[
        "capo_connect.types.current_metric_sort_criteria_max_one.CurrentMetricSortCriteriaMaxOne"
    ]
    """<p>The way to sort the resulting response based on metrics. You can enter one sort criteria. By default resources are sorted based on <code>AGENTS_ONLINE</code>, <code>DESCENDING</code>. The metric collection is sorted based on the input metrics.</p> <p>Note the following:</p> <ul> <li> <p>Sorting on <code>SLOTS_ACTIVE</code> and <code>SLOTS_AVAILABLE</code> is not supported.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCurrentMetricDataRequest) -> dict:
    out: dict = {}
    import capo_connect.types.filters

    out["Filters"] = capo_connect.types.filters.serialize_json(value["filters"])
    if "groupings" in value:
        import capo_connect.types.groupings

        out["Groupings"] = capo_connect.types.groupings.serialize_json(
            value["groupings"]
        )
    import capo_connect.types.current_metrics

    out["CurrentMetrics"] = capo_connect.types.current_metrics.serialize_json(
        value["current_metrics"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "sort_criteria" in value:
        import capo_connect.types.current_metric_sort_criteria_max_one

        out["SortCriteria"] = (
            capo_connect.types.current_metric_sort_criteria_max_one.serialize_json(
                value["sort_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCurrentMetricDataRequest:
    out: GetCurrentMetricDataRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filters") is not None:
        import capo_connect.types.filters

        out["filters"] = capo_connect.types.filters.deserialize_json(data["Filters"])
    else:
        raise DeserializationError("GetCurrentMetricDataRequest.filters required")
    if data.get("Groupings") is not None:
        import capo_connect.types.groupings

        out["groupings"] = capo_connect.types.groupings.deserialize_json(
            data["Groupings"]
        )
    if data.get("CurrentMetrics") is not None:
        import capo_connect.types.current_metrics

        out["current_metrics"] = capo_connect.types.current_metrics.deserialize_json(
            data["CurrentMetrics"]
        )
    else:
        raise DeserializationError(
            "GetCurrentMetricDataRequest.current_metrics required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("SortCriteria") is not None:
        import capo_connect.types.current_metric_sort_criteria_max_one

        out["sort_criteria"] = (
            capo_connect.types.current_metric_sort_criteria_max_one.deserialize_json(
                data["SortCriteria"]
            )
        )
    return out
