"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#RuleType``."""

from typing import Literal, TypeAlias, cast

"""<p>An enumerated type that determines how the evaluated rules are processed. RuleType can be one of the following:</p> <p>ATLEAST - At least N routing controls must be set. You specify N as the Threshold in the rule configuration.</p> <p>AND - All routing controls must be set. This is a shortcut for "At least N," where N is the total number of controls in the rule.</p> <p>OR - Any control must be set. This is a shortcut for "At least N," where N is 1.</p>"""
RuleType: TypeAlias = Literal[
    "ATLEAST",
    "AND",
    "OR",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleType) -> str:
    return value


def deserialize_json(data: str) -> RuleType:
    return cast(RuleType, data)
