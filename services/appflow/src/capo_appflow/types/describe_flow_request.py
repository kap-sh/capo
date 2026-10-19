"""Generated from Smithy shape ``com.amazonaws.appflow#DescribeFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appflow.types.flow_name


class DescribeFlowRequest(TypedDict, closed=True):
    flow_name: "capo_appflow.types.flow_name.FlowName"
    """<p> The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowRequest) -> dict:
    out: dict = {}
    out["flowName"] = value["flow_name"]
    return out


def deserialize_json(data: dict) -> DescribeFlowRequest:
    out: DescribeFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("flowName") is not None:
        out["flow_name"] = data["flowName"]
    else:
        out["flow_name"] = ""
    return out
