"""Generated from Smithy shape ``com.amazonaws.wickr#BatchCreateUserRequestItems``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.batch_create_user_request_item

BatchCreateUserRequestItems: TypeAlias = list[
    "capo_wickr.types.batch_create_user_request_item.BatchCreateUserRequestItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateUserRequestItems) -> list:
    import capo_wickr.types.batch_create_user_request_item

    out: list = []
    for item in value:
        out.append(capo_wickr.types.batch_create_user_request_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchCreateUserRequestItems:
    import capo_wickr.types.batch_create_user_request_item

    out: BatchCreateUserRequestItems = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_wickr.types.batch_create_user_request_item.deserialize_json(item)
        )
    return out


def redact_sensitive(value: BatchCreateUserRequestItems) -> list[Any]:
    import capo_wickr.types.batch_create_user_request_item

    return [
        capo_wickr.types.batch_create_user_request_item.redact_sensitive(item)
        for item in value
    ]
