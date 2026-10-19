"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PreviewPrivacyImpactParametersInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.differential_privacy_preview_parameters_input


class _PreviewPrivacyImpactParametersInput_differentialPrivacy(TypedDict, closed=True):
    differentialPrivacy: "capo_cleanrooms.types.differential_privacy_preview_parameters_input.DifferentialPrivacyPreviewParametersInput"


PreviewPrivacyImpactParametersInput: TypeAlias = (
    _PreviewPrivacyImpactParametersInput_differentialPrivacy | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PreviewPrivacyImpactParametersInput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PreviewPrivacyImpactParametersInput: cannot serialize unknown variant {value.name!r}"
        )
    elif "differentialPrivacy" in value:
        import capo_cleanrooms.types.differential_privacy_preview_parameters_input

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_preview_parameters_input.serialize_json(
                value["differentialPrivacy"]
            )
        }
    else:
        raise SerializationError(
            "PreviewPrivacyImpactParametersInput: no variant present"
        )


def deserialize_json(data: dict) -> PreviewPrivacyImpactParametersInput:
    if data.get("differentialPrivacy") is not None:
        import capo_cleanrooms.types.differential_privacy_preview_parameters_input

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_preview_parameters_input.deserialize_json(
                data["differentialPrivacy"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "PreviewPrivacyImpactParametersInput: no recognized variant key"
        )
