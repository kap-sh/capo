"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AccessBudgetsPrivacyTemplateParametersOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.budget_parameters
    import capo_cleanrooms.types.budgeted_resource_arn


class AccessBudgetsPrivacyTemplateParametersOutput(TypedDict, closed=True):
    budget_parameters: "capo_cleanrooms.types.budget_parameters.BudgetParameters"
    """<p>An array of budget parameters returned from the access budget configuration.</p>"""
    resource_arn: "capo_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource associated with this privacy budget template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudgetsPrivacyTemplateParametersOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.budget_parameters

    out["budgetParameters"] = capo_cleanrooms.types.budget_parameters.serialize_json(
        value["budget_parameters"]
    )
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> AccessBudgetsPrivacyTemplateParametersOutput:
    out: AccessBudgetsPrivacyTemplateParametersOutput = {}  # type: ignore[typeddict-item]
    if data.get("budgetParameters") is not None:
        import capo_cleanrooms.types.budget_parameters

        out["budget_parameters"] = (
            capo_cleanrooms.types.budget_parameters.deserialize_json(
                data["budgetParameters"]
            )
        )
    else:
        out["budget_parameters"] = []
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    return out
