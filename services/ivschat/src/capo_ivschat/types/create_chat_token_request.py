"""Generated from Smithy shape ``com.amazonaws.ivschat#CreateChatTokenRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ivschat.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ivschat.types.chat_token_attributes
    import capo_ivschat.types.chat_token_capabilities
    import capo_ivschat.types.room_identifier
    import capo_ivschat.types.session_duration_in_minutes
    import capo_ivschat.types.user_id


class CreateChatTokenRequest(TypedDict, closed=True):
    room_identifier: "capo_ivschat.types.room_identifier.RoomIdentifier"
    """<p>Identifier of the room that the client is trying to access. Currently this must be an ARN. </p>"""
    user_id: "capo_ivschat.types.user_id.UserID"
    """<p>Application-provided ID that uniquely identifies the user associated with this token. This can be any UTF-8 encoded text.</p>"""
    capabilities: NotRequired[
        "capo_ivschat.types.chat_token_capabilities.ChatTokenCapabilities"
    ]
    """<p>Set of capabilities that the user is allowed to perform in the room. Default: None (the capability to view messages is implicitly included in all requests).</p>"""
    session_duration_in_minutes: NotRequired[
        "capo_ivschat.types.session_duration_in_minutes.SessionDurationInMinutes"
    ]
    """<p>Session duration (in minutes), after which the session expires. Default: 60 (1 hour).</p>"""
    attributes: NotRequired[
        "capo_ivschat.types.chat_token_attributes.ChatTokenAttributes"
    ]
    """<p>Application-provided attributes to encode into the token and attach to a chat session. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChatTokenRequest) -> dict:
    out: dict = {}
    out["roomIdentifier"] = value["room_identifier"]
    out["userId"] = value["user_id"]
    if "capabilities" in value:
        import capo_ivschat.types.chat_token_capabilities

        out["capabilities"] = capo_ivschat.types.chat_token_capabilities.serialize_json(
            value["capabilities"]
        )
    if "session_duration_in_minutes" in value:
        out["sessionDurationInMinutes"] = value["session_duration_in_minutes"]
    if "attributes" in value:
        import capo_ivschat.types.chat_token_attributes

        out["attributes"] = capo_ivschat.types.chat_token_attributes.serialize_json(
            value["attributes"]
        )
    return out


def deserialize_json(data: dict) -> CreateChatTokenRequest:
    out: CreateChatTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("roomIdentifier") is not None:
        out["room_identifier"] = data["roomIdentifier"]
    else:
        raise DeserializationError("CreateChatTokenRequest.room_identifier required")
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    else:
        raise DeserializationError("CreateChatTokenRequest.user_id required")
    if data.get("capabilities") is not None:
        import capo_ivschat.types.chat_token_capabilities

        out["capabilities"] = (
            capo_ivschat.types.chat_token_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    if data.get("sessionDurationInMinutes") is not None:
        out["session_duration_in_minutes"] = data["sessionDurationInMinutes"]
    if data.get("attributes") is not None:
        import capo_ivschat.types.chat_token_attributes

        out["attributes"] = capo_ivschat.types.chat_token_attributes.deserialize_json(
            data["attributes"]
        )
    return out


def redact_sensitive(value: CreateChatTokenRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_id" in value:
        out["user_id"] = "*** Sensitive Data Redacted ***"
    if "attributes" in value:
        out["attributes"] = "*** Sensitive Data Redacted ***"
    return out
