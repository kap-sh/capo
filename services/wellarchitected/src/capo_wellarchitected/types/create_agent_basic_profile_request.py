"""Generated from Smithy shape ``com.amazonaws.wellarchitected#CreateAgentBasicProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.tags


class CreateAgentBasicProfileRequest(TypedDict, closed=True):
    tags: NotRequired["capo_wellarchitected.types.tags.Tags"]
    """<p>Tags to apply to the Basic profile at creation time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentBasicProfileRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_wellarchitected.types.tags

        out["tags"] = capo_wellarchitected.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAgentBasicProfileRequest:
    out: CreateAgentBasicProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("tags") is not None:
        import capo_wellarchitected.types.tags

        out["tags"] = capo_wellarchitected.types.tags.deserialize_json(data["tags"])
    return out
