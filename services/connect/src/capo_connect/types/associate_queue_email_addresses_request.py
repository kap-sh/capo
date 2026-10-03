"""Generated from Smithy shape ``com.amazonaws.connect#AssociateQueueEmailAddressesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.email_address_config_list
    import capo_connect.types.instance_id
    import capo_connect.types.queue_id


class AssociateQueueEmailAddressesRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    queue_id: "capo_connect.types.queue_id.QueueId"
    """<p>The identifier for the queue.</p>"""
    email_addresses_config: (
        "capo_connect.types.email_address_config_list.EmailAddressConfigList"
    )
    """<p>Configuration list containing the email addresses to associate with the queue. Each configuration specifies an email address ID that should be linked to this queue for routing purposes.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateQueueEmailAddressesRequest) -> dict:
    out: dict = {}
    import capo_connect.types.email_address_config_list

    out["EmailAddressesConfig"] = (
        capo_connect.types.email_address_config_list.serialize_json(
            value["email_addresses_config"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AssociateQueueEmailAddressesRequest:
    out: AssociateQueueEmailAddressesRequest = {}  # type: ignore[typeddict-item]
    if data.get("EmailAddressesConfig") is not None:
        import capo_connect.types.email_address_config_list

        out["email_addresses_config"] = (
            capo_connect.types.email_address_config_list.deserialize_json(
                data["EmailAddressesConfig"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateQueueEmailAddressesRequest.email_addresses_config required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
