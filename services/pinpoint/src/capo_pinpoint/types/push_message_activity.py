"""Generated from Smithy shape ``com.amazonaws.pinpoint#PushMessageActivity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.journey_push_message


class PushMessageActivity(TypedDict, closed=True):
    message_config: NotRequired[
        "capo_pinpoint.types.journey_push_message.JourneyPushMessage"
    ]
    """<p>Specifies the time to live (TTL) value for push notifications that are sent to participants in a journey.</p>"""
    next_activity: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the next activity to perform, after the message is sent.</p>"""
    template_name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The name of the push notification template to use for the message. If specified, this value must match the name of an existing message template.</p>"""
    template_version: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the version of the push notification template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the <link linkend="templates-template-name-template-type-versions">Template Versions</link> resource.</p> <p>If you don't specify a value for this property, Amazon Pinpoint uses the <i>active version</i> of the template. The <i>active version</i> is typically the version of a template that's been most recently reviewed and approved for use, depending on your workflow. It isn't necessarily the latest version of a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushMessageActivity) -> dict:
    out: dict = {}
    if "message_config" in value:
        import capo_pinpoint.types.journey_push_message

        out["MessageConfig"] = capo_pinpoint.types.journey_push_message.serialize_json(
            value["message_config"]
        )
    if "next_activity" in value:
        out["NextActivity"] = value["next_activity"]
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_version" in value:
        out["TemplateVersion"] = value["template_version"]
    return out


def deserialize_json(data: dict) -> PushMessageActivity:
    out: PushMessageActivity = {}  # type: ignore[typeddict-item]
    if data.get("MessageConfig") is not None:
        import capo_pinpoint.types.journey_push_message

        out["message_config"] = (
            capo_pinpoint.types.journey_push_message.deserialize_json(
                data["MessageConfig"]
            )
        )
    if data.get("NextActivity") is not None:
        out["next_activity"] = data["NextActivity"]
    if data.get("TemplateName") is not None:
        out["template_name"] = data["TemplateName"]
    if data.get("TemplateVersion") is not None:
        out["template_version"] = data["TemplateVersion"]
    return out
