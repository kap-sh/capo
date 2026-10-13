"""Generated from Smithy shape ``com.amazonaws.qconnect#PushBaiduMessageTemplateContent``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.message_template_body_content_provider
    import capo_qconnect.types.non_empty_unlimited_string
    import capo_qconnect.types.push_message_action


class PushBaiduMessageTemplateContent(TypedDict, closed=True):
    title: NotRequired[
        "capo_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The title to use in a push notification that's based on the message template. This title appears above the notification message on a recipient's device.</p>"""
    body: NotRequired[
        "capo_qconnect.types.message_template_body_content_provider.MessageTemplateBodyContentProvider"
    ]
    """<p>The message body to use in a push notification that is based on the message template.</p>"""
    action: NotRequired["capo_qconnect.types.push_message_action.PushMessageAction"]
    """<p>The action to occur if a recipient taps a push notification that is based on the message template. Valid values are:</p> <ul> <li> <p> <code>OPEN_APP</code> - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.</p> </li> <li> <p> <code>DEEP_LINK</code> - Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform.</p> </li> <li> <p> <code>URL</code> - The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.</p> </li> </ul>"""
    sound: NotRequired[
        "capo_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The sound to play when a recipient receives a push notification that's based on the message template. You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in <code>/res/raw/</code>.</p>"""
    url: NotRequired[
        "capo_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The URL to open in a recipient's default mobile browser, if a recipient taps a push notification that's based on the message template and the value of the <code>action</code> property is <code>URL</code>.</p>"""
    image_url: NotRequired[
        "capo_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The URL of an image to display in a push notification that's based on the message template.</p>"""
    image_icon_url: NotRequired[
        "capo_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The URL of the large icon image to display in the content view of a push notification that's based on the message template.</p>"""
    small_image_icon_url: NotRequired[
        "capo_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString"
    ]
    """<p>The URL of the small icon image to display in the status bar and the content view of a push notification that's based on the message template.</p>"""
    raw_content: NotRequired[
        "capo_qconnect.types.message_template_body_content_provider.MessageTemplateBodyContentProvider"
    ]
    """<p>The URL of the small icon image to display in the status bar and the content view of a push notification that's based on the message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushBaiduMessageTemplateContent) -> dict:
    out: dict = {}
    if "title" in value:
        out["title"] = value["title"]
    if "body" in value:
        import capo_qconnect.types.message_template_body_content_provider

        out["body"] = (
            capo_qconnect.types.message_template_body_content_provider.serialize_json(
                value["body"]
            )
        )
    if "action" in value:
        out["action"] = value["action"]
    if "sound" in value:
        out["sound"] = value["sound"]
    if "url" in value:
        out["url"] = value["url"]
    if "image_url" in value:
        out["imageUrl"] = value["image_url"]
    if "image_icon_url" in value:
        out["imageIconUrl"] = value["image_icon_url"]
    if "small_image_icon_url" in value:
        out["smallImageIconUrl"] = value["small_image_icon_url"]
    if "raw_content" in value:
        import capo_qconnect.types.message_template_body_content_provider

        out["rawContent"] = (
            capo_qconnect.types.message_template_body_content_provider.serialize_json(
                value["raw_content"]
            )
        )
    return out


def deserialize_json(data: dict) -> PushBaiduMessageTemplateContent:
    out: PushBaiduMessageTemplateContent = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("body") is not None:
        import capo_qconnect.types.message_template_body_content_provider

        out["body"] = (
            capo_qconnect.types.message_template_body_content_provider.deserialize_json(
                data["body"]
            )
        )
    if data.get("action") is not None:
        out["action"] = data["action"]
    if data.get("sound") is not None:
        out["sound"] = data["sound"]
    if data.get("url") is not None:
        out["url"] = data["url"]
    if data.get("imageUrl") is not None:
        out["image_url"] = data["imageUrl"]
    if data.get("imageIconUrl") is not None:
        out["image_icon_url"] = data["imageIconUrl"]
    if data.get("smallImageIconUrl") is not None:
        out["small_image_icon_url"] = data["smallImageIconUrl"]
    if data.get("rawContent") is not None:
        import capo_qconnect.types.message_template_body_content_provider

        out["raw_content"] = (
            capo_qconnect.types.message_template_body_content_provider.deserialize_json(
                data["rawContent"]
            )
        )
    return out


def redact_sensitive(value: PushBaiduMessageTemplateContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "body" in value:
        import capo_qconnect.types.message_template_body_content_provider

        out["body"] = (
            capo_qconnect.types.message_template_body_content_provider.redact_sensitive(
                value["body"]
            )
        )
    if "sound" in value:
        out["sound"] = "*** Sensitive Data Redacted ***"
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    if "image_url" in value:
        out["image_url"] = "*** Sensitive Data Redacted ***"
    if "image_icon_url" in value:
        out["image_icon_url"] = "*** Sensitive Data Redacted ***"
    if "small_image_icon_url" in value:
        out["small_image_icon_url"] = "*** Sensitive Data Redacted ***"
    if "raw_content" in value:
        import capo_qconnect.types.message_template_body_content_provider

        out["raw_content"] = (
            capo_qconnect.types.message_template_body_content_provider.redact_sensitive(
                value["raw_content"]
            )
        )
    return out
