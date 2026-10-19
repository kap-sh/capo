"""Generated from Smithy shape ``com.amazonaws.omics#CreateAnnotationStoreVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.creation_time
    import capo_omics.types.resource_id
    import capo_omics.types.store_name
    import capo_omics.types.version_name
    import capo_omics.types.version_options
    import capo_omics.types.version_status


class CreateAnnotationStoreVersionResponse(TypedDict, closed=True):
    id: "capo_omics.types.resource_id.ResourceId"
    """<p> A generated ID for the annotation store </p>"""
    version_name: "capo_omics.types.version_name.VersionName"
    """<p> The name given to an annotation store version to distinguish it from other versions. </p>"""
    store_id: "capo_omics.types.resource_id.ResourceId"
    """<p> The ID for the annotation store from which new versions are being created. </p>"""
    version_options: NotRequired["capo_omics.types.version_options.VersionOptions"]
    """<p> The options for an annotation store version. </p>"""
    name: "capo_omics.types.store_name.StoreName"
    """<p> The name given to an annotation store version to distinguish it from other versions. </p>"""
    status: "capo_omics.types.version_status.VersionStatus"
    """<p> The status of a annotation store version. </p>"""
    creation_time: "capo_omics.types.creation_time.CreationTime"
    """<p> The time stamp for the creation of an annotation store version. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnnotationStoreVersionResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["versionName"] = value["version_name"]
    out["storeId"] = value["store_id"]
    if "version_options" in value:
        import capo_omics.types.version_options

        out["versionOptions"] = capo_omics.types.version_options.serialize_json(
            value["version_options"]
        )
    out["name"] = value["name"]
    out["status"] = value["status"]
    import capo_omics.types.creation_time

    out["creationTime"] = capo_omics.types.creation_time.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> CreateAnnotationStoreVersionResponse:
    out: CreateAnnotationStoreVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    else:
        out["version_name"] = ""
    if data.get("storeId") is not None:
        out["store_id"] = data["storeId"]
    else:
        out["store_id"] = ""
    if data.get("versionOptions") is not None:
        import capo_omics.types.version_options

        out["version_options"] = capo_omics.types.version_options.deserialize_json(
            data["versionOptions"]
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
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
