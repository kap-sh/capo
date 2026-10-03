"""Generated from Smithy shape ``com.amazonaws.connect#CreateViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.tag_map
    import capo_connect.types.view_description
    import capo_connect.types.view_input_content
    import capo_connect.types.view_name
    import capo_connect.types.view_status
    import capo_connect.types.views_client_token
    import capo_connect.types.views_instance_id


class CreateViewRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.views_instance_id.ViewsInstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instanceId in the ARN of the instance.</p>"""
    client_token: NotRequired["capo_connect.types.views_client_token.ViewsClientToken"]
    """<p>A unique Id for each create view request to avoid duplicate view creation. For example, the view is idempotent ClientToken is provided.</p>"""
    status: "capo_connect.types.view_status.ViewStatus"
    """<p>Indicates the view status as either <code>SAVED</code> or <code>PUBLISHED</code>. The <code>PUBLISHED</code> status will initiate validation on the content.</p>"""
    content: "capo_connect.types.view_input_content.ViewInputContent"
    """<p>View content containing all content necessary to render a view except for runtime input data.</p> <p>The total uncompressed content has a maximum file size of 400kB.</p>"""
    description: NotRequired["capo_connect.types.view_description.ViewDescription"]
    """<p>The description of the view.</p>"""
    name: "capo_connect.types.view_name.ViewName"
    """<p>The name of the view.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags associated with the view resource (not specific to view version).These tags can be used to organize, track, or control access for this resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateViewRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import capo_connect.types.view_status

    out["Status"] = capo_connect.types.view_status.serialize_json(value["status"])
    import capo_connect.types.view_input_content

    out["Content"] = capo_connect.types.view_input_content.serialize_json(
        value["content"]
    )
    if "description" in value:
        out["Description"] = value["description"]
    out["Name"] = value["name"]
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateViewRequest:
    out: CreateViewRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Status") is not None:
        import capo_connect.types.view_status

        out["status"] = capo_connect.types.view_status.deserialize_json(data["Status"])
    else:
        raise DeserializationError("CreateViewRequest.status required")
    if data.get("Content") is not None:
        import capo_connect.types.view_input_content

        out["content"] = capo_connect.types.view_input_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError("CreateViewRequest.content required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateViewRequest.name required")
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
