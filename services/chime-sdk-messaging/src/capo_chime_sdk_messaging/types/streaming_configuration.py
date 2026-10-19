"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#StreamingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.messaging_data_type


class StreamingConfiguration(TypedDict, closed=True):
    data_type: "capo_chime_sdk_messaging.types.messaging_data_type.MessagingDataType"
    """<p>The data type of the configuration.</p>"""
    resource_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the resource in the configuration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamingConfiguration) -> dict:
    out: dict = {}
    import capo_chime_sdk_messaging.types.messaging_data_type

    out["DataType"] = capo_chime_sdk_messaging.types.messaging_data_type.serialize_json(
        value["data_type"]
    )
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> StreamingConfiguration:
    out: StreamingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DataType") is not None:
        import capo_chime_sdk_messaging.types.messaging_data_type

        out["data_type"] = (
            capo_chime_sdk_messaging.types.messaging_data_type.deserialize_json(
                data["DataType"]
            )
        )
    else:
        import typing

        out["data_type"] = typing.cast(
            "capo_chime_sdk_messaging.types.messaging_data_type.MessagingDataType", ""
        )
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
