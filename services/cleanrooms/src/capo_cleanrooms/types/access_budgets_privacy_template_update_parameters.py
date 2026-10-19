"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AccessBudgetsPrivacyTemplateUpdateParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.budget_parameters


class AccessBudgetsPrivacyTemplateUpdateParameters(TypedDict, closed=True):
    budget_parameters: "capo_cleanrooms.types.budget_parameters.BudgetParameters"
    """<p>Updated array of budget parameters for the access budget configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudgetsPrivacyTemplateUpdateParameters) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.budget_parameters

    out["budgetParameters"] = capo_cleanrooms.types.budget_parameters.serialize_json(
        value["budget_parameters"]
    )
    return out


def deserialize_json(data: dict) -> AccessBudgetsPrivacyTemplateUpdateParameters:
    out: AccessBudgetsPrivacyTemplateUpdateParameters = {}  # type: ignore[typeddict-item]
    if data.get("budgetParameters") is not None:
        import capo_cleanrooms.types.budget_parameters

        out["budget_parameters"] = (
            capo_cleanrooms.types.budget_parameters.deserialize_json(
                data["budgetParameters"]
            )
        )
    else:
        out["budget_parameters"] = []
    return out
