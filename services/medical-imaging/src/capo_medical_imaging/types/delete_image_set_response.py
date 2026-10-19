"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DeleteImageSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.image_set_id
    import capo_medical_imaging.types.image_set_state
    import capo_medical_imaging.types.image_set_workflow_status


class DeleteImageSetResponse(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The image set identifier.</p>"""
    image_set_state: "capo_medical_imaging.types.image_set_state.ImageSetState"
    """<p>The image set state.</p>"""
    image_set_workflow_status: (
        "capo_medical_imaging.types.image_set_workflow_status.ImageSetWorkflowStatus"
    )
    """<p>The image set workflow status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImageSetResponse) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    out["imageSetId"] = value["image_set_id"]
    import capo_medical_imaging.types.image_set_state

    out["imageSetState"] = capo_medical_imaging.types.image_set_state.serialize_json(
        value["image_set_state"]
    )
    import capo_medical_imaging.types.image_set_workflow_status

    out["imageSetWorkflowStatus"] = (
        capo_medical_imaging.types.image_set_workflow_status.serialize_json(
            value["image_set_workflow_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteImageSetResponse:
    out: DeleteImageSetResponse = {}  # type: ignore[typeddict-item]
    if data.get("datastoreId") is not None:
        out["datastore_id"] = data["datastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("imageSetId") is not None:
        out["image_set_id"] = data["imageSetId"]
    else:
        out["image_set_id"] = ""
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
    else:
        import typing

        out["image_set_workflow_status"] = typing.cast(
            "capo_medical_imaging.types.image_set_workflow_status.ImageSetWorkflowStatus",
            "",
        )
    return out
