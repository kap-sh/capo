"""Generated from Smithy shape ``com.amazonaws.glue#GetIntegrationTablePropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.string128
    import capo_glue.types.string512


class GetIntegrationTablePropertiesRequest(TypedDict, closed=True):
    resource_arn: "capo_glue.types.string512.String512"
    """<p>The Amazon Resource Name (ARN) of the target table for which to retrieve integration table properties. Currently, this API only supports retrieving properties for target tables, and the provided ARN should be the ARN of the target table in the Glue Data Catalog. Support for retrieving integration table properties for source connections (using the connection ARN) is not yet implemented and will be added in a future release. </p>"""
    table_name: "capo_glue.types.string128.String128"
    """<p>The name of the table to be replicated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIntegrationTablePropertiesRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    out["TableName"] = value["table_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIntegrationTablePropertiesRequest:
    out: GetIntegrationTablePropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    return out
