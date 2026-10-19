"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationRulePreviewSummariesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.criteria
    import capo_compute_optimizer_automation.types.next_token
    import capo_compute_optimizer_automation.types.organization_scope
    import capo_compute_optimizer_automation.types.recommended_action_type_list
    import capo_compute_optimizer_automation.types.rule_type


class ListAutomationRulePreviewSummariesRequest(TypedDict, closed=True):
    rule_type: "capo_compute_optimizer_automation.types.rule_type.RuleType"
    """<p>The type of rule.</p>"""
    organization_scope: NotRequired[
        "capo_compute_optimizer_automation.types.organization_scope.OrganizationScope"
    ]
    """<p>The organizational scope for the rule preview.</p>"""
    recommended_action_types: "capo_compute_optimizer_automation.types.recommended_action_type_list.RecommendedActionTypeList"
    """<p>The types of recommended actions to include in the preview.</p>"""
    criteria: NotRequired["capo_compute_optimizer_automation.types.criteria.Criteria"]
    max_results: NotRequired["int"]
    """<p>The maximum number of automation rule preview summaries to return in a single response. Valid range is 1-1000.</p>"""
    next_token: NotRequired[
        "capo_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination to retrieve the next set of results when the response is truncated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationRulePreviewSummariesRequest) -> dict:
    out: dict = {}
    import capo_compute_optimizer_automation.types.rule_type

    out["ruleType"] = (
        capo_compute_optimizer_automation.types.rule_type.serialize_aws_json_1_0(
            value["rule_type"]
        )
    )
    if "organization_scope" in value:
        import capo_compute_optimizer_automation.types.organization_scope

        out["organizationScope"] = (
            capo_compute_optimizer_automation.types.organization_scope.serialize_aws_json_1_0(
                value["organization_scope"]
            )
        )
    import capo_compute_optimizer_automation.types.recommended_action_type_list

    out["recommendedActionTypes"] = (
        capo_compute_optimizer_automation.types.recommended_action_type_list.serialize_aws_json_1_0(
            value["recommended_action_types"]
        )
    )
    if "criteria" in value:
        import capo_compute_optimizer_automation.types.criteria

        out["criteria"] = (
            capo_compute_optimizer_automation.types.criteria.serialize_aws_json_1_0(
                value["criteria"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationRulePreviewSummariesRequest:
    out: ListAutomationRulePreviewSummariesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ruleType") is not None:
        import capo_compute_optimizer_automation.types.rule_type

        out["rule_type"] = (
            capo_compute_optimizer_automation.types.rule_type.deserialize_aws_json_1_0(
                data["ruleType"]
            )
        )
    else:
        import typing

        out["rule_type"] = typing.cast(
            "capo_compute_optimizer_automation.types.rule_type.RuleType", ""
        )
    if data.get("organizationScope") is not None:
        import capo_compute_optimizer_automation.types.organization_scope

        out["organization_scope"] = (
            capo_compute_optimizer_automation.types.organization_scope.deserialize_aws_json_1_0(
                data["organizationScope"]
            )
        )
    if data.get("recommendedActionTypes") is not None:
        import capo_compute_optimizer_automation.types.recommended_action_type_list

        out["recommended_action_types"] = (
            capo_compute_optimizer_automation.types.recommended_action_type_list.deserialize_aws_json_1_0(
                data["recommendedActionTypes"]
            )
        )
    else:
        out["recommended_action_types"] = []
    if data.get("criteria") is not None:
        import capo_compute_optimizer_automation.types.criteria

        out["criteria"] = (
            capo_compute_optimizer_automation.types.criteria.deserialize_aws_json_1_0(
                data["criteria"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
