"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DicomMetadataMapping``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.dicom_series_instance_uid
    import capo_medical_imaging.types.dicom_study_instance_uid
    import capo_medical_imaging.types.metadata_file_path


class DicomMetadataMapping(TypedDict, closed=True):
    study_instance_uid: (
        "capo_medical_imaging.types.dicom_study_instance_uid.DICOMStudyInstanceUID"
    )
    """<p>The Study Instance UID that identifies the study.</p>"""
    series_instance_uid: NotRequired[
        "capo_medical_imaging.types.dicom_series_instance_uid.DICOMSeriesInstanceUID"
    ]
    """<p>The Series Instance UID that identifies the series. This parameter is optional because the mapping might be at the study level.</p>"""
    metadata_file_path: "capo_medical_imaging.types.metadata_file_path.MetadataFilePath"
    """<p>The path to the JSON metadata file relative to inputS3Uri.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DicomMetadataMapping) -> dict:
    out: dict = {}
    out["studyInstanceUID"] = value["study_instance_uid"]
    if "series_instance_uid" in value:
        out["seriesInstanceUID"] = value["series_instance_uid"]
    out["metadataFilePath"] = value["metadata_file_path"]
    return out


def deserialize_json(data: dict) -> DicomMetadataMapping:
    out: DicomMetadataMapping = {}  # type: ignore[typeddict-item]
    if data.get("studyInstanceUID") is not None:
        out["study_instance_uid"] = data["studyInstanceUID"]
    else:
        raise DeserializationError("DicomMetadataMapping.study_instance_uid required")
    if data.get("seriesInstanceUID") is not None:
        out["series_instance_uid"] = data["seriesInstanceUID"]
    if data.get("metadataFilePath") is not None:
        out["metadata_file_path"] = data["metadataFilePath"]
    else:
        raise DeserializationError("DicomMetadataMapping.metadata_file_path required")
    return out


def redact_sensitive(value: DicomMetadataMapping) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "study_instance_uid" in value:
        out["study_instance_uid"] = "*** Sensitive Data Redacted ***"
    if "series_instance_uid" in value:
        out["series_instance_uid"] = "*** Sensitive Data Redacted ***"
    return out
