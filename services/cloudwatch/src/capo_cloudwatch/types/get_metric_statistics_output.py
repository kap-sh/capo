"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetMetricStatisticsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.datapoints
    import capo_cloudwatch.types.metric_label


class GetMetricStatisticsOutput(TypedDict, closed=True):
    label: NotRequired["capo_cloudwatch.types.metric_label.MetricLabel"]
    """<p>A label for the specified metric.</p>"""
    datapoints: NotRequired["capo_cloudwatch.types.datapoints.Datapoints"]
    """<p>The data points for the specified metric.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMetricStatisticsOutput) -> dict:
    out: dict = {}
    if "label" in value:
        out["Label"] = value["label"]
    if "datapoints" in value:
        import capo_cloudwatch.types.datapoints

        out["Datapoints"] = capo_cloudwatch.types.datapoints.serialize_aws_json_1_0(
            value["datapoints"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMetricStatisticsOutput:
    out: GetMetricStatisticsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("Datapoints") is not None:
        import capo_cloudwatch.types.datapoints

        out["datapoints"] = capo_cloudwatch.types.datapoints.deserialize_aws_json_1_0(
            data["Datapoints"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetMetricStatisticsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "label" in value:
        pairs.append((f"{key_prefix}Label", str(value["label"])))
    if "datapoints" in value:
        import capo_cloudwatch.types.datapoints

        capo_cloudwatch.types.datapoints.serialize_query(
            value["datapoints"], pairs, f"{key_prefix}Datapoints"
        )


def deserialize_query(el: Element) -> GetMetricStatisticsOutput:
    out: GetMetricStatisticsOutput = {}  # type: ignore[typeddict-item]
    child_label = el.find("Label")
    if child_label is not None:
        out["label"] = str(child_label.text or "")
    child_datapoints = el.find("Datapoints")
    if child_datapoints is not None:
        import capo_cloudwatch.types.datapoints

        out["datapoints"] = capo_cloudwatch.types.datapoints.deserialize_query(
            child_datapoints
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetMetricStatisticsOutput) -> dict:
    out: dict = {}
    if "label" in value:
        out["Label"] = value["label"]
    if "datapoints" in value:
        import capo_cloudwatch.types.datapoints

        out["Datapoints"] = capo_cloudwatch.types.datapoints.serialize_cbor(
            value["datapoints"]
        )
    return out


def deserialize_cbor(data: dict) -> GetMetricStatisticsOutput:
    out: GetMetricStatisticsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    if data.get("Datapoints") is not None:
        import capo_cloudwatch.types.datapoints

        out["datapoints"] = capo_cloudwatch.types.datapoints.deserialize_cbor(
            data["Datapoints"]
        )
    return out
