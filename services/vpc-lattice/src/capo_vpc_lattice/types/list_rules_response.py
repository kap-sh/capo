"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.rule_summary_list


class ListRulesResponse(TypedDict, closed=True):
    items: "capo_vpc_lattice.types.rule_summary_list.RuleSummaryList"
    """<p>Information about the rules.</p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRulesResponse) -> dict:
    out: dict = {}
    import capo_vpc_lattice.types.rule_summary_list

    out["items"] = capo_vpc_lattice.types.rule_summary_list.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRulesResponse:
    out: ListRulesResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_vpc_lattice.types.rule_summary_list

        out["items"] = capo_vpc_lattice.types.rule_summary_list.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
