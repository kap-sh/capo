"""Generated from Smithy shape ``com.amazonaws.iam#ResourceSpecificResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.context_key_names_result_list_type
    import capo_iam.types.eval_decision_details_type
    import capo_iam.types.permissions_boundary_decision_detail
    import capo_iam.types.policy_evaluation_decision_type
    import capo_iam.types.resource_name_type
    import capo_iam.types.statement_list_type


class ResourceSpecificResult(TypedDict, closed=True):
    eval_resource_name: "capo_iam.types.resource_name_type.ResourceNameType"
    """<p>The name of the simulated resource, in Amazon Resource Name (ARN) format.</p>"""
    eval_resource_decision: (
        "capo_iam.types.policy_evaluation_decision_type.PolicyEvaluationDecisionType"
    )
    """<p>The result of the simulation of the simulated API operation on the resource specified in <code>EvalResourceName</code>.</p>"""
    matched_statements: NotRequired[
        "capo_iam.types.statement_list_type.StatementListType"
    ]
    """<p>A list of the statements in the input policies that determine the result for this part of the simulation. Remember that even if multiple statements allow the operation on the resource, if <i>any</i> statement denies that operation, then the explicit deny overrides any allow. In addition, the deny statement is the only entry included in the result.</p>"""
    missing_context_values: NotRequired[
        "capo_iam.types.context_key_names_result_list_type.ContextKeyNamesResultListType"
    ]
    """<p>A list of context keys that are required by the included input policies but that were not provided by one of the input parameters. This list is used when a list of ARNs is included in the <code>ResourceArns</code> parameter instead of "*". If you do not specify individual resources, by setting <code>ResourceArns</code> to "*" or by not including the <code>ResourceArns</code> parameter, then any missing context values are instead included under the <code>EvaluationResults</code> section. To discover the context keys used by a set of policies, you can call <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetContextKeysForCustomPolicy.html">GetContextKeysForCustomPolicy</a> or <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetContextKeysForPrincipalPolicy.html">GetContextKeysForPrincipalPolicy</a>.</p>"""
    eval_decision_details: NotRequired[
        "capo_iam.types.eval_decision_details_type.EvalDecisionDetailsType"
    ]
    """<p>Additional details about the results of the evaluation decision on a single resource. This parameter is returned only for cross-account simulations. This parameter explains how each policy type contributes to the resource-specific evaluation decision.</p>"""
    permissions_boundary_decision_detail: NotRequired[
        "capo_iam.types.permissions_boundary_decision_detail.PermissionsBoundaryDecisionDetail"
    ]
    """<p>Contains information about the effect that a permissions boundary has on a policy simulation when that boundary is applied to an IAM entity.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceSpecificResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}EvalResourceName", str(value["eval_resource_name"])))
    import capo_iam.types.policy_evaluation_decision_type

    capo_iam.types.policy_evaluation_decision_type.serialize_query(
        value["eval_resource_decision"], pairs, f"{key_prefix}EvalResourceDecision"
    )
    if "matched_statements" in value:
        import capo_iam.types.statement_list_type

        capo_iam.types.statement_list_type.serialize_query(
            value["matched_statements"], pairs, f"{key_prefix}MatchedStatements"
        )
    if "missing_context_values" in value:
        import capo_iam.types.context_key_names_result_list_type

        capo_iam.types.context_key_names_result_list_type.serialize_query(
            value["missing_context_values"], pairs, f"{key_prefix}MissingContextValues"
        )
    if "eval_decision_details" in value:
        import capo_iam.types.eval_decision_details_type

        capo_iam.types.eval_decision_details_type.serialize_query(
            value["eval_decision_details"], pairs, f"{key_prefix}EvalDecisionDetails"
        )
    if "permissions_boundary_decision_detail" in value:
        import capo_iam.types.permissions_boundary_decision_detail

        capo_iam.types.permissions_boundary_decision_detail.serialize_query(
            value["permissions_boundary_decision_detail"],
            pairs,
            f"{key_prefix}PermissionsBoundaryDecisionDetail",
        )


def deserialize_query(el: Element) -> ResourceSpecificResult:
    out: ResourceSpecificResult = {}  # type: ignore[typeddict-item]
    child_eval_resource_name = el.find("EvalResourceName")
    if child_eval_resource_name is not None:
        out["eval_resource_name"] = str(child_eval_resource_name.text or "")
    else:
        raise DeserializationError("ResourceSpecificResult.eval_resource_name required")
    child_eval_resource_decision = el.find("EvalResourceDecision")
    if child_eval_resource_decision is not None:
        import capo_iam.types.policy_evaluation_decision_type

        out["eval_resource_decision"] = (
            capo_iam.types.policy_evaluation_decision_type.deserialize_query(
                child_eval_resource_decision
            )
        )
    else:
        raise DeserializationError(
            "ResourceSpecificResult.eval_resource_decision required"
        )
    child_matched_statements = el.find("MatchedStatements")
    if child_matched_statements is not None:
        import capo_iam.types.statement_list_type

        out["matched_statements"] = (
            capo_iam.types.statement_list_type.deserialize_query(
                child_matched_statements
            )
        )
    child_missing_context_values = el.find("MissingContextValues")
    if child_missing_context_values is not None:
        import capo_iam.types.context_key_names_result_list_type

        out["missing_context_values"] = (
            capo_iam.types.context_key_names_result_list_type.deserialize_query(
                child_missing_context_values
            )
        )
    child_eval_decision_details = el.find("EvalDecisionDetails")
    if child_eval_decision_details is not None:
        import capo_iam.types.eval_decision_details_type

        out["eval_decision_details"] = (
            capo_iam.types.eval_decision_details_type.deserialize_query(
                child_eval_decision_details
            )
        )
    child_permissions_boundary_decision_detail = el.find(
        "PermissionsBoundaryDecisionDetail"
    )
    if child_permissions_boundary_decision_detail is not None:
        import capo_iam.types.permissions_boundary_decision_detail

        out["permissions_boundary_decision_detail"] = (
            capo_iam.types.permissions_boundary_decision_detail.deserialize_query(
                child_permissions_boundary_decision_detail
            )
        )
    return out
