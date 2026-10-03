"""Generated from Smithy shape ``com.amazonaws.connect#StartOutboundChatContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.attributes
    import capo_connect.types.chat_duration_in_minutes
    import capo_connect.types.chat_message
    import capo_connect.types.client_token
    import capo_connect.types.contact_flow_id
    import capo_connect.types.contact_id
    import capo_connect.types.endpoint
    import capo_connect.types.instance_id
    import capo_connect.types.participant_details
    import capo_connect.types.segment_attributes
    import capo_connect.types.supported_messaging_content_types
    import capo_connect.types.templated_message_config


class StartOutboundChatContactRequest(TypedDict, closed=True):
    source_endpoint: "capo_connect.types.endpoint.Endpoint"
    destination_endpoint: "capo_connect.types.endpoint.Endpoint"
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.</p>"""
    segment_attributes: "capo_connect.types.segment_attributes.SegmentAttributes"
    """<p>A set of system defined key-value pairs stored on individual contact segments using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.</p> <ul> <li> <p>Attribute keys can include only alphanumeric, <code>-</code>, and <code>_</code>.</p> </li> <li> <p>This field can be used to show channel subtype, such as <code>connect:SMS</code> and <code>connect:WhatsApp</code>.</p> </li> </ul>"""
    attributes: NotRequired["capo_connect.types.attributes.Attributes"]
    """<p>A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.</p>"""
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow for the call. To see the ContactFlowId in the Connect Customer console user interface, on the navigation menu go to <b>Routing, Contact Flows</b>. Choose the flow. On the flow page, under the name of the flow, choose <b>Show additional flow information</b>. The ContactFlowId is the last part of the ARN, shown here in bold:</p> <ul> <li> <p>arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/<b>123ec456-a007-89c0-1234-xxxxxxxxxxxx</b> </p> </li> </ul>"""
    chat_duration_in_minutes: NotRequired[
        "capo_connect.types.chat_duration_in_minutes.ChatDurationInMinutes"
    ]
    """<p>The total duration of the newly started chat session. If not specified, the chat session duration defaults to 25 hour. The minimum configurable time is 60 minutes. The maximum configurable time is 10,080 minutes (7 days).</p>"""
    participant_details: NotRequired[
        "capo_connect.types.participant_details.ParticipantDetails"
    ]
    initial_system_message: NotRequired["capo_connect.types.chat_message.ChatMessage"]
    initial_templated_system_message: NotRequired[
        "capo_connect.types.templated_message_config.TemplatedMessageConfig"
    ]
    related_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The unique identifier for an Connect Customer contact. This identifier is related to the contact starting.</p>"""
    supported_messaging_content_types: NotRequired[
        "capo_connect.types.supported_messaging_content_types.SupportedMessagingContentTypes"
    ]
    """<p>The supported chat message content types. Supported types are:</p> <ul> <li> <p> <code>text/plain</code> </p> </li> <li> <p> <code>text/markdown</code> </p> </li> <li> <p> <code>application/json, application/vnd.amazonaws.connect.message.interactive</code> </p> </li> <li> <p> <code>application/vnd.amazonaws.connect.message.interactive.response</code> </p> </li> </ul> <p>Content types must always contain <code>text/plain</code>. You can then put any other supported type in the list. For example, all the following lists are valid because they contain <code>text/plain</code>:</p> <ul> <li> <p> <code>[text/plain, text/markdown, application/json]</code> </p> </li> <li> <p> <code>[text/markdown, text/plain]</code> </p> </li> <li> <p> <code>[text/plain, application/json, application/vnd.amazonaws.connect.message.interactive.response]</code> </p> </li> </ul>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>. The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOutboundChatContactRequest) -> dict:
    out: dict = {}
    import capo_connect.types.endpoint

    out["SourceEndpoint"] = capo_connect.types.endpoint.serialize_json(
        value["source_endpoint"]
    )
    import capo_connect.types.endpoint

    out["DestinationEndpoint"] = capo_connect.types.endpoint.serialize_json(
        value["destination_endpoint"]
    )
    out["InstanceId"] = value["instance_id"]
    import capo_connect.types.segment_attributes

    out["SegmentAttributes"] = capo_connect.types.segment_attributes.serialize_json(
        value["segment_attributes"]
    )
    if "attributes" in value:
        import capo_connect.types.attributes

        out["Attributes"] = capo_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    out["ContactFlowId"] = value["contact_flow_id"]
    if "chat_duration_in_minutes" in value:
        out["ChatDurationInMinutes"] = value["chat_duration_in_minutes"]
    if "participant_details" in value:
        import capo_connect.types.participant_details

        out["ParticipantDetails"] = (
            capo_connect.types.participant_details.serialize_json(
                value["participant_details"]
            )
        )
    if "initial_system_message" in value:
        import capo_connect.types.chat_message

        out["InitialSystemMessage"] = capo_connect.types.chat_message.serialize_json(
            value["initial_system_message"]
        )
    if "initial_templated_system_message" in value:
        import capo_connect.types.templated_message_config

        out["InitialTemplatedSystemMessage"] = (
            capo_connect.types.templated_message_config.serialize_json(
                value["initial_templated_system_message"]
            )
        )
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    if "supported_messaging_content_types" in value:
        import capo_connect.types.supported_messaging_content_types

        out["SupportedMessagingContentTypes"] = (
            capo_connect.types.supported_messaging_content_types.serialize_json(
                value["supported_messaging_content_types"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartOutboundChatContactRequest:
    out: StartOutboundChatContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceEndpoint") is not None:
        import capo_connect.types.endpoint

        out["source_endpoint"] = capo_connect.types.endpoint.deserialize_json(
            data["SourceEndpoint"]
        )
    else:
        raise DeserializationError(
            "StartOutboundChatContactRequest.source_endpoint required"
        )
    if data.get("DestinationEndpoint") is not None:
        import capo_connect.types.endpoint

        out["destination_endpoint"] = capo_connect.types.endpoint.deserialize_json(
            data["DestinationEndpoint"]
        )
    else:
        raise DeserializationError(
            "StartOutboundChatContactRequest.destination_endpoint required"
        )
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError(
            "StartOutboundChatContactRequest.instance_id required"
        )
    if data.get("SegmentAttributes") is not None:
        import capo_connect.types.segment_attributes

        out["segment_attributes"] = (
            capo_connect.types.segment_attributes.deserialize_json(
                data["SegmentAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "StartOutboundChatContactRequest.segment_attributes required"
        )
    if data.get("Attributes") is not None:
        import capo_connect.types.attributes

        out["attributes"] = capo_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        raise DeserializationError(
            "StartOutboundChatContactRequest.contact_flow_id required"
        )
    if data.get("ChatDurationInMinutes") is not None:
        out["chat_duration_in_minutes"] = data["ChatDurationInMinutes"]
    if data.get("ParticipantDetails") is not None:
        import capo_connect.types.participant_details

        out["participant_details"] = (
            capo_connect.types.participant_details.deserialize_json(
                data["ParticipantDetails"]
            )
        )
    if data.get("InitialSystemMessage") is not None:
        import capo_connect.types.chat_message

        out["initial_system_message"] = (
            capo_connect.types.chat_message.deserialize_json(
                data["InitialSystemMessage"]
            )
        )
    if data.get("InitialTemplatedSystemMessage") is not None:
        import capo_connect.types.templated_message_config

        out["initial_templated_system_message"] = (
            capo_connect.types.templated_message_config.deserialize_json(
                data["InitialTemplatedSystemMessage"]
            )
        )
    if data.get("RelatedContactId") is not None:
        out["related_contact_id"] = data["RelatedContactId"]
    if data.get("SupportedMessagingContentTypes") is not None:
        import capo_connect.types.supported_messaging_content_types

        out["supported_messaging_content_types"] = (
            capo_connect.types.supported_messaging_content_types.deserialize_json(
                data["SupportedMessagingContentTypes"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
