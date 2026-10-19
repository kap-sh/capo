"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateFlowPermissionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.flow_id
    import capo_quicksight.types.permissions_list
    import capo_quicksight.types.status_code


class UpdateFlowPermissionsOutput(TypedDict, closed=True):
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the flow you are updating permissions against.</p>"""
    permissions: "capo_quicksight.types.permissions_list.PermissionsList"
    """<p>The permissions on the flow after they are updated.</p>"""
    request_id: "str"
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    flow_id: "capo_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow with updated permissions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowPermissionsOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_quicksight.types.permissions_list

    out["Permissions"] = capo_quicksight.types.permissions_list.serialize_json(
        value["permissions"]
    )
    out["RequestId"] = value["request_id"]
    out["FlowId"] = value["flow_id"]
    return out


def deserialize_json(data: dict) -> UpdateFlowPermissionsOutput:
    out: UpdateFlowPermissionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Permissions") is not None:
        import capo_quicksight.types.permissions_list

        out["permissions"] = capo_quicksight.types.permissions_list.deserialize_json(
            data["Permissions"]
        )
    else:
        out["permissions"] = []
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    else:
        out["request_id"] = ""
    if data.get("FlowId") is not None:
        out["flow_id"] = data["FlowId"]
    else:
        out["flow_id"] = ""
    return out
