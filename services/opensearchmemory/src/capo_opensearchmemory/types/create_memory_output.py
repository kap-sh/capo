"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#CreateMemoryOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_opensearchmemory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchmemory.types.create_memory_detail


class CreateMemoryOutput(TypedDict, closed=True):
    memory: "capo_opensearchmemory.types.create_memory_detail.CreateMemoryDetail"
    """<p>The memory, identified but not yet indexed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateMemoryOutput) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.create_memory_detail

    out["memory"] = (
        capo_opensearchmemory.types.create_memory_detail.serialize_aws_json_1_0(
            value["memory"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateMemoryOutput:
    out: CreateMemoryOutput = {}  # type: ignore[typeddict-item]
    if data.get("memory") is not None:
        import capo_opensearchmemory.types.create_memory_detail

        out["memory"] = (
            capo_opensearchmemory.types.create_memory_detail.deserialize_aws_json_1_0(
                data["memory"]
            )
        )
    else:
        raise DeserializationError("CreateMemoryOutput.memory required")
    return out
