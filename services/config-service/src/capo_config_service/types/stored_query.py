"""Generated from Smithy shape ``com.amazonaws.configservice#StoredQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.query_arn
    import capo_config_service.types.query_description
    import capo_config_service.types.query_expression
    import capo_config_service.types.query_id
    import capo_config_service.types.query_name


class StoredQuery(TypedDict, closed=True):
    query_id: NotRequired["capo_config_service.types.query_id.QueryId"]
    """<p>The ID of the query.</p>"""
    query_arn: NotRequired["capo_config_service.types.query_arn.QueryArn"]
    """<p>Amazon Resource Name (ARN) of the query. For example, arn:partition:service:region:account-id:resource-type/resource-name/resource-id.</p>"""
    query_name: "capo_config_service.types.query_name.QueryName"
    """<p>The name of the query.</p>"""
    description: NotRequired[
        "capo_config_service.types.query_description.QueryDescription"
    ]
    """<p>A unique description for the query.</p>"""
    expression: NotRequired[
        "capo_config_service.types.query_expression.QueryExpression"
    ]
    """<p>The expression of the query. For example, <code>SELECT resourceId, resourceType, supplementaryConfiguration.BucketVersioningConfiguration.status WHERE resourceType = 'AWS::S3::Bucket' AND supplementaryConfiguration.BucketVersioningConfiguration.status = 'Off'.</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StoredQuery) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "query_arn" in value:
        out["QueryArn"] = value["query_arn"]
    out["QueryName"] = value["query_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "expression" in value:
        out["Expression"] = value["expression"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StoredQuery:
    out: StoredQuery = {}  # type: ignore[typeddict-item]
    if data.get("QueryId") is not None:
        out["query_id"] = data["QueryId"]
    if data.get("QueryArn") is not None:
        out["query_arn"] = data["QueryArn"]
    if data.get("QueryName") is not None:
        out["query_name"] = data["QueryName"]
    else:
        out["query_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Expression") is not None:
        out["expression"] = data["Expression"]
    return out
