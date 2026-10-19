"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetImageSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.arn
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.date
    import capo_medical_imaging.types.image_set_external_version_id
    import capo_medical_imaging.types.image_set_id
    import capo_medical_imaging.types.image_set_state
    import capo_medical_imaging.types.image_set_workflow_status
    import capo_medical_imaging.types.message
    import capo_medical_imaging.types.overrides
    import capo_medical_imaging.types.storage_tier


class GetImageSetResponse(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier.</p>"""
    version_id: "capo_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    """<p>The image set version identifier.</p>"""
    image_set_state: "capo_medical_imaging.types.image_set_state.ImageSetState"
    """<p>The image set state.</p>"""
    image_set_workflow_status: NotRequired[
        "capo_medical_imaging.types.image_set_workflow_status.ImageSetWorkflowStatus"
    ]
    """<p>The image set workflow status.</p>"""
    created_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when image set properties were created.</p>"""
    updated_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when image set properties were updated.</p>"""
    deleted_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when the image set properties were deleted.</p>"""
    message: NotRequired["capo_medical_imaging.types.message.Message"]
    """<p>The error message thrown if an image set action fails.</p>"""
    image_set_arn: NotRequired["capo_medical_imaging.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) assigned to the image set.</p>"""
    overrides: NotRequired["capo_medical_imaging.types.overrides.Overrides"]
    """<p>This object contains the details of any overrides used while creating a specific image set version. If an image set was copied or updated using the <code>force</code> flag, this object will contain the <code>forced</code> flag.</p>"""
    is_primary: NotRequired["bool"]
    """<p>The flag to determine whether the image set is primary or not.</p>"""
    last_accessed_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>When the image set was last accessed.</p>"""
    storage_tier: NotRequired["capo_medical_imaging.types.storage_tier.StorageTier"]
    """<p>The storage tier of the image set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImageSetResponse) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    out["imageSetId"] = value["image_set_id"]
    out["versionId"] = value["version_id"]
    import capo_medical_imaging.types.image_set_state

    out["imageSetState"] = capo_medical_imaging.types.image_set_state.serialize_json(
        value["image_set_state"]
    )
    if "image_set_workflow_status" in value:
        import capo_medical_imaging.types.image_set_workflow_status

        out["imageSetWorkflowStatus"] = (
            capo_medical_imaging.types.image_set_workflow_status.serialize_json(
                value["image_set_workflow_status"]
            )
        )
    if "created_at" in value:
        import capo_medical_imaging.types.date

        out["createdAt"] = capo_medical_imaging.types.date.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_medical_imaging.types.date

        out["updatedAt"] = capo_medical_imaging.types.date.serialize_json(
            value["updated_at"]
        )
    if "deleted_at" in value:
        import capo_medical_imaging.types.date

        out["deletedAt"] = capo_medical_imaging.types.date.serialize_json(
            value["deleted_at"]
        )
    if "message" in value:
        out["message"] = value["message"]
    if "image_set_arn" in value:
        out["imageSetArn"] = value["image_set_arn"]
    if "overrides" in value:
        import capo_medical_imaging.types.overrides

        out["overrides"] = capo_medical_imaging.types.overrides.serialize_json(
            value["overrides"]
        )
    if "is_primary" in value:
        out["isPrimary"] = value["is_primary"]
    if "last_accessed_at" in value:
        import capo_medical_imaging.types.date

        out["lastAccessedAt"] = capo_medical_imaging.types.date.serialize_json(
            value["last_accessed_at"]
        )
    if "storage_tier" in value:
        import capo_medical_imaging.types.storage_tier

        out["storageTier"] = capo_medical_imaging.types.storage_tier.serialize_json(
            value["storage_tier"]
        )
    return out


def deserialize_json(data: dict) -> GetImageSetResponse:
    out: GetImageSetResponse = {}  # type: ignore[typeddict-item]
    if data.get("datastoreId") is not None:
        out["datastore_id"] = data["datastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("imageSetId") is not None:
        out["image_set_id"] = data["imageSetId"]
    else:
        out["image_set_id"] = ""
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    else:
        out["version_id"] = ""
    if data.get("imageSetState") is not None:
        import capo_medical_imaging.types.image_set_state

        out["image_set_state"] = (
            capo_medical_imaging.types.image_set_state.deserialize_json(
                data["imageSetState"]
            )
        )
    else:
        import typing

        out["image_set_state"] = typing.cast(
            "capo_medical_imaging.types.image_set_state.ImageSetState", ""
        )
    if data.get("imageSetWorkflowStatus") is not None:
        import capo_medical_imaging.types.image_set_workflow_status

        out["image_set_workflow_status"] = (
            capo_medical_imaging.types.image_set_workflow_status.deserialize_json(
                data["imageSetWorkflowStatus"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_medical_imaging.types.date

        out["created_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_medical_imaging.types.date

        out["updated_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["updatedAt"]
        )
    if data.get("deletedAt") is not None:
        import capo_medical_imaging.types.date

        out["deleted_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["deletedAt"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("imageSetArn") is not None:
        out["image_set_arn"] = data["imageSetArn"]
    if data.get("overrides") is not None:
        import capo_medical_imaging.types.overrides

        out["overrides"] = capo_medical_imaging.types.overrides.deserialize_json(
            data["overrides"]
        )
    if data.get("isPrimary") is not None:
        out["is_primary"] = data["isPrimary"]
    if data.get("lastAccessedAt") is not None:
        import capo_medical_imaging.types.date

        out["last_accessed_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["lastAccessedAt"]
        )
    if data.get("storageTier") is not None:
        import capo_medical_imaging.types.storage_tier

        out["storage_tier"] = capo_medical_imaging.types.storage_tier.deserialize_json(
            data["storageTier"]
        )
    return out
