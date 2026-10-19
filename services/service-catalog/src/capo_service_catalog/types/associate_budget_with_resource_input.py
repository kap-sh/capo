"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AssociateBudgetWithResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.budget_name
    import capo_service_catalog.types.id


class AssociateBudgetWithResourceInput(TypedDict, closed=True):
    budget_name: "capo_service_catalog.types.budget_name.BudgetName"
    """<p>The name of the budget you want to associate.</p>"""
    resource_id: "capo_service_catalog.types.id.Id"
    """<p> The resource identifier. Either a portfolio-id or a product-id.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateBudgetWithResourceInput) -> dict:
    out: dict = {}
    out["BudgetName"] = value["budget_name"]
    out["ResourceId"] = value["resource_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateBudgetWithResourceInput:
    out: AssociateBudgetWithResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("BudgetName") is not None:
        out["budget_name"] = data["BudgetName"]
    else:
        out["budget_name"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        out["resource_id"] = ""
    return out
