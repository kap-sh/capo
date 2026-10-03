"""Generated from Smithy shape ``com.amazonaws.connect#UpdateQuickConnectNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.quick_connect_id
    import capo_connect.types.quick_connect_name
    import capo_connect.types.update_quick_connect_description


class UpdateQuickConnectNameRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    quick_connect_id: "capo_connect.types.quick_connect_id.QuickConnectId"
    """<p>The identifier for the quick connect.</p>"""
    name: NotRequired["capo_connect.types.quick_connect_name.QuickConnectName"]
    """<p>The name of the quick connect.</p>"""
    description: NotRequired[
        "capo_connect.types.update_quick_connect_description.UpdateQuickConnectDescription"
    ]
    """<p>The description of the quick connect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuickConnectNameRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateQuickConnectNameRequest:
    out: UpdateQuickConnectNameRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
