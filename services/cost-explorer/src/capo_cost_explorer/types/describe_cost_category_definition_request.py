"""Generated from Smithy shape ``com.amazonaws.costexplorer#DescribeCostCategoryDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.arn
    import capo_cost_explorer.types.zoned_date_time


class DescribeCostCategoryDefinitionRequest(TypedDict, closed=True):
    cost_category_arn: "capo_cost_explorer.types.arn.Arn"
    """<p>The unique identifier for your cost category. </p>"""
    effective_on: NotRequired["capo_cost_explorer.types.zoned_date_time.ZonedDateTime"]
    """<p>The date when the cost category was effective. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCostCategoryDefinitionRequest) -> dict:
    out: dict = {}
    out["CostCategoryArn"] = value["cost_category_arn"]
    if "effective_on" in value:
        out["EffectiveOn"] = value["effective_on"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCostCategoryDefinitionRequest:
    out: DescribeCostCategoryDefinitionRequest = {}  # type: ignore[typeddict-item]
    if data.get("CostCategoryArn") is not None:
        out["cost_category_arn"] = data["CostCategoryArn"]
    else:
        out["cost_category_arn"] = ""
    if data.get("EffectiveOn") is not None:
        out["effective_on"] = data["EffectiveOn"]
    return out
