"""Generated from Smithy shape ``com.amazonaws.connect#CreateQueueRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.common_name_length127
    import capo_connect.types.email_address_config_list
    import capo_connect.types.hours_of_operation_id
    import capo_connect.types.instance_id
    import capo_connect.types.outbound_caller_config
    import capo_connect.types.outbound_email_config
    import capo_connect.types.queue_description
    import capo_connect.types.queue_max_contacts
    import capo_connect.types.quick_connects_list
    import capo_connect.types.tag_map


class CreateQueueRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.common_name_length127.CommonNameLength127"
    """<p>The name of the queue.</p>"""
    description: NotRequired["capo_connect.types.queue_description.QueueDescription"]
    """<p>The description of the queue.</p>"""
    outbound_caller_config: NotRequired[
        "capo_connect.types.outbound_caller_config.OutboundCallerConfig"
    ]
    """<p>The outbound caller ID name, number, and outbound whisper flow.</p>"""
    outbound_email_config: NotRequired[
        "capo_connect.types.outbound_email_config.OutboundEmailConfig"
    ]
    """<p>The outbound email address ID for a specified queue.</p>"""
    hours_of_operation_id: "capo_connect.types.hours_of_operation_id.HoursOfOperationId"
    """<p>The identifier for the hours of operation.</p>"""
    max_contacts: NotRequired["capo_connect.types.queue_max_contacts.QueueMaxContacts"]
    """<p>The maximum number of contacts that can be in the queue before it is considered full.</p>"""
    quick_connect_ids: NotRequired[
        "capo_connect.types.quick_connects_list.QuickConnectsList"
    ]
    """<p>The quick connects available to agents who are working the queue.</p>"""
    email_addresses_config: NotRequired[
        "capo_connect.types.email_address_config_list.EmailAddressConfigList"
    ]
    """<p>Configuration list containing the email addresses to associate with the queue during creation. Each configuration specifies an email address ID that agents can select when handling email contacts in this queue.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateQueueRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "outbound_caller_config" in value:
        import capo_connect.types.outbound_caller_config

        out["OutboundCallerConfig"] = (
            capo_connect.types.outbound_caller_config.serialize_json(
                value["outbound_caller_config"]
            )
        )
    if "outbound_email_config" in value:
        import capo_connect.types.outbound_email_config

        out["OutboundEmailConfig"] = (
            capo_connect.types.outbound_email_config.serialize_json(
                value["outbound_email_config"]
            )
        )
    out["HoursOfOperationId"] = value["hours_of_operation_id"]
    if "max_contacts" in value:
        out["MaxContacts"] = value["max_contacts"]
    if "quick_connect_ids" in value:
        import capo_connect.types.quick_connects_list

        out["QuickConnectIds"] = capo_connect.types.quick_connects_list.serialize_json(
            value["quick_connect_ids"]
        )
    if "email_addresses_config" in value:
        import capo_connect.types.email_address_config_list

        out["EmailAddressesConfig"] = (
            capo_connect.types.email_address_config_list.serialize_json(
                value["email_addresses_config"]
            )
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateQueueRequest:
    out: CreateQueueRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateQueueRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("OutboundCallerConfig") is not None:
        import capo_connect.types.outbound_caller_config

        out["outbound_caller_config"] = (
            capo_connect.types.outbound_caller_config.deserialize_json(
                data["OutboundCallerConfig"]
            )
        )
    if data.get("OutboundEmailConfig") is not None:
        import capo_connect.types.outbound_email_config

        out["outbound_email_config"] = (
            capo_connect.types.outbound_email_config.deserialize_json(
                data["OutboundEmailConfig"]
            )
        )
    if data.get("HoursOfOperationId") is not None:
        out["hours_of_operation_id"] = data["HoursOfOperationId"]
    else:
        raise DeserializationError("CreateQueueRequest.hours_of_operation_id required")
    if data.get("MaxContacts") is not None:
        out["max_contacts"] = data["MaxContacts"]
    if data.get("QuickConnectIds") is not None:
        import capo_connect.types.quick_connects_list

        out["quick_connect_ids"] = (
            capo_connect.types.quick_connects_list.deserialize_json(
                data["QuickConnectIds"]
            )
        )
    if data.get("EmailAddressesConfig") is not None:
        import capo_connect.types.email_address_config_list

        out["email_addresses_config"] = (
            capo_connect.types.email_address_config_list.deserialize_json(
                data["EmailAddressesConfig"]
            )
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
