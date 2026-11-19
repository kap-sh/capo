"""Generated from Smithy shape ``com.amazonaws.pi#MetricKeyDataPoints``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.data_points_list
    import capo_pi.types.response_resource_metric_key


class MetricKeyDataPoints(TypedDict, closed=True):
    key: NotRequired[
        "capo_pi.types.response_resource_metric_key.ResponseResourceMetricKey"
    ]
    """<p>The dimensions to which the data points apply.</p>"""
    data_points: NotRequired["capo_pi.types.data_points_list.DataPointsList"]
    """<p>An array of timestamp-value pairs, representing measurements over a period of time.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricKeyDataPoints) -> dict:
    out: dict = {}
    if "key" in value:
        import capo_pi.types.response_resource_metric_key

        out["Key"] = capo_pi.types.response_resource_metric_key.serialize_aws_json_1_1(
            value["key"]
        )
    if "data_points" in value:
        import capo_pi.types.data_points_list

        out["DataPoints"] = capo_pi.types.data_points_list.serialize_aws_json_1_1(
            value["data_points"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricKeyDataPoints:
    out: MetricKeyDataPoints = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_pi.types.response_resource_metric_key

        out["key"] = (
            capo_pi.types.response_resource_metric_key.deserialize_aws_json_1_1(
                data["Key"]
            )
        )
    if data.get("DataPoints") is not None:
        import capo_pi.types.data_points_list

        out["data_points"] = capo_pi.types.data_points_list.deserialize_aws_json_1_1(
            data["DataPoints"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricKeyDataPoints) -> dict:
    out: dict = {}
    if "key" in value:
        import capo_pi.types.response_resource_metric_key

        out["Key"] = capo_pi.types.response_resource_metric_key.serialize_cbor(
            value["key"]
        )
    if "data_points" in value:
        import capo_pi.types.data_points_list

        out["DataPoints"] = capo_pi.types.data_points_list.serialize_cbor(
            value["data_points"]
        )
    return out


def deserialize_cbor(data: dict) -> MetricKeyDataPoints:
    out: MetricKeyDataPoints = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_pi.types.response_resource_metric_key

        out["key"] = capo_pi.types.response_resource_metric_key.deserialize_cbor(
            data["Key"]
        )
    if data.get("DataPoints") is not None:
        import capo_pi.types.data_points_list

        out["data_points"] = capo_pi.types.data_points_list.deserialize_cbor(
            data["DataPoints"]
        )
    return out
