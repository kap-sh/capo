"""Generated from Smithy shape ``com.amazonaws.cloudwatch#StopMetricStreamsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_stream_names


class StopMetricStreamsInput(TypedDict, closed=True):
    names: NotRequired["capo_cloudwatch.types.metric_stream_names.MetricStreamNames"]
    """<p>The array of the names of metric streams to stop streaming.</p> <p>This is an "all or nothing" operation. If you do not have permission to access all of the metric streams that you list here, then none of the streams that you list in the operation will stop streaming.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopMetricStreamsInput) -> dict:
    out: dict = {}
    if "names" in value:
        import capo_cloudwatch.types.metric_stream_names

        out["Names"] = capo_cloudwatch.types.metric_stream_names.serialize_aws_json_1_0(
            value["names"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StopMetricStreamsInput:
    out: StopMetricStreamsInput = {}  # type: ignore[typeddict-item]
    if data.get("Names") is not None:
        import capo_cloudwatch.types.metric_stream_names

        out["names"] = (
            capo_cloudwatch.types.metric_stream_names.deserialize_aws_json_1_0(
                data["Names"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: StopMetricStreamsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "names" in value:
        import capo_cloudwatch.types.metric_stream_names

        capo_cloudwatch.types.metric_stream_names.serialize_query(
            value["names"], pairs, f"{key_prefix}Names"
        )


def deserialize_query(el: Element) -> StopMetricStreamsInput:
    out: StopMetricStreamsInput = {}  # type: ignore[typeddict-item]
    child_names = el.find("Names")
    if child_names is not None:
        import capo_cloudwatch.types.metric_stream_names

        out["names"] = capo_cloudwatch.types.metric_stream_names.deserialize_query(
            child_names
        )
    return out
