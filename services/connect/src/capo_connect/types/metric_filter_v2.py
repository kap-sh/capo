"""Generated from Smithy shape ``com.amazonaws.connect#MetricFilterV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.metric_filter_value_list
    import capo_connect.types.string


class MetricFilterV2(TypedDict, closed=True):
    metric_filter_key: NotRequired["capo_connect.types.string.String"]
    """<p>The key to use for filtering data. </p> <p>Valid metric filter keys: </p> <ul> <li> <p>ANSWERING_MACHINE_DETECTION_STATUS</p> </li> <li> <p>CASE_STATUS</p> </li> <li> <p>DISCONNECT_REASON</p> </li> <li> <p>FLOWS_ACTION_IDENTIFIER</p> </li> <li> <p>FLOWS_NEXT_ACTION_IDENTIFIER</p> </li> <li> <p>FLOWS_OUTCOME_TYPE</p> </li> <li> <p>FLOWS_RESOURCE_TYPE</p> </li> <li> <p>INITIATION_METHOD</p> </li> </ul>"""
    metric_filter_values: NotRequired[
        "capo_connect.types.metric_filter_value_list.MetricFilterValueList"
    ]
    """<p>The values to use for filtering data. Values for metric-level filters can be either a fixed set of values or a customized list, depending on the use case.</p> <p>For valid values of metric-level filters <code>INITIATION_METHOD</code>, <code>DISCONNECT_REASON</code>, and <code>ANSWERING_MACHINE_DETECTION_STATUS</code>, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/ctr-data-model.html#ctr-ContactTraceRecord">ContactTraceRecord</a> in the <i>Connect Customer Administrator Guide</i>. </p> <p>For valid values of the metric-level filter <code>FLOWS_OUTCOME_TYPE</code>, see the description for the <a href="https://docs.aws.amazon.com/connect/latest/adminguide/metrics-definitions.html#flows-outcome">Flow outcome</a> metric in the <i>Connect Customer Administrator Guide</i>.</p> <p>For valid values of the metric-level filter <code>BOT_CONVERSATION_OUTCOME_TYPE</code>, see the description for the <a href="https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#bot-conversations-completed-metric">Bot conversations completed</a> in the <i>Connect Customer Administrator Guide</i>.</p> <p>For valid values of the metric-level filter <code>BOT_INTENT_OUTCOME_TYPE</code>, see the description for the <a href="https://docs.aws.amazon.com/connect/latest/adminguide/bot-metrics.html#bot-intents-completed-metric">Bot intents completed</a> metric in the <i>Connect Customer Administrator Guide</i>.</p>"""
    negate: "capo_connect.types.boolean.Boolean"
    """<p>If set to <code>true</code>, the API response contains results that filter out the results matched by the metric-level filters condition. By default, <code>Negate</code> is set to <code>false</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricFilterV2) -> dict:
    out: dict = {}
    if "metric_filter_key" in value:
        out["MetricFilterKey"] = value["metric_filter_key"]
    if "metric_filter_values" in value:
        import capo_connect.types.metric_filter_value_list

        out["MetricFilterValues"] = (
            capo_connect.types.metric_filter_value_list.serialize_json(
                value["metric_filter_values"]
            )
        )
    out["Negate"] = value.get("negate", False)
    return out


def deserialize_json(data: dict) -> MetricFilterV2:
    out: MetricFilterV2 = {}  # type: ignore[typeddict-item]
    if data.get("MetricFilterKey") is not None:
        out["metric_filter_key"] = data["MetricFilterKey"]
    if data.get("MetricFilterValues") is not None:
        import capo_connect.types.metric_filter_value_list

        out["metric_filter_values"] = (
            capo_connect.types.metric_filter_value_list.deserialize_json(
                data["MetricFilterValues"]
            )
        )
    if data.get("Negate") is not None:
        out["negate"] = data["Negate"]
    else:
        out["negate"] = False
    return out
