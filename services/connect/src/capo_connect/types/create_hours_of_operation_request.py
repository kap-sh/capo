"""Generated from Smithy shape ``com.amazonaws.connect#CreateHoursOfOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.common_name_length127
    import capo_connect.types.hours_of_operation_config_list
    import capo_connect.types.hours_of_operation_description
    import capo_connect.types.instance_id
    import capo_connect.types.parent_hours_of_operation_config_list
    import capo_connect.types.tag_map
    import capo_connect.types.time_zone


class CreateHoursOfOperationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    name: "capo_connect.types.common_name_length127.CommonNameLength127"
    """<p>The name of the hours of operation.</p>"""
    description: NotRequired[
        "capo_connect.types.hours_of_operation_description.HoursOfOperationDescription"
    ]
    """<p>The description of the hours of operation.</p>"""
    time_zone: "capo_connect.types.time_zone.TimeZone"
    """<p>The time zone of the hours of operation.</p>"""
    config: (
        "capo_connect.types.hours_of_operation_config_list.HoursOfOperationConfigList"
    )
    """<p>Configuration information for the hours of operation: day, start time, and end time.</p>"""
    parent_hours_of_operation_configs: NotRequired[
        "capo_connect.types.parent_hours_of_operation_config_list.ParentHoursOfOperationConfigList"
    ]
    """<p>Configuration for parent hours of operations. Eg: ResourceArn. </p> <p>For more information about parent hours of operations, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/hours-of-operation-overrides.html">Link overrides from different hours of operation</a> in the <i> Administrator Guide</i>.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHoursOfOperationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["TimeZone"] = value["time_zone"]
    import capo_connect.types.hours_of_operation_config_list

    out["Config"] = capo_connect.types.hours_of_operation_config_list.serialize_json(
        value["config"]
    )
    if "parent_hours_of_operation_configs" in value:
        import capo_connect.types.parent_hours_of_operation_config_list

        out["ParentHoursOfOperationConfigs"] = (
            capo_connect.types.parent_hours_of_operation_config_list.serialize_json(
                value["parent_hours_of_operation_configs"]
            )
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateHoursOfOperationRequest:
    out: CreateHoursOfOperationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateHoursOfOperationRequest.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("TimeZone") is not None:
        out["time_zone"] = data["TimeZone"]
    else:
        raise DeserializationError("CreateHoursOfOperationRequest.time_zone required")
    if data.get("Config") is not None:
        import capo_connect.types.hours_of_operation_config_list

        out["config"] = (
            capo_connect.types.hours_of_operation_config_list.deserialize_json(
                data["Config"]
            )
        )
    else:
        raise DeserializationError("CreateHoursOfOperationRequest.config required")
    if data.get("ParentHoursOfOperationConfigs") is not None:
        import capo_connect.types.parent_hours_of_operation_config_list

        out["parent_hours_of_operation_configs"] = (
            capo_connect.types.parent_hours_of_operation_config_list.deserialize_json(
                data["ParentHoursOfOperationConfigs"]
            )
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
