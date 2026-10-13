"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrieveResultList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.retrieve_result

RetrieveResultList: TypeAlias = list[
    "capo_qconnect.types.retrieve_result.RetrieveResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveResultList) -> list:
    import capo_qconnect.types.retrieve_result

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.retrieve_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> RetrieveResultList:
    import capo_qconnect.types.retrieve_result

    out: RetrieveResultList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.retrieve_result.deserialize_json(item))
    return out


def redact_sensitive(value: RetrieveResultList) -> list[Any]:
    import capo_qconnect.types.retrieve_result

    return [
        capo_qconnect.types.retrieve_result.redact_sensitive(item) for item in value
    ]
