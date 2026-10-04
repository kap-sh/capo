"""Generated from Smithy shape ``com.amazonaws.securityagent#ScopeDecision``."""

from typing import Literal, TypeAlias, cast

"""<p>The scoping decision for a CI/CD pentest job, indicating whether the supplied code changes are tested.</p>"""
ScopeDecision: TypeAlias = Literal[
    "IN_SCOPE",
    "SCOPED_OUT",
    "SCOPE_CONFLICT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ScopeDecision) -> str:
    return value


def deserialize_json(data: str) -> ScopeDecision:
    return cast(ScopeDecision, data)
