"""Generated from Smithy shape ``com.amazonaws.connect#DescribeEmailAddressResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.alias_configuration_list
    import capo_connect.types.description
    import capo_connect.types.email_address
    import capo_connect.types.email_address_arn
    import capo_connect.types.email_address_display_name
    import capo_connect.types.email_address_id
    import capo_connect.types.iso8601_datetime
    import capo_connect.types.tag_map


class DescribeEmailAddressResponse(TypedDict, closed=True):
    email_address_id: NotRequired["capo_connect.types.email_address_id.EmailAddressId"]
    """<p>The identifier of the email address.</p>"""
    email_address_arn: NotRequired[
        "capo_connect.types.email_address_arn.EmailAddressArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the email address.</p>"""
    email_address: NotRequired["capo_connect.types.email_address.EmailAddress"]
    """<p>The email address, including the domain.</p>"""
    display_name: NotRequired[
        "capo_connect.types.email_address_display_name.EmailAddressDisplayName"
    ]
    """<p>The display name of email address</p>"""
    description: NotRequired["capo_connect.types.description.Description"]
    """<p>The description of the email address.</p>"""
    create_timestamp: NotRequired["capo_connect.types.iso8601_datetime.ISO8601Datetime"]
    """<p>The email address creation timestamp in ISO 8601 Datetime.</p>"""
    modified_timestamp: NotRequired[
        "capo_connect.types.iso8601_datetime.ISO8601Datetime"
    ]
    """<p>The email address last modification timestamp in ISO 8601 Datetime.</p>"""
    alias_configurations: NotRequired[
        "capo_connect.types.alias_configuration_list.AliasConfigurationList"
    ]
    """<p>A list of alias configurations associated with this email address. Contains details about email addresses that forward to this primary email address. The list can contain at most one alias configuration per email address.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeEmailAddressResponse) -> dict:
    out: dict = {}
    if "email_address_id" in value:
        out["EmailAddressId"] = value["email_address_id"]
    if "email_address_arn" in value:
        out["EmailAddressArn"] = value["email_address_arn"]
    if "email_address" in value:
        out["EmailAddress"] = value["email_address"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "create_timestamp" in value:
        out["CreateTimestamp"] = value["create_timestamp"]
    if "modified_timestamp" in value:
        out["ModifiedTimestamp"] = value["modified_timestamp"]
    if "alias_configurations" in value:
        import capo_connect.types.alias_configuration_list

        out["AliasConfigurations"] = (
            capo_connect.types.alias_configuration_list.serialize_json(
                value["alias_configurations"]
            )
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribeEmailAddressResponse:
    out: DescribeEmailAddressResponse = {}  # type: ignore[typeddict-item]
    if data.get("EmailAddressId") is not None:
        out["email_address_id"] = data["EmailAddressId"]
    if data.get("EmailAddressArn") is not None:
        out["email_address_arn"] = data["EmailAddressArn"]
    if data.get("EmailAddress") is not None:
        out["email_address"] = data["EmailAddress"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreateTimestamp") is not None:
        out["create_timestamp"] = data["CreateTimestamp"]
    if data.get("ModifiedTimestamp") is not None:
        out["modified_timestamp"] = data["ModifiedTimestamp"]
    if data.get("AliasConfigurations") is not None:
        import capo_connect.types.alias_configuration_list

        out["alias_configurations"] = (
            capo_connect.types.alias_configuration_list.deserialize_json(
                data["AliasConfigurations"]
            )
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
