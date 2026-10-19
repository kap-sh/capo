"""Generated from Smithy shape ``com.amazonaws.medicalimaging#UpdateImageSetMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.date
    import capo_medical_imaging.types.image_set_external_version_id
    import capo_medical_imaging.types.image_set_id
    import capo_medical_imaging.types.image_set_state
    import capo_medical_imaging.types.image_set_workflow_status
    import capo_medical_imaging.types.message


class UpdateImageSetMetadataResponse(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier.</p>"""
    latest_version_id: "capo_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    """<p>The latest image set version identifier.</p>"""
    image_set_state: "capo_medical_imaging.types.image_set_state.ImageSetState"
    """<p>The image set state.</p>"""
    image_set_workflow_status: NotRequired[
        "capo_medical_imaging.types.image_set_workflow_status.ImageSetWorkflowStatus"
    ]
    """<p>The image set workflow status.</p>"""
    created_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when image set metadata was created.</p>"""
    updated_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when image set metadata was updated.</p>"""
    message: NotRequired["capo_medical_imaging.types.message.Message"]
    """<p>The error message thrown if an update image set metadata action fails.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateImageSetMetadataResponse) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    out["imageSetId"] = value["image_set_id"]
    out["latestVersionId"] = value["latest_version_id"]
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
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UpdateImageSetMetadataResponse:
    out: UpdateImageSetMetadataResponse = {}  # type: ignore[typeddict-item]
    if data.get("datastoreId") is not None:
        out["datastore_id"] = data["datastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("imageSetId") is not None:
        out["image_set_id"] = data["imageSetId"]
    else:
        out["image_set_id"] = ""
    if data.get("latestVersionId") is not None:
        out["latest_version_id"] = data["latestVersionId"]
    else:
        out["latest_version_id"] = ""
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
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
