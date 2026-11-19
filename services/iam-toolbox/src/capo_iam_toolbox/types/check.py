"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#Check``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iam_toolbox.types.check_effect
    import capo_iam_toolbox.types.check_type
    import capo_iam_toolbox.types.matched_policy_list
    import capo_iam_toolbox.types.policy_type_list


class Check(TypedDict, closed=True):
    check_type: "capo_iam_toolbox.types.check_type.CheckType"
    """<p>The type of requirement that the check evaluates. Valid values:</p> <ul> <li> <p> <code>SERVICE_CONTROL_POLICY</code> - The service control policies (SCPs) attached to one organization target, such as a root, organizational unit, or account, that apply to the principal.</p> </li> <li> <p> <code>RESOURCE_CONTROL_POLICY</code> - The resource control policies (RCPs) attached to one organization target that apply to the resource.</p> </li> <li> <p> <code>VPC_ENDPOINT</code> - The VPC endpoint policy for the endpoint through which the request passes.</p> </li> <li> <p> <code>RESOURCE</code> - The resource owner's resource-based policies, when the owner must allow the request separately, such as a cross-account request or a request to an AWS KMS key.</p> </li> <li> <p> <code>PRINCIPAL</code> - The principal's identity-based policies attached to the IAM user or role.</p> </li> <li> <p> <code>PERMISSIONS_BOUNDARY</code> - The permissions boundary on the IAM user or role.</p> </li> <li> <p> <code>SESSION</code> - The role session that made the request, decided by its session policies.</p> </li> </ul>"""
    evaluated_effect: "capo_iam_toolbox.types.check_effect.CheckEffect"
    """<p>The result of evaluating this requirement. Valid values:</p> <ul> <li> <p> <code>ALLOW</code> - A statement that applies to this check allows the request.</p> </li> <li> <p> <code>EXPLICIT_DENY</code> - A deny statement that applies to this check matches.</p> </li> <li> <p> <code>IMPLICIT_DENY</code> - The check required an allow and nothing that applies to it allows the request.</p> </li> <li> <p> <code>NO_IMPACT</code> - No statement in this check matched, and no allow was needed because another path allowed the request.</p> </li> </ul>"""
    target_arn: NotRequired["str"]
    """<p>The ARN that distinguishes this check from other checks of the same type. This value is absent when the check type alone identifies the check. For SCP and RCP checks, this is the AWS Organizations ARN of the root, organizational unit, or account that the evaluated policies are attached to.</p>"""
    relevant_policy_types: NotRequired[
        "capo_iam_toolbox.types.policy_type_list.PolicyTypeList"
    ]
    """<p>The policy types used to satisfy this check, plus the type of every policy with a statement that matched in it. <code>matchedPolicies</code> lists matching policies in the top-level <code>policies</code> list.</p>"""
    matched_policies: NotRequired[
        "capo_iam_toolbox.types.matched_policy_list.MatchedPolicyList"
    ]
    """<p>Policies in this list have statements that matched for this check. Each URI corresponds to an entry in the top-level <code>policies</code> list. Only policies in the top-level list are included. The check effect can reflect a matched policy omitted from this list, so this list can be empty even when the effect is <code>ALLOW</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Check) -> dict:
    out: dict = {}
    import capo_iam_toolbox.types.check_type

    out["checkType"] = capo_iam_toolbox.types.check_type.serialize_json(
        value["check_type"]
    )
    import capo_iam_toolbox.types.check_effect

    out["evaluatedEffect"] = capo_iam_toolbox.types.check_effect.serialize_json(
        value["evaluated_effect"]
    )
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "relevant_policy_types" in value:
        import capo_iam_toolbox.types.policy_type_list

        out["relevantPolicyTypes"] = (
            capo_iam_toolbox.types.policy_type_list.serialize_json(
                value["relevant_policy_types"]
            )
        )
    if "matched_policies" in value:
        import capo_iam_toolbox.types.matched_policy_list

        out["matchedPolicies"] = (
            capo_iam_toolbox.types.matched_policy_list.serialize_json(
                value["matched_policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> Check:
    out: Check = {}  # type: ignore[typeddict-item]
    if data.get("checkType") is not None:
        import capo_iam_toolbox.types.check_type

        out["check_type"] = capo_iam_toolbox.types.check_type.deserialize_json(
            data["checkType"]
        )
    else:
        import typing

        out["check_type"] = typing.cast(
            "capo_iam_toolbox.types.check_type.CheckType", ""
        )
    if data.get("evaluatedEffect") is not None:
        import capo_iam_toolbox.types.check_effect

        out["evaluated_effect"] = capo_iam_toolbox.types.check_effect.deserialize_json(
            data["evaluatedEffect"]
        )
    else:
        import typing

        out["evaluated_effect"] = typing.cast(
            "capo_iam_toolbox.types.check_effect.CheckEffect", ""
        )
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    if data.get("relevantPolicyTypes") is not None:
        import capo_iam_toolbox.types.policy_type_list

        out["relevant_policy_types"] = (
            capo_iam_toolbox.types.policy_type_list.deserialize_json(
                data["relevantPolicyTypes"]
            )
        )
    if data.get("matchedPolicies") is not None:
        import capo_iam_toolbox.types.matched_policy_list

        out["matched_policies"] = (
            capo_iam_toolbox.types.matched_policy_list.deserialize_json(
                data["matchedPolicies"]
            )
        )
    return out
