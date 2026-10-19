"""Generated from Smithy shape ``com.amazonaws.connecthealth#PatientInsightsEncounterContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.sensitive_non_empty_string


class PatientInsightsEncounterContext(TypedDict, closed=True):
    encounter_reason: (
        "capo_connecthealth.types.sensitive_non_empty_string.SensitiveNonEmptyString"
    )
    """<p>Chief complaint for the visit</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PatientInsightsEncounterContext) -> dict:
    out: dict = {}
    out["encounterReason"] = value["encounter_reason"]
    return out


def deserialize_json(data: dict) -> PatientInsightsEncounterContext:
    out: PatientInsightsEncounterContext = {}  # type: ignore[typeddict-item]
    if data.get("encounterReason") is not None:
        out["encounter_reason"] = data["encounterReason"]
    else:
        out["encounter_reason"] = ""
    return out


def redact_sensitive(value: PatientInsightsEncounterContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "encounter_reason" in value:
        out["encounter_reason"] = "*** Sensitive Data Redacted ***"
    return out
