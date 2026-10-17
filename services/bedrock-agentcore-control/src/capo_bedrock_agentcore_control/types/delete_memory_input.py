"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteMemoryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.memory_id
    import capo_bedrock_agentcore_control.types.non_empty_string


class DeleteMemoryInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
    ]
    """<p>A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique AWS identifier.</p>"""
    memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId"
    """<p>The unique identifier of the memory to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteMemoryInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteMemoryInput:
    out: DeleteMemoryInput = {}  # type: ignore[typeddict-item]
    return out
