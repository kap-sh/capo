"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#TracePart``."""

import json
from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent_runtime._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_alias_id
    import capo_bedrock_agent_runtime.types.agent_id
    import capo_bedrock_agent_runtime.types.agent_version
    import capo_bedrock_agent_runtime.types.caller_chain
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.name
    import capo_bedrock_agent_runtime.types.session_id
    import capo_bedrock_agent_runtime.types.trace


class TracePart(TypedDict, closed=True):
    session_id: NotRequired["capo_bedrock_agent_runtime.types.session_id.SessionId"]
    """<p>The unique identifier of the session with the agent.</p>"""
    trace: NotRequired["capo_bedrock_agent_runtime.types.trace.Trace"]
    r"""<p>Contains one part of the agent's reasoning process and results from calling API actions and querying knowledge bases. You can use the trace to understand how the agent arrived at the response it provided the customer. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-enablement\">Trace enablement</a>.</p>"""
    caller_chain: NotRequired[
        "capo_bedrock_agent_runtime.types.caller_chain.CallerChain"
    ]
    """<p>The part's caller chain.</p>"""
    event_time: NotRequired[
        "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp"
    ]
    """<p> The time of the trace. </p>"""
    collaborator_name: NotRequired["capo_bedrock_agent_runtime.types.name.Name"]
    """<p>The part's collaborator name.</p>"""
    agent_id: NotRequired["capo_bedrock_agent_runtime.types.agent_id.AgentId"]
    """<p>The unique identifier of the agent.</p>"""
    agent_alias_id: NotRequired[
        "capo_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId"
    ]
    """<p>The unique identifier of the alias of the agent.</p>"""
    agent_version: NotRequired[
        "capo_bedrock_agent_runtime.types.agent_version.AgentVersion"
    ]
    """<p>The version of the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TracePart) -> dict:
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
    if "agent_id" in value:
        out["agentId"] = value["agent_id"]
    if "agent_alias_id" in value:
        out["agentAliasId"] = value["agent_alias_id"]
    if "agent_version" in value:
        out["agentVersion"] = value["agent_version"]
    return out


def deserialize_json(data: dict) -> TracePart:
    out: TracePart = {}  # type: ignore[typeddict-item]
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
    if data.get("agentId") is not None:
        out["agent_id"] = data["agentId"]
    if data.get("agentAliasId") is not None:
        out["agent_alias_id"] = data["agentAliasId"]
    if data.get("agentVersion") is not None:
        out["agent_version"] = data["agentVersion"]
    return out


def serialize_event_json(value: TracePart) -> bytes:
    headers: dict[str, HeaderValue] = {
        ":message-type": "event",
        ":event-type": "trace",
        ":content-type": "application/json",
    }
    payload = b""
    payload = json.dumps(serialize_json(value)).encode("utf-8")
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> TracePart:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: TracePart = {}  # type: ignore[typeddict-item]
    if payload:
        out = deserialize_json(json.loads(payload))
    return out
