"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ParticipantTokenList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.participant_token

ParticipantTokenList: TypeAlias = list[
    "capo_ivs_realtime.types.participant_token.ParticipantToken"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipantTokenList) -> list:
    import capo_ivs_realtime.types.participant_token

    out: list = []
    for item in value:
        out.append(capo_ivs_realtime.types.participant_token.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParticipantTokenList:
    import capo_ivs_realtime.types.participant_token

    out: ParticipantTokenList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ivs_realtime.types.participant_token.deserialize_json(item))
    return out


def redact_sensitive(value: ParticipantTokenList) -> list[Any]:
    import capo_ivs_realtime.types.participant_token

    return [
        capo_ivs_realtime.types.participant_token.redact_sensitive(item)
        for item in value
    ]
