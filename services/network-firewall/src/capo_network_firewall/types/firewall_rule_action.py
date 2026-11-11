"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallRuleAction``."""

from typing import Literal, TypeAlias, cast

FirewallRuleAction: TypeAlias = Literal[
    "ACCEPT",
    "DROP",
    "REJECT",
    "REJECT_DST",
    "REJECT_BOTH",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallRuleAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FirewallRuleAction:
    return cast(FirewallRuleAction, data)
