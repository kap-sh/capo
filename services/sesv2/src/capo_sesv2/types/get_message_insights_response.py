"""Generated from Smithy shape ``com.amazonaws.sesv2#GetMessageInsightsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_insights_list
    import capo_sesv2.types.email_subject
    import capo_sesv2.types.insights_email_address
    import capo_sesv2.types.message_tag_list
    import capo_sesv2.types.outbound_message_id


class GetMessageInsightsResponse(TypedDict, closed=True):
    message_id: NotRequired["capo_sesv2.types.outbound_message_id.OutboundMessageId"]
    """<p>A unique identifier for the message.</p>"""
    from_email_address: NotRequired[
        "capo_sesv2.types.insights_email_address.InsightsEmailAddress"
    ]
    """<p>The from address used to send the message.</p>"""
    subject: NotRequired["capo_sesv2.types.email_subject.EmailSubject"]
    """<p>The subject line of the message.</p>"""
    email_tags: NotRequired["capo_sesv2.types.message_tag_list.MessageTagList"]
    """<p> A list of tags, in the form of name/value pairs, that were applied to the email you sent, along with Amazon SES <a href="https://docs.aws.amazon.com/ses/latest/dg/monitor-using-event-publishing.html">Auto-Tags</a>. </p>"""
    insights: NotRequired["capo_sesv2.types.email_insights_list.EmailInsightsList"]
    """<p>A set of insights associated with the message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMessageInsightsResponse) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["MessageId"] = value["message_id"]
    if "from_email_address" in value:
        out["FromEmailAddress"] = value["from_email_address"]
    if "subject" in value:
        out["Subject"] = value["subject"]
    if "email_tags" in value:
        import capo_sesv2.types.message_tag_list

        out["EmailTags"] = capo_sesv2.types.message_tag_list.serialize_json(
            value["email_tags"]
        )
    if "insights" in value:
        import capo_sesv2.types.email_insights_list

        out["Insights"] = capo_sesv2.types.email_insights_list.serialize_json(
            value["insights"]
        )
    return out


def deserialize_json(data: dict) -> GetMessageInsightsResponse:
    out: GetMessageInsightsResponse = {}  # type: ignore[typeddict-item]
    if data.get("MessageId") is not None:
        out["message_id"] = data["MessageId"]
    if data.get("FromEmailAddress") is not None:
        out["from_email_address"] = data["FromEmailAddress"]
    if data.get("Subject") is not None:
        out["subject"] = data["Subject"]
    if data.get("EmailTags") is not None:
        import capo_sesv2.types.message_tag_list

        out["email_tags"] = capo_sesv2.types.message_tag_list.deserialize_json(
            data["EmailTags"]
        )
    if data.get("Insights") is not None:
        import capo_sesv2.types.email_insights_list

        out["insights"] = capo_sesv2.types.email_insights_list.deserialize_json(
            data["Insights"]
        )
    return out
