"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InlineAgentTracePart``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.caller_chain
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.name
    import capo_bedrock_agent_runtime.types.session_id
    import capo_bedrock_agent_runtime.types.trace


class InlineAgentTracePart(TypedDict, closed=True):
    session_id: NotRequired["capo_bedrock_agent_runtime.types.session_id.SessionId"]
    """<p>The unique identifier of the session with the agent.</p>"""
    trace: NotRequired["capo_bedrock_agent_runtime.types.trace.Trace"]
    r"""<p>Contains one part of the agent's reasoning process and results from calling API actions and querying knowledge bases. You can use the trace to understand how the agent arrived at the response it provided the customer. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-enablement\">Trace enablement</a>. </p>"""
    caller_chain: NotRequired[
        "capo_bedrock_agent_runtime.types.caller_chain.CallerChain"
    ]
    """<p>The caller chain for the trace part.</p>"""
    event_time: NotRequired[
        "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time that trace occurred. </p>"""
    collaborator_name: NotRequired["capo_bedrock_agent_runtime.types.name.Name"]
    """<p>The collaborator name for the trace part.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineAgentTracePart) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "trace" in value:
        import capo_bedrock_agent_runtime.types.trace

        out["trace"] = capo_bedrock_agent_runtime.types.trace.serialize_json(
            value["trace"]
        )
    if "caller_chain" in value:
        import capo_bedrock_agent_runtime.types.caller_chain

        out["callerChain"] = (
            capo_bedrock_agent_runtime.types.caller_chain.serialize_json(
                value["caller_chain"]
            )
        )
    if "event_time" in value:
        import capo_bedrock_agent_runtime._protocol.serialize

        out["eventTime"] = capo_bedrock_agent_runtime._protocol.serialize.fmt_date_time(
            value["event_time"]
        )
    if "collaborator_name" in value:
        out["collaboratorName"] = value["collaborator_name"]
    return out


def deserialize_json(data: dict) -> InlineAgentTracePart:
    out: InlineAgentTracePart = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    if data.get("trace") is not None:
        import capo_bedrock_agent_runtime.types.trace

        out["trace"] = capo_bedrock_agent_runtime.types.trace.deserialize_json(
            data["trace"]
        )
    if data.get("callerChain") is not None:
        import capo_bedrock_agent_runtime.types.caller_chain

        out["caller_chain"] = (
            capo_bedrock_agent_runtime.types.caller_chain.deserialize_json(
                data["callerChain"]
            )
        )
    if data.get("eventTime") is not None:
        import datetime

        out["event_time"] = datetime.datetime.fromisoformat(
            data["eventTime"].replace("Z", "+00:00")
        )
    if data.get("collaboratorName") is not None:
        out["collaborator_name"] = data["collaboratorName"]
    return out


def serialize_event_json(value: InlineAgentTracePart) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "trace",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> InlineAgentTracePart:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: InlineAgentTracePart = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
