"""Generated from Smithy shape ``com.amazonaws.ssm#CommandList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.command

CommandList: TypeAlias = list["capo_ssm.types.command.Command"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommandList) -> list:
    import capo_ssm.types.command

    out: list = []
    for item in value:
        out.append(capo_ssm.types.command.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CommandList:
    import capo_ssm.types.command

    out: CommandList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ssm.types.command.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: CommandList) -> list[Any]:
    import capo_ssm.types.command

    return [capo_ssm.types.command.redact_sensitive(item) for item in value]
