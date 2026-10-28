"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetTemplateParametersOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError
from capo_cleanrooms.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cleanrooms.types.access_budgets_privacy_template_parameters_output
    import capo_cleanrooms.types.differential_privacy_template_parameters_output


class PrivacyBudgetTemplateParametersOutputDifferentialPrivacyMember(
    TypedDict, closed=True
):
    differentialPrivacy: "capo_cleanrooms.types.differential_privacy_template_parameters_output.DifferentialPrivacyTemplateParametersOutput"


class PrivacyBudgetTemplateParametersOutputAccessBudgetMember(TypedDict, closed=True):
    accessBudget: "capo_cleanrooms.types.access_budgets_privacy_template_parameters_output.AccessBudgetsPrivacyTemplateParametersOutput"


PrivacyBudgetTemplateParametersOutput: TypeAlias = (
    PrivacyBudgetTemplateParametersOutputDifferentialPrivacyMember
    | PrivacyBudgetTemplateParametersOutputAccessBudgetMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetTemplateParametersOutput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PrivacyBudgetTemplateParametersOutput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "differentialPrivacy" in value:
        import capo_cleanrooms.types.differential_privacy_template_parameters_output

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_template_parameters_output.serialize_json(
                value["differentialPrivacy"]
            )
        }
    elif "accessBudget" in value:
        import capo_cleanrooms.types.access_budgets_privacy_template_parameters_output

        return {
            "accessBudget": capo_cleanrooms.types.access_budgets_privacy_template_parameters_output.serialize_json(
                value["accessBudget"]
            )
        }
    else:
        raise SerializationError(
            "PrivacyBudgetTemplateParametersOutput: no variant present"
        )


def deserialize_json(data: dict) -> PrivacyBudgetTemplateParametersOutput:
    if data.get("differentialPrivacy") is not None:
        import capo_cleanrooms.types.differential_privacy_template_parameters_output

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_template_parameters_output.deserialize_json(
                data["differentialPrivacy"]
            )
        }
    elif data.get("accessBudget") is not None:
        import capo_cleanrooms.types.access_budgets_privacy_template_parameters_output

        return {
            "accessBudget": capo_cleanrooms.types.access_budgets_privacy_template_parameters_output.deserialize_json(
                data["accessBudget"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "PrivacyBudgetTemplateParametersOutput: no recognized variant key"
        )
