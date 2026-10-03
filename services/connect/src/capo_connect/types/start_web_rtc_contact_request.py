"""Generated from Smithy shape ``com.amazonaws.connect#StartWebRTCContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.allowed_capabilities
    import capo_connect.types.attributes
    import capo_connect.types.client_token
    import capo_connect.types.contact_flow_id
    import capo_connect.types.contact_id
    import capo_connect.types.contact_references
    import capo_connect.types.description
    import capo_connect.types.instance_id
    import capo_connect.types.participant_details
    import capo_connect.types.segment_attributes


class StartWebRTCContactRequest(TypedDict, closed=True):
    attributes: NotRequired["capo_connect.types.attributes.Attributes"]
    """<p>A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.</p> <p>There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, -, and _ characters.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p> <p>The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned.</p>"""
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow for the call. To see the ContactFlowId in the Connect Customer admin website, on the navigation menu go to <b>Routing</b>, <b>Flows</b>. Choose the flow. On the flow page, under the name of the flow, choose <b>Show additional flow information</b>. The ContactFlowId is the last part of the ARN, shown here in bold: </p> <p>arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/<b>846ec553-a005-41c0-8341-xxxxxxxxxxxx</b> </p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    allowed_capabilities: NotRequired[
        "capo_connect.types.allowed_capabilities.AllowedCapabilities"
    ]
    """<p>Information about the video sharing capabilities of the participants (customer, agent).</p>"""
    participant_details: "capo_connect.types.participant_details.ParticipantDetails"
    related_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The unique identifier for an Connect Customer contact. This identifier is related to the contact starting.</p>"""
    references: NotRequired["capo_connect.types.contact_references.ContactReferences"]
    """<p>A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Tasks can have the following reference types at the time of creation: <code>URL</code> | <code>NUMBER</code> | <code>STRING</code> | <code>DATE</code> | <code>EMAIL</code>. <code>ATTACHMENT</code> is not a supported reference type during task creation.</p>"""
    description: NotRequired["capo_connect.types.description.Description"]
    """<p>A description of the task that is shown to an agent in the Contact Control Panel (CCP).</p>"""
    segment_attributes: NotRequired[
        "capo_connect.types.segment_attributes.SegmentAttributes"
    ]
    """<p>A map of system-defined attributes for the WebRTC contact segment. Use the <code>connect:Subtype</code> attribute to specify the channel subtype, such as <code>connect:WebRTC</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartWebRTCContactRequest) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_connect.types.attributes

        out["Attributes"] = capo_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["ContactFlowId"] = value["contact_flow_id"]
    out["InstanceId"] = value["instance_id"]
    if "allowed_capabilities" in value:
        import capo_connect.types.allowed_capabilities

        out["AllowedCapabilities"] = (
            capo_connect.types.allowed_capabilities.serialize_json(
                value["allowed_capabilities"]
            )
        )
    import capo_connect.types.participant_details

    out["ParticipantDetails"] = capo_connect.types.participant_details.serialize_json(
        value["participant_details"]
    )
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    if "references" in value:
        import capo_connect.types.contact_references

        out["References"] = capo_connect.types.contact_references.serialize_json(
            value["references"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "segment_attributes" in value:
        import capo_connect.types.segment_attributes

        out["SegmentAttributes"] = capo_connect.types.segment_attributes.serialize_json(
            value["segment_attributes"]
        )
    return out


def deserialize_json(data: dict) -> StartWebRTCContactRequest:
    out: StartWebRTCContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("Attributes") is not None:
        import capo_connect.types.attributes

        out["attributes"] = capo_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        raise DeserializationError("StartWebRTCContactRequest.contact_flow_id required")
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("StartWebRTCContactRequest.instance_id required")
    if data.get("AllowedCapabilities") is not None:
        import capo_connect.types.allowed_capabilities

        out["allowed_capabilities"] = (
            capo_connect.types.allowed_capabilities.deserialize_json(
                data["AllowedCapabilities"]
            )
        )
    if data.get("ParticipantDetails") is not None:
        import capo_connect.types.participant_details

        out["participant_details"] = (
            capo_connect.types.participant_details.deserialize_json(
                data["ParticipantDetails"]
            )
        )
    else:
        raise DeserializationError(
            "StartWebRTCContactRequest.participant_details required"
        )
    if data.get("RelatedContactId") is not None:
        out["related_contact_id"] = data["RelatedContactId"]
    if data.get("References") is not None:
        import capo_connect.types.contact_references

        out["references"] = capo_connect.types.contact_references.deserialize_json(
            data["References"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SegmentAttributes") is not None:
        import capo_connect.types.segment_attributes

        out["segment_attributes"] = (
            capo_connect.types.segment_attributes.deserialize_json(
                data["SegmentAttributes"]
            )
        )
    return out
