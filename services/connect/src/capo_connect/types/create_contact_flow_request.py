"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactFlowRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_content
    import capo_connect.types.contact_flow_description
    import capo_connect.types.contact_flow_name
    import capo_connect.types.contact_flow_status
    import capo_connect.types.contact_flow_type
    import capo_connect.types.instance_id
    import capo_connect.types.tag_map


class CreateContactFlowRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance.</p>"""
    name: "capo_connect.types.contact_flow_name.ContactFlowName"
    """<p>The name of the flow.</p>"""
    type: "capo_connect.types.contact_flow_type.ContactFlowType"
    """<p>The type of the flow. For descriptions of the available types, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/create-contact-flow.html#contact-flow-types">Choose a flow type</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    description: NotRequired[
        "capo_connect.types.contact_flow_description.ContactFlowDescription"
    ]
    """<p>The description of the flow. </p>"""
    content: "capo_connect.types.contact_flow_content.ContactFlowContent"
    """<p>The JSON string that represents the content of the flow. For an example, see <a href="https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html">Example flow in Connect Customer Flow language</a>. </p> <p>Length Constraints: Minimum length of 1. Maximum length of 256000.</p>"""
    status: NotRequired["capo_connect.types.contact_flow_status.ContactFlowStatus"]
    """<p>Indicates the flow status as either <code>SAVED</code> or <code>PUBLISHED</code>. The <code>PUBLISHED</code> status will initiate validation on the content. the <code>SAVED</code> status does not initiate validation of the content. <code>SAVED</code> | <code>PUBLISHED</code>.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactFlowRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_connect.types.contact_flow_type

    out["Type"] = capo_connect.types.contact_flow_type.serialize_json(value["type"])
    if "description" in value:
        out["Description"] = value["description"]
    out["Content"] = value["content"]
    if "status" in value:
        import capo_connect.types.contact_flow_status

        out["Status"] = capo_connect.types.contact_flow_status.serialize_json(
            value["status"]
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateContactFlowRequest:
    out: CreateContactFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateContactFlowRequest.name required")
    if data.get("Type") is not None:
        import capo_connect.types.contact_flow_type

        out["type"] = capo_connect.types.contact_flow_type.deserialize_json(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateContactFlowRequest.type required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Content") is not None:
        out["content"] = data["Content"]
    else:
        raise DeserializationError("CreateContactFlowRequest.content required")
    if data.get("Status") is not None:
        import capo_connect.types.contact_flow_status

        out["status"] = capo_connect.types.contact_flow_status.deserialize_json(
            data["Status"]
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
