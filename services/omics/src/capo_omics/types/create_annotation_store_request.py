"""Generated from Smithy shape ``com.amazonaws.omics#CreateAnnotationStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.description
    import capo_omics.types.reference_item
    import capo_omics.types.sse_config
    import capo_omics.types.store_format
    import capo_omics.types.store_name
    import capo_omics.types.store_options
    import capo_omics.types.tag_map
    import capo_omics.types.version_name


class CreateAnnotationStoreRequest(TypedDict, closed=True):
    reference: NotRequired["capo_omics.types.reference_item.ReferenceItem"]
    """<p>The genome reference for the store's annotations.</p>"""
    name: NotRequired["capo_omics.types.store_name.StoreName"]
    """<p>A name for the store.</p>"""
    description: NotRequired["capo_omics.types.description.Description"]
    """<p>A description for the store.</p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p>Tags for the store.</p>"""
    version_name: NotRequired["capo_omics.types.version_name.VersionName"]
    """<p> The name given to an annotation store version to distinguish it from other versions. </p>"""
    sse_config: NotRequired["capo_omics.types.sse_config.SseConfig"]
    """<p>Server-side encryption (SSE) settings for the store.</p>"""
    store_format: "capo_omics.types.store_format.StoreFormat"
    """<p>The annotation file format of the store.</p>"""
    store_options: NotRequired["capo_omics.types.store_options.StoreOptions"]
    """<p>File parsing options for the annotation store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnnotationStoreRequest) -> dict:
    out: dict = {}
    if "reference" in value:
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
    if "version_name" in value:
        out["versionName"] = value["version_name"]
    if "sse_config" in value:
        import capo_omics.types.sse_config

        out["sseConfig"] = capo_omics.types.sse_config.serialize_json(
            value["sse_config"]
        )
    out["storeFormat"] = value["store_format"]
    if "store_options" in value:
        import capo_omics.types.store_options

        out["storeOptions"] = capo_omics.types.store_options.serialize_json(
            value["store_options"]
        )
    return out


def deserialize_json(data: dict) -> CreateAnnotationStoreRequest:
    out: CreateAnnotationStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("reference") is not None:
        import capo_omics.types.reference_item

        out["reference"] = capo_omics.types.reference_item.deserialize_json(
            data["reference"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    if data.get("sseConfig") is not None:
        import capo_omics.types.sse_config

        out["sse_config"] = capo_omics.types.sse_config.deserialize_json(
            data["sseConfig"]
        )
    if data.get("storeFormat") is not None:
        out["store_format"] = data["storeFormat"]
    else:
        out["store_format"] = ""
    if data.get("storeOptions") is not None:
        import capo_omics.types.store_options

        out["store_options"] = capo_omics.types.store_options.deserialize_json(
            data["storeOptions"]
        )
    return out
