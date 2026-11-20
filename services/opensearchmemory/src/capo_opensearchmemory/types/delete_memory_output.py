"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#DeleteMemoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory_id


class DeleteMemoryOutput(TypedDict, closed=True):
    memory_id: "capo_opensearchmemory.types.memory_id.MemoryId"
    """<p>The ID of the deleted memory.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteMemoryOutput) -> dict:
    out: dict = {}
    out["memoryId"] = value["memory_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteMemoryOutput:
    out: DeleteMemoryOutput = {}  # type: ignore[typeddict-item]
    if data.get("memoryId") is not None:
        out["memory_id"] = data["memoryId"]
    else:
        out["memory_id"] = ""
    return out
