"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamSessionSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gameliftstreams.types.stream_session_summary

StreamSessionSummaryList: TypeAlias = list[
    "capo_gameliftstreams.types.stream_session_summary.StreamSessionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamSessionSummaryList) -> list:
    import capo_gameliftstreams.types.stream_session_summary

    out: list = []
    for item in value:
        out.append(
            capo_gameliftstreams.types.stream_session_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StreamSessionSummaryList:
    import capo_gameliftstreams.types.stream_session_summary

    out: StreamSessionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_gameliftstreams.types.stream_session_summary.deserialize_json(item)
        )
    return out


def redact_sensitive(value: StreamSessionSummaryList) -> list[Any]:
    import capo_gameliftstreams.types.stream_session_summary

    return [
        capo_gameliftstreams.types.stream_session_summary.redact_sensitive(item)
        for item in value
    ]
