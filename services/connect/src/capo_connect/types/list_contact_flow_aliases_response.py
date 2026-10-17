"""Generated from Smithy shape ``com.amazonaws.connect#ListContactFlowAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_alias_summary_list
    import capo_connect.types.next_token


class ListContactFlowAliasesResponse(TypedDict, closed=True):
    contact_flow_alias_summary_list: NotRequired[
        "capo_connect.types.contact_flow_alias_summary_list.ContactFlowAliasSummaryList"
    ]
    """<p>Information about the flow aliases.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactFlowAliasesResponse) -> dict:
    out: dict = {}
    if "contact_flow_alias_summary_list" in value:
        import capo_connect.types.contact_flow_alias_summary_list

        out["ContactFlowAliasSummaryList"] = (
            capo_connect.types.contact_flow_alias_summary_list.serialize_json(
                value["contact_flow_alias_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContactFlowAliasesResponse:
    out: ListContactFlowAliasesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContactFlowAliasSummaryList") is not None:
        import capo_connect.types.contact_flow_alias_summary_list

        out["contact_flow_alias_summary_list"] = (
            capo_connect.types.contact_flow_alias_summary_list.deserialize_json(
                data["ContactFlowAliasSummaryList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
