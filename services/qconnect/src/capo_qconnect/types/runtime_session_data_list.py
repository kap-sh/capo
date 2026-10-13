"""Generated from Smithy shape ``com.amazonaws.qconnect#RuntimeSessionDataList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.runtime_session_data

RuntimeSessionDataList: TypeAlias = list[
    "capo_qconnect.types.runtime_session_data.RuntimeSessionData"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuntimeSessionDataList) -> list:
    import capo_qconnect.types.runtime_session_data

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.runtime_session_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuntimeSessionDataList:
    import capo_qconnect.types.runtime_session_data

    out: RuntimeSessionDataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.runtime_session_data.deserialize_json(item))
    return out


def redact_sensitive(value: RuntimeSessionDataList) -> list[Any]:
    import capo_qconnect.types.runtime_session_data

    return [
        capo_qconnect.types.runtime_session_data.redact_sensitive(item)
        for item in value
    ]
