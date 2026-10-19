"""Generated from Smithy shape ``com.amazonaws.wickr#BatchLookupUserUnameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.client_token
    import capo_wickr.types.network_id
    import capo_wickr.types.unames


class BatchLookupUserUnameRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network where the users will be looked up.</p>"""
    unames: "capo_wickr.types.unames.Unames"
    """<p>A list of username hashes (unames) to look up. Each uname is a unique identifier for a user's username. Maximum 50 unames per batch request.</p>"""
    client_token: NotRequired["capo_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchLookupUserUnameRequest) -> dict:
    out: dict = {}
    import capo_wickr.types.unames

    out["unames"] = capo_wickr.types.unames.serialize_json(value["unames"])
    return out


def deserialize_json(data: dict) -> BatchLookupUserUnameRequest:
    out: BatchLookupUserUnameRequest = {}  # type: ignore[typeddict-item]
    if data.get("unames") is not None:
        import capo_wickr.types.unames

        out["unames"] = capo_wickr.types.unames.deserialize_json(data["unames"])
    else:
        out["unames"] = []
    return out
