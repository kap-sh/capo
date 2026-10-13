"""Generated from Smithy shape ``com.amazonaws.wickr#BatchCreateUserRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.batch_create_user_request_items
    import capo_wickr.types.client_token
    import capo_wickr.types.network_id


class BatchCreateUserRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network where users will be created.</p>"""
    users: (
        "capo_wickr.types.batch_create_user_request_items.BatchCreateUserRequestItems"
    )
    """<p>A list of user objects containing the details for each user to be created, including username, name, security groups, and optional invite codes. Maximum 50 users per batch request.</p>"""
    client_token: NotRequired["capo_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency. If you retry a request with the same client token, the service will return the same response without creating duplicate users.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateUserRequest) -> dict:
    out: dict = {}
    import capo_wickr.types.batch_create_user_request_items

    out["users"] = capo_wickr.types.batch_create_user_request_items.serialize_json(
        value["users"]
    )
    return out


def deserialize_json(data: dict) -> BatchCreateUserRequest:
    out: BatchCreateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("users") is not None:
        import capo_wickr.types.batch_create_user_request_items

        out["users"] = (
            capo_wickr.types.batch_create_user_request_items.deserialize_json(
                data["users"]
            )
        )
    else:
        raise DeserializationError("BatchCreateUserRequest.users required")
    return out


def redact_sensitive(value: BatchCreateUserRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "users" in value:
        import capo_wickr.types.batch_create_user_request_items

        out["users"] = (
            capo_wickr.types.batch_create_user_request_items.redact_sensitive(
                value["users"]
            )
        )
    return out
