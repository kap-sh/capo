"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#StaticPolicyDefinition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_statement
    import capo_verifiedpermissions.types.static_policy_description


class StaticPolicyDefinition(TypedDict, closed=True):
    description: NotRequired[
        "capo_verifiedpermissions.types.static_policy_description.StaticPolicyDescription"
    ]
    """<p>The description of the static policy.</p>"""
    statement: "capo_verifiedpermissions.types.policy_statement.PolicyStatement"
    """<p>The policy content of the static policy, written in the Cedar policy language.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StaticPolicyDefinition) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["statement"] = value["statement"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StaticPolicyDefinition:
    out: StaticPolicyDefinition = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("statement") is not None:
        out["statement"] = data["statement"]
    else:
        out["statement"] = ""
    return out


def redact_sensitive(value: StaticPolicyDefinition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "statement" in value:
        out["statement"] = "*** Sensitive Data Redacted ***"
    return out
