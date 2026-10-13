"""Generated from Smithy shape ``com.amazonaws.ivschat#CreateChatTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.chat_token
    import capo_ivschat.types.time


class CreateChatTokenResponse(TypedDict, closed=True):
    token: NotRequired["capo_ivschat.types.chat_token.ChatToken"]
    """<p>The issued client token, encrypted.</p>"""
    token_expiration_time: NotRequired["capo_ivschat.types.time.Time"]
    """<p>Time after which the token is no longer valid and cannot be used to connect to a room. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""
    session_expiration_time: NotRequired["capo_ivschat.types.time.Time"]
    """<p>Time after which an end user's session is no longer valid. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChatTokenResponse) -> dict:
    out: dict = {}
    if "token" in value:
        out["token"] = value["token"]
    if "token_expiration_time" in value:
        import capo_ivschat.types.time

        out["tokenExpirationTime"] = capo_ivschat.types.time.serialize_json(
            value["token_expiration_time"]
        )
    if "session_expiration_time" in value:
        import capo_ivschat.types.time

        out["sessionExpirationTime"] = capo_ivschat.types.time.serialize_json(
            value["session_expiration_time"]
        )
    return out


def deserialize_json(data: dict) -> CreateChatTokenResponse:
    out: CreateChatTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("token") is not None:
        out["token"] = data["token"]
    if data.get("tokenExpirationTime") is not None:
        import capo_ivschat.types.time

        out["token_expiration_time"] = capo_ivschat.types.time.deserialize_json(
            data["tokenExpirationTime"]
        )
    if data.get("sessionExpirationTime") is not None:
        import capo_ivschat.types.time

        out["session_expiration_time"] = capo_ivschat.types.time.deserialize_json(
            data["sessionExpirationTime"]
        )
    return out


def redact_sensitive(value: CreateChatTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token" in value:
        out["token"] = "*** Sensitive Data Redacted ***"
    return out
