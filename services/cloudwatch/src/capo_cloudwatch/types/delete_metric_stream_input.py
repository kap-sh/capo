"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteMetricStreamInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.metric_stream_name


class DeleteMetricStreamInput(TypedDict, closed=True):
    name: NotRequired["capo_cloudwatch.types.metric_stream_name.MetricStreamName"]
    """<p>The name of the metric stream to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteMetricStreamInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteMetricStreamInput:
    out: DeleteMetricStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteMetricStreamInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))


def deserialize_query(el: Element) -> DeleteMetricStreamInput:
    out: DeleteMetricStreamInput = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteMetricStreamInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> DeleteMetricStreamInput:
    out: DeleteMetricStreamInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    return out
