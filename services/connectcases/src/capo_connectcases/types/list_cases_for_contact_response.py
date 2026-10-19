"""Generated from Smithy shape ``com.amazonaws.connectcases#ListCasesForContactResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.case_summary_list
    import capo_connectcases.types.next_token


class ListCasesForContactResponse(TypedDict, closed=True):
    cases: "capo_connectcases.types.case_summary_list.CaseSummaryList"
    """<p>A list of Case summary information.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCasesForContactResponse) -> dict:
    out: dict = {}
    import capo_connectcases.types.case_summary_list

    out["cases"] = capo_connectcases.types.case_summary_list.serialize_json(
        value["cases"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCasesForContactResponse:
    out: ListCasesForContactResponse = {}  # type: ignore[typeddict-item]
    if data.get("cases") is not None:
        import capo_connectcases.types.case_summary_list

        out["cases"] = capo_connectcases.types.case_summary_list.deserialize_json(
            data["cases"]
        )
    else:
        out["cases"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
