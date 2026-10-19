"""Generated from Smithy shape ``com.amazonaws.supplychain#ListDataLakeNamespacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_namespace_list
    import capo_supplychain.types.data_lake_namespace_next_token


class ListDataLakeNamespacesResponse(TypedDict, closed=True):
    namespaces: "capo_supplychain.types.data_lake_namespace_list.DataLakeNamespaceList"
    """<p>The list of fetched namespace details. Noted it only contains custom namespaces, pre-defined namespaces are not included.</p>"""
    next_token: NotRequired[
        "capo_supplychain.types.data_lake_namespace_next_token.DataLakeNamespaceNextToken"
    ]
    """<p>The pagination token to fetch next page of namespaces.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataLakeNamespacesResponse) -> dict:
    out: dict = {}
    import capo_supplychain.types.data_lake_namespace_list

    out["namespaces"] = capo_supplychain.types.data_lake_namespace_list.serialize_json(
        value["namespaces"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataLakeNamespacesResponse:
    out: ListDataLakeNamespacesResponse = {}  # type: ignore[typeddict-item]
    if data.get("namespaces") is not None:
        import capo_supplychain.types.data_lake_namespace_list

        out["namespaces"] = (
            capo_supplychain.types.data_lake_namespace_list.deserialize_json(
                data["namespaces"]
            )
        )
    else:
        out["namespaces"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
