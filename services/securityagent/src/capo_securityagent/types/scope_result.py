"""Generated from Smithy shape ``com.amazonaws.securityagent#ScopeResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.scope_decision


class ScopeResult(TypedDict, closed=True):
    decision: "capo_securityagent.types.scope_decision.ScopeDecision"
    """<p>The scoping decision for the job's code changes.</p>"""
    reason: "str"
    """<p>A human-readable explanation of the scoping decision.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScopeResult) -> dict:
    out: dict = {}
    import capo_securityagent.types.scope_decision

    out["decision"] = capo_securityagent.types.scope_decision.serialize_json(
        value["decision"]
    )
    out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> ScopeResult:
    out: ScopeResult = {}  # type: ignore[typeddict-item]
    if data.get("decision") is not None:
        import capo_securityagent.types.scope_decision

        out["decision"] = capo_securityagent.types.scope_decision.deserialize_json(
            data["decision"]
        )
    else:
        raise DeserializationError("ScopeResult.decision required")
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        raise DeserializationError("ScopeResult.reason required")
    return out
