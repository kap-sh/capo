"""Generated from Smithy shape ``com.amazonaws.qconnect#MessageTemplateContentProvider``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError, SerializationError
from capo_qconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qconnect.types.email_message_template_content
    import capo_qconnect.types.push_message_template_content
    import capo_qconnect.types.sms_message_template_content
    import capo_qconnect.types.whats_app_message_template_content


class _MessageTemplateContentProvider_email(TypedDict, closed=True):
    email: (
        "capo_qconnect.types.email_message_template_content.EmailMessageTemplateContent"
    )


class _MessageTemplateContentProvider_sms(TypedDict, closed=True):
    sms: "capo_qconnect.types.sms_message_template_content.SMSMessageTemplateContent"


class _MessageTemplateContentProvider_whatsApp(TypedDict, closed=True):
    whatsApp: "capo_qconnect.types.whats_app_message_template_content.WhatsAppMessageTemplateContent"


class _MessageTemplateContentProvider_push(TypedDict, closed=True):
    push: "capo_qconnect.types.push_message_template_content.PushMessageTemplateContent"


MessageTemplateContentProvider: TypeAlias = (
    _MessageTemplateContentProvider_email
    | _MessageTemplateContentProvider_sms
    | _MessageTemplateContentProvider_whatsApp
    | _MessageTemplateContentProvider_push
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MessageTemplateContentProvider) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MessageTemplateContentProvider: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "email" in value:
        import capo_qconnect.types.email_message_template_content

        return {
            "email": capo_qconnect.types.email_message_template_content.serialize_json(
                value["email"]
            )
        }
    elif "sms" in value:
        import capo_qconnect.types.sms_message_template_content

        return {
            "sms": capo_qconnect.types.sms_message_template_content.serialize_json(
                value["sms"]
            )
        }
    elif "whatsApp" in value:
        import capo_qconnect.types.whats_app_message_template_content

        return {
            "whatsApp": capo_qconnect.types.whats_app_message_template_content.serialize_json(
                value["whatsApp"]
            )
        }
    elif "push" in value:
        import capo_qconnect.types.push_message_template_content

        return {
            "push": capo_qconnect.types.push_message_template_content.serialize_json(
                value["push"]
            )
        }
    else:
        raise SerializationError("MessageTemplateContentProvider: no variant present")


def deserialize_json(data: dict) -> MessageTemplateContentProvider:
    if data.get("email") is not None:
        import capo_qconnect.types.email_message_template_content

        return {
            "email": capo_qconnect.types.email_message_template_content.deserialize_json(
                data["email"]
            )
        }
    elif data.get("sms") is not None:
        import capo_qconnect.types.sms_message_template_content

        return {
            "sms": capo_qconnect.types.sms_message_template_content.deserialize_json(
                data["sms"]
            )
        }
    elif data.get("whatsApp") is not None:
        import capo_qconnect.types.whats_app_message_template_content

        return {
            "whatsApp": capo_qconnect.types.whats_app_message_template_content.deserialize_json(
                data["whatsApp"]
            )
        }
    elif data.get("push") is not None:
        import capo_qconnect.types.push_message_template_content

        return {
            "push": capo_qconnect.types.push_message_template_content.deserialize_json(
                data["push"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "MessageTemplateContentProvider: no recognized variant key"
        )


def redact_sensitive(value: MessageTemplateContentProvider) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email" in value:
        import capo_qconnect.types.email_message_template_content

        out["email"] = (
            capo_qconnect.types.email_message_template_content.redact_sensitive(
                value["email"]
            )
        )
    if "sms" in value:
        import capo_qconnect.types.sms_message_template_content

        out["sms"] = capo_qconnect.types.sms_message_template_content.redact_sensitive(
            value["sms"]
        )
    if "push" in value:
        import capo_qconnect.types.push_message_template_content

        out["push"] = (
            capo_qconnect.types.push_message_template_content.redact_sensitive(
                value["push"]
            )
        )
    return out
