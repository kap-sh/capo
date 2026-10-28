"""Generated from Smithy shape ``com.amazonaws.appconfig#TreatmentOverrides``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_appconfig.errors import DeserializationError, SerializationError
from capo_appconfig.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_appconfig.types.treatment_override_map


class TreatmentOverridesInlineMember(TypedDict, closed=True):
    Inline: "capo_appconfig.types.treatment_override_map.TreatmentOverrideMap"


TreatmentOverrides: TypeAlias = TreatmentOverridesInlineMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: TreatmentOverrides) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"TreatmentOverrides: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Inline" in value:
        import capo_appconfig.types.treatment_override_map

        return {
            "Inline": capo_appconfig.types.treatment_override_map.serialize_json(
                value["Inline"]
            )
        }
    else:
        raise SerializationError("TreatmentOverrides: no variant present")


def deserialize_json(data: dict) -> TreatmentOverrides:
    if data.get("Inline") is not None:
        import capo_appconfig.types.treatment_override_map

        return {
            "Inline": capo_appconfig.types.treatment_override_map.deserialize_json(
                data["Inline"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("TreatmentOverrides: no recognized variant key")
