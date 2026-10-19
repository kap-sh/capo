"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetTemplateParametersInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.access_budgets_privacy_template_parameters_input
    import capo_cleanrooms.types.differential_privacy_template_parameters_input


class _PrivacyBudgetTemplateParametersInput_differentialPrivacy(TypedDict, closed=True):
    differentialPrivacy: "capo_cleanrooms.types.differential_privacy_template_parameters_input.DifferentialPrivacyTemplateParametersInput"


class _PrivacyBudgetTemplateParametersInput_accessBudget(TypedDict, closed=True):
    accessBudget: "capo_cleanrooms.types.access_budgets_privacy_template_parameters_input.AccessBudgetsPrivacyTemplateParametersInput"


PrivacyBudgetTemplateParametersInput: TypeAlias = (
    _PrivacyBudgetTemplateParametersInput_differentialPrivacy
    | _PrivacyBudgetTemplateParametersInput_accessBudget
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetTemplateParametersInput) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PrivacyBudgetTemplateParametersInput: cannot serialize unknown variant {value.name!r}"
        )
    elif "differentialPrivacy" in value:
        import capo_cleanrooms.types.differential_privacy_template_parameters_input

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_template_parameters_input.serialize_json(
                value["differentialPrivacy"]
            )
        }
    elif "accessBudget" in value:
        import capo_cleanrooms.types.access_budgets_privacy_template_parameters_input

        return {
            "accessBudget": capo_cleanrooms.types.access_budgets_privacy_template_parameters_input.serialize_json(
                value["accessBudget"]
            )
        }
    else:
        raise SerializationError(
            "PrivacyBudgetTemplateParametersInput: no variant present"
        )


def deserialize_json(data: dict) -> PrivacyBudgetTemplateParametersInput:
    if data.get("differentialPrivacy") is not None:
        import capo_cleanrooms.types.differential_privacy_template_parameters_input

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_template_parameters_input.deserialize_json(
                data["differentialPrivacy"]
            )
        }
    elif data.get("accessBudget") is not None:
        import capo_cleanrooms.types.access_budgets_privacy_template_parameters_input

        return {
            "accessBudget": capo_cleanrooms.types.access_budgets_privacy_template_parameters_input.deserialize_json(
                data["accessBudget"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "PrivacyBudgetTemplateParametersInput: no recognized variant key"
        )
