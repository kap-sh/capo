"""Generated from Smithy shape ``com.amazonaws.medicalimaging#CopySourceImageSetInformation``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.image_set_external_version_id
    import capo_medical_imaging.types.metadata_copies


class CopySourceImageSetInformation(TypedDict, closed=True):
    latest_version_id: "capo_medical_imaging.types.image_set_external_version_id.ImageSetExternalVersionId"
    """<p>The latest version identifier for the source image set.</p>"""
    dicom_copies: NotRequired[
        "capo_medical_imaging.types.metadata_copies.MetadataCopies"
    ]
    """<p>Contains <code>MetadataCopies</code> structure and wraps information related to specific copy use cases. For example, when copying subsets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CopySourceImageSetInformation) -> dict:
    out: dict = {}
    out["latestVersionId"] = value["latest_version_id"]
    if "dicom_copies" in value:
        import capo_medical_imaging.types.metadata_copies

        out["DICOMCopies"] = capo_medical_imaging.types.metadata_copies.serialize_json(
            value["dicom_copies"]
        )
    return out


def deserialize_json(data: dict) -> CopySourceImageSetInformation:
    out: CopySourceImageSetInformation = {}  # type: ignore[typeddict-item]
    if data.get("latestVersionId") is not None:
        out["latest_version_id"] = data["latestVersionId"]
    else:
        raise DeserializationError(
            "CopySourceImageSetInformation.latest_version_id required"
        )
    if data.get("DICOMCopies") is not None:
        import capo_medical_imaging.types.metadata_copies

        out["dicom_copies"] = (
            capo_medical_imaging.types.metadata_copies.deserialize_json(
                data["DICOMCopies"]
            )
        )
    return out


def redact_sensitive(value: CopySourceImageSetInformation) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dicom_copies" in value:
        import capo_medical_imaging.types.metadata_copies

        out["dicom_copies"] = (
            capo_medical_imaging.types.metadata_copies.redact_sensitive(
                value["dicom_copies"]
            )
        )
    return out
