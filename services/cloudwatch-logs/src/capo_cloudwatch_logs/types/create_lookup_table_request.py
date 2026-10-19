"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateLookupTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.kms_key_id
    import capo_cloudwatch_logs.types.lookup_table_description
    import capo_cloudwatch_logs.types.lookup_table_name
    import capo_cloudwatch_logs.types.query_id
    import capo_cloudwatch_logs.types.table_body
    import capo_cloudwatch_logs.types.tags


class CreateLookupTableRequest(TypedDict, closed=True):
    lookup_table_name: "capo_cloudwatch_logs.types.lookup_table_name.LookupTableName"
    """<p>The name of the lookup table. The name must be unique within your account and Region. The name can contain only alphanumeric characters and underscores, and can be up to 256 characters long.</p>"""
    description: NotRequired[
        "capo_cloudwatch_logs.types.lookup_table_description.LookupTableDescription"
    ]
    """<p>A description of the lookup table. The description can be up to 1024 characters long.</p>"""
    table_body: NotRequired["capo_cloudwatch_logs.types.table_body.TableBody"]
    """<p>The CSV content of the lookup table. The first row must be a header row with column names. The content must use UTF-8 encoding and not exceed 10 MB.</p> <p>You must specify either <code>tableBody</code> or <code>queryId</code>, but not both.</p>"""
    query_id: NotRequired["capo_cloudwatch_logs.types.query_id.QueryId"]
    """<p>The ID of a completed or cancelled CloudWatch Logs query whose results populate the lookup table. A cancelled query populates the table with the partial results that were available when the query was stopped.</p> <p>You must specify either <code>tableBody</code> or <code>queryId</code>, but not both.</p>"""
    kms_key_id: NotRequired["capo_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    """<p>The ARN of the KMS key to use to encrypt the lookup table data. If you don't specify a key, the data is encrypted with an Amazon Web Services-owned key.</p>"""
    tags: NotRequired["capo_cloudwatch_logs.types.tags.Tags"]
    """<p>A list of key-value pairs to associate with the lookup table. You can associate as many as 50 tags with a lookup table. Tags can help you organize and categorize your resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLookupTableRequest) -> dict:
    out: dict = {}
    out["lookupTableName"] = value["lookup_table_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "table_body" in value:
        out["tableBody"] = value["table_body"]
    if "query_id" in value:
        out["queryId"] = value["query_id"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLookupTableRequest:
    out: CreateLookupTableRequest = {}  # type: ignore[typeddict-item]
    if data.get("lookupTableName") is not None:
        out["lookup_table_name"] = data["lookupTableName"]
    else:
        out["lookup_table_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tableBody") is not None:
        out["table_body"] = data["tableBody"]
    if data.get("queryId") is not None:
        out["query_id"] = data["queryId"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_cloudwatch_logs.types.tags

        out["tags"] = capo_cloudwatch_logs.types.tags.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
