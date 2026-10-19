"""Generated from Smithy shape ``com.amazonaws.omics#CreateAnnotationStoreVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.description
    import capo_omics.types.store_name
    import capo_omics.types.tag_map
    import capo_omics.types.version_name
    import capo_omics.types.version_options


class CreateAnnotationStoreVersionRequest(TypedDict, closed=True):
    name: "capo_omics.types.store_name.StoreName"
    """<p> The name of an annotation store version from which versions are being created. </p>"""
    version_name: "capo_omics.types.version_name.VersionName"
    """<p> The name given to an annotation store version to distinguish it from other versions. </p>"""
    description: NotRequired["capo_omics.types.description.Description"]
    """<p> The description of an annotation store version. </p>"""
    version_options: NotRequired["capo_omics.types.version_options.VersionOptions"]
    """<p> The options for an annotation store version. </p>"""
    tags: NotRequired["capo_omics.types.tag_map.TagMap"]
    """<p> Any tags added to annotation store version. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnnotationStoreVersionRequest) -> dict:
    out: dict = {}
    out["versionName"] = value["version_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "version_options" in value:
        import capo_omics.types.version_options

        out["versionOptions"] = capo_omics.types.version_options.serialize_json(
            value["version_options"]
        )
    if "tags" in value:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAnnotationStoreVersionRequest:
    out: CreateAnnotationStoreVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    else:
        out["version_name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("versionOptions") is not None:
        import capo_omics.types.version_options

        out["version_options"] = capo_omics.types.version_options.deserialize_json(
            data["versionOptions"]
        )
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    return out
