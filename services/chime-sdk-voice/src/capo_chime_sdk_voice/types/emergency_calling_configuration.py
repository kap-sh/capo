"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#EmergencyCallingConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.dnis_emergency_calling_configuration_list


class EmergencyCallingConfiguration(TypedDict, closed=True):
    dnis: NotRequired[
        "capo_chime_sdk_voice.types.dnis_emergency_calling_configuration_list.DNISEmergencyCallingConfigurationList"
    ]
    """<p>The Dialed Number Identification Service (DNIS) emergency calling configuration details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmergencyCallingConfiguration) -> dict:
    out: dict = {}
    if "dnis" in value:
        import capo_chime_sdk_voice.types.dnis_emergency_calling_configuration_list

        out["DNIS"] = (
            capo_chime_sdk_voice.types.dnis_emergency_calling_configuration_list.serialize_json(
                value["dnis"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmergencyCallingConfiguration:
    out: EmergencyCallingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DNIS") is not None:
        import capo_chime_sdk_voice.types.dnis_emergency_calling_configuration_list

        out["dnis"] = (
            capo_chime_sdk_voice.types.dnis_emergency_calling_configuration_list.deserialize_json(
                data["DNIS"]
            )
        )
    return out


def redact_sensitive(value: EmergencyCallingConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dnis" in value:
        import capo_chime_sdk_voice.types.dnis_emergency_calling_configuration_list

        out["dnis"] = (
            capo_chime_sdk_voice.types.dnis_emergency_calling_configuration_list.redact_sensitive(
                value["dnis"]
            )
        )
    return out
