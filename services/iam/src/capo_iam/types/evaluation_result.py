"""Generated from Smithy shape ``com.amazonaws.iam#EvaluationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iam.types.action_name_type
    import capo_iam.types.context_key_names_result_list_type
    import capo_iam.types.eval_decision_details_type
    import capo_iam.types.organizations_decision_detail
    import capo_iam.types.permissions_boundary_decision_detail
    import capo_iam.types.policy_evaluation_decision_type
    import capo_iam.types.resource_name_type
    import capo_iam.types.resource_specific_result_list_type
    import capo_iam.types.statement_list_type


class EvaluationResult(TypedDict, closed=True):
    eval_action_name: "capo_iam.types.action_name_type.ActionNameType"
    """<p>The name of the API operation tested on the indicated resource.</p>"""
    eval_resource_name: NotRequired[
        "capo_iam.types.resource_name_type.ResourceNameType"
    ]
    """<p>The ARN template for the simulated resource type (for example, <code>arn:${Partition}:s3:::${BucketName}/${KeyName}</code>), or <code>*</code> if no ARN format is defined for the action. This is not a specific customer-provided resource ARN. To find the decision for a specific resource, use <code>ResourceSpecificResults</code>.</p> <note> <p>If you previously relied on <code>EvalResourceName</code> to identify which specific resource a result applies to, you must now use the <code>EvalResourceName</code> field within individual entries in <code>ResourceSpecificResults</code> instead.</p> </note>"""
    eval_decision: (
        "capo_iam.types.policy_evaluation_decision_type.PolicyEvaluationDecisionType"
    )
    """<p>The result of the simulation.</p>"""
    matched_statements: NotRequired[
        "capo_iam.types.statement_list_type.StatementListType"
    ]
    """<p>A list of the statements in the input policies that determine the result for this scenario. Remember that even if multiple statements allow the operation on the resource, if only one statement denies that operation, then the explicit deny overrides any allow. In addition, the deny statement is the only entry included in the result.</p> <p>In the top-level result, this field contains the union of matched statements across all requested resources. Only statements that contributed to the reported decision are included. For per-resource matched statements, see <code>ResourceSpecificResults</code>. This field doesn't include statements from service control policies (SCPs). Only statements from identity-based and resource-based policies appear here.</p>"""
    missing_context_values: NotRequired[
        "capo_iam.types.context_key_names_result_list_type.ContextKeyNamesResultListType"
    ]
    """<p>A list of context keys that are required by the included input policies but that were not provided by one of the input parameters. This list is used when the resource in a simulation is "*", either explicitly, or when the <code>ResourceArns</code> parameter blank. If you include a list of resources, then any missing context values are instead included under the <code>ResourceSpecificResults</code> section. To discover the context keys used by a set of policies, you can call <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetContextKeysForCustomPolicy.html">GetContextKeysForCustomPolicy</a> or <a href="https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetContextKeysForPrincipalPolicy.html">GetContextKeysForPrincipalPolicy</a>.</p> <p>In the top-level result, this field contains the deduplicated set of missing context values across all requested resources. This field doesn't include context keys referenced by service control policies (SCPs). Only context keys referenced by identity-based and resource-based policies appear here.</p>"""
    organizations_decision_detail: NotRequired[
        "capo_iam.types.organizations_decision_detail.OrganizationsDecisionDetail"
    ]
    """<p>A structure that details how Organizations and its service control policies affect the results of the simulation. Only applies if the simulated user's account is part of an organization.</p> <p>For resources that don't support organization-level evaluation, this field is omitted from the top-level result. For per-resource details, see <code>ResourceSpecificResults</code>.</p>"""
    permissions_boundary_decision_detail: NotRequired[
        "capo_iam.types.permissions_boundary_decision_detail.PermissionsBoundaryDecisionDetail"
    ]
    """<p>Contains information about the effect that a permissions boundary has on a policy simulation when the boundary is applied to an IAM entity.</p>"""
    eval_decision_details: NotRequired[
        "capo_iam.types.eval_decision_details_type.EvalDecisionDetailsType"
    ]
    """<p>Additional details about the results of the cross-account evaluation decision. This parameter is populated for only cross-account simulations. It contains a brief summary of how each policy type contributes to the final evaluation decision.</p> <p>In the top-level result, this map reports the most restrictive decision per policy type across all requested resources.</p> <p>If the simulation evaluates policies within the same account and includes a resource ARN, then the parameter is present but the response is empty. If the simulation evaluates policies within the same account and specifies all resources (<code>*</code>), then the parameter is not returned.</p> <p>When you make a cross-account request, Amazon Web Services evaluates the request in the trusting account and the trusted account. The request is allowed only if both evaluations return <code>true</code>. For more information about how policies are evaluated, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policy-eval-basics">Evaluating policies within a single account</a>.</p> <p>If an Organizations SCP included in the evaluation denies access, the simulation ends. In this case, policy evaluation does not proceed any further and this parameter is not returned.</p>"""
    resource_specific_results: NotRequired[
        "capo_iam.types.resource_specific_result_list_type.ResourceSpecificResultListType"
    ]
    """<p>The individual results of the simulation of the API operation specified in EvalActionName on each resource.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EvaluationResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}EvalActionName", str(value["eval_action_name"])))
    if "eval_resource_name" in value:
        pairs.append(
            (f"{key_prefix}EvalResourceName", str(value["eval_resource_name"]))
        )
    import capo_iam.types.policy_evaluation_decision_type

    capo_iam.types.policy_evaluation_decision_type.serialize_query(
        value["eval_decision"], pairs, f"{key_prefix}EvalDecision"
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
    if "organizations_decision_detail" in value:
        import capo_iam.types.organizations_decision_detail

        capo_iam.types.organizations_decision_detail.serialize_query(
            value["organizations_decision_detail"],
            pairs,
            f"{key_prefix}OrganizationsDecisionDetail",
        )
    if "permissions_boundary_decision_detail" in value:
        import capo_iam.types.permissions_boundary_decision_detail

        capo_iam.types.permissions_boundary_decision_detail.serialize_query(
            value["permissions_boundary_decision_detail"],
            pairs,
            f"{key_prefix}PermissionsBoundaryDecisionDetail",
        )
    if "eval_decision_details" in value:
        import capo_iam.types.eval_decision_details_type

        capo_iam.types.eval_decision_details_type.serialize_query(
            value["eval_decision_details"], pairs, f"{key_prefix}EvalDecisionDetails"
        )
    if "resource_specific_results" in value:
        import capo_iam.types.resource_specific_result_list_type

        capo_iam.types.resource_specific_result_list_type.serialize_query(
            value["resource_specific_results"],
            pairs,
            f"{key_prefix}ResourceSpecificResults",
        )


def deserialize_query(el: Element) -> EvaluationResult:
    out: EvaluationResult = {}  # type: ignore[typeddict-item]
    child_eval_action_name = el.find("EvalActionName")
    if child_eval_action_name is not None:
        out["eval_action_name"] = str(child_eval_action_name.text or "")
    else:
        raise DeserializationError("EvaluationResult.eval_action_name required")
    child_eval_resource_name = el.find("EvalResourceName")
    if child_eval_resource_name is not None:
        out["eval_resource_name"] = str(child_eval_resource_name.text or "")
    child_eval_decision = el.find("EvalDecision")
    if child_eval_decision is not None:
        import capo_iam.types.policy_evaluation_decision_type

        out["eval_decision"] = (
            capo_iam.types.policy_evaluation_decision_type.deserialize_query(
                child_eval_decision
            )
        )
    else:
        raise DeserializationError("EvaluationResult.eval_decision required")
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
    child_organizations_decision_detail = el.find("OrganizationsDecisionDetail")
    if child_organizations_decision_detail is not None:
        import capo_iam.types.organizations_decision_detail

        out["organizations_decision_detail"] = (
            capo_iam.types.organizations_decision_detail.deserialize_query(
                child_organizations_decision_detail
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
    child_eval_decision_details = el.find("EvalDecisionDetails")
    if child_eval_decision_details is not None:
        import capo_iam.types.eval_decision_details_type

        out["eval_decision_details"] = (
            capo_iam.types.eval_decision_details_type.deserialize_query(
                child_eval_decision_details
            )
        )
    child_resource_specific_results = el.find("ResourceSpecificResults")
    if child_resource_specific_results is not None:
        import capo_iam.types.resource_specific_result_list_type

        out["resource_specific_results"] = (
            capo_iam.types.resource_specific_result_list_type.deserialize_query(
                child_resource_specific_results
            )
        )
    return out
