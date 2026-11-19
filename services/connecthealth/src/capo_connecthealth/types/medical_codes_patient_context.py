"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalCodesPatientContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.patient_status
    import capo_connecthealth.types.sensitive_iso_date_string
    import capo_connecthealth.types.sensitive_non_empty_string
    import capo_connecthealth.types.sex


class MedicalCodesPatientContext(TypedDict, closed=True):
    sex: NotRequired["capo_connecthealth.types.sex.Sex"]
    """<p>The sex of the patient.</p>"""
    status: NotRequired["capo_connecthealth.types.patient_status.PatientStatus"]
    """<p>The status of the patient, either new or established.</p>"""
    date_of_birth: NotRequired[
        "capo_connecthealth.types.sensitive_iso_date_string.SensitiveIsoDateString"
    ]
    """<p>The date of birth of the patient, in YYYY-MM-DD format. The date can't be after the current date in UTC.</p>"""
    insurance: NotRequired[
        "capo_connecthealth.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The insurance of the patient.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalCodesPatientContext) -> dict:
    out: dict = {}
    if "sex" in value:
        import capo_connecthealth.types.sex

        out["sex"] = capo_connecthealth.types.sex.serialize_json(value["sex"])
    if "status" in value:
        import capo_connecthealth.types.patient_status

        out["status"] = capo_connecthealth.types.patient_status.serialize_json(
            value["status"]
        )
    if "date_of_birth" in value:
        out["dateOfBirth"] = value["date_of_birth"]
    if "insurance" in value:
        out["insurance"] = value["insurance"]
    return out


def deserialize_json(data: dict) -> MedicalCodesPatientContext:
    out: MedicalCodesPatientContext = {}  # type: ignore[typeddict-item]
    if data.get("sex") is not None:
        import capo_connecthealth.types.sex

        out["sex"] = capo_connecthealth.types.sex.deserialize_json(data["sex"])
    if data.get("status") is not None:
        import capo_connecthealth.types.patient_status

        out["status"] = capo_connecthealth.types.patient_status.deserialize_json(
            data["status"]
        )
    if data.get("dateOfBirth") is not None:
        out["date_of_birth"] = data["dateOfBirth"]
    if data.get("insurance") is not None:
        out["insurance"] = data["insurance"]
    return out


def redact_sensitive(value: MedicalCodesPatientContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sex" in value:
        out["sex"] = "*** Sensitive Data Redacted ***"
    if "status" in value:
        out["status"] = "*** Sensitive Data Redacted ***"
    if "date_of_birth" in value:
        out["date_of_birth"] = "*** Sensitive Data Redacted ***"
    if "insurance" in value:
        out["insurance"] = "*** Sensitive Data Redacted ***"
    return out
