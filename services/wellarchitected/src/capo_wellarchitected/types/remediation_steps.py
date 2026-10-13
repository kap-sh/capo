"""Generated from Smithy shape ``com.amazonaws.wellarchitected#RemediationSteps``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_wellarchitected.types.remediation_step

RemediationSteps: TypeAlias = list[
    "capo_wellarchitected.types.remediation_step.RemediationStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: RemediationSteps) -> list:
    import capo_wellarchitected.types.remediation_step

    out: list = []
    for item in value:
        out.append(capo_wellarchitected.types.remediation_step.serialize_json(item))
    return out


def deserialize_json(data: list) -> RemediationSteps:
    import capo_wellarchitected.types.remediation_step

    out: RemediationSteps = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wellarchitected.types.remediation_step.deserialize_json(item))
    return out


def redact_sensitive(value: RemediationSteps) -> list[Any]:
    import capo_wellarchitected.types.remediation_step

    return [
        capo_wellarchitected.types.remediation_step.redact_sensitive(item)
        for item in value
    ]
