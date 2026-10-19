"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ListIndexesForMembersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.account_id_list


class ListIndexesForMembersInput(TypedDict, closed=True):
    account_id_list: "capo_resource_explorer_2.types.account_id_list.AccountIdList"
    """<p>The account IDs will limit the output to only indexes from these accounts.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value appropriate to the operation. If additional items exist beyond those included in the current response, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results.</p> <note> <p>An API operation can return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p> </note>"""
    next_token: NotRequired["str"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value of the previous call's <code>NextToken</code> response to indicate where the output should continue from. The pagination tokens expire after 24 hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndexesForMembersInput) -> dict:
    out: dict = {}
    import capo_resource_explorer_2.types.account_id_list

    out["AccountIdList"] = (
        capo_resource_explorer_2.types.account_id_list.serialize_json(
            value["account_id_list"]
        )
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIndexesForMembersInput:
    out: ListIndexesForMembersInput = {}  # type: ignore[typeddict-item]
    if data.get("AccountIdList") is not None:
        import capo_resource_explorer_2.types.account_id_list

        out["account_id_list"] = (
            capo_resource_explorer_2.types.account_id_list.deserialize_json(
                data["AccountIdList"]
            )
        )
    else:
        out["account_id_list"] = []
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
