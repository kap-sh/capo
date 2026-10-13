"""Generated from Smithy shape ``com.amazonaws.proton#OutputsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.output

OutputsList: TypeAlias = list["capo_proton.types.output.Output"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutputsList) -> list:
    import capo_proton.types.output

    out: list = []
    for item in value:
        out.append(capo_proton.types.output.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> OutputsList:
    import capo_proton.types.output

    out: OutputsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_proton.types.output.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: OutputsList) -> list[Any]:
    return ["*** Sensitive Data Redacted ***"] * len(value)
