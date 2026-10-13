"""Generated from Smithy shape ``com.amazonaws.wickr#BatchCreateUserResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.batch_user_error_response_items
    import capo_wickr.types.generic_string
    import capo_wickr.types.users


class BatchCreateUserResponse(TypedDict, closed=True):
    message: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A message indicating the overall result of the batch operation.</p>"""
    successful: NotRequired["capo_wickr.types.users.Users"]
    """<p>A list of user objects that were successfully created, including their assigned user IDs and invite codes.</p>"""
    failed: NotRequired[
        "capo_wickr.types.batch_user_error_response_items.BatchUserErrorResponseItems"
    ]
    """<p>A list of user creation attempts that failed, including error details explaining why each user could not be created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateUserResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "successful" in value:
        import capo_wickr.types.users

        out["successful"] = capo_wickr.types.users.serialize_json(value["successful"])
    if "failed" in value:
        import capo_wickr.types.batch_user_error_response_items

        out["failed"] = capo_wickr.types.batch_user_error_response_items.serialize_json(
            value["failed"]
        )
    return out


def deserialize_json(data: dict) -> BatchCreateUserResponse:
    out: BatchCreateUserResponse = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("successful") is not None:
        import capo_wickr.types.users

        out["successful"] = capo_wickr.types.users.deserialize_json(data["successful"])
    if data.get("failed") is not None:
        import capo_wickr.types.batch_user_error_response_items

        out["failed"] = (
            capo_wickr.types.batch_user_error_response_items.deserialize_json(
                data["failed"]
            )
        )
    return out


def redact_sensitive(value: BatchCreateUserResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "successful" in value:
        import capo_wickr.types.users

        out["successful"] = capo_wickr.types.users.redact_sensitive(value["successful"])
    return out
