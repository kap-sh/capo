"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ResourceMetricsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.resource_arn
    import capo_cloudwatch.types.resource_metric_selection_list
    import capo_cloudwatch.types.timestamp


class ResourceMetricsConfiguration(TypedDict, closed=True):
    resource_arn: NotRequired["capo_cloudwatch.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services resource that this configuration applies to.</p>"""
    created_at: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time that the resource metrics configuration was created.</p>"""
    updated_at: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time that the resource metrics configuration was last updated. When the configuration is first created, this value is the same as <code>CreatedAt</code>.</p>"""
    metric_selections: NotRequired[
        "capo_cloudwatch.types.resource_metric_selection_list.ResourceMetricSelectionList"
    ]
    """<p>The metrics that Amazon CloudWatch collects for the resource. If this field is not present, Amazon CloudWatch collects all available detailed metrics for the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceMetricsConfiguration) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "created_at" in value:
        import capo_cloudwatch.types.timestamp

        out["CreatedAt"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_cloudwatch.types.timestamp

        out["UpdatedAt"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    if "metric_selections" in value:
        import capo_cloudwatch.types.resource_metric_selection_list

        out["MetricSelections"] = (
            capo_cloudwatch.types.resource_metric_selection_list.serialize_aws_json_1_0(
                value["metric_selections"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceMetricsConfiguration:
    out: ResourceMetricsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("CreatedAt") is not None:
        import capo_cloudwatch.types.timestamp

        out["created_at"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_cloudwatch.types.timestamp

        out["updated_at"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["UpdatedAt"]
        )
    if data.get("MetricSelections") is not None:
        import capo_cloudwatch.types.resource_metric_selection_list

        out["metric_selections"] = (
            capo_cloudwatch.types.resource_metric_selection_list.deserialize_aws_json_1_0(
                data["MetricSelections"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceMetricsConfiguration, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_arn" in value:
        pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))
    if "created_at" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["created_at"], pairs, f"{key_prefix}CreatedAt"
        )
    if "updated_at" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["updated_at"], pairs, f"{key_prefix}UpdatedAt"
        )
    if "metric_selections" in value:
        import capo_cloudwatch.types.resource_metric_selection_list

        capo_cloudwatch.types.resource_metric_selection_list.serialize_query(
            value["metric_selections"], pairs, f"{key_prefix}MetricSelections"
        )


def deserialize_query(el: Element) -> ResourceMetricsConfiguration:
    out: ResourceMetricsConfiguration = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    child_created_at = el.find("CreatedAt")
    if child_created_at is not None:
        import capo_cloudwatch.types.timestamp

        out["created_at"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_created_at
        )
    child_updated_at = el.find("UpdatedAt")
    if child_updated_at is not None:
        import capo_cloudwatch.types.timestamp

        out["updated_at"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_updated_at
        )
    child_metric_selections = el.find("MetricSelections")
    if child_metric_selections is not None:
        import capo_cloudwatch.types.resource_metric_selection_list

        out["metric_selections"] = (
            capo_cloudwatch.types.resource_metric_selection_list.deserialize_query(
                child_metric_selections
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceMetricsConfiguration) -> dict:
    out: dict = {}
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "created_at" in value:
        import capo_cloudwatch.types.timestamp

        out["CreatedAt"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_cloudwatch.types.timestamp

        out["UpdatedAt"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["updated_at"]
        )
    if "metric_selections" in value:
        import capo_cloudwatch.types.resource_metric_selection_list

        out["MetricSelections"] = (
            capo_cloudwatch.types.resource_metric_selection_list.serialize_cbor(
                value["metric_selections"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ResourceMetricsConfiguration:
    out: ResourceMetricsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    if data.get("CreatedAt") is not None:
        import capo_cloudwatch.types.timestamp

        out["created_at"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_cloudwatch.types.timestamp

        out["updated_at"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["UpdatedAt"]
        )
    if data.get("MetricSelections") is not None:
        import capo_cloudwatch.types.resource_metric_selection_list

        out["metric_selections"] = (
            capo_cloudwatch.types.resource_metric_selection_list.deserialize_cbor(
                data["MetricSelections"]
            )
        )
    return out
