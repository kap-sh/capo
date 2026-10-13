"""Generated from Smithy shape ``com.amazonaws.fsx#AdministrativeActions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.administrative_action

AdministrativeActions: TypeAlias = list[
    "capo_fsx.types.administrative_action.AdministrativeAction"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdministrativeActions) -> list:
    import capo_fsx.types.administrative_action

    out: list = []
    for item in value:
        out.append(capo_fsx.types.administrative_action.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AdministrativeActions:
    import capo_fsx.types.administrative_action

    out: AdministrativeActions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fsx.types.administrative_action.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: AdministrativeActions) -> list[Any]:
    import capo_fsx.types.administrative_action

    return [
        capo_fsx.types.administrative_action.redact_sensitive(item) for item in value
    ]
