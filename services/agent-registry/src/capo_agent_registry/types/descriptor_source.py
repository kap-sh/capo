"""Generated from Smithy shape ``com.amazonaws.agentregistry#DescriptorSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry.types.descriptor_source_from_url


class DescriptorSource(TypedDict, closed=True):
    from_url: NotRequired[
        "capo_agent_registry.types.descriptor_source_from_url.DescriptorSourceFromUrl"
    ]
    """<p> The URL-based descriptor source, populated when descriptor content is synchronized from a URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescriptorSource) -> dict:
    out: dict = {}
    if "from_url" in value:
        import capo_agent_registry.types.descriptor_source_from_url

        out["fromUrl"] = (
            capo_agent_registry.types.descriptor_source_from_url.serialize_json(
                value["from_url"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescriptorSource:
    out: DescriptorSource = {}  # type: ignore[typeddict-item]
    if data.get("fromUrl") is not None:
        import capo_agent_registry.types.descriptor_source_from_url

        out["from_url"] = (
            capo_agent_registry.types.descriptor_source_from_url.deserialize_json(
                data["fromUrl"]
            )
        )
    return out
