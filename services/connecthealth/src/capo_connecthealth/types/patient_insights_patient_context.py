"""Generated from Smithy shape ``com.amazonaws.connecthealth#PatientInsightsPatientContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.pronouns
    import capo_connecthealth.types.sensitive_iso_date_string
    import capo_connecthealth.types.sensitive_non_empty_string


class PatientInsightsPatientContext(TypedDict, closed=True):
    patient_id: (
        "capo_connecthealth.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>Unique identifier of the patient</p>"""
    date_of_birth: NotRequired[
        "capo_connecthealth.types.sensitive_iso_date_string.SensitiveIsoDateString"
    ]
    """<p>Date of birth of the patient.</p>"""
    pronouns: NotRequired["capo_connecthealth.types.pronouns.Pronouns"]
    """<p>Pronouns preferred by the patient.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PatientInsightsPatientContext) -> dict:
    out: dict = {}
    out["patientId"] = value["patient_id"]
    if "date_of_birth" in value:
        out["dateOfBirth"] = value["date_of_birth"]
    if "pronouns" in value:
        import capo_connecthealth.types.pronouns

        out["pronouns"] = capo_connecthealth.types.pronouns.serialize_json(
            value["pronouns"]
        )
    return out


def deserialize_json(data: dict) -> PatientInsightsPatientContext:
    out: PatientInsightsPatientContext = {}  # type: ignore[typeddict-item]
    if data.get("patientId") is not None:
        out["patient_id"] = data["patientId"]
    else:
        out["patient_id"] = ""
    if data.get("dateOfBirth") is not None:
        out["date_of_birth"] = data["dateOfBirth"]
    if data.get("pronouns") is not None:
        import capo_connecthealth.types.pronouns

        out["pronouns"] = capo_connecthealth.types.pronouns.deserialize_json(
            data["pronouns"]
        )
    return out


def redact_sensitive(value: PatientInsightsPatientContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "patient_id" in value:
        out["patient_id"] = "*** Sensitive Data Redacted ***"
    if "date_of_birth" in value:
        out["date_of_birth"] = "*** Sensitive Data Redacted ***"
    if "pronouns" in value:
        out["pronouns"] = "*** Sensitive Data Redacted ***"
    return out
