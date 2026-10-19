"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowAliasConcurrencyConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.concurrency_type


class FlowAliasConcurrencyConfiguration(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.concurrency_type.ConcurrencyType"
    """<p>The type of concurrency to use for parallel node execution. Specify one of the following options:</p> <ul> <li> <p> <code>Automatic</code> - Amazon Bedrock determines which nodes can be executed in parallel based on the flow definition and its dependencies.</p> </li> <li> <p> <code>Manual</code> - You specify which nodes can be executed in parallel.</p> </li> </ul>"""
    max_concurrency: NotRequired["int"]
    """<p>The maximum number of nodes that can be executed concurrently in the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowAliasConcurrencyConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.concurrency_type

    out["type"] = capo_bedrock_agent.types.concurrency_type.serialize_json(
        value["type"]
    )
    if "max_concurrency" in value:
        out["maxConcurrency"] = value["max_concurrency"]
    return out


def deserialize_json(data: dict) -> FlowAliasConcurrencyConfiguration:
    out: FlowAliasConcurrencyConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.concurrency_type

        out["type"] = capo_bedrock_agent.types.concurrency_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.concurrency_type.ConcurrencyType", ""
        )
    if data.get("maxConcurrency") is not None:
        out["max_concurrency"] = data["maxConcurrency"]
    return out
