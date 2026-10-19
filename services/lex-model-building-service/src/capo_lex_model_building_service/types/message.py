"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#Message``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.content_string
    import capo_lex_model_building_service.types.content_type
    import capo_lex_model_building_service.types.group_number


class Message(TypedDict, closed=True):
    content_type: "capo_lex_model_building_service.types.content_type.ContentType"
    """<p>The content type of the message string.</p>"""
    content: "capo_lex_model_building_service.types.content_string.ContentString"
    """<p>The text of the message.</p>"""
    group_number: NotRequired[
        "capo_lex_model_building_service.types.group_number.GroupNumber"
    ]
    """<p>Identifies the message group that the message belongs to. When a group is assigned to a message, Amazon Lex returns one message from each group in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    import capo_lex_model_building_service.types.content_type

    out["contentType"] = (
        capo_lex_model_building_service.types.content_type.serialize_json(
            value["content_type"]
        )
    )
    out["content"] = value["content"]
    if "group_number" in value:
        out["groupNumber"] = value["group_number"]
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if data.get("contentType") is not None:
        import capo_lex_model_building_service.types.content_type

        out["content_type"] = (
            capo_lex_model_building_service.types.content_type.deserialize_json(
                data["contentType"]
            )
        )
    else:
        import typing

        out["content_type"] = typing.cast(
            "capo_lex_model_building_service.types.content_type.ContentType", ""
        )
    if data.get("content") is not None:
        out["content"] = data["content"]
    else:
        out["content"] = ""
    if data.get("groupNumber") is not None:
        out["group_number"] = data["groupNumber"]
    return out
