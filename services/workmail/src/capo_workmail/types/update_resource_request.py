"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateResourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.booking_options
    import capo_workmail.types.boolean_object
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.new_resource_description
    import capo_workmail.types.organization_id
    import capo_workmail.types.resource_name
    import capo_workmail.types.resource_type


class UpdateResourceRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier associated with the organization for which the resource is updated.</p>"""
    resource_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier of the resource to be updated.</p> <p>The identifier can accept <i>ResourceId</i>, <i>Resourcename</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Resource ID: r-0123456789a0123456789b0123456789</p> </li> <li> <p>Email address: resource@domain.tld</p> </li> <li> <p>Resource name: resource</p> </li> </ul>"""
    name: NotRequired["capo_workmail.types.resource_name.ResourceName"]
    """<p>The name of the resource to be updated.</p>"""
    booking_options: NotRequired["capo_workmail.types.booking_options.BookingOptions"]
    """<p>The resource's booking options to be updated.</p>"""
    description: NotRequired[
        "capo_workmail.types.new_resource_description.NewResourceDescription"
    ]
    """<p>Updates the resource description.</p>"""
    type: NotRequired["capo_workmail.types.resource_type.ResourceType"]
    """<p>Updates the resource type.</p>"""
    hidden_from_global_address_list: NotRequired[
        "capo_workmail.types.boolean_object.BooleanObject"
    ]
    """<p>If enabled, the resource is hidden from the global address list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResourceRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["ResourceId"] = value["resource_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "booking_options" in value:
        import capo_workmail.types.booking_options

        out["BookingOptions"] = (
            capo_workmail.types.booking_options.serialize_aws_json_1_1(
                value["booking_options"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import capo_workmail.types.resource_type

        out["Type"] = capo_workmail.types.resource_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "hidden_from_global_address_list" in value:
        out["HiddenFromGlobalAddressList"] = value["hidden_from_global_address_list"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResourceRequest:
    out: UpdateResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("UpdateResourceRequest.organization_id required")
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("UpdateResourceRequest.resource_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("BookingOptions") is not None:
        import capo_workmail.types.booking_options

        out["booking_options"] = (
            capo_workmail.types.booking_options.deserialize_aws_json_1_1(
                data["BookingOptions"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        import capo_workmail.types.resource_type

        out["type"] = capo_workmail.types.resource_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("HiddenFromGlobalAddressList") is not None:
        out["hidden_from_global_address_list"] = data["HiddenFromGlobalAddressList"]
    return out


def redact_sensitive(value: UpdateResourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
