"""Generated from Smithy shape ``com.amazonaws.connect#StartChatContactRequest``."""

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
    import capo_connect.types.customer_id_non_empty
    import capo_connect.types.disconnect_on_customer_exit
    import capo_connect.types.instance_id
    import capo_connect.types.participant_configuration
    import capo_connect.types.participant_details
    import capo_connect.types.persistent_chat
    import capo_connect.types.segment_attributes
    import capo_connect.types.supported_messaging_content_types


class StartChatContactRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_flow_id: "capo_connect.types.contact_flow_id.ContactFlowId"
    """<p>The identifier of the flow for initiating the chat. To see the ContactFlowId in the Connect Customer admin website, on the navigation menu go to <b>Routing</b>, <b>Flows</b>. Choose the flow. On the flow page, under the name of the flow, choose <b>Show additional flow information</b>. The ContactFlowId is the last part of the ARN, shown here in bold: </p> <p>arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/<b>846ec553-a005-41c0-8341-xxxxxxxxxxxx</b> </p>"""
    attributes: NotRequired["capo_connect.types.attributes.Attributes"]
    """<p>A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows just like any other contact attributes. </p> <p>There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.</p>"""
    participant_details: "capo_connect.types.participant_details.ParticipantDetails"
    """<p>Information identifying the participant.</p>"""
    participant_configuration: NotRequired[
        "capo_connect.types.participant_configuration.ParticipantConfiguration"
    ]
    """<p> The configuration of the participant. </p>"""
    initial_message: NotRequired["capo_connect.types.chat_message.ChatMessage"]
    """<p>The initial message to be sent to the newly created chat.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    chat_duration_in_minutes: NotRequired[
        "capo_connect.types.chat_duration_in_minutes.ChatDurationInMinutes"
    ]
    """<p>The total duration of the newly started chat session. If not specified, the chat session duration defaults to 25 hour. The minimum configurable time is 60 minutes. The maximum configurable time is 10,080 minutes (7 days).</p>"""
    supported_messaging_content_types: NotRequired[
        "capo_connect.types.supported_messaging_content_types.SupportedMessagingContentTypes"
    ]
    """<p>The supported chat message content types. Supported types are <code>text/plain</code>, <code>text/markdown</code>, <code>application/json</code>, <code>application/vnd.amazonaws.connect.message.interactive</code>, and <code>application/vnd.amazonaws.connect.message.interactive.response</code>. </p> <p>Content types must always contain <code>text/plain</code>. You can then put any other supported type in the list. For example, all the following lists are valid because they contain <code>text/plain</code>: <code>[text/plain, text/markdown, application/json]</code>, <code>[text/markdown, text/plain]</code>, <code>[text/plain, application/json, application/vnd.amazonaws.connect.message.interactive.response]</code>. </p> <note> <p>The type <code>application/vnd.amazonaws.connect.message.interactive</code> is required to use the <a href="https://docs.aws.amazon.com/connect/latest/adminguide/show-view-block.html">Show view</a> flow block.</p> </note>"""
    persistent_chat: NotRequired["capo_connect.types.persistent_chat.PersistentChat"]
    """<p>Enable persistent chats. For more information about enabling persistent chat, and for example use cases and how to configure for them, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/chat-persistence.html">Enable persistent chat</a>.</p>"""
    related_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The unique identifier for an Connect Customer contact. This identifier is related to the chat starting.</p> <note> <p>You cannot provide data for both RelatedContactId and PersistentChat. </p> </note>"""
    segment_attributes: NotRequired[
        "capo_connect.types.segment_attributes.SegmentAttributes"
    ]
    """<p>A set of system defined key-value pairs stored on individual contact segments using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.</p> <p>Attribute keys can include only alphanumeric, -, and _.</p> <p>This field can be used to show channel subtype, such as <code>connect:Guide</code>.</p> <note> <p>The types <code>application/vnd.amazonaws.connect.message.interactive</code> and <code>application/vnd.amazonaws.connect.message.interactive.response</code> must be present in the SupportedMessagingContentTypes field of this API in order to set <code>SegmentAttributes</code> as {<code> "connect:Subtype": {"valueString" : "connect:Guide" }}</code>.</p> </note>"""
    customer_id: NotRequired[
        "capo_connect.types.customer_id_non_empty.CustomerIdNonEmpty"
    ]
    """<p>The customer's identification number. For example, the <code>CustomerId</code> may be a customer number from your CRM.</p>"""
    disconnect_on_customer_exit: NotRequired[
        "capo_connect.types.disconnect_on_customer_exit.DisconnectOnCustomerExit"
    ]
    """<p>A list of participant types to automatically disconnect when the end customer ends the chat session, allowing them to continue through disconnect flows such as surveys or feedback forms.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartChatContactRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactFlowId"] = value["contact_flow_id"]
    if "attributes" in value:
        import capo_connect.types.attributes

        out["Attributes"] = capo_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    import capo_connect.types.participant_details

    out["ParticipantDetails"] = capo_connect.types.participant_details.serialize_json(
        value["participant_details"]
    )
    if "participant_configuration" in value:
        import capo_connect.types.participant_configuration

        out["ParticipantConfiguration"] = (
            capo_connect.types.participant_configuration.serialize_json(
                value["participant_configuration"]
            )
        )
    if "initial_message" in value:
        import capo_connect.types.chat_message

        out["InitialMessage"] = capo_connect.types.chat_message.serialize_json(
            value["initial_message"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "chat_duration_in_minutes" in value:
        out["ChatDurationInMinutes"] = value["chat_duration_in_minutes"]
    if "supported_messaging_content_types" in value:
        import capo_connect.types.supported_messaging_content_types

        out["SupportedMessagingContentTypes"] = (
            capo_connect.types.supported_messaging_content_types.serialize_json(
                value["supported_messaging_content_types"]
            )
        )
    if "persistent_chat" in value:
        import capo_connect.types.persistent_chat

        out["PersistentChat"] = capo_connect.types.persistent_chat.serialize_json(
            value["persistent_chat"]
        )
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    if "segment_attributes" in value:
        import capo_connect.types.segment_attributes

        out["SegmentAttributes"] = capo_connect.types.segment_attributes.serialize_json(
            value["segment_attributes"]
        )
    if "customer_id" in value:
        out["CustomerId"] = value["customer_id"]
    if "disconnect_on_customer_exit" in value:
        import capo_connect.types.disconnect_on_customer_exit

        out["DisconnectOnCustomerExit"] = (
            capo_connect.types.disconnect_on_customer_exit.serialize_json(
                value["disconnect_on_customer_exit"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartChatContactRequest:
    out: StartChatContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("StartChatContactRequest.instance_id required")
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    else:
        raise DeserializationError("StartChatContactRequest.contact_flow_id required")
    if data.get("Attributes") is not None:
        import capo_connect.types.attributes

        out["attributes"] = capo_connect.types.attributes.deserialize_json(
            data["Attributes"]
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
            "StartChatContactRequest.participant_details required"
        )
    if data.get("ParticipantConfiguration") is not None:
        import capo_connect.types.participant_configuration

        out["participant_configuration"] = (
            capo_connect.types.participant_configuration.deserialize_json(
                data["ParticipantConfiguration"]
            )
        )
    if data.get("InitialMessage") is not None:
        import capo_connect.types.chat_message

        out["initial_message"] = capo_connect.types.chat_message.deserialize_json(
            data["InitialMessage"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("ChatDurationInMinutes") is not None:
        out["chat_duration_in_minutes"] = data["ChatDurationInMinutes"]
    if data.get("SupportedMessagingContentTypes") is not None:
        import capo_connect.types.supported_messaging_content_types

        out["supported_messaging_content_types"] = (
            capo_connect.types.supported_messaging_content_types.deserialize_json(
                data["SupportedMessagingContentTypes"]
            )
        )
    if data.get("PersistentChat") is not None:
        import capo_connect.types.persistent_chat

        out["persistent_chat"] = capo_connect.types.persistent_chat.deserialize_json(
            data["PersistentChat"]
        )
    if data.get("RelatedContactId") is not None:
        out["related_contact_id"] = data["RelatedContactId"]
    if data.get("SegmentAttributes") is not None:
        import capo_connect.types.segment_attributes

        out["segment_attributes"] = (
            capo_connect.types.segment_attributes.deserialize_json(
                data["SegmentAttributes"]
            )
        )
    if data.get("CustomerId") is not None:
        out["customer_id"] = data["CustomerId"]
    if data.get("DisconnectOnCustomerExit") is not None:
        import capo_connect.types.disconnect_on_customer_exit

        out["disconnect_on_customer_exit"] = (
            capo_connect.types.disconnect_on_customer_exit.deserialize_json(
                data["DisconnectOnCustomerExit"]
            )
        )
    return out
