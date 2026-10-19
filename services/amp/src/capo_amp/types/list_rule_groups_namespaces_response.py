"""Generated from Smithy shape ``com.amazonaws.amp#ListRuleGroupsNamespacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amp.types.pagination_token
    import capo_amp.types.rule_groups_namespace_summary_list


class ListRuleGroupsNamespacesResponse(TypedDict, closed=True):
    rule_groups_namespaces: "capo_amp.types.rule_groups_namespace_summary_list.RuleGroupsNamespaceSummaryList"
    """<p>The returned list of rule groups namespaces.</p>"""
    next_token: NotRequired["capo_amp.types.pagination_token.PaginationToken"]
    """<p>A token indicating that there are more results to retrieve. You can use this token as part of your next <code>ListRuleGroupsNamespaces</code> request to retrieve those results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRuleGroupsNamespacesResponse) -> dict:
    out: dict = {}
    import capo_amp.types.rule_groups_namespace_summary_list

    out["ruleGroupsNamespaces"] = (
        capo_amp.types.rule_groups_namespace_summary_list.serialize_json(
            value["rule_groups_namespaces"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRuleGroupsNamespacesResponse:
    out: ListRuleGroupsNamespacesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ruleGroupsNamespaces") is not None:
        import capo_amp.types.rule_groups_namespace_summary_list

        out["rule_groups_namespaces"] = (
            capo_amp.types.rule_groups_namespace_summary_list.deserialize_json(
                data["ruleGroupsNamespaces"]
            )
        )
    else:
        out["rule_groups_namespaces"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
