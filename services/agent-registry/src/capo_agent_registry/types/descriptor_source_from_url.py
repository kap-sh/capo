"""Generated from Smithy shape ``com.amazonaws.agentregistry#DescriptorSourceFromUrl``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry.types.descriptor_source_url


class DescriptorSourceFromUrl(TypedDict, closed=True):
    url: "capo_agent_registry.types.descriptor_source_url.DescriptorSourceUrl"
    """<p> The URL from which the descriptor content is retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescriptorSourceFromUrl) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    return out


def deserialize_json(data: dict) -> DescriptorSourceFromUrl:
    out: DescriptorSourceFromUrl = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        raise DeserializationError("DescriptorSourceFromUrl.url required")
    return out
