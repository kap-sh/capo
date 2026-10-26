"""Generated from Smithy shape ``com.amazonaws.datazone#ActionParameters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.aws_console_link_parameters


class _ActionParameters_awsConsoleLink(TypedDict, closed=True):
    awsConsoleLink: (
        "capo_datazone.types.aws_console_link_parameters.AwsConsoleLinkParameters"
    )


ActionParameters: TypeAlias = _ActionParameters_awsConsoleLink | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ActionParameters) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ActionParameters: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "awsConsoleLink" in value:
        import capo_datazone.types.aws_console_link_parameters

        return {
            "awsConsoleLink": capo_datazone.types.aws_console_link_parameters.serialize_json(
                value["awsConsoleLink"]
            )
        }
    else:
        raise SerializationError("ActionParameters: no variant present")


def deserialize_json(data: dict) -> ActionParameters:
    if data.get("awsConsoleLink") is not None:
        import capo_datazone.types.aws_console_link_parameters

        return {
            "awsConsoleLink": capo_datazone.types.aws_console_link_parameters.deserialize_json(
                data["awsConsoleLink"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ActionParameters: no recognized variant key")
