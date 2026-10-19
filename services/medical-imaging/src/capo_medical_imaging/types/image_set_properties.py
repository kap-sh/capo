"""Generated from Smithy shape ``com.amazonaws.medicalimaging#ImageSetProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.date
    import capo_medical_imaging.types.image_set_external_version_id
    import capo_medical_imaging.types.image_set_id
    import capo_medical_imaging.types.image_set_state
    import capo_medical_imaging.types.image_set_workflow_status
    import capo_medical_imaging.types.message
    import capo_medical_imaging.types.overrides


class ImageSetProperties(TypedDict, closed=True):
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
    """<p>The timestamp when the image set properties were created.</p>"""
    updated_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when the image set properties were updated.</p>"""
    deleted_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when the image set properties were deleted.</p>"""
    message: NotRequired["capo_medical_imaging.types.message.Message"]
    """<p>The error message thrown if an image set action fails.</p>"""
    overrides: NotRequired["capo_medical_imaging.types.overrides.Overrides"]
    """<p>Contains details on overrides used when creating the returned version of an image set. For example, if <code>forced</code> exists, the <code>forced</code> flag was used when creating the image set.</p>"""
    is_primary: NotRequired["bool"]
    """<p>The flag to determine whether the image set is primary or not.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageSetProperties) -> dict:
    out: dict = {}
    out["imageSetId"] = value["image_set_id"]
    out["versionId"] = value["version_id"]
    import capo_medical_imaging.types.image_set_state

    out["imageSetState"] = capo_medical_imaging.types.image_set_state.serialize_json(
        value["image_set_state"]
    )
    if "image_set_workflow_status" in value:
        import capo_medical_imaging.types.image_set_workflow_status

        out["ImageSetWorkflowStatus"] = (
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
    if "overrides" in value:
        import capo_medical_imaging.types.overrides

        out["overrides"] = capo_medical_imaging.types.overrides.serialize_json(
            value["overrides"]
        )
    if "is_primary" in value:
        out["isPrimary"] = value["is_primary"]
    return out


def deserialize_json(data: dict) -> ImageSetProperties:
    out: ImageSetProperties = {}  # type: ignore[typeddict-item]
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
    if data.get("ImageSetWorkflowStatus") is not None:
        import capo_medical_imaging.types.image_set_workflow_status

        out["image_set_workflow_status"] = (
            capo_medical_imaging.types.image_set_workflow_status.deserialize_json(
                data["ImageSetWorkflowStatus"]
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
    if data.get("overrides") is not None:
        import capo_medical_imaging.types.overrides

        out["overrides"] = capo_medical_imaging.types.overrides.deserialize_json(
            data["overrides"]
        )
    if data.get("isPrimary") is not None:
        out["is_primary"] = data["isPrimary"]
    return out
