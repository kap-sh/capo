"""Generated from Smithy shape ``com.amazonaws.connect#DisassociateQueueEmailAddressesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.email_address_id_list
    import capo_connect.types.instance_id
    import capo_connect.types.queue_id


class DisassociateQueueEmailAddressesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    queue_id: "capo_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    email_addresses_id: "capo_connect.types.email_address_id_list.EmailAddressIdList"
    """<p>List of email address identifiers to disassociate from the queue. These are the unique identifiers of email addresses that should no longer be routed to this queue.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateQueueEmailAddressesRequest) -> dict:
    out: dict = {}
    import capo_connect.types.email_address_id_list

    out["EmailAddressesId"] = capo_connect.types.email_address_id_list.serialize_json(
        value["email_addresses_id"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> DisassociateQueueEmailAddressesRequest:
    out: DisassociateQueueEmailAddressesRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmailAddressesId") is not None:
        import capo_connect.types.email_address_id_list

        out["email_addresses_id"] = (
            capo_connect.types.email_address_id_list.deserialize_json(
                data["EmailAddressesId"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateQueueEmailAddressesRequest.email_addresses_id required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
