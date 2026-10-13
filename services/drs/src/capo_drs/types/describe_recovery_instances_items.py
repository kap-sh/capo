"""Generated from Smithy shape ``com.amazonaws.drs#DescribeRecoveryInstancesItems``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.recovery_instance

DescribeRecoveryInstancesItems: TypeAlias = list[
    "capo_drs.types.recovery_instance.RecoveryInstance"
]


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecoveryInstancesItems) -> list:
    import capo_drs.types.recovery_instance

    out: list = []
    for item in value:
        out.append(capo_drs.types.recovery_instance.serialize_json(item))
    return out


def deserialize_json(data: list) -> DescribeRecoveryInstancesItems:
    import capo_drs.types.recovery_instance

    out: DescribeRecoveryInstancesItems = []
    for item in data:
        if item is None:
            continue
        out.append(capo_drs.types.recovery_instance.deserialize_json(item))
    return out


def redact_sensitive(value: DescribeRecoveryInstancesItems) -> list[Any]:
    import capo_drs.types.recovery_instance

    return [capo_drs.types.recovery_instance.redact_sensitive(item) for item in value]
