"""Generated from Smithy shape ``com.amazonaws.pinpoint#CampaignEmailMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.list_of_message_header


class CampaignEmailMessage(TypedDict, closed=True):
    body: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The body of the email for recipients whose email clients don't render HTML content.</p>"""
    from_address: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The verified email address to send the email from. The default address is the FromAddress specified for the email channel for the application.</p>"""
    headers: NotRequired[
        "capo_pinpoint.types.list_of_message_header.ListOfMessageHeader"
    ]
    """<p>The list of <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-campaigns-campaign-id.html#apps-application-id-campaigns-campaign-id-model-messageheader">MessageHeaders</a> for the email. You can have up to 15 MessageHeaders for each email.</p>"""
    html_body: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The body of the email, in HTML format, for recipients whose email clients render HTML content.</p>"""
    title: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The subject line, or title, of the email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CampaignEmailMessage) -> dict:
    out: dict = {}
    if "body" in value:
        out["Body"] = value["body"]
    if "from_address" in value:
        out["FromAddress"] = value["from_address"]
    if "headers" in value:
        import capo_pinpoint.types.list_of_message_header

        out["Headers"] = capo_pinpoint.types.list_of_message_header.serialize_json(
            value["headers"]
        )
    if "html_body" in value:
        out["HtmlBody"] = value["html_body"]
    if "title" in value:
        out["Title"] = value["title"]
    return out


def deserialize_json(data: dict) -> CampaignEmailMessage:
    out: CampaignEmailMessage = {}  # type: ignore[typeddict-item]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    if data.get("FromAddress") is not None:
        out["from_address"] = data["FromAddress"]
    if data.get("Headers") is not None:
        import capo_pinpoint.types.list_of_message_header

        out["headers"] = capo_pinpoint.types.list_of_message_header.deserialize_json(
            data["Headers"]
        )
    if data.get("HtmlBody") is not None:
        out["html_body"] = data["HtmlBody"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    return out
