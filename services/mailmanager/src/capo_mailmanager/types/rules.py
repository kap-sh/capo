"""Generated from Smithy shape ``com.amazonaws.mailmanager#Rules``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.rule

Rules: TypeAlias = list["capo_mailmanager.types.rule.Rule"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Rules) -> list:
    import capo_mailmanager.types.rule

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.rule.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Rules:
    import capo_mailmanager.types.rule

    out: Rules = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mailmanager.types.rule.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: Rules) -> list[Any]:
    import capo_mailmanager.types.rule

    return [capo_mailmanager.types.rule.redact_sensitive(item) for item in value]
