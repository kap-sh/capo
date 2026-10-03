"""Generated from Smithy shape ``com.amazonaws.kendra#CreateQuerySuggestionsBlockListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.client_token_name
    import capo_kendra.types.description
    import capo_kendra.types.index_id
    import capo_kendra.types.query_suggestions_block_list_name
    import capo_kendra.types.role_arn
    import capo_kendra.types.s3_path
    import capo_kendra.types.tag_list


class CreateQuerySuggestionsBlockListRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index you want to create a query suggestions block list for.</p>"""
    name: "capo_kendra.types.query_suggestions_block_list_name.QuerySuggestionsBlockListName"
    """<p>A name for the block list.</p> <p>For example, the name 'offensive-words', which includes all offensive words that could appear in user queries and need to be blocked from suggestions.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>A description for the block list.</p> <p>For example, the description "List of all offensive words that can appear in user queries and need to be blocked from suggestions."</p>"""
    source_s3_path: "capo_kendra.types.s3_path.S3Path"
    """<p>The S3 path to your block list text file in your S3 bucket.</p> <p>Each block word or phrase should be on a separate line in a text file.</p> <p>For information on the current quota limits for block lists, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/quotas.html">Quotas for Amazon Kendra</a>.</p>"""
    client_token: NotRequired["capo_kendra.types.client_token_name.ClientTokenName"]
    """<p>A token that you provide to identify the request to create a query suggestions block list.</p>"""
    role_arn: "capo_kendra.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket that contains the block list text file. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM access roles for Amazon Kendra</a>.</p>"""
    tags: NotRequired["capo_kendra.types.tag_list.TagList"]
    """<p>A list of key-value pairs that identify or categorize the block list. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateQuerySuggestionsBlockListRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_kendra.types.s3_path

    out["SourceS3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(
        value["source_s3_path"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_kendra.types.tag_list

        out["Tags"] = capo_kendra.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateQuerySuggestionsBlockListRequest:
    out: CreateQuerySuggestionsBlockListRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError(
            "CreateQuerySuggestionsBlockListRequest.index_id required"
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError(
            "CreateQuerySuggestionsBlockListRequest.name required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SourceS3Path") is not None:
        import capo_kendra.types.s3_path

        out["source_s3_path"] = capo_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["SourceS3Path"]
        )
    else:
        raise DeserializationError(
            "CreateQuerySuggestionsBlockListRequest.source_s3_path required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError(
            "CreateQuerySuggestionsBlockListRequest.role_arn required"
        )
    if data.get("Tags") is not None:
        import capo_kendra.types.tag_list

        out["tags"] = capo_kendra.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    return out
