"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricDataQueryDefinitionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.definition_id
    import capo_cloudwatch.types.definition_path
    import capo_cloudwatch.types.query_type
    import capo_cloudwatch.types.timestamp


class MetricDataQueryDefinitionSummary(TypedDict, closed=True):
    id: NotRequired["capo_cloudwatch.types.definition_id.DefinitionId"]
    """<p>The ID of the metric data query definition.</p>"""
    path: NotRequired["capo_cloudwatch.types.definition_path.DefinitionPath"]
    """<p>The path of the metric data query definition.</p>"""
    type: NotRequired["capo_cloudwatch.types.query_type.QueryType"]
    """<p>The language of the expression. Valid values are the following:</p> <ul> <li> <p> <code>PROMQL</code> – A PromQL query.</p> </li> <li> <p> <code>SQL</code> – A CloudWatch Metrics Insights query.</p> </li> <li> <p> <code>METRIC_MATH</code> – A metric math expression.</p> </li> </ul>"""
    updated_at: NotRequired["capo_cloudwatch.types.timestamp.Timestamp"]
    """<p>The date and time when you last updated the metric data query definition.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricDataQueryDefinitionSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "path" in value:
        out["Path"] = value["path"]
    if "type" in value:
        import capo_cloudwatch.types.query_type

        out["Type"] = capo_cloudwatch.types.query_type.serialize_aws_json_1_0(
            value["type"]
        )
    if "updated_at" in value:
        import capo_cloudwatch.types.timestamp

        out["UpdatedAt"] = capo_cloudwatch.types.timestamp.serialize_aws_json_1_0(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricDataQueryDefinitionSummary:
    out: MetricDataQueryDefinitionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("Type") is not None:
        import capo_cloudwatch.types.query_type

        out["type"] = capo_cloudwatch.types.query_type.deserialize_aws_json_1_0(
            data["Type"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_cloudwatch.types.timestamp

        out["updated_at"] = capo_cloudwatch.types.timestamp.deserialize_aws_json_1_0(
            data["UpdatedAt"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricDataQueryDefinitionSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "id" in value:
        pairs.append((f"{key_prefix}Id", str(value["id"])))
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    if "type" in value:
        import capo_cloudwatch.types.query_type

        capo_cloudwatch.types.query_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "updated_at" in value:
        import capo_cloudwatch.types.timestamp

        capo_cloudwatch.types.timestamp.serialize_query(
            value["updated_at"], pairs, f"{key_prefix}UpdatedAt"
        )


def deserialize_query(el: Element) -> MetricDataQueryDefinitionSummary:
    out: MetricDataQueryDefinitionSummary = {}  # type: ignore[typeddict-item]
    child_id = el.find("Id")
    if child_id is not None:
        out["id"] = str(child_id.text or "")
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudwatch.types.query_type

        out["type"] = capo_cloudwatch.types.query_type.deserialize_query(child_type)
    child_updated_at = el.find("UpdatedAt")
    if child_updated_at is not None:
        import capo_cloudwatch.types.timestamp

        out["updated_at"] = capo_cloudwatch.types.timestamp.deserialize_query(
            child_updated_at
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MetricDataQueryDefinitionSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "path" in value:
        out["Path"] = value["path"]
    if "type" in value:
        import capo_cloudwatch.types.query_type

        out["Type"] = capo_cloudwatch.types.query_type.serialize_cbor(value["type"])
    if "updated_at" in value:
        import capo_cloudwatch.types.timestamp

        out["UpdatedAt"] = capo_cloudwatch.types.timestamp.serialize_cbor(
            value["updated_at"]
        )
    return out


def deserialize_cbor(data: dict) -> MetricDataQueryDefinitionSummary:
    out: MetricDataQueryDefinitionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Path") is not None:
        out["path"] = data["Path"]
    if data.get("Type") is not None:
        import capo_cloudwatch.types.query_type

        out["type"] = capo_cloudwatch.types.query_type.deserialize_cbor(data["Type"])
    if data.get("UpdatedAt") is not None:
        import capo_cloudwatch.types.timestamp

        out["updated_at"] = capo_cloudwatch.types.timestamp.deserialize_cbor(
            data["UpdatedAt"]
        )
    return out
