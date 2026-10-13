"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionHeaderParametersList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_eventbridge.types.connection_header_parameter

ConnectionHeaderParametersList: TypeAlias = list[
    "capo_eventbridge.types.connection_header_parameter.ConnectionHeaderParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionHeaderParametersList) -> list:
    import capo_eventbridge.types.connection_header_parameter

    out: list = []
    for item in value:
        out.append(
            capo_eventbridge.types.connection_header_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ConnectionHeaderParametersList:
    import capo_eventbridge.types.connection_header_parameter

    out: ConnectionHeaderParametersList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_eventbridge.types.connection_header_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out


def redact_sensitive(value: ConnectionHeaderParametersList) -> list[Any]:
    import capo_eventbridge.types.connection_header_parameter

    return [
        capo_eventbridge.types.connection_header_parameter.redact_sensitive(item)
        for item in value
    ]
