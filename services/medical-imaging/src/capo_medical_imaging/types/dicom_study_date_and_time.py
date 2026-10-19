"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DICOMStudyDateAndTime``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.dicom_study_date
    import capo_medical_imaging.types.dicom_study_time


class DICOMStudyDateAndTime(TypedDict, closed=True):
    dicom_study_date: "capo_medical_imaging.types.dicom_study_date.DICOMStudyDate"
    """<p>The DICOM study date provided in <code>yyMMdd</code> format.</p>"""
    dicom_study_time: NotRequired[
        "capo_medical_imaging.types.dicom_study_time.DICOMStudyTime"
    ]
    """<p>The DICOM study time provided in <code>HHmmss.FFFFFF</code> format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DICOMStudyDateAndTime) -> dict:
    out: dict = {}
    out["DICOMStudyDate"] = value["dicom_study_date"]
    if "dicom_study_time" in value:
        out["DICOMStudyTime"] = value["dicom_study_time"]
    return out


def deserialize_json(data: dict) -> DICOMStudyDateAndTime:
    out: DICOMStudyDateAndTime = {}  # type: ignore[typeddict-item]
    if data.get("DICOMStudyDate") is not None:
        out["dicom_study_date"] = data["DICOMStudyDate"]
    else:
        out["dicom_study_date"] = ""
    if data.get("DICOMStudyTime") is not None:
        out["dicom_study_time"] = data["DICOMStudyTime"]
    return out


def redact_sensitive(value: DICOMStudyDateAndTime) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dicom_study_date" in value:
        out["dicom_study_date"] = "*** Sensitive Data Redacted ***"
    if "dicom_study_time" in value:
        out["dicom_study_time"] = "*** Sensitive Data Redacted ***"
    return out
