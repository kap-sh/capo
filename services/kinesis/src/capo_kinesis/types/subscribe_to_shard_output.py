"""Generated from Smithy shape ``com.amazonaws.kinesis#SubscribeToShardOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.subscribe_to_shard_event_stream


class SubscribeToShardOutput(TypedDict, closed=True):
    event_stream: (
        "capo_kinesis.types.subscribe_to_shard_event_stream.SubscribeToShardEventStream"
    )
    """<p>The event stream that your consumer can use to read records from the shard.</p>"""


def redact_sensitive(value: SubscribeToShardOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "event_stream" in value:
        out["event_stream"] = "*** Streaming Data Redacted ***"
    return out
