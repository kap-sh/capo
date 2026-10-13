"""Generated from Smithy shape ``com.amazonaws.medicalimaging#GetDICOMImportJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_medical_imaging.types.dicom_import_job_properties


class GetDICOMImportJobResponse(TypedDict, closed=True):
    job_properties: "capo_medical_imaging.types.dicom_import_job_properties.DICOMImportJobProperties"
    """<p>The properties of the import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDICOMImportJobResponse) -> dict:
    out: dict = {}
    import capo_medical_imaging.types.dicom_import_job_properties

    out["jobProperties"] = (
        capo_medical_imaging.types.dicom_import_job_properties.serialize_json(
            value["job_properties"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetDICOMImportJobResponse:
    out: GetDICOMImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobProperties") is not None:
        import capo_medical_imaging.types.dicom_import_job_properties

        out["job_properties"] = (
            capo_medical_imaging.types.dicom_import_job_properties.deserialize_json(
                data["jobProperties"]
            )
        )
    else:
        raise DeserializationError("GetDICOMImportJobResponse.job_properties required")
    return out


def redact_sensitive(value: GetDICOMImportJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_properties" in value:
        import capo_medical_imaging.types.dicom_import_job_properties

        out["job_properties"] = (
            capo_medical_imaging.types.dicom_import_job_properties.redact_sensitive(
                value["job_properties"]
            )
        )
    return out
