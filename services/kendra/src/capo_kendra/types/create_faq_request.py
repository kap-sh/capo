"""Generated from Smithy shape ``com.amazonaws.kendra#CreateFaqRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.client_token_name
    import capo_kendra.types.description
    import capo_kendra.types.faq_file_format
    import capo_kendra.types.faq_name
    import capo_kendra.types.index_id
    import capo_kendra.types.language_code
    import capo_kendra.types.role_arn
    import capo_kendra.types.s3_path
    import capo_kendra.types.tag_list


class CreateFaqRequest(TypedDict, closed=True):
    index_id: "capo_kendra.types.index_id.IndexId"
    """<p>The identifier of the index for the FAQ.</p>"""
    name: "capo_kendra.types.faq_name.FaqName"
    """<p>A name for the FAQ.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>A description for the FAQ.</p>"""
    s3_path: "capo_kendra.types.s3_path.S3Path"
    """<p>The path to the FAQ file in S3.</p>"""
    role_arn: "capo_kendra.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access the S3 bucket that contains the FAQ file. For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html">IAM access roles for Amazon Kendra</a>.</p>"""
    tags: NotRequired["capo_kendra.types.tag_list.TagList"]
    """<p>A list of key-value pairs that identify the FAQ. You can use the tags to identify and organize your resources and to control access to resources.</p>"""
    file_format: NotRequired["capo_kendra.types.faq_file_format.FaqFileFormat"]
    """<p>The format of the FAQ input file. You can choose between a basic CSV format, a CSV format that includes customs attributes in a header, and a JSON format that includes custom attributes.</p> <p>The default format is CSV.</p> <p>The format must match the format of the file stored in the S3 bucket identified in the <code>S3Path</code> parameter.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html">Adding questions and answers</a>.</p>"""
    client_token: NotRequired["capo_kendra.types.client_token_name.ClientTokenName"]
    """<p>A token that you provide to identify the request to create a FAQ. Multiple calls to the <code>CreateFaqRequest</code> API with the same client token will create only one FAQ. </p>"""
    language_code: NotRequired["capo_kendra.types.language_code.LanguageCode"]
    """<p>The code for a language. This allows you to support a language for the FAQ document. English is supported by default. For more information on supported languages, including their codes, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html">Adding documents in languages other than English</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateFaqRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_kendra.types.s3_path

    out["S3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(value["s3_path"])
    out["RoleArn"] = value["role_arn"]
    if "tags" in value:
        import capo_kendra.types.tag_list

        out["Tags"] = capo_kendra.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "file_format" in value:
        import capo_kendra.types.faq_file_format

        out["FileFormat"] = capo_kendra.types.faq_file_format.serialize_aws_json_1_1(
            value["file_format"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateFaqRequest:
    out: CreateFaqRequest = {}  # type: ignore[typeddict-item]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("CreateFaqRequest.index_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateFaqRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("S3Path") is not None:
        import capo_kendra.types.s3_path

        out["s3_path"] = capo_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["S3Path"]
        )
    else:
        raise DeserializationError("CreateFaqRequest.s3_path required")
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    else:
        raise DeserializationError("CreateFaqRequest.role_arn required")
    if data.get("Tags") is not None:
        import capo_kendra.types.tag_list

        out["tags"] = capo_kendra.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    if data.get("FileFormat") is not None:
        import capo_kendra.types.faq_file_format

        out["file_format"] = capo_kendra.types.faq_file_format.deserialize_aws_json_1_1(
            data["FileFormat"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("LanguageCode") is not None:
        out["language_code"] = data["LanguageCode"]
    return out
