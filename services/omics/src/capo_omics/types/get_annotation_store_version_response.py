"""Generated from Smithy shape ``com.amazonaws.omics#GetAnnotationStoreVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.arn
    import capo_omics.types.creation_time
    import capo_omics.types.description
    import capo_omics.types.resource_id
    import capo_omics.types.status_message
    import capo_omics.types.store_name
    import capo_omics.types.tag_map
    import capo_omics.types.update_time
    import capo_omics.types.version_name
    import capo_omics.types.version_options
    import capo_omics.types.version_status


class GetAnnotationStoreVersionResponse(TypedDict, closed=True):
    store_id: "capo_omics.types.resource_id.ResourceId"
    """<p> The store ID for annotation store version. </p>"""
    id: "capo_omics.types.resource_id.ResourceId"
    """<p> The annotation store version ID. </p>"""
    status: "capo_omics.types.version_status.VersionStatus"
    """<p> The status of an annotation store version. </p>"""
    version_arn: "capo_omics.types.arn.Arn"
    """<p> The Arn for the annotation store. </p>"""
    name: "capo_omics.types.store_name.StoreName"
    """<p> The name of the annotation store. </p>"""
    version_name: "capo_omics.types.version_name.VersionName"
    """<p> The name given to an annotation store version to distinguish it from others. </p>"""
    description: "capo_omics.types.description.Description"
    """<p> The description for an annotation store version. </p>"""
    creation_time: "capo_omics.types.creation_time.CreationTime"
    """<p> The time stamp for when an annotation store version was created. </p>"""
    update_time: "capo_omics.types.update_time.UpdateTime"
    """<p> The time stamp for when an annotation store version was updated. </p>"""
    tags: "capo_omics.types.tag_map.TagMap"
    """<p> Any tags associated with an annotation store version. </p>"""
    version_options: NotRequired["capo_omics.types.version_options.VersionOptions"]
    """<p> The options for an annotation store version. </p>"""
    status_message: "capo_omics.types.status_message.StatusMessage"
    """<p> The status of an annotation store version. </p>"""
    version_size_bytes: "int"
    """<p> The size of the annotation store version in Bytes. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAnnotationStoreVersionResponse) -> dict:
    out: dict = {}
    out["storeId"] = value["store_id"]
    out["id"] = value["id"]
    out["status"] = value["status"]
    out["versionArn"] = value["version_arn"]
    out["name"] = value["name"]
    out["versionName"] = value["version_name"]
    out["description"] = value["description"]
    import capo_omics.types.creation_time

    out["creationTime"] = capo_omics.types.creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_omics.types.update_time

    out["updateTime"] = capo_omics.types.update_time.serialize_json(
        value["update_time"]
    )
    import capo_omics.types.tag_map

    out["tags"] = capo_omics.types.tag_map.serialize_json(value["tags"])
    if "version_options" in value:
        import capo_omics.types.version_options

        out["versionOptions"] = capo_omics.types.version_options.serialize_json(
            value["version_options"]
        )
    out["statusMessage"] = value["status_message"]
    out["versionSizeBytes"] = value["version_size_bytes"]
    return out


def deserialize_json(data: dict) -> GetAnnotationStoreVersionResponse:
    out: GetAnnotationStoreVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("storeId") is not None:
        out["store_id"] = data["storeId"]
    else:
        out["store_id"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("versionArn") is not None:
        out["version_arn"] = data["versionArn"]
    else:
        out["version_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("versionName") is not None:
        out["version_name"] = data["versionName"]
    else:
        out["version_name"] = ""
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
    if data.get("tags") is not None:
        import capo_omics.types.tag_map

        out["tags"] = capo_omics.types.tag_map.deserialize_json(data["tags"])
    else:
        out["tags"] = {}
    if data.get("versionOptions") is not None:
        import capo_omics.types.version_options

        out["version_options"] = capo_omics.types.version_options.deserialize_json(
            data["versionOptions"]
        )
    if data.get("statusMessage") is not None:
        out["status_message"] = data["statusMessage"]
    else:
        out["status_message"] = ""
    if data.get("versionSizeBytes") is not None:
        out["version_size_bytes"] = data["versionSizeBytes"]
    else:
        out["version_size_bytes"] = 0
    return out
