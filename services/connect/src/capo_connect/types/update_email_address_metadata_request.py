"""Generated from Smithy shape ``com.amazonaws.connect#UpdateEmailAddressMetadataRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.description
    import capo_connect.types.email_address_display_name
    import capo_connect.types.email_address_id
    import capo_connect.types.instance_id


class UpdateEmailAddressMetadataRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    email_address_id: "capo_connect.types.email_address_id.EmailAddressId"
    """<p>The identifier of the email address.</p>"""
    description: NotRequired["capo_connect.types.description.Description"]
    """<p>The description of the email address.</p>"""
    display_name: NotRequired[
        "capo_connect.types.email_address_display_name.EmailAddressDisplayName"
    ]
    """<p>The display name of email address.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEmailAddressMetadataRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateEmailAddressMetadataRequest:
    out: UpdateEmailAddressMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
