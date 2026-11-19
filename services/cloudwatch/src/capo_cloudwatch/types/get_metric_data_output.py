"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetMetricDataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_data_result_messages
    import capo_cloudwatch.types.metric_data_results
    import capo_cloudwatch.types.next_token


class GetMetricDataOutput(TypedDict, closed=True):
    metric_data_results: NotRequired[
        "capo_cloudwatch.types.metric_data_results.MetricDataResults"
    ]
    """<p>The metrics that are returned, including the metric name, namespace, and dimensions.</p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>A token that marks the next batch of returned results.</p>"""
    messages: NotRequired[
        "capo_cloudwatch.types.metric_data_result_messages.MetricDataResultMessages"
    ]
    """<p>Contains a message about this <code>GetMetricData</code> operation, if the operation results in such a message. An example of a message that might be returned is <code>Maximum number of allowed metrics exceeded</code>. If there is a message, as much of the operation as possible is still executed.</p> <p>A message appears here only if it is related to the global <code>GetMetricData</code> operation. Any message about a specific metric returned by the operation appears in the <code>MetricDataResult</code> object returned for that metric.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMetricDataOutput) -> dict:
    out: dict = {}
    if "metric_data_results" in value:
        import capo_cloudwatch.types.metric_data_results

        out["MetricDataResults"] = (
            capo_cloudwatch.types.metric_data_results.serialize_aws_json_1_0(
                value["metric_data_results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "messages" in value:
        import capo_cloudwatch.types.metric_data_result_messages

        out["Messages"] = (
            capo_cloudwatch.types.metric_data_result_messages.serialize_aws_json_1_0(
                value["messages"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMetricDataOutput:
    out: GetMetricDataOutput = {}  # type: ignore[typeddict-item]
    if data.get("MetricDataResults") is not None:
        import capo_cloudwatch.types.metric_data_results

        out["metric_data_results"] = (
            capo_cloudwatch.types.metric_data_results.deserialize_aws_json_1_0(
                data["MetricDataResults"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Messages") is not None:
        import capo_cloudwatch.types.metric_data_result_messages

        out["messages"] = (
            capo_cloudwatch.types.metric_data_result_messages.deserialize_aws_json_1_0(
                data["Messages"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetMetricDataOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "metric_data_results" in value:
        import capo_cloudwatch.types.metric_data_results

        capo_cloudwatch.types.metric_data_results.serialize_query(
            value["metric_data_results"], pairs, f"{key_prefix}MetricDataResults"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))
    if "messages" in value:
        import capo_cloudwatch.types.metric_data_result_messages

        capo_cloudwatch.types.metric_data_result_messages.serialize_query(
            value["messages"], pairs, f"{key_prefix}Messages"
        )


def deserialize_query(el: Element) -> GetMetricDataOutput:
    out: GetMetricDataOutput = {}  # type: ignore[typeddict-item]
    child_metric_data_results = el.find("MetricDataResults")
    if child_metric_data_results is not None:
        import capo_cloudwatch.types.metric_data_results

        out["metric_data_results"] = (
            capo_cloudwatch.types.metric_data_results.deserialize_query(
                child_metric_data_results
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_messages = el.find("Messages")
    if child_messages is not None:
        import capo_cloudwatch.types.metric_data_result_messages

        out["messages"] = (
            capo_cloudwatch.types.metric_data_result_messages.deserialize_query(
                child_messages
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetMetricDataOutput) -> dict:
    out: dict = {}
    if "metric_data_results" in value:
        import capo_cloudwatch.types.metric_data_results

        out["MetricDataResults"] = (
            capo_cloudwatch.types.metric_data_results.serialize_cbor(
                value["metric_data_results"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "messages" in value:
        import capo_cloudwatch.types.metric_data_result_messages

        out["Messages"] = (
            capo_cloudwatch.types.metric_data_result_messages.serialize_cbor(
                value["messages"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetMetricDataOutput:
    out: GetMetricDataOutput = {}  # type: ignore[typeddict-item]
    if data.get("MetricDataResults") is not None:
        import capo_cloudwatch.types.metric_data_results

        out["metric_data_results"] = (
            capo_cloudwatch.types.metric_data_results.deserialize_cbor(
                data["MetricDataResults"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Messages") is not None:
        import capo_cloudwatch.types.metric_data_result_messages

        out["messages"] = (
            capo_cloudwatch.types.metric_data_result_messages.deserialize_cbor(
                data["Messages"]
            )
        )
    return out
