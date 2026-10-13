"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeFlowResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.flow_detail
    import capo_quicksight.types.status_code


class DescribeFlowResponse(TypedDict, closed=True):
    flow: "capo_quicksight.types.flow_detail.FlowDetail"
    """<p>The full details of the flow.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeFlowResponse) -> dict:
    out: dict = {}
    import capo_quicksight.types.flow_detail

    out["Flow"] = capo_quicksight.types.flow_detail.serialize_json(value["flow"])
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeFlowResponse:
    out: DescribeFlowResponse = {}  # type: ignore[typeddict-item]
    if data.get("Flow") is not None:
        import capo_quicksight.types.flow_detail

        out["flow"] = capo_quicksight.types.flow_detail.deserialize_json(data["Flow"])
    else:
        raise DeserializationError("DescribeFlowResponse.flow required")
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out


def redact_sensitive(value: DescribeFlowResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "flow" in value:
        import capo_quicksight.types.flow_detail

        out["flow"] = capo_quicksight.types.flow_detail.redact_sensitive(value["flow"])
    return out
