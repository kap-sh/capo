"""Generated from Smithy shape ``com.amazonaws.kendra#FaqSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.faq_file_format
    import capo_kendra.types.faq_id
    import capo_kendra.types.faq_name
    import capo_kendra.types.faq_status
    import capo_kendra.types.language_code
    import capo_kendra.types.timestamp


class FaqSummary(TypedDict, closed=True):
    id: NotRequired["capo_kendra.types.faq_id.FaqId"]
    """<p>The identifier of the FAQ.</p>"""
    name: NotRequired["capo_kendra.types.faq_name.FaqName"]
    """<p>The name that you assigned the FAQ when you created or updated the FAQ.</p>"""
    status: NotRequired["capo_kendra.types.faq_status.FaqStatus"]
    """<p>The current status of the FAQ. When the status is <code>ACTIVE</code> the FAQ is ready for use.</p>"""
    created_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the FAQ was created.</p>"""
    updated_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the FAQ was last updated.</p>"""
    file_format: NotRequired["capo_kendra.types.faq_file_format.FaqFileFormat"]
    """<p>The file type used to create the FAQ. </p>"""
    language_code: NotRequired["capo_kendra.types.language_code.LanguageCode"]
    """<p>The code for a language. This shows a supported language for the FAQ document as part of the summary information for FAQs. English is supported by default. For more information on supported languages, including their codes, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html">Adding documents in languages other than English</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FaqSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import capo_kendra.types.faq_status

        out["Status"] = capo_kendra.types.faq_status.serialize_aws_json_1_1(
            value["status"]
        )
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
    if "file_format" in value:
        import capo_kendra.types.faq_file_format

        out["FileFormat"] = capo_kendra.types.faq_file_format.serialize_aws_json_1_1(
            value["file_format"]
        )
    if "language_code" in value:
        out["LanguageCode"] = value["language_code"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FaqSummary:
    out: FaqSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Status") is not None:
        import capo_kendra.types.faq_status

        out["status"] = capo_kendra.types.faq_status.deserialize_aws_json_1_1(
            data["Status"]
        )
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
    if data.get("FileFormat") is not None:
        import capo_kendra.types.faq_file_format

        out["file_format"] = capo_kendra.types.faq_file_format.deserialize_aws_json_1_1(
            data["FileFormat"]
        )
    if data.get("LanguageCode") is not None:
        out["language_code"] = data["LanguageCode"]
    return out
