"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#StreamUrlSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_gameliftstreams.types.stream_url_summary

StreamUrlSummaryList: TypeAlias = list[
    "capo_gameliftstreams.types.stream_url_summary.StreamUrlSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StreamUrlSummaryList) -> list:
    import capo_gameliftstreams.types.stream_url_summary

    out: list = []
    for item in value:
        out.append(capo_gameliftstreams.types.stream_url_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StreamUrlSummaryList:
    import capo_gameliftstreams.types.stream_url_summary

    out: StreamUrlSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_gameliftstreams.types.stream_url_summary.deserialize_json(item))
    return out


def redact_sensitive(value: StreamUrlSummaryList) -> list[Any]:
    import capo_gameliftstreams.types.stream_url_summary

    return [
        capo_gameliftstreams.types.stream_url_summary.redact_sensitive(item)
        for item in value
    ]
