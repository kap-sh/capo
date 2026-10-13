"""Generated from Smithy shape ``com.amazonaws.mailmanager#RowsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.row

RowsList: TypeAlias = list["capo_mailmanager.types.row.Row"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RowsList) -> list:
    import capo_mailmanager.types.row

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.row.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> RowsList:
    import capo_mailmanager.types.row

    out: RowsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.row.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: RowsList) -> list[Any]:
    import capo_mailmanager.types.row

    return [capo_mailmanager.types.row.redact_sensitive(item) for item in value]
