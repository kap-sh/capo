"""Generated from Smithy shape ``com.amazonaws.omics#CreateVariantStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.description
    import capo_omics.types.reference_item
    import capo_omics.types.sse_config
    import capo_omics.types.store_name
    import capo_omics.types.tag_map


class CreateVariantStoreRequest(TypedDict, closed=True):
    reference: "capo_omics.types.reference_item.ReferenceItem"
    """<p>The genome reference for the store's variants.</p>"""
    name: NotRequired["capo_omics.types.store_name.StoreName"]
    """<p>A name for the store.</p>"""
    description: NotRequired["capo_omics.types.description.Description"]
    """<p>A description for the store.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>Tags for the store.</p>"""
    sse_config: NotRequired["capo_omics.types.sse_config.SseConfig"]
    """<p>Server-side encryption (SSE) settings for the store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVariantStoreRequest) -> dict:
    out: dict = {}
    import capo_omics.types.reference_item

    out["reference"] = capo_omics.types.reference_item.serialize_json(
        value["reference"]
    )
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    if "sse_config" in value:
        import capo_omics.types.sse_config

        out["sseConfig"] = capo_omics.types.sse_config.serialize_json(
            value["sse_config"]
        )
    return out


def deserialize_json(data: dict) -> CreateVariantStoreRequest:
    out: CreateVariantStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("reference") is not None:
        import capo_omics.types.reference_item

        out["reference"] = capo_omics.types.reference_item.deserialize_json(
            data["reference"]
        )
    else:
        out["reference"] = {"$unknown": {"name": ""}}
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if data.get("sseConfig") is not None:
        import capo_omics.types.sse_config

        out["sse_config"] = capo_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    return out
