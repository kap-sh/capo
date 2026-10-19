"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CreateParticipantTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_token_attributes
    import capo_ivs_realtime.types.participant_token_capabilities
    import capo_ivs_realtime.types.participant_token_duration_minutes
    import capo_ivs_realtime.types.participant_token_user_id
    import capo_ivs_realtime.types.stage_arn


class CreateParticipantTokenRequest(TypedDict, closed=True):
    stage_arn: "capo_ivs_realtime.types.stage_arn.StageArn"
    """<p>ARN of the stage to which this token is scoped.</p>"""
    duration: NotRequired[
        "capo_ivs_realtime.types.participant_token_duration_minutes.ParticipantTokenDurationMinutes"
    ]
    """<p>Duration (in minutes), after which the token expires. Default: 720 (12 hours).</p>"""
    user_id: NotRequired[
        "capo_ivs_realtime.types.participant_token_user_id.ParticipantTokenUserId"
    ]
    """<p>Name that can be specified to help identify the token. This can be any UTF-8 encoded text. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    attributes: NotRequired[
        "capo_ivs_realtime.types.participant_token_attributes.ParticipantTokenAttributes"
    ]
    """<p>Application-provided attributes to encode into the token and attach to a stage. Map keys and values can contain UTF-8 encoded text. The maximum length of this field is 1 KB total. <i>This field is exposed to all stage participants and should not be used for personally identifying, confidential, or sensitive information.</i> </p>"""
    capabilities: NotRequired[
        "capo_ivs_realtime.types.participant_token_capabilities.ParticipantTokenCapabilities"
    ]
    """<p>Set of capabilities that the user is allowed to perform in the stage. Default: <code>PUBLISH, SUBSCRIBE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateParticipantTokenRequest) -> dict:
    out: dict = {}
    out["stageArn"] = value["stage_arn"]
    if "duration" in value:
        out["duration"] = value["duration"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "attributes" in value:
        import capo_ivs_realtime.types.participant_token_attributes

        out["attributes"] = (
            capo_ivs_realtime.types.participant_token_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "capabilities" in value:
        import capo_ivs_realtime.types.participant_token_capabilities

        out["capabilities"] = (
            capo_ivs_realtime.types.participant_token_capabilities.serialize_json(
                value["capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateParticipantTokenRequest:
    out: CreateParticipantTokenRequest = {}  # type: ignore[typeddict-item]
    if data.get("stageArn") is not None:
        out["stage_arn"] = data["stageArn"]
    else:
        out["stage_arn"] = ""
    if data.get("duration") is not None:
        out["duration"] = data["duration"]
    if data.get("userId") is not None:
        out["user_id"] = data["userId"]
    if data.get("attributes") is not None:
        import capo_ivs_realtime.types.participant_token_attributes

        out["attributes"] = (
            capo_ivs_realtime.types.participant_token_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if data.get("capabilities") is not None:
        import capo_ivs_realtime.types.participant_token_capabilities

        out["capabilities"] = (
            capo_ivs_realtime.types.participant_token_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    return out
