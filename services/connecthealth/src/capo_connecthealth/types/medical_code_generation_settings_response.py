"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalCodeGenerationSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.non_null_boolean


class MedicalCodeGenerationSettingsResponse(TypedDict, closed=True):
    enabled: NotRequired["capo_connecthealth.types.non_null_boolean.NonNullBoolean"]
    """<p>Indicates whether medical code generation was requested for the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalCodeGenerationSettingsResponse) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    return out


def deserialize_json(data: dict) -> MedicalCodeGenerationSettingsResponse:
    out: MedicalCodeGenerationSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    return out
