"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#CreateIndexInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.tag_map


class CreateIndexInput(TypedDict, closed=True):
    client_token: NotRequired["str"]
    """<p>This value helps ensure idempotency. Resource Explorer uses this value to prevent the accidental creation of duplicate versions. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type value</a> to ensure the uniqueness of your index.</p>"""
    tags: NotRequired["capo_resource_explorer_2.types.tag_map.TagMap"]
    """<p>The specified tags are attached only to the index created in this Amazon Web Services Region. The tags aren't attached to any of the resources listed in the index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIndexInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_resource_explorer_2.types.tag_map

        out["Tags"] = capo_resource_explorer_2.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateIndexInput:
    out: CreateIndexInput = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_resource_explorer_2.types.tag_map

        out["tags"] = capo_resource_explorer_2.types.tag_map.deserialize_json(
            data["Tags"]
        )
    return out
