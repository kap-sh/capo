"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetMetricDataQueryDefinitionOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.amazon_resource_name
    import capo_cloudwatch.types.definition_id
    import capo_cloudwatch.types.definition_path
    import capo_cloudwatch.types.metric_expression_string
    import capo_cloudwatch.types.query_type
    import capo_cloudwatch.types.timestamp


class GetMetricDataQueryDefinitionOutput(TypedDict, closed=True):
    id: NotRequired["capo_cloudwatch.types.definition_id.DefinitionId"]
    """<p>The ID of the metric data query definition.</p>"""
    arn: NotRequired["capo_cloudwatch.types.amazon_resource_name.AmazonResourceName"]
    """<p>The Amazon Resource Name (ARN) of the metric data query definition.</p>"""
    path: NotRequired["capo_cloudwatch.types.definition_path.DefinitionPath"]
    """<p>The path of the metric data query definition.</p>"""
    expression: NotRequired[
        "capo_cloudwatch.types.metric_expression_string.MetricExpressionString"
    ]
    """<p>The query expression.</p>"""
    type: NotRequired["capo_cloudwatch.types.query_type.QueryType"]
    """<p>The language of the expression. Valid values are the following:</p> <ul> <li> <p> <code>PROMQL</code> – A PromQL query.</p> </li> <li> <p> <code>SQL</code> – A CloudWatch Metrics Insights query.</p> </li> <li> <p> <code>METRIC_MATH</code> – A metric math expression.</p> </li> </ul>"""
    created_at: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time when you created the metric data query definition.</p>"""
    updated_at: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time when you last updated the metric data query definition.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMetricDataQueryDefinitionOutput) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "path" in value:
        out["Path"] = value["path"]
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "type" in value:
        import capo_cloudwatch.types.query_type

        out["Type"] = capo_cloudwatch.types.query_type.serialize_aws_json_1_0(
            value["type"]
        )
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
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMetricDataQueryDefinitionOutput:
    out: GetMetricDataQueryDefinitionOutput = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    if data.get("Type") is not None:
        import capo_cloudwatch.types.query_type

        out["type"] = capo_cloudwatch.types.query_type.deserialize_aws_json_1_0(
            data["Type"]
        )
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
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetMetricDataQueryDefinitionOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "id" in value:
        pairs.append((f"{key_prefix}Id", str(value["id"])))
    if "arn" in value:
        pairs.append((f"{key_prefix}Arn", str(value["arn"])))
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    if "expression" in value:
        pairs.append((f"{key_prefix}Expression", str(value["expression"])))
    if "type" in value:
        import capo_cloudwatch.types.query_type

        capo_cloudwatch.types.query_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
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


def deserialize_query(el: Element) -> GetMetricDataQueryDefinitionOutput:
    out: GetMetricDataQueryDefinitionOutput = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_arn = el.find("Arn")
    if child_arn is not None:
        out["arn"] = str(child_arn.text or "")
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_expression = el.find("Expression")
    if child_expression is not None:
        out["expression"] = str(child_expression.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudwatch.types.query_type

        out["type"] = capo_cloudwatch.types.query_type.deserialize_query(child_type)
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
    return out


def redact_sensitive(value: GetMetricDataQueryDefinitionOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
