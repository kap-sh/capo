"""Generated from Smithy shape ``com.amazonaws.kendra#CreateThesaurusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.client_token_name
    import capo_kendra.types.description
    import capo_kendra.types.index_id
    import capo_kendra.types.role_arn
    import capo_kendra.types.s3_path
    import capo_kendra.types.tag_list
    import capo_kendra.types.thesaurus_name


class CreateThesaurusRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the thesaurus.</p>"""
    name: "capo_kendra.types.thesaurus_name.ThesaurusName"
    """<p>A name for the thesaurus.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>A description for the thesaurus.</p>"""
    role_arn: "capo_kendra.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket that contains the thesaurus file. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM access roles for Amazon Kendra</a>.</p>"""
    tags: NotRequired["capo_kendra.types.tag_list.TagList"]
    """<p>A list of key-value pairs that identify or categorize the thesaurus. You can also use tags to help control access to the thesaurus. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""
    source_s3_path: "capo_kendra.types.s3_path.S3Path"
    """<p>The path to the thesaurus file in S3.</p>"""
    client_token: NotRequired["capo_kendra.types.client_token_name.ClientTokenName"]
    """<p>A token that you provide to identify the request to create a thesaurus. Multiple calls to the <code>CreateThesaurus</code> API with the same client token will create only one thesaurus. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateThesaurusRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_kendra.types.tag_list

        out["Tags"] = capo_kendra.types.tag_list.serialize_aws_json_1_1(value["tags"])
    import capo_kendra.types.s3_path

    out["SourceS3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(
        value["source_s3_path"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateThesaurusRequest:
    out: CreateThesaurusRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("CreateThesaurusRequest.index_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateThesaurusRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreateThesaurusRequest.role_arn required")
    if data.get("Tags") is not None:
        import capo_kendra.types.tag_list

        out["tags"] = capo_kendra.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("SourceS3Path") is not None:
        import capo_kendra.types.s3_path

        out["source_s3_path"] = capo_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["SourceS3Path"]
        )
    else:
        raise DeserializationError("CreateThesaurusRequest.source_s3_path required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
