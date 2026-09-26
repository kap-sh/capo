"""Generated from Smithy shape ``com.amazonaws.agentregistry#HttpDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry.types.descriptor_source


class HttpDescriptor(TypedDict, closed=True):
    source: NotRequired["capo_agent_registry.types.descriptor_source.DescriptorSource"]
    """<p> The source location of the HTTP endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HttpDescriptor) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_agent_registry.types.descriptor_source

        out["source"] = capo_agent_registry.types.descriptor_source.serialize_json(
            value["source"]
        )
    return out


def deserialize_json(data: dict) -> HttpDescriptor:
    out: HttpDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_agent_registry.types.descriptor_source

        out["source"] = capo_agent_registry.types.descriptor_source.deserialize_json(
            data["source"]
        )
    return out
