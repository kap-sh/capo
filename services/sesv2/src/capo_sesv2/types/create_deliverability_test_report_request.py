"""Generated from Smithy shape ``com.amazonaws.sesv2#CreateDeliverabilityTestReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sesv2.types.email_address
    import capo_sesv2.types.email_content
    import capo_sesv2.types.report_name
    import capo_sesv2.types.tag_list


class CreateDeliverabilityTestReportRequest(TypedDict, closed=True):
    report_name: NotRequired["capo_sesv2.types.report_name.ReportName"]
    """<p>A unique name that helps you to identify the predictive inbox placement test when you retrieve the results.</p>"""
    from_email_address: "capo_sesv2.types.email_address.EmailAddress"
    """<p>The email address that the predictive inbox placement test email was sent from.</p>"""
    content: "capo_sesv2.types.email_content.EmailContent"
    """<p>The HTML body of the message that you sent when you performed the predictive inbox placement test.</p>"""
    tags: NotRequired["capo_sesv2.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) that you want to associate with the predictive inbox placement test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeliverabilityTestReportRequest) -> dict:
    out: dict = {}
    if "report_name" in value:
        out["ReportName"] = value["report_name"]
    out["FromEmailAddress"] = value["from_email_address"]
    import capo_sesv2.types.email_content

    out["Content"] = capo_sesv2.types.email_content.serialize_json(value["content"])
    if "tags" in value:
        import capo_sesv2.types.tag_list

        out["Tags"] = capo_sesv2.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDeliverabilityTestReportRequest:
    out: CreateDeliverabilityTestReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("ReportName") is not None:
        out["report_name"] = data["ReportName"]
    if data.get("FromEmailAddress") is not None:
        out["from_email_address"] = data["FromEmailAddress"]
    else:
        out["from_email_address"] = ""
    if data.get("Content") is not None:
        import capo_sesv2.types.email_content

        out["content"] = capo_sesv2.types.email_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError(
            "CreateDeliverabilityTestReportRequest.content required"
        )
    if data.get("Tags") is not None:
        import capo_sesv2.types.tag_list

        out["tags"] = capo_sesv2.types.tag_list.deserialize_json(data["Tags"])
    return out
