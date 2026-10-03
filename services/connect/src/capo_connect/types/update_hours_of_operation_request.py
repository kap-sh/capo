"""Generated from Smithy shape ``com.amazonaws.connect#UpdateHoursOfOperationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.common_name_length127
    import capo_connect.types.hours_of_operation_config_list
    import capo_connect.types.hours_of_operation_id
    import capo_connect.types.instance_id
    import capo_connect.types.time_zone
    import capo_connect.types.update_hours_of_operation_description


class UpdateHoursOfOperationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    hours_of_operation_id: "capo_connect.types.hours_of_operation_id.HoursOfOperationId"
    """<p>The identifier of the hours of operation.</p>"""
    name: NotRequired["capo_connect.types.common_name_length127.CommonNameLength127"]
    """<p>The name of the hours of operation.</p>"""
    description: NotRequired[
        "capo_connect.types.update_hours_of_operation_description.UpdateHoursOfOperationDescription"
    ]
    """<p>The description of the hours of operation.</p>"""
    time_zone: NotRequired["capo_connect.types.time_zone.TimeZone"]
    """<p>The time zone of the hours of operation.</p>"""
    config: NotRequired[
        "capo_connect.types.hours_of_operation_config_list.HoursOfOperationConfigList"
    ]
    """<p>Configuration information of the hours of operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateHoursOfOperationRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "time_zone" in value:
        out["TimeZone"] = value["time_zone"]
    if "config" in value:
        import capo_connect.types.hours_of_operation_config_list

        out["Config"] = (
            capo_connect.types.hours_of_operation_config_list.serialize_json(
                value["config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateHoursOfOperationRequest:
    out: UpdateHoursOfOperationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("TimeZone") is not None:
        out["time_zone"] = data["TimeZone"]
    if data.get("Config") is not None:
        import capo_connect.types.hours_of_operation_config_list

        out["config"] = (
            capo_connect.types.hours_of_operation_config_list.deserialize_json(
                data["Config"]
            )
        )
    return out
