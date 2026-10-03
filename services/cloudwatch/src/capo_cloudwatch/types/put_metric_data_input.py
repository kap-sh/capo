"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutMetricDataInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.entity_metric_data_list
    import capo_cloudwatch.types.metric_data
    import capo_cloudwatch.types.namespace
    import capo_cloudwatch.types.strict_entity_validation


class PutMetricDataInput(TypedDict, closed=True):
    namespace: NotRequired["capo_cloudwatch.types.namespace.Namespace"]
    """<p>The namespace for the metric data. You can use ASCII characters for the namespace, except for control characters which are not supported.</p> <p>To avoid conflicts with Amazon Web Services service namespaces, you should not specify a namespace that begins with <code>AWS/</code> </p>"""
    metric_data: NotRequired["capo_cloudwatch.types.metric_data.MetricData"]
    """<p>The data for the metrics. Use this parameter if your metrics do not contain associated entities. The array can include no more than 1000 metrics per call.</p> <p>The limit of metrics allowed, 1000, is the sum of both <code>EntityMetricData</code> and <code>MetricData</code> metrics.</p>"""
    entity_metric_data: NotRequired[
        "capo_cloudwatch.types.entity_metric_data_list.EntityMetricDataList"
    ]
    """<p>Data for metrics that contain associated entity information. You can include up to two <code>EntityMetricData</code> objects, each of which can contain a single <code>Entity</code> and associated metrics.</p> <p>The limit of metrics allowed, 1000, is the sum of both <code>EntityMetricData</code> and <code>MetricData</code> metrics.</p>"""
    strict_entity_validation: NotRequired[
        "capo_cloudwatch.types.strict_entity_validation.StrictEntityValidation"
    ]
    """<p>Whether to accept valid metric data when an invalid entity is sent.</p> <ul> <li> <p>When set to <code>true</code>: Any validation error (for entity or metric data) will fail the entire request, and no data will be ingested. The failed operation will return a 400 result with the error.</p> </li> <li> <p>When set to <code>false</code>: Validation errors in the entity will not associate the metric with the entity, but the metric data will still be accepted and ingested. Validation errors in the metric data will fail the entire request, and no data will be ingested.</p> <p>In the case of an invalid entity, the operation will return a <code>200</code> status, but an additional response header will contain information about the validation errors. The new header, <code>X-Amzn-Failure-Message</code> is an enumeration of the following values:</p> <ul> <li> <p> <code>InvalidEntity</code> - The provided entity is invalid.</p> </li> <li> <p> <code>InvalidKeyAttributes</code> - The provided <code>KeyAttributes</code> of an entity is invalid.</p> </li> <li> <p> <code>InvalidAttributes</code> - The provided <code>Attributes</code> of an entity is invalid.</p> </li> <li> <p> <code>InvalidTypeValue</code> - The provided <code>Type</code> in the <code>KeyAttributes</code> of an entity is invalid.</p> </li> <li> <p> <code>EntitySizeTooLarge</code> - The number of <code>EntityMetricData</code> objects allowed is 2.</p> </li> <li> <p> <code>MissingRequiredFields</code> - There are missing required fields in the <code>KeyAttributes</code> for the provided <code>Type</code>.</p> </li> </ul> <p>For details of the requirements for specifying an entity, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html">How to add related information to telemetry</a> in the <i>CloudWatch User Guide</i>.</p> </li> </ul> <p>This parameter is <i>required</i> when <code>EntityMetricData</code> is included.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutMetricDataInput) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "metric_data" in value:
        import capo_cloudwatch.types.metric_data

        out["MetricData"] = capo_cloudwatch.types.metric_data.serialize_aws_json_1_0(
            value["metric_data"]
        )
    if "entity_metric_data" in value:
        import capo_cloudwatch.types.entity_metric_data_list

        out["EntityMetricData"] = (
            capo_cloudwatch.types.entity_metric_data_list.serialize_aws_json_1_0(
                value["entity_metric_data"]
            )
        )
    if "strict_entity_validation" in value:
        out["StrictEntityValidation"] = value["strict_entity_validation"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutMetricDataInput:
    out: PutMetricDataInput = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    if data.get("MetricData") is not None:
        import capo_cloudwatch.types.metric_data

        out["metric_data"] = capo_cloudwatch.types.metric_data.deserialize_aws_json_1_0(
            data["MetricData"]
        )
    if data.get("EntityMetricData") is not None:
        import capo_cloudwatch.types.entity_metric_data_list

        out["entity_metric_data"] = (
            capo_cloudwatch.types.entity_metric_data_list.deserialize_aws_json_1_0(
                data["EntityMetricData"]
            )
        )
    if data.get("StrictEntityValidation") is not None:
        out["strict_entity_validation"] = data["StrictEntityValidation"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutMetricDataInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "metric_data" in value:
        import capo_cloudwatch.types.metric_data

        capo_cloudwatch.types.metric_data.serialize_query(
            value["metric_data"], pairs, f"{key_prefix}MetricData"
        )
    if "entity_metric_data" in value:
        import capo_cloudwatch.types.entity_metric_data_list

        capo_cloudwatch.types.entity_metric_data_list.serialize_query(
            value["entity_metric_data"], pairs, f"{key_prefix}EntityMetricData"
        )
    if "strict_entity_validation" in value:
        pairs.append(
            (
                f"{key_prefix}StrictEntityValidation",
                "true" if value["strict_entity_validation"] else "false",
            )
        )


def deserialize_query(el: Element) -> PutMetricDataInput:
    out: PutMetricDataInput = {}  # type: ignore[typeddict-item]
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_metric_data = el.find("MetricData")
    if child_metric_data is not None:
        import capo_cloudwatch.types.metric_data

        out["metric_data"] = capo_cloudwatch.types.metric_data.deserialize_query(
            child_metric_data
        )
    child_entity_metric_data = el.find("EntityMetricData")
    if child_entity_metric_data is not None:
        import capo_cloudwatch.types.entity_metric_data_list

        out["entity_metric_data"] = (
            capo_cloudwatch.types.entity_metric_data_list.deserialize_query(
                child_entity_metric_data
            )
        )
    child_strict_entity_validation = el.find("StrictEntityValidation")
    if child_strict_entity_validation is not None:
        out["strict_entity_validation"] = (
            child_strict_entity_validation.text or ""
        ).lower() == "true"
    return out
