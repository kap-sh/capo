"""Generated from Smithy shape ``com.amazonaws.iotevents#InputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.input_arn
    import capo_iot_events.types.input_description
    import capo_iot_events.types.input_name
    import capo_iot_events.types.input_status
    import capo_iot_events.types.timestamp


class InputConfiguration(TypedDict, closed=True):
    input_name: "capo_iot_events.types.input_name.InputName"
    """<p>The name of the input.</p>"""
    input_description: NotRequired[
        "capo_iot_events.types.input_description.InputDescription"
    ]
    """<p>A brief description of the input.</p>"""
    input_arn: "capo_iot_events.types.input_arn.InputArn"
    """<p>The ARN of the input.</p>"""
    creation_time: "capo_iot_events.types.timestamp.Timestamp"
    """<p>The time the input was created.</p>"""
    last_update_time: "capo_iot_events.types.timestamp.Timestamp"
    """<p>The last time the input was updated.</p>"""
    status: "capo_iot_events.types.input_status.InputStatus"
    """<p>The status of the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputConfiguration) -> dict:
    out: dict = {}
    out["inputName"] = value["input_name"]
    if "input_description" in value:
        out["inputDescription"] = value["input_description"]
    out["inputArn"] = value["input_arn"]
    import capo_iot_events.types.timestamp

    out["creationTime"] = capo_iot_events.types.timestamp.serialize_json(
        value["creation_time"]
    )
    import capo_iot_events.types.timestamp

    out["lastUpdateTime"] = capo_iot_events.types.timestamp.serialize_json(
        value["last_update_time"]
    )
    import capo_iot_events.types.input_status

    out["status"] = capo_iot_events.types.input_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> InputConfiguration:
    out: InputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("inputName") is not None:
        out["input_name"] = data["inputName"]
    else:
        out["input_name"] = ""
    if data.get("inputDescription") is not None:
        out["input_description"] = data["inputDescription"]
    if data.get("inputArn") is not None:
        out["input_arn"] = data["inputArn"]
    else:
        out["input_arn"] = ""
    if data.get("creationTime") is not None:
        import capo_iot_events.types.timestamp

        out["creation_time"] = capo_iot_events.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastUpdateTime") is not None:
        import capo_iot_events.types.timestamp

        out["last_update_time"] = capo_iot_events.types.timestamp.deserialize_json(
            data["lastUpdateTime"]
        )
    else:
        import datetime

        out["last_update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("status") is not None:
        import capo_iot_events.types.input_status

        out["status"] = capo_iot_events.types.input_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iot_events.types.input_status.InputStatus", ""
        )
    return out
