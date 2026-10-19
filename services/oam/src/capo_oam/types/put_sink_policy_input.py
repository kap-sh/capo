"""Generated from Smithy shape ``com.amazonaws.oam#PutSinkPolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_oam.types.resource_identifier
    import capo_oam.types.sink_policy


class PutSinkPolicyInput(TypedDict, closed=True):
    sink_identifier: "capo_oam.types.resource_identifier.ResourceIdentifier"
    """<p>The ARN of the sink to attach this policy to.</p>"""
    policy: "capo_oam.types.sink_policy.SinkPolicy"
    """<p>The JSON policy to use. If you are updating an existing policy, the entire existing policy is replaced by what you specify here.</p> <p>The policy must be in JSON string format with quotation marks escaped and no newlines.</p> <p>For examples of different types of policies, see the <b>Examples</b> section on this page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutSinkPolicyInput) -> dict:
    out: dict = {}
    out["SinkIdentifier"] = value["sink_identifier"]
    out["Policy"] = value["policy"]
    return out


def deserialize_json(data: dict) -> PutSinkPolicyInput:
    out: PutSinkPolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("SinkIdentifier") is not None:
        out["sink_identifier"] = data["SinkIdentifier"]
    else:
        out["sink_identifier"] = ""
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    else:
        out["policy"] = ""
    return out
