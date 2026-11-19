"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#Evaluation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iam_toolbox.types.authorization_context
    import capo_iam_toolbox.types.check_list
    import capo_iam_toolbox.types.evaluated_effect
    import capo_iam_toolbox.types.matched_policy_list


class Evaluation(TypedDict, closed=True):
    action: "str"
    """<p>The action evaluated for this request (for example, <code>iam:PassRole</code>).</p>"""
    resource: "str"
    """<p>The resource that the action targeted. This is typically a resource ARN, but can be a wildcard ARN that matches multiple resources, or empty for actions that are not resource-specific.</p>"""
    context: NotRequired[
        "capo_iam_toolbox.types.authorization_context.AuthorizationContext"
    ]
    """<p>The context keys and values specific to this evaluation. These are applied on top of the request context.</p>"""
    evaluated_effect: NotRequired[
        "capo_iam_toolbox.types.evaluated_effect.EvaluatedEffect"
    ]
    """<p>The result of the evaluation. Valid values:</p> <ul> <li> <p> <code>ALLOW</code> - The action was allowed.</p> </li> <li> <p> <code>EXPLICIT_DENY</code> - The action was explicitly denied by a policy.</p> </li> <li> <p> <code>IMPLICIT_DENY</code> - The action was denied because at least one required authorization check had no matching allow statement.</p> </li> </ul>"""
    matched_policies: NotRequired[
        "capo_iam_toolbox.types.matched_policy_list.MatchedPolicyList"
    ]
    """<p> <code>matchedPolicies</code> is deprecated. Use <code>checks</code> instead. This value contains the policies that matched during evaluation of this action and resource.</p>"""
    checks: NotRequired["capo_iam_toolbox.types.check_list.CheckList"]
    """<p> <code>checks</code> contains the authorization checks that explain an evaluation result. Each check is one authorization requirement and reports its result and policies from the top-level <code>policies</code> list with matching statements. The output lists RCP checks from the organization root to the account, then SCP checks from the organization root to the account. It then lists VPC endpoint, resource, principal, permissions boundary, and session checks. When <code>checks</code> is present, an <code>EXPLICIT_DENY</code> evaluation includes an <code>EXPLICIT_DENY</code> check. When <code>checks</code> is present for an <code>IMPLICIT_DENY</code> evaluation, it includes an <code>IMPLICIT_DENY</code> check and no <code>EXPLICIT_DENY</code> check. For more information about how IAM evaluates policies, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-denyallow.html">Policy evaluation logic</a>.</p> <p> <code>PRINCIPAL</code>, <code>PERMISSIONS_BOUNDARY</code>, and <code>SESSION</code> checks appear when they apply to the principal that made the request, even if none of their policies matched. A missing allow produces <code>IMPLICIT_DENY</code>, or <code>NO_IMPACT</code> when another path already allowed the request.</p> <p>Returned when the caller is in the request principal's account or organization. The absence of <code>checks</code> does not mean no authorization checks applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Evaluation) -> dict:
    out: dict = {}
    out["action"] = value["action"]
    out["resource"] = value["resource"]
    if "context" in value:
        import capo_iam_toolbox.types.authorization_context

        out["context"] = capo_iam_toolbox.types.authorization_context.serialize_json(
            value["context"]
        )
    if "evaluated_effect" in value:
        import capo_iam_toolbox.types.evaluated_effect

        out["evaluatedEffect"] = capo_iam_toolbox.types.evaluated_effect.serialize_json(
            value["evaluated_effect"]
        )
    if "matched_policies" in value:
        import capo_iam_toolbox.types.matched_policy_list

        out["matchedPolicies"] = (
            capo_iam_toolbox.types.matched_policy_list.serialize_json(
                value["matched_policies"]
            )
        )
    if "checks" in value:
        import capo_iam_toolbox.types.check_list

        out["checks"] = capo_iam_toolbox.types.check_list.serialize_json(
            value["checks"]
        )
    return out


def deserialize_json(data: dict) -> Evaluation:
    out: Evaluation = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        out["action"] = ""
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    else:
        out["resource"] = ""
    if data.get("context") is not None:
        import capo_iam_toolbox.types.authorization_context

        out["context"] = capo_iam_toolbox.types.authorization_context.deserialize_json(
            data["context"]
        )
    if data.get("evaluatedEffect") is not None:
        import capo_iam_toolbox.types.evaluated_effect

        out["evaluated_effect"] = (
            capo_iam_toolbox.types.evaluated_effect.deserialize_json(
                data["evaluatedEffect"]
            )
        )
    if data.get("matchedPolicies") is not None:
        import capo_iam_toolbox.types.matched_policy_list

        out["matched_policies"] = (
            capo_iam_toolbox.types.matched_policy_list.deserialize_json(
                data["matchedPolicies"]
            )
        )
    if data.get("checks") is not None:
        import capo_iam_toolbox.types.check_list

        out["checks"] = capo_iam_toolbox.types.check_list.deserialize_json(
            data["checks"]
        )
    return out
