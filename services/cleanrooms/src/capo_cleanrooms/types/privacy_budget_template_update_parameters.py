"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetTemplateUpdateParameters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.access_budgets_privacy_template_update_parameters
    import capo_cleanrooms.types.differential_privacy_template_update_parameters


class _PrivacyBudgetTemplateUpdateParameters_differentialPrivacy(
    TypedDict, closed=True
):
    differentialPrivacy: "capo_cleanrooms.types.differential_privacy_template_update_parameters.DifferentialPrivacyTemplateUpdateParameters"


class _PrivacyBudgetTemplateUpdateParameters_accessBudget(TypedDict, closed=True):
    accessBudget: "capo_cleanrooms.types.access_budgets_privacy_template_update_parameters.AccessBudgetsPrivacyTemplateUpdateParameters"


PrivacyBudgetTemplateUpdateParameters: TypeAlias = (
    _PrivacyBudgetTemplateUpdateParameters_differentialPrivacy
    | _PrivacyBudgetTemplateUpdateParameters_accessBudget
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetTemplateUpdateParameters) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"PrivacyBudgetTemplateUpdateParameters: cannot serialize unknown variant {value.name!r}"
        )
    elif "differentialPrivacy" in value:
        import capo_cleanrooms.types.differential_privacy_template_update_parameters

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_template_update_parameters.serialize_json(
                value["differentialPrivacy"]
            )
        }
    elif "accessBudget" in value:
        import capo_cleanrooms.types.access_budgets_privacy_template_update_parameters

        return {
            "accessBudget": capo_cleanrooms.types.access_budgets_privacy_template_update_parameters.serialize_json(
                value["accessBudget"]
            )
        }
    else:
        raise SerializationError(
            "PrivacyBudgetTemplateUpdateParameters: no variant present"
        )


def deserialize_json(data: dict) -> PrivacyBudgetTemplateUpdateParameters:
    if data.get("differentialPrivacy") is not None:
        import capo_cleanrooms.types.differential_privacy_template_update_parameters

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_template_update_parameters.deserialize_json(
                data["differentialPrivacy"]
            )
        }
    elif data.get("accessBudget") is not None:
        import capo_cleanrooms.types.access_budgets_privacy_template_update_parameters

        return {
            "accessBudget": capo_cleanrooms.types.access_budgets_privacy_template_update_parameters.deserialize_json(
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
            "PrivacyBudgetTemplateUpdateParameters: no recognized variant key"
        )
