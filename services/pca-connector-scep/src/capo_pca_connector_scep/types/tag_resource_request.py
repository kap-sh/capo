"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_scep.types.tags


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: "capo_pca_connector_scep.types.tags.Tags"
    """<p>The key-value pairs to associate with the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import capo_pca_connector_scep.types.tags

    out["Tags"] = capo_pca_connector_scep.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tags") is not None:
        import capo_pca_connector_scep.types.tags

        out["tags"] = capo_pca_connector_scep.types.tags.deserialize_json(data["Tags"])
    else:
        out["tags"] = {}
    return out
