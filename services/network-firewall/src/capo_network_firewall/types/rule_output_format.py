"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleOutputFormat``."""

from typing import Literal, TypeAlias, cast

RuleOutputFormat: TypeAlias = Literal[
    "FIREWALL_RULES",
    "RULES_STRING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleOutputFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleOutputFormat:
    return cast(RuleOutputFormat, data)
