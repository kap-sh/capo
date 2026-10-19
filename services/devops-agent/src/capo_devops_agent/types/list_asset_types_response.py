"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListAssetTypesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.asset_type_list
    import capo_devops_agent.types.next_token


class ListAssetTypesResponse(TypedDict, closed=True):
    items: "capo_devops_agent.types.asset_type_list.AssetTypeList"
    """<p>The list of supported asset types</p>"""
    next_token: NotRequired["capo_devops_agent.types.next_token.NextToken"]
    """<p>Pagination token to retrieve the next page of results. Absent when there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetTypesResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.asset_type_list

    out["items"] = capo_devops_agent.types.asset_type_list.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAssetTypesResponse:
    out: ListAssetTypesResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_devops_agent.types.asset_type_list

        out["items"] = capo_devops_agent.types.asset_type_list.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
