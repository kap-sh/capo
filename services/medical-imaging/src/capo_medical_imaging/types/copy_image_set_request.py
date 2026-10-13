"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CopyImageSetRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.copy_image_set_information
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.image_set_id


class CopyImageSetRequest(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    source_image_set_id: "capo_medical_imaging.types.image_set_id.ImageSetId"
    """<p>The source image set identifier.</p>"""
    copy_image_set_information: (
        "capo_medical_imaging.types.copy_image_set_information.CopyImageSetInformation"
    )
    """<p>Copy image set information.</p>"""
    force: NotRequired["bool"]
    """<p>Providing this parameter will force completion of the <code>CopyImageSet</code> operation, even if there are inconsistent Patient, Study, and/or Series level metadata elements between the <code>sourceImageSet</code> and <code>destinationImageSet</code>.</p>"""
    promote_to_primary: NotRequired["bool"]
    """<p>Providing this parameter will configure the <code>CopyImageSet</code> operation to promote the given image set to the primary DICOM hierarchy. If successful, a new primary image set ID will be returned as the destination image set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyImageSetRequest) -> dict:
    out: dict = {}
    import capo_medical_imaging.types.copy_image_set_information

    out["copyImageSetInformation"] = (
        capo_medical_imaging.types.copy_image_set_information.serialize_json(
            value["copy_image_set_information"]
        )
    )
    return out


def deserialize_json(data: dict) -> CopyImageSetRequest:
    out: CopyImageSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("copyImageSetInformation") is not None:
        import capo_medical_imaging.types.copy_image_set_information

        out["copy_image_set_information"] = (
            capo_medical_imaging.types.copy_image_set_information.deserialize_json(
                data["copyImageSetInformation"]
            )
        )
    else:
        raise DeserializationError(
            "CopyImageSetRequest.copy_image_set_information required"
        )
    return out


def redact_sensitive(value: CopyImageSetRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "copy_image_set_information" in value:
        import capo_medical_imaging.types.copy_image_set_information

        out["copy_image_set_information"] = (
            capo_medical_imaging.types.copy_image_set_information.redact_sensitive(
                value["copy_image_set_information"]
            )
        )
    return out
