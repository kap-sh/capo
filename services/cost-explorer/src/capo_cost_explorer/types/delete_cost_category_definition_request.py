"""Generated from Smithy shape ``com.amazonaws.costexplorer#DeleteCostCategoryDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.arn


class DeleteCostCategoryDefinitionRequest(TypedDict, closed=True):
    cost_category_arn: "capo_cost_explorer.types.arn.Arn"
    """<p>The unique identifier for your cost category. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCostCategoryDefinitionRequest) -> dict:
    out: dict = {}
    out["CostCategoryArn"] = value["cost_category_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCostCategoryDefinitionRequest:
    out: DeleteCostCategoryDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CostCategoryArn") is not None:
        out["cost_category_arn"] = data["CostCategoryArn"]
    else:
        out["cost_category_arn"] = ""
    return out
