"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#UpdateMemoryOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_opensearchmemory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory


class UpdateMemoryOutput(TypedDict, closed=True):
    memory: "capo_opensearchmemory.types.memory.Memory"
    """<p>The updated memory, in the same shape that <code>GetMemory</code> returns.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateMemoryOutput) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.memory

    out["memory"] = capo_opensearchmemory.types.memory.serialize_aws_json_1_0(
        value["memory"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateMemoryOutput:
    out: UpdateMemoryOutput = {}  # type: ignore[typeddict-item]
    if data.get("memory") is not None:
        import capo_opensearchmemory.types.memory

        out["memory"] = capo_opensearchmemory.types.memory.deserialize_aws_json_1_0(
            data["memory"]
        )
    else:
        raise DeserializationError("UpdateMemoryOutput.memory required")
    return out


def redact_sensitive(value: UpdateMemoryOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "memory" in value:
        import capo_opensearchmemory.types.memory

        out["memory"] = capo_opensearchmemory.types.memory.redact_sensitive(
            value["memory"]
        )
    return out
