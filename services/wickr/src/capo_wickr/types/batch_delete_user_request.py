"""Generated from Smithy shape ``com.amazonaws.wickr#BatchDeleteUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.client_token
    import capo_wickr.types.network_id
    import capo_wickr.types.user_ids


class BatchDeleteUserRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network from which users will be deleted.</p>"""
    user_ids: "capo_wickr.types.user_ids.UserIds"
    """<p>A list of user IDs identifying the users to be deleted from the network. Maximum 50 users per batch request.</p>"""
    client_token: NotRequired["capo_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency. If you retry a request with the same client token, the service will return the same response without attempting to delete users again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteUserRequest) -> dict:
    out: dict = {}
    import capo_wickr.types.user_ids

    out["userIds"] = capo_wickr.types.user_ids.serialize_json(value["user_ids"])
    return out


def deserialize_json(data: dict) -> BatchDeleteUserRequest:
    out: BatchDeleteUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("userIds") is not None:
        import capo_wickr.types.user_ids

        out["user_ids"] = capo_wickr.types.user_ids.deserialize_json(data["userIds"])
    else:
        out["user_ids"] = []
    return out
