"""Generated from Smithy shape ``com.amazonaws.securityir#ListCommentsItems``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_security_ir.types.list_comments_item

ListCommentsItems: TypeAlias = list[
    "capo_security_ir.types.list_comments_item.ListCommentsItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListCommentsItems) -> list:
    import capo_security_ir.types.list_comments_item

    out: list = []
    for item in value:
        out.append(capo_security_ir.types.list_comments_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListCommentsItems:
    import capo_security_ir.types.list_comments_item

    out: ListCommentsItems = []
    for item in data:
        if item is None:
            continue
        out.append(capo_security_ir.types.list_comments_item.deserialize_json(item))
    return out


def redact_sensitive(value: ListCommentsItems) -> list[Any]:
    import capo_security_ir.types.list_comments_item

    return [
        capo_security_ir.types.list_comments_item.redact_sensitive(item)
        for item in value
    ]
