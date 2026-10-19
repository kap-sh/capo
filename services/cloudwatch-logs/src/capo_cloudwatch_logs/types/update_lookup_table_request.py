"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#UpdateLookupTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.kms_key_id
    import capo_cloudwatch_logs.types.lookup_table_description
    import capo_cloudwatch_logs.types.query_id
    import capo_cloudwatch_logs.types.table_body


class UpdateLookupTableRequest(TypedDict, closed=True):
    lookup_table_arn: "capo_cloudwatch_logs.types.arn.Arn"
    """<p>The ARN of the lookup table to update.</p>"""
    description: NotRequired[
        "capo_cloudwatch_logs.types.lookup_table_description.LookupTableDescription"
    ]
    """<p>An updated description of the lookup table.</p>"""
    table_body: NotRequired["capo_cloudwatch_logs.types.table_body.TableBody"]
    """<p>The new CSV content to replace the existing data. The first row must be a header row with column names. The content must use UTF-8 encoding and not exceed 10 MB.</p> <p>You must specify either <code>tableBody</code> or <code>queryId</code>, but not both.</p>"""
    query_id: NotRequired["capo_cloudwatch_logs.types.query_id.QueryId"]
    """<p>The ID of a completed or cancelled CloudWatch Logs query whose results replace the lookup table content. A cancelled query replaces the content with the partial results that were available when the query was stopped.</p> <p>You must specify either <code>tableBody</code> or <code>queryId</code>, but not both.</p>"""
    kms_key_id: NotRequired["capo_cloudwatch_logs.types.kms_key_id.KmsKeyId"]
    """<p>The ARN of the KMS key to use to encrypt the lookup table data. You can use this parameter to add, update, or remove the KMS key. To remove the KMS key and use an Amazon Web Services-owned key instead, specify an empty string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLookupTableRequest) -> dict:
    out: dict = {}
    out["lookupTableArn"] = value["lookup_table_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "table_body" in value:
        out["tableBody"] = value["table_body"]
    if "query_id" in value:
        out["queryId"] = value["query_id"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLookupTableRequest:
    out: UpdateLookupTableRequest = {}  # type: ignore[typeddict-item]
    if data.get("lookupTableArn") is not None:
        out["lookup_table_arn"] = data["lookupTableArn"]
    else:
        out["lookup_table_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tableBody") is not None:
        out["table_body"] = data["tableBody"]
    if data.get("queryId") is not None:
        out["query_id"] = data["queryId"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
