"""Generated from Smithy shape ``com.amazonaws.medicalimaging#SearchByAttributeValue``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_medical_imaging.errors import DeserializationError, SerializationError
from capo_medical_imaging.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_medical_imaging.types.date
    import capo_medical_imaging.types.dicom_accession_number
    import capo_medical_imaging.types.dicom_patient_id
    import capo_medical_imaging.types.dicom_series_instance_uid
    import capo_medical_imaging.types.dicom_study_date_and_time
    import capo_medical_imaging.types.dicom_study_id
    import capo_medical_imaging.types.dicom_study_instance_uid


class _SearchByAttributeValue_DICOMPatientId(TypedDict, closed=True):
    DICOMPatientId: "capo_medical_imaging.types.dicom_patient_id.DICOMPatientId"


class _SearchByAttributeValue_DICOMAccessionNumber(TypedDict, closed=True):
    DICOMAccessionNumber: (
        "capo_medical_imaging.types.dicom_accession_number.DICOMAccessionNumber"
    )


class _SearchByAttributeValue_DICOMStudyId(TypedDict, closed=True):
    DICOMStudyId: "capo_medical_imaging.types.dicom_study_id.DICOMStudyId"


class _SearchByAttributeValue_DICOMStudyInstanceUID(TypedDict, closed=True):
    DICOMStudyInstanceUID: (
        "capo_medical_imaging.types.dicom_study_instance_uid.DICOMStudyInstanceUID"
    )


class _SearchByAttributeValue_DICOMSeriesInstanceUID(TypedDict, closed=True):
    DICOMSeriesInstanceUID: (
        "capo_medical_imaging.types.dicom_series_instance_uid.DICOMSeriesInstanceUID"
    )


class _SearchByAttributeValue_createdAt(TypedDict, closed=True):
    createdAt: "capo_medical_imaging.types.date.Date"


class _SearchByAttributeValue_updatedAt(TypedDict, closed=True):
    updatedAt: "capo_medical_imaging.types.date.Date"


class _SearchByAttributeValue_DICOMStudyDateAndTime(TypedDict, closed=True):
    DICOMStudyDateAndTime: (
        "capo_medical_imaging.types.dicom_study_date_and_time.DICOMStudyDateAndTime"
    )


class _SearchByAttributeValue_isPrimary(TypedDict, closed=True):
    isPrimary: "bool"


SearchByAttributeValue: TypeAlias = (
    _SearchByAttributeValue_DICOMPatientId
    | _SearchByAttributeValue_DICOMAccessionNumber
    | _SearchByAttributeValue_DICOMStudyId
    | _SearchByAttributeValue_DICOMStudyInstanceUID
    | _SearchByAttributeValue_DICOMSeriesInstanceUID
    | _SearchByAttributeValue_createdAt
    | _SearchByAttributeValue_updatedAt
    | _SearchByAttributeValue_DICOMStudyDateAndTime
    | _SearchByAttributeValue_isPrimary
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SearchByAttributeValue) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"SearchByAttributeValue: cannot serialize unknown variant {value.name!r}"
        )
    elif "DICOMPatientId" in value:
        return {"DICOMPatientId": value["DICOMPatientId"]}
    elif "DICOMAccessionNumber" in value:
        return {"DICOMAccessionNumber": value["DICOMAccessionNumber"]}
    elif "DICOMStudyId" in value:
        return {"DICOMStudyId": value["DICOMStudyId"]}
    elif "DICOMStudyInstanceUID" in value:
        return {"DICOMStudyInstanceUID": value["DICOMStudyInstanceUID"]}
    elif "DICOMSeriesInstanceUID" in value:
        return {"DICOMSeriesInstanceUID": value["DICOMSeriesInstanceUID"]}
    elif "createdAt" in value:
        import capo_medical_imaging.types.date

        return {
            "createdAt": capo_medical_imaging.types.date.serialize_json(
                value["createdAt"]
            )
        }
    elif "updatedAt" in value:
        import capo_medical_imaging.types.date

        return {
            "updatedAt": capo_medical_imaging.types.date.serialize_json(
                value["updatedAt"]
            )
        }
    elif "DICOMStudyDateAndTime" in value:
        import capo_medical_imaging.types.dicom_study_date_and_time

        return {
            "DICOMStudyDateAndTime": capo_medical_imaging.types.dicom_study_date_and_time.serialize_json(
                value["DICOMStudyDateAndTime"]
            )
        }
    elif "isPrimary" in value:
        return {"isPrimary": value["isPrimary"]}
    else:
        raise SerializationError("SearchByAttributeValue: no variant present")


def deserialize_json(data: dict) -> SearchByAttributeValue:
    if data.get("DICOMPatientId") is not None:
        return {"DICOMPatientId": data["DICOMPatientId"]}
    elif data.get("DICOMAccessionNumber") is not None:
        return {"DICOMAccessionNumber": data["DICOMAccessionNumber"]}
    elif data.get("DICOMStudyId") is not None:
        return {"DICOMStudyId": data["DICOMStudyId"]}
    elif data.get("DICOMStudyInstanceUID") is not None:
        return {"DICOMStudyInstanceUID": data["DICOMStudyInstanceUID"]}
    elif data.get("DICOMSeriesInstanceUID") is not None:
        return {"DICOMSeriesInstanceUID": data["DICOMSeriesInstanceUID"]}
    elif data.get("createdAt") is not None:
        import capo_medical_imaging.types.date

        return {
            "createdAt": capo_medical_imaging.types.date.deserialize_json(
                data["createdAt"]
            )
        }
    elif data.get("updatedAt") is not None:
        import capo_medical_imaging.types.date

        return {
            "updatedAt": capo_medical_imaging.types.date.deserialize_json(
                data["updatedAt"]
            )
        }
    elif data.get("DICOMStudyDateAndTime") is not None:
        import capo_medical_imaging.types.dicom_study_date_and_time

        return {
            "DICOMStudyDateAndTime": capo_medical_imaging.types.dicom_study_date_and_time.deserialize_json(
                data["DICOMStudyDateAndTime"]
            )
        }
    elif data.get("isPrimary") is not None:
        return {"isPrimary": data["isPrimary"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("SearchByAttributeValue: no recognized variant key")


def redact_sensitive(
    value: SearchByAttributeValue,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "DICOMPatientId" in value:
        out["DICOMPatientId"] = "*** Sensitive Data Redacted ***"
    if "DICOMAccessionNumber" in value:
        out["DICOMAccessionNumber"] = "*** Sensitive Data Redacted ***"
    if "DICOMStudyId" in value:
        out["DICOMStudyId"] = "*** Sensitive Data Redacted ***"
    if "DICOMStudyInstanceUID" in value:
        out["DICOMStudyInstanceUID"] = "*** Sensitive Data Redacted ***"
    if "DICOMSeriesInstanceUID" in value:
        out["DICOMSeriesInstanceUID"] = "*** Sensitive Data Redacted ***"
    if "DICOMStudyDateAndTime" in value:
        import capo_medical_imaging.types.dicom_study_date_and_time

        out["DICOMStudyDateAndTime"] = (
            capo_medical_imaging.types.dicom_study_date_and_time.redact_sensitive(
                value["DICOMStudyDateAndTime"]
            )
        )
    return out
