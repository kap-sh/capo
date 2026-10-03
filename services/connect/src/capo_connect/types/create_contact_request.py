"""Generated from Smithy shape ``com.amazonaws.connect#CreateContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.attributes
    import capo_connect.types.channel
    import capo_connect.types.client_token
    import capo_connect.types.contact_id
    import capo_connect.types.contact_initiation_method
    import capo_connect.types.contact_references
    import capo_connect.types.description
    import capo_connect.types.expiry_duration_in_minutes
    import capo_connect.types.initiate_as
    import capo_connect.types.instance_id
    import capo_connect.types.name
    import capo_connect.types.segment_attributes
    import capo_connect.types.user_info


class CreateContactRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    related_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    attributes: NotRequired["capo_connect.types.attributes.Attributes"]
    """<p>A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.</p> <p>There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.</p>"""
    references: NotRequired["capo_connect.types.contact_references.ContactReferences"]
    """<p>A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Tasks can have the following reference types at the time of creation: <code>URL</code> | <code>NUMBER</code> | <code>STRING</code> | <code>DATE</code> | <code>EMAIL</code> | <code>ATTACHMENT</code>.</p>"""
    channel: "capo_connect.types.channel.Channel"
    """<p>The channel for the contact.</p> <important> <p>The CHAT channel is not supported. The following information is incorrect. We're working to correct it.</p> </important>"""
    initiation_method: (
        "capo_connect.types.contact_initiation_method.ContactInitiationMethod"
    )
    """<p>Indicates how the contact was initiated. </p> <important> <p>CreateContact only supports the following initiation methods. Valid values by channel are: </p> <ul> <li> <p>For VOICE: <code>TRANSFER</code> and the subtype <code>connect:ExternalAudio</code> </p> </li> <li> <p>For EMAIL: <code>OUTBOUND</code> | <code>AGENT_REPLY</code> | <code>FLOW</code> </p> </li> <li> <p>For TASK: <code>API</code> </p> </li> </ul> <p>The other channels listed below are incorrect. We're working to correct this information.</p> </important>"""
    expiry_duration_in_minutes: NotRequired[
        "capo_connect.types.expiry_duration_in_minutes.ExpiryDurationInMinutes"
    ]
    """<p>Number of minutes the contact will be active for before expiring</p>"""
    user_info: NotRequired["capo_connect.types.user_info.UserInfo"]
    """<p>User details for the contact</p> <important> <p>UserInfo is required when creating an EMAIL contact with <code>OUTBOUND</code> and <code>AGENT_REPLY</code> contact initiation methods.</p> </important>"""
    initiate_as: NotRequired["capo_connect.types.initiate_as.InitiateAs"]
    """<p>Initial state of the contact when it's created. Only TASK channel contacts can be initiated with <code>COMPLETED</code> state.</p>"""
    name: NotRequired["capo_connect.types.name.Name"]
    """<p>The name of a the contact.</p>"""
    description: NotRequired["capo_connect.types.description.Description"]
    """<p>A description of the contact.</p>"""
    segment_attributes: NotRequired[
        "capo_connect.types.segment_attributes.SegmentAttributes"
    ]
    """<p>A set of system defined key-value pairs stored on individual contact segments (unique contact ID) using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.</p> <p>Attribute keys can include only alphanumeric, -, and _.</p> <p>This field can be used to set Segment Contact Expiry as a duration in minutes.</p> <note> <p>To set contact expiry, a ValueMap must be specified containing the integer number of minutes the contact will be active for before expiring, with <code>SegmentAttributes</code> like { <code> "connect:ContactExpiry": {"ValueMap" : { "ExpiryDuration": { "ValueInteger": 135}}}}</code>. </p> </note>"""
    previous_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The ID of the previous contact when creating a transfer contact. This value can be provided only for external audio contacts. For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html">Integrate Connect Customer Contact Lens with external voice systems</a> in the <i>Connect Customer Administrator Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateContactRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    if "attributes" in value:
        import capo_connect.types.attributes

        out["Attributes"] = capo_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    if "references" in value:
        import capo_connect.types.contact_references

        out["References"] = capo_connect.types.contact_references.serialize_json(
            value["references"]
        )
    import capo_connect.types.channel

    out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    import capo_connect.types.contact_initiation_method

    out["InitiationMethod"] = (
        capo_connect.types.contact_initiation_method.serialize_json(
            value["initiation_method"]
        )
    )
    if "expiry_duration_in_minutes" in value:
        out["ExpiryDurationInMinutes"] = value["expiry_duration_in_minutes"]
    if "user_info" in value:
        import capo_connect.types.user_info

        out["UserInfo"] = capo_connect.types.user_info.serialize_json(
            value["user_info"]
        )
    if "initiate_as" in value:
        import capo_connect.types.initiate_as

        out["InitiateAs"] = capo_connect.types.initiate_as.serialize_json(
            value["initiate_as"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "segment_attributes" in value:
        import capo_connect.types.segment_attributes

        out["SegmentAttributes"] = capo_connect.types.segment_attributes.serialize_json(
            value["segment_attributes"]
        )
    if "previous_contact_id" in value:
        out["PreviousContactId"] = value["previous_contact_id"]
    return out


def deserialize_json(data: dict) -> CreateContactRequest:
    out: CreateContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("CreateContactRequest.instance_id required")
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("RelatedContactId") is not None:
        out["related_contact_id"] = data["RelatedContactId"]
    if data.get("Attributes") is not None:
        import capo_connect.types.attributes

        out["attributes"] = capo_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if data.get("References") is not None:
        import capo_connect.types.contact_references

        out["references"] = capo_connect.types.contact_references.deserialize_json(
            data["References"]
        )
    if data.get("Channel") is not None:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    else:
        raise DeserializationError("CreateContactRequest.channel required")
    if data.get("InitiationMethod") is not None:
        import capo_connect.types.contact_initiation_method

        out["initiation_method"] = (
            capo_connect.types.contact_initiation_method.deserialize_json(
                data["InitiationMethod"]
            )
        )
    else:
        raise DeserializationError("CreateContactRequest.initiation_method required")
    if data.get("ExpiryDurationInMinutes") is not None:
        out["expiry_duration_in_minutes"] = data["ExpiryDurationInMinutes"]
    if data.get("UserInfo") is not None:
        import capo_connect.types.user_info

        out["user_info"] = capo_connect.types.user_info.deserialize_json(
            data["UserInfo"]
        )
    if data.get("InitiateAs") is not None:
        import capo_connect.types.initiate_as

        out["initiate_as"] = capo_connect.types.initiate_as.deserialize_json(
            data["InitiateAs"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SegmentAttributes") is not None:
        import capo_connect.types.segment_attributes

        out["segment_attributes"] = (
            capo_connect.types.segment_attributes.deserialize_json(
                data["SegmentAttributes"]
            )
        )
    if data.get("PreviousContactId") is not None:
        out["previous_contact_id"] = data["PreviousContactId"]
    return out
