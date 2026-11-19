"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalCodingContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.encounter_type
    import capo_connecthealth.types.patient_status
    import capo_connecthealth.types.sensitive_iso_date_string
    import capo_connecthealth.types.sensitive_non_empty_string
    import capo_connecthealth.types.sex


class MedicalCodingContext(TypedDict, closed=True):
    sex: NotRequired["capo_connecthealth.types.sex.Sex"]
    """<p>The sex of the patient.</p>"""
    status: NotRequired["capo_connecthealth.types.patient_status.PatientStatus"]
    """<p>The status of the patient, either new or established.</p>"""
    date_of_birth: NotRequired[
        "capo_connecthealth.types.sensitive_iso_date_string.SensitiveIsoDateString"
    ]
    """<p>The date of birth of the patient, in YYYY-MM-DD format. The date can't be after the current date in UTC.</p>"""
    encounter_type: NotRequired["capo_connecthealth.types.encounter_type.EncounterType"]
    """<p>The type of the encounter, either in person or telehealth.</p>"""
    encounter_reason: NotRequired[
        "capo_connecthealth.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    ]
    """<p>The reason for the encounter. The reason can contain letters, numbers, spaces, periods, commas, and hyphens, and can't contain only spaces.</p>"""
    after_hours: NotRequired["bool"]
    """<p>Specifies whether the encounter took place outside regular business hours.</p>"""
    encounter_date: NotRequired[
        "capo_connecthealth.types.sensitive_iso_date_string.SensitiveIsoDateString"
    ]
    """<p>The date of the encounter, in YYYY-MM-DD format. The date can't be more than one day after the current date in UTC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalCodingContext) -> dict:
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
    if "encounter_type" in value:
        import capo_connecthealth.types.encounter_type

        out["encounterType"] = capo_connecthealth.types.encounter_type.serialize_json(
            value["encounter_type"]
        )
    if "encounter_reason" in value:
        out["encounterReason"] = value["encounter_reason"]
    if "after_hours" in value:
        out["afterHours"] = value["after_hours"]
    if "encounter_date" in value:
        out["encounterDate"] = value["encounter_date"]
    return out


def deserialize_json(data: dict) -> MedicalCodingContext:
    out: MedicalCodingContext = {}  # type: ignore[typeddict-item]
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
    if data.get("encounterType") is not None:
        import capo_connecthealth.types.encounter_type

        out["encounter_type"] = (
            capo_connecthealth.types.encounter_type.deserialize_json(
                data["encounterType"]
            )
        )
    if data.get("encounterReason") is not None:
        out["encounter_reason"] = data["encounterReason"]
    if data.get("afterHours") is not None:
        out["after_hours"] = data["afterHours"]
    if data.get("encounterDate") is not None:
        out["encounter_date"] = data["encounterDate"]
    return out


def redact_sensitive(value: MedicalCodingContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sex" in value:
        out["sex"] = "*** Sensitive Data Redacted ***"
    if "status" in value:
        out["status"] = "*** Sensitive Data Redacted ***"
    if "date_of_birth" in value:
        out["date_of_birth"] = "*** Sensitive Data Redacted ***"
    if "encounter_reason" in value:
        out["encounter_reason"] = "*** Sensitive Data Redacted ***"
    if "encounter_date" in value:
        out["encounter_date"] = "*** Sensitive Data Redacted ***"
    return out
