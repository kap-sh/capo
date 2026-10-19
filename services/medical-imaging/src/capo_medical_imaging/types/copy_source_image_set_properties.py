"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CopySourceImageSetProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.arn
    import capo_medical_imaging.types.date
    import capo_medical_imaging.types.image_set_external_version_id
    import capo_medical_imaging.types.image_set_id
    import capo_medical_imaging.types.image_set_state
    import capo_medical_imaging.types.image_set_workflow_status


class CopySourceImageSetProperties(TypedDict, closed=True):
    image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier for the copied source image set.</p>"""
    latest_version_id: "capo_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    """<p>The latest version identifier for the copied source image set.</p>"""
    image_set_state: NotRequired[
        "capo_medical_imaging.types.image_set_state.ImageSetState"
    ]
    """<p>The image set state of the copied source image set.</p>"""
    image_set_workflow_status: NotRequired[
        "capo_medical_imaging.types.image_set_workflow_status.ImageSetWorkflowStatus"
    ]
    """<p>The workflow status of the copied source image set.</p>"""
    created_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when the source image set properties were created.</p>"""
    updated_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when the source image set properties were updated.</p>"""
    image_set_arn: NotRequired["capo_medical_imaging.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) assigned to the source image set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopySourceImageSetProperties) -> dict:
    out: dict = {}
    out["imageSetId"] = value["image_set_id"]
    out["latestVersionId"] = value["latest_version_id"]
    if "image_set_state" in value:
        import capo_medical_imaging.types.image_set_state

        out["imageSetState"] = (
            capo_medical_imaging.types.image_set_state.serialize_json(
                value["image_set_state"]
            )
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
    if "image_set_arn" in value:
        out["imageSetArn"] = value["image_set_arn"]
    return out


def deserialize_json(data: dict) -> CopySourceImageSetProperties:
    out: CopySourceImageSetProperties = {}  # type: ignore[typeddict-item]
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
    if data.get("imageSetArn") is not None:
        out["image_set_arn"] = data["imageSetArn"]
    return out
