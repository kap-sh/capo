"""Generated from Smithy shape ``com.amazonaws.omics#UpdateAnnotationStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.creation_time
    import capo_omics.types.description
    import capo_omics.types.reference_item
    import capo_omics.types.resource_id
    import capo_omics.types.store_format
    import capo_omics.types.store_options
    import capo_omics.types.store_status
    import capo_omics.types.update_time


class UpdateAnnotationStoreResponse(TypedDict, closed=True):
    id: "capo_omics.types.resource_id.ResourceId"
    """<p>The store's ID.</p>"""
    reference: "capo_omics.types.reference_item.ReferenceItem"
    """<p>The store's genome reference.</p>"""
    status: "capo_omics.types.store_status.StoreStatus"
    """<p>The store's status.</p>"""
    name: "str"
    """<p>The store's name.</p>"""
    description: "capo_omics.types.description.Description"
    """<p>The store's description.</p>"""
    creation_time: "capo_omics.types.creation_time.CreationTime"
    """<p>When the store was created.</p>"""
    update_time: "capo_omics.types.update_time.UpdateTime"
    """<p>When the store was updated.</p>"""
    store_options: NotRequired["capo_omics.types.store_options.StoreOptions"]
    """<p>Parsing options for the store.</p>"""
    store_format: NotRequired["capo_omics.types.store_format.StoreFormat"]
    """<p>The annotation file format of the store.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnnotationStoreResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import capo_omics.types.reference_item

    out["reference"] = capo_omics.types.reference_item.serialize_json(
        value["reference"]
    )
    out["status"] = value["status"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    import capo_omics.types.creation_time

    out["creationTime"] = capo_omics.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_omics.types.update_time

    out["updateTime"] = capo_omics.types.update_time.serialize_json(
        value["update_time"]
    )
    if "store_options" in value:
        import capo_omics.types.store_options

        out["storeOptions"] = capo_omics.types.store_options.serialize_json(
            value["store_options"]
        )
    if "store_format" in value:
        out["storeFormat"] = value["store_format"]
    return out


def deserialize_json(data: dict) -> UpdateAnnotationStoreResponse:
    out: UpdateAnnotationStoreResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("reference") is not None:
        import capo_omics.types.reference_item

        out["reference"] = capo_omics.types.reference_item.deserialize_json(
            data["reference"]
        )
    else:
        out["reference"] = {"$unknown": {"name": ""}}
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
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
    if data.get("updateTime") is not None:
        import capo_omics.types.update_time

        out["update_time"] = capo_omics.types.update_time.deserialize_json(
            data["updateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("storeOptions") is not None:
        import capo_omics.types.store_options

        out["store_options"] = capo_omics.types.store_options.deserialize_json(
            data["storeOptions"]
        )
    if data.get("storeFormat") is not None:
        out["store_format"] = data["storeFormat"]
    return out
