"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ImageResponseCard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.attachment_title
    import capo_lex_models_v2.types.attachment_url
    import capo_lex_models_v2.types.buttons_list


class ImageResponseCard(TypedDict, closed=True):
    title: "capo_lex_models_v2.types.attachment_title.AttachmentTitle"
    """<p>The title to display on the response card. The format of the title is determined by the platform displaying the response card.</p>"""
    subtitle: NotRequired["capo_lex_models_v2.types.attachment_title.AttachmentTitle"]
    """<p>The subtitle to display on the response card. The format of the subtitle is determined by the platform displaying the response card.</p>"""
    image_url: NotRequired["capo_lex_models_v2.types.attachment_url.AttachmentUrl"]
    """<p>The URL of an image to display on the response card. The image URL must be publicly available so that the platform displaying the response card has access to the image.</p>"""
    buttons: NotRequired["capo_lex_models_v2.types.buttons_list.ButtonsList"]
    """<p>A list of buttons that should be displayed on the response card. The arrangement of the buttons is determined by the platform that displays the button.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageResponseCard) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    if "subtitle" in value:
        out["subtitle"] = value["subtitle"]
    if "image_url" in value:
        out["imageUrl"] = value["image_url"]
    if "buttons" in value:
        import capo_lex_models_v2.types.buttons_list

        out["buttons"] = capo_lex_models_v2.types.buttons_list.serialize_json(
            value["buttons"]
        )
    return out


def deserialize_json(data: dict) -> ImageResponseCard:
    out: ImageResponseCard = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("subtitle") is not None:
        out["subtitle"] = data["subtitle"]
    if data.get("imageUrl") is not None:
        out["image_url"] = data["imageUrl"]
    if data.get("buttons") is not None:
        import capo_lex_models_v2.types.buttons_list

        out["buttons"] = capo_lex_models_v2.types.buttons_list.deserialize_json(
            data["buttons"]
        )
    return out
