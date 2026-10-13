"""Generated from Smithy shape ``com.amazonaws.connect#EmailAddressMetadata``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.alias_configuration_list
    import capo_connect.types.description
    import capo_connect.types.email_address
    import capo_connect.types.email_address_arn
    import capo_connect.types.email_address_display_name
    import capo_connect.types.email_address_id


class EmailAddressMetadata(TypedDict, closed=True):
    email_address_id: NotRequired["capo_connect.types.email_address_id.EmailAddressId"]
    """<p>The identifier of the email address.</p>"""
    email_address_arn: NotRequired[
        "capo_connect.types.email_address_arn.EmailAddressArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the email address.</p>"""
    email_address: NotRequired["capo_connect.types.email_address.EmailAddress"]
    """<p>The email address, including the domain.</p>"""
    description: NotRequired["capo_connect.types.description.Description"]
    """<p>The description of the email address.</p>"""
    display_name: NotRequired[
        "capo_connect.types.email_address_display_name.EmailAddressDisplayName"
    ]
    """<p>The display name of email address.</p>"""
    alias_configurations: NotRequired[
        "capo_connect.types.alias_configuration_list.AliasConfigurationList"
    ]
    """<p>A list of alias configurations for this email address, showing which email addresses forward to this primary address. Each configuration contains the email address ID of an alias that forwards emails to this address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailAddressMetadata) -> dict:
    out: dict = {}
    if "email_address_id" in value:
        out["EmailAddressId"] = value["email_address_id"]
    if "email_address_arn" in value:
        out["EmailAddressArn"] = value["email_address_arn"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "description" in value:
        out["Description"] = value["description"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "alias_configurations" in value:
        import capo_connect.types.alias_configuration_list

        out["AliasConfigurations"] = (
            capo_connect.types.alias_configuration_list.serialize_json(
                value["alias_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmailAddressMetadata:
    out: EmailAddressMetadata = {}  # type: ignore[typeddict-item]
    if data.get("EmailAddressId") is not None:
        out["email_address_id"] = data["EmailAddressId"]
    if data.get("EmailAddressArn") is not None:
        out["email_address_arn"] = data["EmailAddressArn"]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("AliasConfigurations") is not None:
        import capo_connect.types.alias_configuration_list

        out["alias_configurations"] = (
            capo_connect.types.alias_configuration_list.deserialize_json(
                data["AliasConfigurations"]
            )
        )
    return out


def redact_sensitive(value: EmailAddressMetadata) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "email_address" in value:
        out["email_address"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    return out
