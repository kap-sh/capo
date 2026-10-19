"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DicomJsonMetadataImportConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.dicom_metadata_mappings


class DicomJsonMetadataImportConfiguration(TypedDict, closed=True):
    dicom_metadata_mappings: (
        "capo_medical_imaging.types.dicom_metadata_mappings.DicomMetadataMappings"
    )
    """<p>Maps DCM files to their metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DicomJsonMetadataImportConfiguration) -> dict:
    out: dict = {}
    import capo_medical_imaging.types.dicom_metadata_mappings

    out["dicomMetadataMappings"] = (
        capo_medical_imaging.types.dicom_metadata_mappings.serialize_json(
            value["dicom_metadata_mappings"]
        )
    )
    return out


def deserialize_json(data: dict) -> DicomJsonMetadataImportConfiguration:
    out: DicomJsonMetadataImportConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("dicomMetadataMappings") is not None:
        import capo_medical_imaging.types.dicom_metadata_mappings

        out["dicom_metadata_mappings"] = (
            capo_medical_imaging.types.dicom_metadata_mappings.deserialize_json(
                data["dicomMetadataMappings"]
            )
        )
    else:
        out["dicom_metadata_mappings"] = []
    return out


def redact_sensitive(value: DicomJsonMetadataImportConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dicom_metadata_mappings" in value:
        import capo_medical_imaging.types.dicom_metadata_mappings

        out["dicom_metadata_mappings"] = (
            capo_medical_imaging.types.dicom_metadata_mappings.redact_sensitive(
                value["dicom_metadata_mappings"]
            )
        )
    return out
