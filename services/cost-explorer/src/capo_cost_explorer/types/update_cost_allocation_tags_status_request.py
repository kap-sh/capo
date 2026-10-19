"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateCostAllocationTagsStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_allocation_tag_status_list


class UpdateCostAllocationTagsStatusRequest(TypedDict, closed=True):
    cost_allocation_tags_status: "capo_cost_explorer.types.cost_allocation_tag_status_list.CostAllocationTagStatusList"
    """<p>The list of <code>CostAllocationTagStatusEntry</code> objects that are used to update cost allocation tags status for this request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCostAllocationTagsStatusRequest) -> dict:
    out: dict = {}
    import capo_cost_explorer.types.cost_allocation_tag_status_list

    out["CostAllocationTagsStatus"] = (
        capo_cost_explorer.types.cost_allocation_tag_status_list.serialize_aws_json_1_1(
            value["cost_allocation_tags_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCostAllocationTagsStatusRequest:
    out: UpdateCostAllocationTagsStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("CostAllocationTagsStatus") is not None:
        import capo_cost_explorer.types.cost_allocation_tag_status_list

        out["cost_allocation_tags_status"] = (
            capo_cost_explorer.types.cost_allocation_tag_status_list.deserialize_aws_json_1_1(
                data["CostAllocationTagsStatus"]
            )
        )
    else:
        out["cost_allocation_tags_status"] = []
    return out
