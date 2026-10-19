"""Generated from Smithy shape ``com.amazonaws.connectcases#RelatedItemUpdateContent``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.comment_update_content
    import capo_connectcases.types.custom_update_content


class _RelatedItemUpdateContent_comment(TypedDict, closed=True):
    comment: "capo_connectcases.types.comment_update_content.CommentUpdateContent"


class _RelatedItemUpdateContent_custom(TypedDict, closed=True):
    custom: "capo_connectcases.types.custom_update_content.CustomUpdateContent"


RelatedItemUpdateContent: TypeAlias = (
    _RelatedItemUpdateContent_comment
    | _RelatedItemUpdateContent_custom
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemUpdateContent) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RelatedItemUpdateContent: cannot serialize unknown variant {value.name!r}"
        )
    elif "comment" in value:
        import capo_connectcases.types.comment_update_content

        return {
            "comment": capo_connectcases.types.comment_update_content.serialize_json(
                value["comment"]
            )
        }
    elif "custom" in value:
        import capo_connectcases.types.custom_update_content

        return {
            "custom": capo_connectcases.types.custom_update_content.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError("RelatedItemUpdateContent: no variant present")


def deserialize_json(data: dict) -> RelatedItemUpdateContent:
    if data.get("comment") is not None:
        import capo_connectcases.types.comment_update_content

        return {
            "comment": capo_connectcases.types.comment_update_content.deserialize_json(
                data["comment"]
            )
        }
    elif data.get("custom") is not None:
        import capo_connectcases.types.custom_update_content

        return {
            "custom": capo_connectcases.types.custom_update_content.deserialize_json(
                data["custom"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "RelatedItemUpdateContent: no recognized variant key"
        )
