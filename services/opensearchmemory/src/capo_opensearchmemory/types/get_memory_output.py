"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#GetMemoryOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_opensearchmemory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_opensearchmemory.types.memory


class GetMemoryOutput(TypedDict, closed=True):
    memory: "capo_opensearchmemory.types.memory.Memory"
    """<p>The memory. Always present: a memory that doesn't exist returns <code>ResourceNotFoundException</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMemoryOutput) -> dict:
    out: dict = {}
    import capo_opensearchmemory.types.memory

    out["memory"] = capo_opensearchmemory.types.memory.serialize_aws_json_1_0(
        value["memory"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMemoryOutput:
    out: GetMemoryOutput = {}  # type: ignore[typeddict-item]
    if data.get("memory") is not None:
        import capo_opensearchmemory.types.memory

        out["memory"] = capo_opensearchmemory.types.memory.deserialize_aws_json_1_0(
            data["memory"]
        )
    else:
        raise DeserializationError("GetMemoryOutput.memory required")
    return out


def redact_sensitive(value: GetMemoryOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "memory" in value:
        import capo_opensearchmemory.types.memory

        out["memory"] = capo_opensearchmemory.types.memory.redact_sensitive(
            value["memory"]
        )
    return out
