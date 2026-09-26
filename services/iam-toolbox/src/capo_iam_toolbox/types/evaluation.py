"""Generated from Smithy shape ``com.amazonaws.iamtoolbox#Evaluation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam_toolbox.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam_toolbox.types.authorization_context
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
    """<p>The result of the evaluation. Valid values:</p> <ul> <li> <p> <code>ALLOW</code> - The action was allowed.</p> </li> <li> <p> <code>EXPLICIT_DENY</code> - The action was explicitly denied by a policy.</p> </li> <li> <p> <code>IMPLICIT_DENY</code> - The action was denied because no policy allowed it.</p> </li> </ul>"""
    matched_policies: NotRequired[
        "capo_iam_toolbox.types.matched_policy_list.MatchedPolicyList"
    ]
    """<p>The policies that matched during evaluation of this action and resource. An implicit denial produces no matched policies.</p>"""


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
    return out


def deserialize_json(data: dict) -> Evaluation:
    out: Evaluation = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        raise DeserializationError("Evaluation.action required")
    if data.get("resource") is not None:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError("Evaluation.resource required")
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
    return out
