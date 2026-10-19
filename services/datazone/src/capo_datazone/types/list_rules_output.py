"""Generated from Smithy shape ``com.amazonaws.datazone#ListRulesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.pagination_token
    import capo_datazone.types.rule_summaries


class ListRulesOutput(TypedDict, closed=True):
    items: "capo_datazone.types.rule_summaries.RuleSummaries"
    """<p>The results of the <code>ListRules</code> action.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of rules is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of rules, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListRules</code> to list the next set of rules.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.rule_summaries

    out["items"] = capo_datazone.types.rule_summaries.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRulesOutput:
    out: ListRulesOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_datazone.types.rule_summaries

        out["items"] = capo_datazone.types.rule_summaries.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListRulesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_datazone.types.rule_summaries

        out["items"] = capo_datazone.types.rule_summaries.redact_sensitive(
            value["items"]
        )
    return out
