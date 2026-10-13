"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#UpdateStaticPolicyDefinition``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_verifiedpermissions.errors import DeserializationError

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.policy_statement
    import capo_verifiedpermissions.types.static_policy_description


class UpdateStaticPolicyDefinition(TypedDict, closed=True):
    description: NotRequired[
        "capo_verifiedpermissions.types.static_policy_description.StaticPolicyDescription"
    ]
    """<p>Specifies the description to be added to or replaced on the static policy.</p>"""
    statement: "capo_verifiedpermissions.types.policy_statement.PolicyStatement"
    """<p>Specifies the Cedar policy language text to be added to or replaced on the static policy.</p> <important> <p>You can change only the following elements from the original content:</p> <ul> <li> <p>The <code>action</code> referenced by the policy.</p> </li> <li> <p>Any conditional clauses, such as <code>when</code> or <code>unless</code> clauses.</p> </li> </ul> <p>You <b>can't</b> change the following elements:</p> <ul> <li> <p>Changing from <code>StaticPolicy</code> to <code>TemplateLinkedPolicy</code>.</p> </li> <li> <p>The effect (<code>permit</code> or <code>forbid</code>) of the policy.</p> </li> <li> <p>The <code>principal</code> referenced by the policy.</p> </li> <li> <p>The <code>resource</code> referenced by the policy.</p> </li> </ul> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateStaticPolicyDefinition) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["statement"] = value["statement"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateStaticPolicyDefinition:
    out: UpdateStaticPolicyDefinition = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("statement") is not None:
        out["statement"] = data["statement"]
    else:
        raise DeserializationError("UpdateStaticPolicyDefinition.statement required")
    return out


def redact_sensitive(value: UpdateStaticPolicyDefinition) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "statement" in value:
        out["statement"] = "*** Sensitive Data Redacted ***"
    return out
