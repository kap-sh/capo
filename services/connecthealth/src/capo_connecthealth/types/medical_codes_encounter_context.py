"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalCodesEncounterContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.encounter_type
    import capo_connecthealth.types.sensitive_iso_date_string
    import capo_connecthealth.types.sensitive_non_empty_string
    import capo_connecthealth.types.sensitive_non_negative_integer


class MedicalCodesEncounterContext(TypedDict, closed=True):
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
    encounter_duration_minutes: NotRequired[
        "capo_connecthealth.types.sensitive_non_negative_integer.SensitiveNonNegativeInteger"
    ]
    """<p>The duration of the encounter, in minutes, from 1 to 1440.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalCodesEncounterContext) -> dict:
    out: dict = {}
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
    if "encounter_duration_minutes" in value:
        out["encounterDurationMinutes"] = value["encounter_duration_minutes"]
    return out


def deserialize_json(data: dict) -> MedicalCodesEncounterContext:
    out: MedicalCodesEncounterContext = {}  # type: ignore[typeddict-item]
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
    if data.get("encounterDurationMinutes") is not None:
        out["encounter_duration_minutes"] = data["encounterDurationMinutes"]
    return out


def redact_sensitive(value: MedicalCodesEncounterContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "encounter_reason" in value:
        out["encounter_reason"] = "*** Sensitive Data Redacted ***"
    if "encounter_date" in value:
        out["encounter_date"] = "*** Sensitive Data Redacted ***"
    if "encounter_duration_minutes" in value:
        out["encounter_duration_minutes"] = "*** Sensitive Data Redacted ***"
    return out
