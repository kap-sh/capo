"""Generated from Smithy shape ``com.amazonaws.kendra#DescribeFaqResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.description
    import capo_kendra.types.error_message
    import capo_kendra.types.faq_file_format
    import capo_kendra.types.faq_id
    import capo_kendra.types.faq_name
    import capo_kendra.types.faq_status
    import capo_kendra.types.index_id
    import capo_kendra.types.language_code
    import capo_kendra.types.role_arn
    import capo_kendra.types.s3_path
    import capo_kendra.types.timestamp


class DescribeFaqResponse(TypedDict, closed=True):
    id: NotRequired["capo_kendra.types.faq_id.FaqId"]
    """<p>The identifier of the FAQ.</p>"""
    index_id: NotRequired["capo_kendra.types.index_id.IndexId"]
    """<p>The identifier of the index for the FAQ.</p>"""
    name: NotRequired["capo_kendra.types.faq_name.FaqName"]
    """<p>The name that you gave the FAQ when it was created.</p>"""
    description: NotRequired["capo_kendra.types.description.Description"]
    """<p>The description of the FAQ that you provided when it was created.</p>"""
    created_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the FAQ was created.</p>"""
    updated_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the FAQ was last updated.</p>"""
    s3_path: NotRequired["capo_kendra.types.s3_path.S3Path"]
    status: NotRequired["capo_kendra.types.faq_status.FaqStatus"]
    """<p>The status of the FAQ. It is ready to use when the status is <code>ACTIVE</code>.</p>"""
    role_arn: NotRequired["capo_kendra.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that provides access to the S3 bucket containing the FAQ file.</p>"""
    error_message: NotRequired["capo_kendra.types.error_message.ErrorMessage"]
    """<p>If the <code>Status</code> field is <code>FAILED</code>, the <code>ErrorMessage</code> field contains the reason why the FAQ failed.</p>"""
    file_format: NotRequired["capo_kendra.types.faq_file_format.FaqFileFormat"]
    """<p>The file format used for the FAQ file.</p>"""
    language_code: NotRequired["capo_kendra.types.language_code.LanguageCode"]
    """<p>The code for a language. This shows a supported language for the FAQ document. English is supported by default. For more information on supported languages, including their codes, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html">Adding documents in languages other than English</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeFaqResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "index_id" in value:
        out["IndexId"] = value["index_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
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
    if "s3_path" in value:
        import capo_kendra.types.s3_path

        out["S3Path"] = capo_kendra.types.s3_path.serialize_aws_json_1_1(
            value["s3_path"]
        )
    if "status" in value:
        import capo_kendra.types.faq_status

        out["Status"] = capo_kendra.types.faq_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "file_format" in value:
        import capo_kendra.types.faq_file_format

        out["FileFormat"] = capo_kendra.types.faq_file_format.serialize_aws_json_1_1(
            value["file_format"]
        )
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeFaqResponse:
    out: DescribeFaqResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("IndexId") is not None:
        out["index_id"] = data["IndexId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
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
    if data.get("S3Path") is not None:
        import capo_kendra.types.s3_path

        out["s3_path"] = capo_kendra.types.s3_path.deserialize_aws_json_1_1(
            data["S3Path"]
        )
    if data.get("Status") is not None:
        import capo_kendra.types.faq_status

        out["status"] = capo_kendra.types.faq_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("FileFormat") is not None:
        import capo_kendra.types.faq_file_format

        out["file_format"] = capo_kendra.types.faq_file_format.deserialize_aws_json_1_1(
            data["FileFormat"]
        )
    if data.get("LanguageCode") is not None:
        out["language_code"] = data["LanguageCode"]
    return out
