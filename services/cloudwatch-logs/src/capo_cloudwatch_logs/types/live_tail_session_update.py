"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#LiveTailSessionUpdate``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_logs._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.live_tail_session_metadata
    import capo_cloudwatch_logs.types.live_tail_session_results


class LiveTailSessionUpdate(TypedDict, closed=True):
    session_metadata: NotRequired[
        "capo_cloudwatch_logs.types.live_tail_session_metadata.LiveTailSessionMetadata"
    ]
    """<p>This object contains the session metadata for a Live Tail session.</p>"""
    session_results: NotRequired[
        "capo_cloudwatch_logs.types.live_tail_session_results.LiveTailSessionResults"
    ]
    """<p>An array, where each member of the array includes the information for one log event in the Live Tail session.</p> <p>A <code>sessionResults</code> array can include as many as 500 log events. If the number of log events matching the request exceeds 500 per second, the log events are sampled down to 500 log events to be included in each <code>sessionUpdate</code> structure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LiveTailSessionUpdate) -> dict:
    out: dict = {}
    if "session_metadata" in value:
        import capo_cloudwatch_logs.types.live_tail_session_metadata

        out["sessionMetadata"] = (
            capo_cloudwatch_logs.types.live_tail_session_metadata.serialize_aws_json_1_1(
                value["session_metadata"]
            )
        )
    if "session_results" in value:
        import capo_cloudwatch_logs.types.live_tail_session_results

        out["sessionResults"] = (
            capo_cloudwatch_logs.types.live_tail_session_results.serialize_aws_json_1_1(
                value["session_results"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LiveTailSessionUpdate:
    out: LiveTailSessionUpdate = {}  # type: ignore[typeddict-item]
    if data.get("sessionMetadata") is not None:
        import capo_cloudwatch_logs.types.live_tail_session_metadata

        out["session_metadata"] = (
            capo_cloudwatch_logs.types.live_tail_session_metadata.deserialize_aws_json_1_1(
                data["sessionMetadata"]
            )
        )
    if data.get("sessionResults") is not None:
        import capo_cloudwatch_logs.types.live_tail_session_results

        out["session_results"] = (
            capo_cloudwatch_logs.types.live_tail_session_results.deserialize_aws_json_1_1(
                data["sessionResults"]
            )
        )
    return out


def serialize_event_aws_json_1_1(value: LiveTailSessionUpdate) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "sessionUpdate",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_aws_json_1_1(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_1(message: Message) -> LiveTailSessionUpdate:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: LiveTailSessionUpdate = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_aws_json_1_1(json.loads(payload))
    return out
