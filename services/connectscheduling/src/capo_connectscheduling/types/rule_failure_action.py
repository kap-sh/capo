"""Generated from Smithy shape ``com.amazonaws.connectscheduling#RuleFailureAction``."""

from typing import Literal, TypeAlias, cast

"""<p>Controls what happens when a configured rule fails during rule evaluation. <code>REJECT</code> records the failure as an <code>ERROR</code> and ends the request <code>REJECTED</code>. <code>OVERRIDE</code> records it as a <code>WARNING</code> and ends the request <code>APPROVED</code>.</p>"""
RuleFailureAction: TypeAlias = Literal[
    "REJECT",
    "OVERRIDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleFailureAction) -> str:
    return value


def deserialize_json(data: str) -> RuleFailureAction:
    return cast(RuleFailureAction, data)
