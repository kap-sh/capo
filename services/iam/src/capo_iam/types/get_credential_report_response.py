"""Generated from Smithy shape ``com.amazonaws.iam#GetCredentialReportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.date_type
    import capo_iam.types.report_content_type
    import capo_iam.types.report_format_type


class GetCredentialReportResponse(TypedDict, closed=True):
    content: NotRequired["capo_iam.types.report_content_type.ReportContentType"]
    """<p>Contains the credential report. The report is Base64-encoded.</p>"""
    report_format: NotRequired["capo_iam.types.report_format_type.ReportFormatType"]
    """<p>The format (MIME type) of the credential report.</p>"""
    generated_time: NotRequired["capo_iam.types.date_type.dateType"]
    """<p> The date and time when the credential report was created, in <a href="http://www.iso.org/iso/iso8601">ISO 8601 date-time format</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetCredentialReportResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "content" in value:
        import capo_iam.types.report_content_type

        capo_iam.types.report_content_type.serialize_query(
            value["content"], pairs, f"{key_prefix}Content"
        )
    if "report_format" in value:
        import capo_iam.types.report_format_type

        capo_iam.types.report_format_type.serialize_query(
            value["report_format"], pairs, f"{key_prefix}ReportFormat"
        )
    if "generated_time" in value:
        import capo_iam.types.date_type

        capo_iam.types.date_type.serialize_query(
            value["generated_time"], pairs, f"{key_prefix}GeneratedTime"
        )


def deserialize_query(el: Element) -> GetCredentialReportResponse:
    out: GetCredentialReportResponse = {}  # type: ignore[typeddict-item]
    child_content = el.find("Content")
    if child_content is not None:
        import capo_iam.types.report_content_type

        out["content"] = capo_iam.types.report_content_type.deserialize_query(
            child_content
        )
    child_report_format = el.find("ReportFormat")
    if child_report_format is not None:
        import capo_iam.types.report_format_type

        out["report_format"] = capo_iam.types.report_format_type.deserialize_query(
            child_report_format
        )
    child_generated_time = el.find("GeneratedTime")
    if child_generated_time is not None:
        import capo_iam.types.date_type

        out["generated_time"] = capo_iam.types.date_type.deserialize_query(
            child_generated_time
        )
    return out
