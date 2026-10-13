"""Generated from Smithy shape ``com.amazonaws.connect#UpdateViewMetadataRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.view_description
    import capo_connect.types.view_id
    import capo_connect.types.view_name
    import capo_connect.types.views_instance_id


class UpdateViewMetadataRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.views_instance_id.ViewsInstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.</p>"""
    view_id: "capo_connect.types.view_id.ViewId"
    """<p>The identifier of the view. Both <code>ViewArn</code> and <code>ViewId</code> can be used.</p>"""
    name: NotRequired["capo_connect.types.view_name.ViewName"]
    """<p>The name of the view.</p>"""
    description: NotRequired["capo_connect.types.view_description.ViewDescription"]
    """<p>The description of the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateViewMetadataRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateViewMetadataRequest:
    out: UpdateViewMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


def redact_sensitive(value: UpdateViewMetadataRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
