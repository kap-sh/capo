"""Generated from Smithy shape ``com.amazonaws.connect#StartEmailContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.attributes
    import capo_connect.types.client_token
    import capo_connect.types.contact_flow_id
    import capo_connect.types.contact_id
    import capo_connect.types.contact_references
    import capo_connect.types.description
    import capo_connect.types.email_address
    import capo_connect.types.email_address_info
    import capo_connect.types.email_attachments
    import capo_connect.types.inbound_additional_recipients
    import capo_connect.types.inbound_email_content
    import capo_connect.types.instance_id
    import capo_connect.types.name
    import capo_connect.types.segment_attributes


class StartEmailContactRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    from_email_address: "capo_connect.types.email_address_info.EmailAddressInfo"
    """<p>The email address of the customer.</p>"""
    destination_email_address: "capo_connect.types.email_address.EmailAddress"
    """<p>The email address associated with the Connect Customer instance.</p>"""
    description: NotRequired["capo_connect.types.description.Description"]
    """<p>A description of the email contact.</p>"""
    references: NotRequired["capo_connect.types.contact_references.ContactReferences"]
    """<p>A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Emails can have the following reference types at the time of creation: <code>URL</code> | <code>NUMBER</code> | <code>STRING</code> | <code>DATE</code>. <code>EMAIL</code> | <code>EMAIL_MESSAGE</code> |<code>ATTACHMENT</code> are not a supported reference type during email creation.</p>"""
    name: NotRequired["capo_connect.types.name.Name"]
    """<p>The name of a email that is shown to an agent in the Contact Control Panel (CCP).</p>"""
    email_message: "capo_connect.types.inbound_email_content.InboundEmailContent"
    """<p>The email message body to be sent to the newly created email.</p>"""
    additional_recipients: NotRequired[
        "capo_connect.types.inbound_additional_recipients.InboundAdditionalRecipients"
    ]
    """<p>The additional recipients address of the email.</p>"""
    attachments: NotRequired["capo_connect.types.email_attachments.EmailAttachments"]
    """<p>List of S3 presigned URLs of email attachments and their file name. </p>"""
    contact_flow_id: NotRequired["capo_connect.types.contact_flow_id.ContactFlowId"]
    """<p>The identifier of the flow for initiating the emails. To see the ContactFlowId in the Connect Customer admin website, on the navigation menu go to <b>Routing</b>, <b>Flows</b>. Choose the flow. On the flow page, under the name of the flow, choose <b>Show additional flow information</b>. The ContactFlowId is the last part of the ARN, shown here in bold: </p> <p>arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/<b>846ec553-a005-41c0-8341-xxxxxxxxxxxx</b> </p>"""
    related_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The contactId that is related to this contact. Linking emails together by using <code>RelatedContactID</code> copies over contact attributes from the related email contact to the new email contact. All updates to user-defined attributes in the new email contact are limited to the individual contact ID. There are no limits to the number of contacts that can be linked by using <code>RelatedContactId</code>. </p>"""
    attributes: NotRequired["capo_connect.types.attributes.Attributes"]
    """<p>A custom key-value pair using an attribute map. The attributes are standard Connect Customer attributes, and can be accessed in flows just like any other contact attributes.</p> <p>There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.</p>"""
    segment_attributes: NotRequired[
        "capo_connect.types.segment_attributes.SegmentAttributes"
    ]
    """<p>A set of system defined key-value pairs stored on individual contact segments using an attribute map. The attributes are standard Connect Customer attributes. They can be accessed in flows.</p> <p>Attribute keys can include only alphanumeric, -, and _.</p> <p>This field can be used to show channel subtype, such as <code>connect:Guide</code>.</p> <note> <p>To set contact expiry, a <code>ValueMap</code> must be specified containing the integer number of minutes the contact will be active for before expiring, with <code>SegmentAttributes</code> like { <code> "connect:ContactExpiry": {"ValueMap" : { "ExpiryDuration": { "ValueInteger":135}}}}</code>.</p> </note>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartEmailContactRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    import capo_connect.types.email_address_info

    out["FromEmailAddress"] = capo_connect.types.email_address_info.serialize_json(
        value["from_email_address"]
    )
    out["DestinationEmailAddress"] = value["destination_email_address"]
    if "description" in value:
        out["Description"] = value["description"]
    if "references" in value:
        import capo_connect.types.contact_references

        out["References"] = capo_connect.types.contact_references.serialize_json(
            value["references"]
        )
    if "name" in value:
        out["Name"] = value["name"]
    import capo_connect.types.inbound_email_content

    out["EmailMessage"] = capo_connect.types.inbound_email_content.serialize_json(
        value["email_message"]
    )
    if "additional_recipients" in value:
        import capo_connect.types.inbound_additional_recipients

        out["AdditionalRecipients"] = (
            capo_connect.types.inbound_additional_recipients.serialize_json(
                value["additional_recipients"]
            )
        )
    if "attachments" in value:
        import capo_connect.types.email_attachments

        out["Attachments"] = capo_connect.types.email_attachments.serialize_json(
            value["attachments"]
        )
    if "contact_flow_id" in value:
        out["ContactFlowId"] = value["contact_flow_id"]
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    if "attributes" in value:
        import capo_connect.types.attributes

        out["Attributes"] = capo_connect.types.attributes.serialize_json(
            value["attributes"]
        )
    if "segment_attributes" in value:
        import capo_connect.types.segment_attributes

        out["SegmentAttributes"] = capo_connect.types.segment_attributes.serialize_json(
            value["segment_attributes"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartEmailContactRequest:
    out: StartEmailContactRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("StartEmailContactRequest.instance_id required")
    if data.get("FromEmailAddress") is not None:
        import capo_connect.types.email_address_info

        out["from_email_address"] = (
            capo_connect.types.email_address_info.deserialize_json(
                data["FromEmailAddress"]
            )
        )
    else:
        raise DeserializationError(
            "StartEmailContactRequest.from_email_address required"
        )
    if data.get("DestinationEmailAddress") is not None:
        out["destination_email_address"] = data["DestinationEmailAddress"]
    else:
        raise DeserializationError(
            "StartEmailContactRequest.destination_email_address required"
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("References") is not None:
        import capo_connect.types.contact_references

        out["references"] = capo_connect.types.contact_references.deserialize_json(
            data["References"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("EmailMessage") is not None:
        import capo_connect.types.inbound_email_content

        out["email_message"] = (
            capo_connect.types.inbound_email_content.deserialize_json(
                data["EmailMessage"]
            )
        )
    else:
        raise DeserializationError("StartEmailContactRequest.email_message required")
    if data.get("AdditionalRecipients") is not None:
        import capo_connect.types.inbound_additional_recipients

        out["additional_recipients"] = (
            capo_connect.types.inbound_additional_recipients.deserialize_json(
                data["AdditionalRecipients"]
            )
        )
    if data.get("Attachments") is not None:
        import capo_connect.types.email_attachments

        out["attachments"] = capo_connect.types.email_attachments.deserialize_json(
            data["Attachments"]
        )
    if data.get("ContactFlowId") is not None:
        out["contact_flow_id"] = data["ContactFlowId"]
    if data.get("RelatedContactId") is not None:
        out["related_contact_id"] = data["RelatedContactId"]
    if data.get("Attributes") is not None:
        import capo_connect.types.attributes

        out["attributes"] = capo_connect.types.attributes.deserialize_json(
            data["Attributes"]
        )
    if data.get("SegmentAttributes") is not None:
        import capo_connect.types.segment_attributes

        out["segment_attributes"] = (
            capo_connect.types.segment_attributes.deserialize_json(
                data["SegmentAttributes"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
