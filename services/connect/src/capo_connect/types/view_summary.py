"""Generated from Smithy shape ``com.amazonaws.connect#ViewSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.view_description
    import capo_connect.types.view_id
    import capo_connect.types.view_name
    import capo_connect.types.view_status
    import capo_connect.types.view_type


class ViewSummary(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.view_id.ViewId"]
    """<p>The identifier of the view.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the view.</p>"""
    name: NotRequired["capo_connect.types.view_name.ViewName"]
    """<p>The name of the view.</p>"""
    type: NotRequired["capo_connect.types.view_type.ViewType"]
    """<p>The type of the view.</p>"""
    status: NotRequired["capo_connect.types.view_status.ViewStatus"]
    """<p>Indicates the view status as either <code>SAVED</code> or <code>PUBLISHED</code>. The <code>PUBLISHED</code> status will initiate validation on the content.</p>"""
    description: NotRequired["capo_connect.types.view_description.ViewDescription"]
    """<p>The description of the view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViewSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_connect.types.view_type

        out["Type"] = capo_connect.types.view_type.serialize_json(value["type"])
    if "status" in value:
        import capo_connect.types.view_status

        out["Status"] = capo_connect.types.view_status.serialize_json(value["status"])
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ViewSummary:
    out: ViewSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_connect.types.view_type

        out["type"] = capo_connect.types.view_type.deserialize_json(data["Type"])
    if data.get("Status") is not None:
        import capo_connect.types.view_status

        out["status"] = capo_connect.types.view_status.deserialize_json(data["Status"])
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


def redact_sensitive(value: ViewSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
