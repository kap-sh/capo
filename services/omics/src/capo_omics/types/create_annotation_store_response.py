"""Generated from Smithy shape ``com.amazonaws.omics#CreateAnnotationStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.creation_time
    import capo_omics.types.reference_item
    import capo_omics.types.resource_id
    import capo_omics.types.store_format
    import capo_omics.types.store_options
    import capo_omics.types.store_status
    import capo_omics.types.version_name


class CreateAnnotationStoreResponse(TypedDict, closed=True):
    id: "capo_omics.types.resource_id.ResourceId"
    """<p>The store's ID.</p>"""
    reference: NotRequired["capo_omics.types.reference_item.ReferenceItem"]
    """<p>The store's genome reference. Required for all stores except TSV format with generic annotations.</p>"""
    store_format: NotRequired["capo_omics.types.store_format.StoreFormat"]
    """<p>The annotation file format of the store.</p>"""
    store_options: NotRequired["capo_omics.types.store_options.StoreOptions"]
    """<p>The store's file parsing options.</p>"""
    status: "capo_omics.types.store_status.StoreStatus"
    """<p>The store's status.</p>"""
    name: "str"
    """<p>The store's name.</p>"""
    version_name: "capo_omics.types.version_name.VersionName"
    """<p> The name given to an annotation store version to distinguish it from other versions. </p>"""
    creation_time: "capo_omics.types.creation_time.CreationTime"
    """<p>When the store was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnnotationStoreResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "reference" in value:
        import capo_omics.types.reference_item

        out["reference"] = capo_omics.types.reference_item.serialize_json(
            value["reference"]
        )
    if "store_format" in value:
        out["storeFormat"] = value["store_format"]
    if "store_options" in value:
        import capo_omics.types.store_options

        out["storeOptions"] = capo_omics.types.store_options.serialize_json(
            value["store_options"]
        )
    out["status"] = value["status"]
    out["name"] = value["name"]
    out["versionName"] = value["version_name"]
    import capo_omics.types.creation_time

    out["creationTime"] = capo_omics.types.creation_time.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateAnnotationStoreResponse:
    out: CreateAnnotationStoreResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("reference") is not None:
        import capo_omics.types.reference_item

        out["reference"] = capo_omics.types.reference_item.deserialize_json(
            data["reference"]
        )
    if data.get("storeFormat") is not None:
        out["store_format"] = data["storeFormat"]
    if data.get("storeOptions") is not None:
        import capo_omics.types.store_options

        out["store_options"] = capo_omics.types.store_options.deserialize_json(
            data["storeOptions"]
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    else:
        out["version_name"] = ""
    if data.get("creationTime") is not None:
        import capo_omics.types.creation_time

        out["creation_time"] = capo_omics.types.creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
