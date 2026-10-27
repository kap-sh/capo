"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#RevokeConnectionTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.connection_token_id


class RevokeConnectionTokenRequest(TypedDict, closed=True):
    token_id: "capo_ivs_realtime.types.connection_token_id.ConnectionTokenId"
    """<p>The ID of the connection token to revoke.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokeConnectionTokenRequest) -> dict:
    out: dict = {}
    out["tokenId"] = value["token_id"]
    return out


def deserialize_json(data: dict) -> RevokeConnectionTokenRequest:
    out: RevokeConnectionTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("tokenId") is not None:
        out["token_id"] = data["tokenId"]
    else:
        out["token_id"] = ""
    return out
