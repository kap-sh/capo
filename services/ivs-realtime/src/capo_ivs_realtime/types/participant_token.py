"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantToken``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_token_attributes
    import capo_ivs_realtime.types.participant_token_capabilities
    import capo_ivs_realtime.types.participant_token_duration_minutes
    import capo_ivs_realtime.types.participant_token_expiration_time
    import capo_ivs_realtime.types.participant_token_id
    import capo_ivs_realtime.types.participant_token_string
    import capo_ivs_realtime.types.participant_token_user_id


class ParticipantToken(TypedDict, closed=True):
    participant_id: NotRequired[
        "capo_ivs_realtime.types.participant_token_id.ParticipantTokenId"
    ]
    """<p>Unique identifier for this participant token, assigned by IVS.</p>"""
    token: NotRequired[
        "capo_ivs_realtime.types.participant_token_string.ParticipantTokenString"
    ]
    """<p>The issued client token, encrypted.</p>"""
    user_id: NotRequired[
        "capo_ivs_realtime.types.participant_token_user_id.ParticipantTokenUserId"
    ]
    """<p>Customer-assigned name to help identify the token; this can be used to link a participant to a user in the customer’s own systems. This can be any UTF-8 encoded text. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    attributes: NotRequired[
        "capo_ivs_realtime.types.participant_token_attributes.ParticipantTokenAttributes"
    ]
    """<p>Application-provided attributes to encode into the token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    duration: NotRequired[
        "capo_ivs_realtime.types.participant_token_duration_minutes.ParticipantTokenDurationMinutes"
    ]
    """<p>Duration (in minutes), after which the participant token expires. Default: 720 (12 hours).</p>"""
    capabilities: NotRequired[
        "capo_ivs_realtime.types.participant_token_capabilities.ParticipantTokenCapabilities"
    ]
    """<p>Set of capabilities that the user is allowed to perform in the stage.</p>"""
    expiration_time: NotRequired[
        "capo_ivs_realtime.types.participant_token_expiration_time.ParticipantTokenExpirationTime"
    ]
    """<p>ISO 8601 timestamp (returned as a string) for when this token expires.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantToken) -> dict:
    out: dict = {}
    if "participant_id" in value:
        out["participantId"] = value["participant_id"]
    if "token" in value:
        out["token"] = value["token"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "attributes" in value:
        import capo_ivs_realtime.types.participant_token_attributes

        out["attributes"] = (
            capo_ivs_realtime.types.participant_token_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "duration" in value:
        out["duration"] = value["duration"]
    if "capabilities" in value:
        import capo_ivs_realtime.types.participant_token_capabilities

        out["capabilities"] = (
            capo_ivs_realtime.types.participant_token_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    if "expiration_time" in value:
        import capo_ivs_realtime.types.participant_token_expiration_time

        out["expirationTime"] = (
            capo_ivs_realtime.types.participant_token_expiration_time.serialize_json(
                value["expiration_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParticipantToken:
    out: ParticipantToken = {}  # type: ignore[typeddict-item]
    if data.get("participantId") is not None:
        out["participant_id"] = data["participantId"]
    if data.get("token") is not None:
        out["token"] = data["token"]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("attributes") is not None:
        import capo_ivs_realtime.types.participant_token_attributes

        out["attributes"] = (
            capo_ivs_realtime.types.participant_token_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if data.get("duration") is not None:
        out["duration"] = data["duration"]
    if data.get("capabilities") is not None:
        import capo_ivs_realtime.types.participant_token_capabilities

        out["capabilities"] = (
            capo_ivs_realtime.types.participant_token_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    if data.get("expirationTime") is not None:
        import capo_ivs_realtime.types.participant_token_expiration_time

        out["expiration_time"] = (
            capo_ivs_realtime.types.participant_token_expiration_time.deserialize_json(
                data["expirationTime"]
            )
        )
    return out


def redact_sensitive(value: ParticipantToken) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token" in value:
        out["token"] = "*** Sensitive Data Redacted ***"
    return out
