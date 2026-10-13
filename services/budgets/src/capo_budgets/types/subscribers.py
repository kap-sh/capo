"""Generated from Smithy shape ``com.amazonaws.budgets#Subscribers``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_budgets.types.subscriber

Subscribers: TypeAlias = list["capo_budgets.types.subscriber.Subscriber"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Subscribers) -> list:
    import capo_budgets.types.subscriber

    out: list = []
    for item in value:
        out.append(capo_budgets.types.subscriber.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Subscribers:
    import capo_budgets.types.subscriber

    out: Subscribers = []
    for item in data:
        if item is None:
            continue
        out.append(capo_budgets.types.subscriber.deserialize_aws_json_1_1(item))
    return out


def redact_sensitive(value: Subscribers) -> list[Any]:
    import capo_budgets.types.subscriber

    return [capo_budgets.types.subscriber.redact_sensitive(item) for item in value]
