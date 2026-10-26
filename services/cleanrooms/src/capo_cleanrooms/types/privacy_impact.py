"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyImpact``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.differential_privacy_privacy_impact


class _PrivacyImpact_differentialPrivacy(TypedDict, closed=True):
    differentialPrivacy: "capo_cleanrooms.types.differential_privacy_privacy_impact.DifferentialPrivacyPrivacyImpact"


PrivacyImpact: TypeAlias = _PrivacyImpact_differentialPrivacy | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyImpact) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PrivacyImpact: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "differentialPrivacy" in value:
        import capo_cleanrooms.types.differential_privacy_privacy_impact

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_privacy_impact.serialize_json(
                value["differentialPrivacy"]
            )
        }
    else:
        raise SerializationError("PrivacyImpact: no variant present")


def deserialize_json(data: dict) -> PrivacyImpact:
    if data.get("differentialPrivacy") is not None:
        import capo_cleanrooms.types.differential_privacy_privacy_impact

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_privacy_impact.deserialize_json(
                data["differentialPrivacy"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PrivacyImpact: no recognized variant key")
