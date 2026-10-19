"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryRecordDeleteInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.memory_record_id
    import capo_bedrock_agentcore.types.namespace


class MemoryRecordDeleteInput(TypedDict, closed=True):
    memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId"
    """<p>The unique ID of the memory record to be deleted.</p>"""
    namespace: NotRequired["capo_bedrock_agentcore.types.namespace.Namespace"]
    """<p>The namespace of the memory record being deleted. This value is used for IAM condition key authorization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MemoryRecordDeleteInput) -> dict:
    out: dict = {}
    out["memoryRecordId"] = value["memory_record_id"]
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    return out


def deserialize_json(data: dict) -> MemoryRecordDeleteInput:
    out: MemoryRecordDeleteInput = {}  # type: ignore[typeddict-item]
    if data.get("memoryRecordId") is not None:
        out["memory_record_id"] = data["memoryRecordId"]
    else:
        out["memory_record_id"] = ""
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    return out
