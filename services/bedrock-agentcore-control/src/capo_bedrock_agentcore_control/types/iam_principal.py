"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#IamPrincipal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.iam_principal_arn
    import capo_bedrock_agentcore_control.types.principal_match_operator


class IamPrincipal(TypedDict, closed=True):
    arn: "capo_bedrock_agentcore_control.types.iam_principal_arn.IamPrincipalArn"
    """<p>The Amazon Resource Name (ARN) of the IAM principal. Supports user, role, and assumed-role ARNs. Wildcards can be used with the <code>StringLike</code> operator.</p>"""
    operator: NotRequired[
        "capo_bedrock_agentcore_control.types.principal_match_operator.PrincipalMatchOperator"
    ]
    """<p>The match operator. <code>StringEquals</code> requires an exact match. <code>StringLike</code> supports wildcard patterns using <code>*</code> and <code>?</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamPrincipal) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "operator" in value:
        import capo_bedrock_agentcore_control.types.principal_match_operator

        out["operator"] = (
            capo_bedrock_agentcore_control.types.principal_match_operator.serialize_json(
                value["operator"]
            )
        )
    return out


def deserialize_json(data: dict) -> IamPrincipal:
    out: IamPrincipal = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("operator") is not None:
        import capo_bedrock_agentcore_control.types.principal_match_operator

        out["operator"] = (
            capo_bedrock_agentcore_control.types.principal_match_operator.deserialize_json(
                data["operator"]
            )
        )
    return out
