"""Generated from Smithy shape ``com.amazonaws.mpa#ListSessionsResponseSessions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mpa.types.list_sessions_response_session

ListSessionsResponseSessions: TypeAlias = list[
    "capo_mpa.types.list_sessions_response_session.ListSessionsResponseSession"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsResponseSessions) -> list:
    import capo_mpa.types.list_sessions_response_session

    out: list = []
    for item in value:
        out.append(capo_mpa.types.list_sessions_response_session.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListSessionsResponseSessions:
    import capo_mpa.types.list_sessions_response_session

    out: ListSessionsResponseSessions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mpa.types.list_sessions_response_session.deserialize_json(item))
    return out


def redact_sensitive(value: ListSessionsResponseSessions) -> list[Any]:
    import capo_mpa.types.list_sessions_response_session

    return [
        capo_mpa.types.list_sessions_response_session.redact_sensitive(item)
        for item in value
    ]
