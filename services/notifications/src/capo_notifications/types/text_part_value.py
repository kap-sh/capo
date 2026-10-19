"""Generated from Smithy shape ``com.amazonaws.notifications#TextPartValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.text_by_locale
    import capo_notifications.types.text_part_type
    import capo_notifications.types.url


class TextPartValue(TypedDict, closed=True):
    type: "capo_notifications.types.text_part_type.TextPartType"
    """<p>The type of text part. Determines the usage of all other fields and whether or not they're required.</p>"""
    display_text: NotRequired["str"]
    """<p>A short single line description of the link. Must be hyper-linked with the URL itself. </p> <p>Used for text parts with the type <code>URL</code>.</p>"""
    text_by_locale: NotRequired["capo_notifications.types.text_by_locale.TextByLocale"]
    """<p>A map of locales to the text in that locale.</p>"""
    url: NotRequired["capo_notifications.types.url.Url"]
    """<p>The URL itself.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TextPartValue) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "display_text" in value:
        out["displayText"] = value["display_text"]
    if "text_by_locale" in value:
        import capo_notifications.types.text_by_locale

        out["textByLocale"] = capo_notifications.types.text_by_locale.serialize_json(
            value["text_by_locale"]
        )
    if "url" in value:
        out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> TextPartValue:
    out: TextPartValue = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    else:
        out["type"] = ""
    if data.get("displayText") is not None:
        out["display_text"] = data["displayText"]
    if data.get("textByLocale") is not None:
        import capo_notifications.types.text_by_locale

        out["text_by_locale"] = (
            capo_notifications.types.text_by_locale.deserialize_json(
                data["textByLocale"]
            )
        )
    if data.get("url") is not None:
        out["url"] = data["url"]
    return out
