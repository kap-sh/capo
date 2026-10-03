"""Generated from Smithy shape ``com.amazonaws.connect#AssociateEmailAddressAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.alias_configuration
    import capo_connect.types.client_token
    import capo_connect.types.email_address_id
    import capo_connect.types.instance_id


class AssociateEmailAddressAliasRequest(TypedDict, closed=True):
    email_address_id: "capo_connect.types.email_address_id.EmailAddressId"
    """<p>The identifier of the email address.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    alias_configuration: "capo_connect.types.alias_configuration.AliasConfiguration"
    """<p>Configuration object that specifies which email address will serve as the alias. The specified email address must already exist in the Connect Customer instance and cannot already be configured as an alias or have an alias of its own.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateEmailAddressAliasRequest) -> dict:
    out: dict = {}
    import capo_connect.types.alias_configuration

    out["AliasConfiguration"] = capo_connect.types.alias_configuration.serialize_json(
        value["alias_configuration"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> AssociateEmailAddressAliasRequest:
    out: AssociateEmailAddressAliasRequest = {}  # type: ignore[typeddict-item]
    if data.get("AliasConfiguration") is not None:
        import capo_connect.types.alias_configuration

        out["alias_configuration"] = (
            capo_connect.types.alias_configuration.deserialize_json(
                data["AliasConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateEmailAddressAliasRequest.alias_configuration required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
