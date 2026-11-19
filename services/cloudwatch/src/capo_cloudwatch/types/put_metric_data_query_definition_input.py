"""Generated from Smithy shape ``com.amazonaws.cloudwatch#PutMetricDataQueryDefinitionInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.definition_id
    import capo_cloudwatch.types.definition_path
    import capo_cloudwatch.types.metric_expression_string
    import capo_cloudwatch.types.query_type
    import capo_cloudwatch.types.tag_list


class PutMetricDataQueryDefinitionInput(TypedDict, closed=True):
    id: NotRequired["capo_cloudwatch.types.definition_id.DefinitionId"]
    """<p>The ID of the metric data query definition to update. Omit this parameter to create a definition. CloudWatch then generates the ID and returns it in the response.</p>"""
    path: NotRequired["capo_cloudwatch.types.definition_path.DefinitionPath"]
    """<p>The name of the metric data query definition. Use slashes (<code>/</code>) to organize definitions into folders, for example <code>team/web/latency</code>. The path must meet the following requirements:</p> <ul> <li> <p>It must be unique in your account and Region.</p> </li> <li> <p>It can't start or end with a slash.</p> </li> <li> <p>It can't contain an empty folder name (<code>//</code>).</p> </li> <li> <p>It can be at most 1,015 bytes when encoded as UTF-8.</p> </li> </ul>"""
    expression: NotRequired[
        "capo_cloudwatch.types.metric_expression_string.MetricExpressionString"
    ]
    """<p>The query expression, in the language that <code>Type</code> specifies. CloudWatch doesn't validate or run the expression when you save it.</p>"""
    type: NotRequired["capo_cloudwatch.types.query_type.QueryType"]
    """<p>The language of the expression. Valid values are the following:</p> <ul> <li> <p> <code>PROMQL</code> – A PromQL query.</p> </li> <li> <p> <code>SQL</code> – A CloudWatch Metrics Insights query.</p> </li> <li> <p> <code>METRIC_MATH</code> – A metric math expression.</p> </li> </ul>"""
    tags: NotRequired["capo_cloudwatch.types.tag_list.TagList"]
    """<p>A list of key-value pairs to associate with the metric data query definition. You can use tags to categorize definitions and to control access to them. Tags are applied only when the request creates a definition, that is, when you omit <code>Id</code>. To change the tags of an existing definition, use <code>TagResource</code> and <code>UntagResource</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutMetricDataQueryDefinitionInput) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "path" in value:
        out["Path"] = value["path"]
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "type" in value:
        import capo_cloudwatch.types.query_type

        out["Type"] = capo_cloudwatch.types.query_type.serialize_aws_json_1_0(
            value["type"]
        )
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        out["Tags"] = capo_cloudwatch.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PutMetricDataQueryDefinitionInput:
    out: PutMetricDataQueryDefinitionInput = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    if data.get("Type") is not None:
        import capo_cloudwatch.types.query_type

        out["type"] = capo_cloudwatch.types.query_type.deserialize_aws_json_1_0(
            data["Type"]
        )
    if data.get("Tags") is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: PutMetricDataQueryDefinitionInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "id" in value:
        pairs.append((f"{key_prefix}Id", str(value["id"])))
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    if "expression" in value:
        pairs.append((f"{key_prefix}Expression", str(value["expression"])))
    if "type" in value:
        import capo_cloudwatch.types.query_type

        capo_cloudwatch.types.query_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "tags" in value:
        import capo_cloudwatch.types.tag_list

        capo_cloudwatch.types.tag_list.serialize_query(
            value["tags"], pairs, f"{key_prefix}Tags"
        )


def deserialize_query(el: Element) -> PutMetricDataQueryDefinitionInput:
    out: PutMetricDataQueryDefinitionInput = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
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
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_cloudwatch.types.tag_list

        out["tags"] = capo_cloudwatch.types.tag_list.deserialize_query(child_tags)
    return out


def redact_sensitive(value: PutMetricDataQueryDefinitionInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
