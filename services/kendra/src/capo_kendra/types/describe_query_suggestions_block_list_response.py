"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeQuerySuggestionsBlockListResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.description
    import capo_kendra.types.error_message
    import capo_kendra.types.index_id
    import capo_kendra.types.integer
    import capo_kendra.types.long
    import capo_kendra.types.query_suggestions_block_list_id
    import capo_kendra.types.query_suggestions_block_list_name
    import capo_kendra.types.query_suggestions_block_list_status
    import capo_kendra.types.role_arn
    import capo_kendra.types.s3_path
    import capo_kendra.types.timestamp


class DescribeQuerySuggestionsBlockListResponse(TypedDict, closed=True):
    index_id: NotRequired["capo_kendra.types.index_id.IndexId"]
    """<p>The identifier of the index for the block list.</p>"""
    id: NotRequired[
        "capo_kendra.types.query_suggestions_block_list_id.QuerySuggestionsBlockListId"
    ]
    """<p>The identifier of the block list.</p>"""
    name: NotRequired[
        "capo_kendra.types.query_suggestions_block_list_name.QuerySuggestionsBlockListName"
    ]
    """<p>The name of the block list.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>The description for the block list.</p>"""
    status: NotRequired[
        "capo_kendra.types.query_suggestions_block_list_status.QuerySuggestionsBlockListStatus"
    ]
    """<p>The current status of the block list. When the value is <code>ACTIVE</code>, the block list is ready for use.</p>"""
    error_message: NotRequired["capo_kendra.types.error_message.ErrorMessage"]
    """<p>The error message containing details if there are issues processing the block list.</p>"""
    created_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when a block list for query suggestions was created.</p>"""
    updated_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when a block list for query suggestions was last updated.</p>"""
    source_s3_path: NotRequired["capo_kendra.types.s3_path.S3Path"]
    """<p>Shows the current S3 path to your block list text file in your S3 bucket.</p> <p>Each block word or phrase should be on a separate line in a text file.</p> <p>For information on the current quota limits for block lists, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas for Amazon Kendra</a>.</p>"""
    item_count: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>The current number of valid, non-empty words or phrases in the block list text file.</p>"""
    file_size_bytes: NotRequired["capo_kendra.types.long.Long"]
    """<p>The current size of the block list text file in S3.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>The IAM (Identity and Access Management) role used by Amazon Kendra to access the block list text file in S3.</p> <p>The role needs S3 read permissions to your file in S3 and needs to give STS (Security Token Service) assume role permissions to Amazon Kendra.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeQuerySuggestionsBlockListResponse) -> dict:
    out: dict = {}
    if "index_id" in value:
        out["IndexId"] = value["index_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "status" in value:
        import capo_kendra.types.query_suggestions_block_list_status

        out["Status"] = (
            capo_kendra.types.query_suggestions_block_list_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "created_at" in value:
        import capo_kendra.types.timestamp

        out["CreatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_kendra.types.timestamp

        out["UpdatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "source_s3_path" in value:
        import capo_kendra.types.s3_path

        out["SourceS3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(
            value["source_s3_path"]
        )
    if "item_count" in value:
        out["ItemCount"] = value["item_count"]
    if "file_size_bytes" in value:
        out["FileSizeBytes"] = value["file_size_bytes"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeQuerySuggestionsBlockListResponse:
    out: DescribeQuerySuggestionsBlockListResponse = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Status") is not None:
        import capo_kendra.types.query_suggestions_block_list_status

        out["status"] = (
            capo_kendra.types.query_suggestions_block_list_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("CreatedAt") is not None:
        import capo_kendra.types.timestamp

        out["created_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_kendra.types.timestamp

        out["updated_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if data.get("SourceS3Path") is not None:
        import capo_kendra.types.s3_path

        out["source_s3_path"] = capo_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["SourceS3Path"]
        )
    if data.get("ItemCount") is not None:
        out["item_count"] = data["ItemCount"]
    if data.get("FileSizeBytes") is not None:
        out["file_size_bytes"] = data["FileSizeBytes"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
