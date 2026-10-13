"""Generated from Smithy shape ``com.amazonaws.chime#BatchUpdateUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_chime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime.types.non_empty_string
    import capo_chime.types.update_user_request_item_list


class BatchUpdateUserRequest(TypedDict, closed=True):
    account_id: "capo_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    update_user_request_items: (
        "capo_chime.types.update_user_request_item_list.UpdateUserRequestItemList"
    )
    """<p>The request containing the user IDs and details to update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateUserRequest) -> dict:
    out: dict = {}
    import capo_chime.types.update_user_request_item_list

    out["UpdateUserRequestItems"] = (
        capo_chime.types.update_user_request_item_list.serialize_json(
            value["update_user_request_items"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateUserRequest:
    out: BatchUpdateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("UpdateUserRequestItems") is not None:
        import capo_chime.types.update_user_request_item_list

        out["update_user_request_items"] = (
            capo_chime.types.update_user_request_item_list.deserialize_json(
                data["UpdateUserRequestItems"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateUserRequest.update_user_request_items required"
        )
    return out


def redact_sensitive(value: BatchUpdateUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "update_user_request_items" in value:
        import capo_chime.types.update_user_request_item_list

        out["update_user_request_items"] = (
            capo_chime.types.update_user_request_item_list.redact_sensitive(
                value["update_user_request_items"]
            )
        )
    return out
