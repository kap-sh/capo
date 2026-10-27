"""Generated from Smithy shape ``com.amazonaws.deadline#TaskRunManifestPropertiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.string


class TaskRunManifestPropertiesRequest(TypedDict, closed=True):
    output_manifest_path: NotRequired["capo_deadline.types.string.String"]
    """The manifest file path."""
    output_manifest_hash: NotRequired["capo_deadline.types.string.String"]
    """The hash value of the file."""


# --- restJson1 ser/de ---
def serialize_json(value: TaskRunManifestPropertiesRequest) -> dict:
    out: dict = {}
    if "output_manifest_path" in value:
        out["outputManifestPath"] = value["output_manifest_path"]
    if "output_manifest_hash" in value:
        out["outputManifestHash"] = value["output_manifest_hash"]
    return out


def deserialize_json(data: dict) -> TaskRunManifestPropertiesRequest:
    out: TaskRunManifestPropertiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("outputManifestPath") is not None:
        out["output_manifest_path"] = data["outputManifestPath"]
    if data.get("outputManifestHash") is not None:
        out["output_manifest_hash"] = data["outputManifestHash"]
    return out
