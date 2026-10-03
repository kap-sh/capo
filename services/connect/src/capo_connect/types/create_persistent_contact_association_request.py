"""Generated from Smithy shape ``com.amazonaws.connect#CreatePersistentContactAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id
    import capo_connect.types.rehydration_type


class CreatePersistentContactAssociationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    initial_contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>This is the contactId of the current contact that the <code>CreatePersistentContactAssociation</code> API is being called from.</p>"""
    rehydration_type: "capo_connect.types.rehydration_type.RehydrationType"
    """<p>The contactId chosen for rehydration depends on the type chosen.</p> <ul> <li> <p> <code>ENTIRE_PAST_SESSION</code>: Rehydrates a chat from the most recently terminated past chat contact of the specified past ended chat session. To use this type, provide the <code>initialContactId</code> of the past ended chat session in the <code>sourceContactId</code> field. In this type, Connect Customer determines what the most recent chat contact on the past ended chat session and uses it to start a persistent chat. </p> </li> <li> <p> <code>FROM_SEGMENT</code>: Rehydrates a chat from the specified past chat contact provided in the <code>sourceContactId</code> field. </p> </li> </ul> <p>The actual contactId used for rehydration is provided in the response of this API.</p> <p>To illustrate how to use rehydration type, consider the following example: A customer starts a chat session. Agent a1 accepts the chat and a conversation starts between the customer and Agent a1. This first contact creates a contact ID <b>C1</b>. Agent a1 then transfers the chat to Agent a2. This creates another contact ID <b>C2</b>. At this point Agent a2 ends the chat. The customer is forwarded to the disconnect flow for a post chat survey that creates another contact ID <b>C3</b>. After the chat survey, the chat session ends. Later, the customer returns and wants to resume their past chat session. At this point, the customer can have following use cases: </p> <ul> <li> <p> <b>Use Case 1</b>: The customer wants to continue the past chat session but they want to hide the post chat survey. For this they will use the following configuration:</p> <ul> <li> <p> <b>Configuration</b> </p> <ul> <li> <p>SourceContactId = "C2"</p> </li> <li> <p>RehydrationType = "FROM_SEGMENT"</p> </li> </ul> </li> <li> <p> <b>Expected behavior</b> </p> <ul> <li> <p>This starts a persistent chat session from the specified past ended contact (C2). Transcripts of past chat sessions C2 and C1 are accessible in the current persistent chat session. Note that chat segment C3 is dropped from the persistent chat session.</p> </li> </ul> </li> </ul> </li> <li> <p> <b>Use Case 2</b>: The customer wants to continue the past chat session and see the transcript of the entire past engagement, including the post chat survey. For this they will use the following configuration:</p> <ul> <li> <p> <b>Configuration</b> </p> <ul> <li> <p>SourceContactId = "C1"</p> </li> <li> <p>RehydrationType = "ENTIRE_PAST_SESSION"</p> </li> </ul> </li> <li> <p> <b>Expected behavior</b> </p> <ul> <li> <p>This starts a persistent chat session from the most recently ended chat contact (C3). Transcripts of past chat sessions C3, C2 and C1 are accessible in the current persistent chat session.</p> </li> </ul> </li> </ul> </li> </ul>"""
    source_contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The contactId from which a persistent chat session must be started.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePersistentContactAssociationRequest) -> dict:
    out: dict = {}
    import capo_connect.types.rehydration_type

    out["RehydrationType"] = capo_connect.types.rehydration_type.serialize_json(
        value["rehydration_type"]
    )
    out["SourceContactId"] = value["source_contact_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreatePersistentContactAssociationRequest:
    out: CreatePersistentContactAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("RehydrationType") is not None:
        import capo_connect.types.rehydration_type

        out["rehydration_type"] = capo_connect.types.rehydration_type.deserialize_json(
            data["RehydrationType"]
        )
    else:
        raise DeserializationError(
            "CreatePersistentContactAssociationRequest.rehydration_type required"
        )
    if data.get("SourceContactId") is not None:
        out["source_contact_id"] = data["SourceContactId"]
    else:
        raise DeserializationError(
            "CreatePersistentContactAssociationRequest.source_contact_id required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
