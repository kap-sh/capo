"""Generated from Smithy shape ``com.amazonaws.mailmanager#ListRuleSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.pagination_token
    import capo_mailmanager.types.rule_sets


class ListRuleSetsResponse(TypedDict, closed=True):
    rule_sets: "capo_mailmanager.types.rule_sets.RuleSets"
    """<p>The list of rule sets.</p>"""
    next_token: NotRequired["capo_mailmanager.types.pagination_token.PaginationToken"]
    """<p>If NextToken is returned, there are more results available. The value of NextToken is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRuleSetsResponse) -> dict:
    out: dict = {}
    import capo_mailmanager.types.rule_sets

    out["RuleSets"] = capo_mailmanager.types.rule_sets.serialize_aws_json_1_0(
        value["rule_sets"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRuleSetsResponse:
    out: ListRuleSetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("RuleSets") is not None:
        import capo_mailmanager.types.rule_sets

        out["rule_sets"] = capo_mailmanager.types.rule_sets.deserialize_aws_json_1_0(
            data["RuleSets"]
        )
    else:
        out["rule_sets"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
