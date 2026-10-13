"""Generated from Smithy shape ``com.amazonaws.workmail#DescribeResourceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.booking_options
    import capo_workmail.types.boolean
    import capo_workmail.types.email_address
    import capo_workmail.types.entity_state
    import capo_workmail.types.resource_description
    import capo_workmail.types.resource_id
    import capo_workmail.types.resource_name
    import capo_workmail.types.resource_type
    import capo_workmail.types.timestamp


class DescribeResourceResponse(TypedDict, closed=True):
    resource_id: NotRequired["capo_workmail.types.resource_id.ResourceId"]
    """<p>The identifier of the described resource.</p>"""
    email: NotRequired["capo_workmail.types.email_address.EmailAddress"]
    """<p>The email of the described resource.</p>"""
    name: NotRequired["capo_workmail.types.resource_name.ResourceName"]
    """<p>The name of the described resource.</p>"""
    type: NotRequired["capo_workmail.types.resource_type.ResourceType"]
    """<p>The type of the described resource.</p>"""
    booking_options: NotRequired["capo_workmail.types.booking_options.BookingOptions"]
    """<p>The booking options for the described resource.</p>"""
    state: NotRequired["capo_workmail.types.entity_state.EntityState"]
    """<p>The state of the resource: enabled (registered to WorkMail), disabled (deregistered or never registered to WorkMail), or deleted.</p>"""
    enabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date and time when a resource was enabled for WorkMail, in UNIX epoch time format.</p>"""
    disabled_date: NotRequired["capo_workmail.types.timestamp.Timestamp"]
    """<p>The date and time when a resource was disabled from WorkMail, in UNIX epoch time format.</p>"""
    description: NotRequired[
        "capo_workmail.types.resource_description.ResourceDescription"
    ]
    """<p>Description of the resource.</p>"""
    hidden_from_global_address_list: "capo_workmail.types.boolean.Boolean"
    """<p>If enabled, the resource is hidden from the global address list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeResourceResponse) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "email" in value:
        out["Email"] = value["email"]
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        import capo_workmail.types.resource_type

        out["Type"] = capo_workmail.types.resource_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "booking_options" in value:
        import capo_workmail.types.booking_options

        out["BookingOptions"] = (
            capo_workmail.types.booking_options.serialize_aws_json_1_1(
                value["booking_options"]
            )
        )
    if "state" in value:
        import capo_workmail.types.entity_state

        out["State"] = capo_workmail.types.entity_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "enabled_date" in value:
        import capo_workmail.types.timestamp

        out["EnabledDate"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["enabled_date"]
        )
    if "disabled_date" in value:
        import capo_workmail.types.timestamp

        out["DisabledDate"] = capo_workmail.types.timestamp.serialize_aws_json_1_1(
            value["disabled_date"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    out["HiddenFromGlobalAddressList"] = value.get(
        "hidden_from_global_address_list", False
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeResourceResponse:
    out: DescribeResourceResponse = {}  # type: ignore[typeddict-item]
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_workmail.types.resource_type

        out["type"] = capo_workmail.types.resource_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if data.get("BookingOptions") is not None:
        import capo_workmail.types.booking_options

        out["booking_options"] = (
            capo_workmail.types.booking_options.deserialize_aws_json_1_1(
                data["BookingOptions"]
            )
        )
    if data.get("State") is not None:
        import capo_workmail.types.entity_state

        out["state"] = capo_workmail.types.entity_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("EnabledDate") is not None:
        import capo_workmail.types.timestamp

        out["enabled_date"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["EnabledDate"]
        )
    if data.get("DisabledDate") is not None:
        import capo_workmail.types.timestamp

        out["disabled_date"] = capo_workmail.types.timestamp.deserialize_aws_json_1_1(
            data["DisabledDate"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("HiddenFromGlobalAddressList") is not None:
        out["hidden_from_global_address_list"] = data["HiddenFromGlobalAddressList"]
    else:
        out["hidden_from_global_address_list"] = False
    return out


def redact_sensitive(value: DescribeResourceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
