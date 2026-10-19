"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListIdNamespaceAssociationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.id_namespace_association_summary_list
    import capo_cleanrooms.types.pagination_token


class ListIdNamespaceAssociationsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The token value provided to access the next page of results.</p>"""
    id_namespace_association_summaries: "capo_cleanrooms.types.id_namespace_association_summary_list.IdNamespaceAssociationSummaryList"
    """<p>The summary information of the ID namespace associations that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdNamespaceAssociationsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanrooms.types.id_namespace_association_summary_list

    out["idNamespaceAssociationSummaries"] = (
        capo_cleanrooms.types.id_namespace_association_summary_list.serialize_json(
            value["id_namespace_association_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListIdNamespaceAssociationsOutput:
    out: ListIdNamespaceAssociationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("idNamespaceAssociationSummaries") is not None:
        import capo_cleanrooms.types.id_namespace_association_summary_list

        out["id_namespace_association_summaries"] = (
            capo_cleanrooms.types.id_namespace_association_summary_list.deserialize_json(
                data["idNamespaceAssociationSummaries"]
            )
        )
    else:
        out["id_namespace_association_summaries"] = []
    return out
