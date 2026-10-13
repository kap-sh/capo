"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryResultsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.result_data

QueryResultsList: TypeAlias = list["capo_qconnect.types.result_data.ResultData"]


# --- restJson1 ser/de ---
def serialize_json(value: QueryResultsList) -> list:
    import capo_qconnect.types.result_data

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.result_data.serialize_json(item))
    return out


def deserialize_json(data: list) -> QueryResultsList:
    import capo_qconnect.types.result_data

    out: QueryResultsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.result_data.deserialize_json(item))
    return out


def redact_sensitive(value: QueryResultsList) -> list[Any]:
    import capo_qconnect.types.result_data

    return [capo_qconnect.types.result_data.redact_sensitive(item) for item in value]
