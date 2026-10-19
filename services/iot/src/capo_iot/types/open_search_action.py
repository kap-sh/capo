"""Generated from Smithy shape ``com.amazonaws.iot#OpenSearchAction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.elasticsearch_endpoint
    import capo_iot.types.elasticsearch_id
    import capo_iot.types.elasticsearch_index
    import capo_iot.types.elasticsearch_type


class OpenSearchAction(TypedDict, closed=True):
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The IAM role ARN that has access to OpenSearch.</p>"""
    endpoint: "capo_iot.types.elasticsearch_endpoint.ElasticsearchEndpoint"
    """<p>The endpoint of your OpenSearch domain.</p>"""
    index: "capo_iot.types.elasticsearch_index.ElasticsearchIndex"
    """<p>The OpenSearch index where you want to store your data.</p>"""
    type: "capo_iot.types.elasticsearch_type.ElasticsearchType"
    """<p>The type of document you are storing.</p>"""
    id: "capo_iot.types.elasticsearch_id.ElasticsearchId"
    """<p>The unique identifier for the document you are storing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenSearchAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["endpoint"] = value["endpoint"]
    out["index"] = value["index"]
    out["type"] = value["type"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> OpenSearchAction:
    out: OpenSearchAction = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        out["endpoint"] = ""
    if data.get("index") is not None:
        out["index"] = data["index"]
    else:
        out["index"] = ""
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    return out
