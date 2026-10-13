"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#CandidateAddressList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.candidate_address

CandidateAddressList: TypeAlias = list[
    "capo_chime_sdk_voice.types.candidate_address.CandidateAddress"
]


# --- restJson1 ser/de ---
def serialize_json(value: CandidateAddressList) -> list:
    import capo_chime_sdk_voice.types.candidate_address

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.candidate_address.serialize_json(item))
    return out


def deserialize_json(data: list) -> CandidateAddressList:
    import capo_chime_sdk_voice.types.candidate_address

    out: CandidateAddressList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_chime_sdk_voice.types.candidate_address.deserialize_json(item))
    return out


def redact_sensitive(value: CandidateAddressList) -> list[Any]:
    import capo_chime_sdk_voice.types.candidate_address

    return [
        capo_chime_sdk_voice.types.candidate_address.redact_sensitive(item)
        for item in value
    ]
