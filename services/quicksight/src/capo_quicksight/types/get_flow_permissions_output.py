"""Generated from Smithy shape ``com.amazonaws.quicksight#GetFlowPermissionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.flow_id
    import capo_quicksight.types.permissions_list
    import capo_quicksight.types.status_code


class GetFlowPermissionsOutput(TypedDict, closed=True):
    arn: "capo_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the flow you are getting permissions against.</p>"""
    flow_id: "capo_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow with permissions.</p>"""
    permissions: "capo_quicksight.types.permissions_list.PermissionsList"
    """<p>A structure that contains the permissions for the flow.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFlowPermissionsOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["FlowId"] = value["flow_id"]
    import capo_quicksight.types.permissions_list

    out["Permissions"] = capo_quicksight.types.permissions_list.serialize_json(
        value["permissions"]
    )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> GetFlowPermissionsOutput:
    out: GetFlowPermissionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("FlowId") is not None:
        out["flow_id"] = data["FlowId"]
    else:
        out["flow_id"] = ""
    if data.get("Permissions") is not None:
        import capo_quicksight.types.permissions_list

        out["permissions"] = capo_quicksight.types.permissions_list.deserialize_json(
            data["Permissions"]
        )
    else:
        out["permissions"] = []
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    return out
