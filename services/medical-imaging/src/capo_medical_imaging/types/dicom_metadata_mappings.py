"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DicomMetadataMappings``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_medical_imaging.types.dicom_metadata_mapping

DicomMetadataMappings: TypeAlias = list[
    "capo_medical_imaging.types.dicom_metadata_mapping.DicomMetadataMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: DicomMetadataMappings) -> list:
    import capo_medical_imaging.types.dicom_metadata_mapping

    out: list = []
    for item in value:
        out.append(
            capo_medical_imaging.types.dicom_metadata_mapping.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DicomMetadataMappings:
    import capo_medical_imaging.types.dicom_metadata_mapping

    out: DicomMetadataMappings = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_medical_imaging.types.dicom_metadata_mapping.deserialize_json(item)
        )
    return out


def redact_sensitive(value: DicomMetadataMappings) -> list[Any]:
    import capo_medical_imaging.types.dicom_metadata_mapping

    return [
        capo_medical_imaging.types.dicom_metadata_mapping.redact_sensitive(item)
        for item in value
    ]
