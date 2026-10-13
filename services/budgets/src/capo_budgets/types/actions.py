"""Generated from Smithy shape ``com.amazonaws.budgets#Actions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.action

Actions: TypeAlias = list["capo_budgets.types.action.Action"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Actions) -> list:
    import capo_budgets.types.action

    out: list = []
    for item in value:
        out.append(capo_budgets.types.action.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Actions:
    import capo_budgets.types.action

    out: Actions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_budgets.types.action.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Actions) -> list[Any]:
    import capo_budgets.types.action

    return [capo_budgets.types.action.redact_sensitive(item) for item in value]
