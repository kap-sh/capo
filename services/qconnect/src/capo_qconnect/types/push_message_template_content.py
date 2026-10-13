"""Generated from Smithy shape ``com.amazonaws.qconnect#PushMessageTemplateContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.push_adm_message_template_content
    import capo_qconnect.types.push_apns_message_template_content
    import capo_qconnect.types.push_baidu_message_template_content
    import capo_qconnect.types.push_fcm_message_template_content


class PushMessageTemplateContent(TypedDict, closed=True):
    adm: NotRequired[
        "capo_qconnect.types.push_adm_message_template_content.PushADMMessageTemplateContent"
    ]
    """<p>The content of the message template that applies to ADM (Amazon Device Messaging) notification service.</p>"""
    apns: NotRequired[
        "capo_qconnect.types.push_apns_message_template_content.PushAPNSMessageTemplateContent"
    ]
    """<p>The content of the message template that applies to APNS(Apple Push Notification service) notification service.</p>"""
    fcm: NotRequired[
        "capo_qconnect.types.push_fcm_message_template_content.PushFCMMessageTemplateContent"
    ]
    """<p>The content of the message template that applies to FCM (Firebase Cloud Messaging) notification service.</p>"""
    baidu: NotRequired[
        "capo_qconnect.types.push_baidu_message_template_content.PushBaiduMessageTemplateContent"
    ]
    """<p>The content of the message template that applies to Baidu notification service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushMessageTemplateContent) -> dict:
    out: dict = {}
    if "adm" in value:
        import capo_qconnect.types.push_adm_message_template_content

        out["adm"] = (
            capo_qconnect.types.push_adm_message_template_content.serialize_json(
                value["adm"]
            )
        )
    if "apns" in value:
        import capo_qconnect.types.push_apns_message_template_content

        out["apns"] = (
            capo_qconnect.types.push_apns_message_template_content.serialize_json(
                value["apns"]
            )
        )
    if "fcm" in value:
        import capo_qconnect.types.push_fcm_message_template_content

        out["fcm"] = (
            capo_qconnect.types.push_fcm_message_template_content.serialize_json(
                value["fcm"]
            )
        )
    if "baidu" in value:
        import capo_qconnect.types.push_baidu_message_template_content

        out["baidu"] = (
            capo_qconnect.types.push_baidu_message_template_content.serialize_json(
                value["baidu"]
            )
        )
    return out


def deserialize_json(data: dict) -> PushMessageTemplateContent:
    out: PushMessageTemplateContent = {}  # type: ignore[typeddict-item]
    if data.get("adm") is not None:
        import capo_qconnect.types.push_adm_message_template_content

        out["adm"] = (
            capo_qconnect.types.push_adm_message_template_content.deserialize_json(
                data["adm"]
            )
        )
    if data.get("apns") is not None:
        import capo_qconnect.types.push_apns_message_template_content

        out["apns"] = (
            capo_qconnect.types.push_apns_message_template_content.deserialize_json(
                data["apns"]
            )
        )
    if data.get("fcm") is not None:
        import capo_qconnect.types.push_fcm_message_template_content

        out["fcm"] = (
            capo_qconnect.types.push_fcm_message_template_content.deserialize_json(
                data["fcm"]
            )
        )
    if data.get("baidu") is not None:
        import capo_qconnect.types.push_baidu_message_template_content

        out["baidu"] = (
            capo_qconnect.types.push_baidu_message_template_content.deserialize_json(
                data["baidu"]
            )
        )
    return out


def redact_sensitive(value: PushMessageTemplateContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "adm" in value:
        import capo_qconnect.types.push_adm_message_template_content

        out["adm"] = (
            capo_qconnect.types.push_adm_message_template_content.redact_sensitive(
                value["adm"]
            )
        )
    if "apns" in value:
        import capo_qconnect.types.push_apns_message_template_content

        out["apns"] = (
            capo_qconnect.types.push_apns_message_template_content.redact_sensitive(
                value["apns"]
            )
        )
    if "fcm" in value:
        import capo_qconnect.types.push_fcm_message_template_content

        out["fcm"] = (
            capo_qconnect.types.push_fcm_message_template_content.redact_sensitive(
                value["fcm"]
            )
        )
    if "baidu" in value:
        import capo_qconnect.types.push_baidu_message_template_content

        out["baidu"] = (
            capo_qconnect.types.push_baidu_message_template_content.redact_sensitive(
                value["baidu"]
            )
        )
    return out
