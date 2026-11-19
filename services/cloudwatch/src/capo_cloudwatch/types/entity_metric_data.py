"""Generated from Smithy shape ``com.amazonaws.cloudwatch#EntityMetricData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.entity
    import capo_cloudwatch.types.metric_data


class EntityMetricData(TypedDict, closed=True):
    entity: NotRequired["capo_cloudwatch.types.entity.Entity"]
    """<p>The entity associated with the metrics.</p>"""
    metric_data: NotRequired["capo_cloudwatch.types.metric_data.MetricData"]
    """<p>The metric data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntityMetricData) -> dict:
    out: dict = {}
    if "entity" in value:
        import capo_cloudwatch.types.entity

        out["Entity"] = capo_cloudwatch.types.entity.serialize_aws_json_1_0(
            value["entity"]
        )
    if "metric_data" in value:
        import capo_cloudwatch.types.metric_data

        out["MetricData"] = capo_cloudwatch.types.metric_data.serialize_aws_json_1_0(
            value["metric_data"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EntityMetricData:
    out: EntityMetricData = {}  # type: ignore[typeddict-item]
    if data.get("Entity") is not None:
        import capo_cloudwatch.types.entity

        out["entity"] = capo_cloudwatch.types.entity.deserialize_aws_json_1_0(
            data["Entity"]
        )
    if data.get("MetricData") is not None:
        import capo_cloudwatch.types.metric_data

        out["metric_data"] = capo_cloudwatch.types.metric_data.deserialize_aws_json_1_0(
            data["MetricData"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: EntityMetricData, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "entity" in value:
        import capo_cloudwatch.types.entity

        capo_cloudwatch.types.entity.serialize_query(
            value["entity"], pairs, f"{key_prefix}Entity"
        )
    if "metric_data" in value:
        import capo_cloudwatch.types.metric_data

        capo_cloudwatch.types.metric_data.serialize_query(
            value["metric_data"], pairs, f"{key_prefix}MetricData"
        )


def deserialize_query(el: Element) -> EntityMetricData:
    out: EntityMetricData = {}  # type: ignore[typeddict-item]
    child_entity = el.find("Entity")
    if child_entity is not None:
        import capo_cloudwatch.types.entity

        out["entity"] = capo_cloudwatch.types.entity.deserialize_query(child_entity)
    child_metric_data = el.find("MetricData")
    if child_metric_data is not None:
        import capo_cloudwatch.types.metric_data

        out["metric_data"] = capo_cloudwatch.types.metric_data.deserialize_query(
            child_metric_data
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EntityMetricData) -> dict:
    out: dict = {}
    if "entity" in value:
        import capo_cloudwatch.types.entity

        out["Entity"] = capo_cloudwatch.types.entity.serialize_cbor(value["entity"])
    if "metric_data" in value:
        import capo_cloudwatch.types.metric_data

        out["MetricData"] = capo_cloudwatch.types.metric_data.serialize_cbor(
            value["metric_data"]
        )
    return out


def deserialize_cbor(data: dict) -> EntityMetricData:
    out: EntityMetricData = {}  # type: ignore[typeddict-item]
    if data.get("Entity") is not None:
        import capo_cloudwatch.types.entity

        out["entity"] = capo_cloudwatch.types.entity.deserialize_cbor(data["Entity"])
    if data.get("MetricData") is not None:
        import capo_cloudwatch.types.metric_data

        out["metric_data"] = capo_cloudwatch.types.metric_data.deserialize_cbor(
            data["MetricData"]
        )
    return out
