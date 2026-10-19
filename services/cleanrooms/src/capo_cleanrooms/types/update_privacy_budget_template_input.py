"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdatePrivacyBudgetTemplateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.privacy_budget_template_identifier
    import capo_cleanrooms.types.privacy_budget_template_update_parameters
    import capo_cleanrooms.types.privacy_budget_type


class UpdatePrivacyBudgetTemplateInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for one of your memberships for a collaboration. The privacy budget template is updated in the collaboration that this membership belongs to. Accepts a membership ID.</p>"""
    privacy_budget_template_identifier: "capo_cleanrooms.types.privacy_budget_template_identifier.PrivacyBudgetTemplateIdentifier"
    """<p>A unique identifier for your privacy budget template that you want to update.</p>"""
    privacy_budget_type: "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType"
    """<p>Specifies the type of the privacy budget template.</p>"""
    parameters: NotRequired[
        "capo_cleanrooms.types.privacy_budget_template_update_parameters.PrivacyBudgetTemplateUpdateParameters"
    ]
    """<p>Specifies the epsilon and noise parameters for the privacy budget template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePrivacyBudgetTemplateInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.privacy_budget_type

    out["privacyBudgetType"] = capo_cleanrooms.types.privacy_budget_type.serialize_json(
        value["privacy_budget_type"]
    )
    if "parameters" in value:
        import capo_cleanrooms.types.privacy_budget_template_update_parameters

        out["parameters"] = (
            capo_cleanrooms.types.privacy_budget_template_update_parameters.serialize_json(
                value["parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePrivacyBudgetTemplateInput:
    out: UpdatePrivacyBudgetTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("privacyBudgetType") is not None:
        import capo_cleanrooms.types.privacy_budget_type

        out["privacy_budget_type"] = (
            capo_cleanrooms.types.privacy_budget_type.deserialize_json(
                data["privacyBudgetType"]
            )
        )
    else:
        import typing

        out["privacy_budget_type"] = typing.cast(
            "capo_cleanrooms.types.privacy_budget_type.PrivacyBudgetType", ""
        )
    if data.get("parameters") is not None:
        import capo_cleanrooms.types.privacy_budget_template_update_parameters

        out["parameters"] = (
            capo_cleanrooms.types.privacy_budget_template_update_parameters.deserialize_json(
                data["parameters"]
            )
        )
    return out
