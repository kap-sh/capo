"""Generated from Smithy shape ``com.amazonaws.datazone#ListDataProductRevisionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.data_product_revisions
    import capo_datazone.types.pagination_token


class ListDataProductRevisionsOutput(TypedDict, closed=True):
    items: "capo_datazone.types.data_product_revisions.DataProductRevisions"
    """<p>The results of the <code>ListDataProductRevisions</code> action.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of data product revisions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of data product revisions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataProductRevisions</code> to list the next set of data product revisions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataProductRevisionsOutput) -> dict:
    out: dict = {}
    import capo_datazone.types.data_product_revisions

    out["items"] = capo_datazone.types.data_product_revisions.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataProductRevisionsOutput:
    out: ListDataProductRevisionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_datazone.types.data_product_revisions

        out["items"] = capo_datazone.types.data_product_revisions.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
