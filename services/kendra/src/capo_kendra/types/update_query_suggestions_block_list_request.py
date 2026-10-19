"""Generated from Smithy shape ``com.amazonaws.kendra#UpdateQuerySuggestionsBlockListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.description
    import capo_kendra.types.index_id
    import capo_kendra.types.query_suggestions_block_list_id
    import capo_kendra.types.query_suggestions_block_list_name
    import capo_kendra.types.role_arn
    import capo_kendra.types.s3_path


class UpdateQuerySuggestionsBlockListRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the block list.</p>"""
    id: "capo_kendra.types.query_suggestions_block_list_id.QuerySuggestionsBlockListId"
    """<p>The identifier of the block list you want to update.</p>"""
    name: NotRequired[
        "capo_kendra.types.query_suggestions_block_list_name.QuerySuggestionsBlockListName"
    ]
    """<p>A new name for the block list.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>A new description for the block list.</p>"""
    source_s3_path: NotRequired["capo_kendra.types.s3_path.S3Path"]
    """<p>The S3 path where your block list text file sits in S3.</p> <p>If you update your block list and provide the same path to the block list text file in S3, then Amazon Kendra reloads the file to refresh the block list. Amazon Kendra does not automatically refresh your block list. You need to call the <code>UpdateQuerySuggestionsBlockList</code> API to refresh you block list.</p> <p>If you update your block list, then Amazon Kendra asynchronously refreshes all query suggestions with the latest content in the S3 file. This means changes might not take effect immediately.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>The IAM (Identity and Access Management) role used to access the block list text file in S3.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateQuerySuggestionsBlockListRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "source_s3_path" in value:
        import capo_kendra.types.s3_path

        out["SourceS3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(
            value["source_s3_path"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateQuerySuggestionsBlockListRequest:
    out: UpdateQuerySuggestionsBlockListRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        out["index_id"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SourceS3Path") is not None:
        import capo_kendra.types.s3_path

        out["source_s3_path"] = capo_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["SourceS3Path"]
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
