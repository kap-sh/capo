"""Generated from Smithy shape ``com.amazonaws.glue#DeleteIntegrationTablePropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.string128
    import capo_glue.types.string512


class DeleteIntegrationTablePropertiesRequest(TypedDict, closed=True):
    resource_arn: "capo_glue.types.string512.String512"
    """<p>The connection ARN of the source, or the database ARN of the target.</p>"""
    table_name: "capo_glue.types.string128.String128"
    """<p>The name of the table to be replicated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteIntegrationTablePropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteIntegrationTablePropertiesRequest:
    out: DeleteIntegrationTablePropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    return out
