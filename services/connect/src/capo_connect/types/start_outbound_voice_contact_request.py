"""Generated from Smithy shape ``com.amazonaws.connect#StartOutboundVoiceContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.answer_machine_detection_config
    import capo_connect.types.attributes
    import capo_connect.types.campaign_id
    import capo_connect.types.client_token
    import capo_connect.types.contact_flow_id
    import capo_connect.types.contact_id
    import capo_connect.types.contact_references
    import capo_connect.types.description
    import capo_connect.types.instance_id
    import capo_connect.types.name
    import capo_connect.types.outbound_strategy
    import capo_connect.types.phone_number
    import capo_connect.types.queue_id
    import capo_connect.types.ring_timeout_in_seconds
    import capo_connect.types.traffic_type


class StartOutboundVoiceContactRequest(TypedDict, closed=True):
    name: NotRequired["capo_connect.types.name.Name"]
    """<p>The name of a voice contact that is shown to an agent in the Contact Control Panel (CCP).</p>"""
    description: NotRequired["capo_connect.types.description.Description"]
    """<p>A description of the voice contact that appears in the agent's snapshot in the CCP logs. For more information about CCP logs, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/download-ccp-logs.html">Download and review CCP logs</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""
    references: NotRequired["capo_connect.types.contact_references.ContactReferences"]
    """<p>A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Contacts can have the following reference types at the time of creation: <code>URL</code> | <code>NUMBER</code> | <code>STRING</code> | <code>DATE</code> | <code>EMAIL</code>. <code>ATTACHMENT</code> is not a supported reference type during voice contact creation.</p>"""
    related_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The <code>contactId</code> that is related to this contact. Linking voice, task, or chat by using <code>RelatedContactID</code> copies over contact attributes from the related contact to the new contact. All updates to user-defined attributes in the new contact are limited to the individual contact ID. There are no limits to the number of contacts that can be linked by using <code>RelatedContactId</code>. </p>"""
    destination_phone_number: "capo_connect.types.phone_number.PhoneNumber"
    """<p>The phone number of the customer, in E.164 format.</p>"""
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow for the outbound call. To see the ContactFlowId in the Connect Customer admin website, on the navigation menu go to <b>Routing</b>, <b>Contact Flows</b>. Choose the flow. On the flow page, under the name of the flow, choose <b>Show additional flow information</b>. The ContactFlowId is the last part of the ARN, shown here in bold: </p> <p>arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/<b>846ec553-a005-41c0-8341-xxxxxxxxxxxx</b> </p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>. The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned. </p>"""
    source_phone_number: NotRequired["capo_connect.types.phone_number.PhoneNumber"]
    """<p>The phone number associated with the Connect Customer instance, in E.164 format. If you do not specify a source phone number, you must specify a queue.</p>"""
    queue_id: NotRequired["capo_connect.types.queue_id.QueueId"]
    """<p>The queue for the call. If you specify a queue, the phone displayed for caller ID is the phone number specified in the queue. If you do not specify a queue, the queue defined in the flow is used. If you do not specify a queue, you must specify a source phone number.</p>"""
    attributes: NotRequired["capo_connect.types.attributes.Attributes"]
    """<p>A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.</p> <p>There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.</p>"""
    answer_machine_detection_config: NotRequired[
        "capo_connect.types.answer_machine_detection_config.AnswerMachineDetectionConfig"
    ]
    """<p>Configuration of the answering machine detection for this outbound call. </p>"""
    campaign_id: NotRequired["capo_connect.types.campaign_id.CampaignId"]
    """<p>The campaign identifier of the outbound communication.</p>"""
    traffic_type: NotRequired["capo_connect.types.traffic_type.TrafficType"]
    """<p>Denotes the class of traffic. Calls with different traffic types are handled differently by Connect Customer. The default value is <code>GENERAL</code>. Use <code>CAMPAIGN</code> if <code>EnableAnswerMachineDetection</code> is set to <code>true</code>. For all other cases, use <code>GENERAL</code>. </p>"""
    outbound_strategy: NotRequired[
        "capo_connect.types.outbound_strategy.OutboundStrategy"
    ]
    """<p>Information about the outbound strategy.</p>"""
    ring_timeout_in_seconds: NotRequired[
        "capo_connect.types.ring_timeout_in_seconds.RingTimeoutInSeconds"
    ]
    """<p>The maximum time the outbound call will wait for the destination to answer the call, in seconds </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOutboundVoiceContactRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "references" in value:
        import capo_connect.types.contact_references

        out["References"] = capo_connect.types.contact_references.serialize_json(
            value["references"]
        )
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    out["DestinationPhoneNumber"] = value["destination_phone_number"]
    out["ContactFlowId"] = value["contact_flow_id"]
    out["InstanceId"] = value["instance_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "source_phone_number" in value:
        out["SourcePhoneNumber"] = value["source_phone_number"]
    if "queue_id" in value:
        out["QueueId"] = value["queue_id"]
    if "attributes" in value:
        import capo_connect.types.attributes

        out["Attributes"] = capo_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    if "answer_machine_detection_config" in value:
        import capo_connect.types.answer_machine_detection_config

        out["AnswerMachineDetectionConfig"] = (
            capo_connect.types.answer_machine_detection_config.serialize_json(
                value["answer_machine_detection_config"]
            )
        )
    if "campaign_id" in value:
        out["CampaignId"] = value["campaign_id"]
    if "traffic_type" in value:
        import capo_connect.types.traffic_type

        out["TrafficType"] = capo_connect.types.traffic_type.serialize_json(
            value["traffic_type"]
        )
    if "outbound_strategy" in value:
        import capo_connect.types.outbound_strategy

        out["OutboundStrategy"] = capo_connect.types.outbound_strategy.serialize_json(
            value["outbound_strategy"]
        )
    if "ring_timeout_in_seconds" in value:
        out["RingTimeoutInSeconds"] = value["ring_timeout_in_seconds"]
    return out


def deserialize_json(data: dict) -> StartOutboundVoiceContactRequest:
    out: StartOutboundVoiceContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("References") is not None:
        import capo_connect.types.contact_references

        out["references"] = capo_connect.types.contact_references.deserialize_json(
            data["References"]
        )
    if data.get("RelatedContactId") is not None:
        out["related_contact_id"] = data["RelatedContactId"]
    if data.get("DestinationPhoneNumber") is not None:
        out["destination_phone_number"] = data["DestinationPhoneNumber"]
    else:
        raise DeserializationError(
            "StartOutboundVoiceContactRequest.destination_phone_number required"
        )
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        raise DeserializationError(
            "StartOutboundVoiceContactRequest.contact_flow_id required"
        )
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "StartOutboundVoiceContactRequest.instance_id required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("SourcePhoneNumber") is not None:
        out["source_phone_number"] = data["SourcePhoneNumber"]
    if data.get("QueueId") is not None:
        out["queue_id"] = data["QueueId"]
    if data.get("Attributes") is not None:
        import capo_connect.types.attributes

        out["attributes"] = capo_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if data.get("AnswerMachineDetectionConfig") is not None:
        import capo_connect.types.answer_machine_detection_config

        out["answer_machine_detection_config"] = (
            capo_connect.types.answer_machine_detection_config.deserialize_json(
                data["AnswerMachineDetectionConfig"]
            )
        )
    if data.get("CampaignId") is not None:
        out["campaign_id"] = data["CampaignId"]
    if data.get("TrafficType") is not None:
        import capo_connect.types.traffic_type

        out["traffic_type"] = capo_connect.types.traffic_type.deserialize_json(
            data["TrafficType"]
        )
    if data.get("OutboundStrategy") is not None:
        import capo_connect.types.outbound_strategy

        out["outbound_strategy"] = (
            capo_connect.types.outbound_strategy.deserialize_json(
                data["OutboundStrategy"]
            )
        )
    if data.get("RingTimeoutInSeconds") is not None:
        out["ring_timeout_in_seconds"] = data["RingTimeoutInSeconds"]
    return out
