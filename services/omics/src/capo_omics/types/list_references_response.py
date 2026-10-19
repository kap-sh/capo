"""Generated from Smithy shape ``com.amazonaws.omics#ListReferencesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.next_token
    import capo_omics.types.reference_list


class ListReferencesResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_omics.types.next_token.NextToken"]
    """<p>A pagination token that's included if more results are available.</p>"""
    references: "capo_omics.types.reference_list.ReferenceList"
    """<p>A list of references.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReferencesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_omics.types.reference_list

    out["references"] = capo_omics.types.reference_list.serialize_json(
        value["references"]
    )
    return out


def deserialize_json(data: dict) -> ListReferencesResponse:
    out: ListReferencesResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("references") is not None:
        import capo_omics.types.reference_list

        out["references"] = capo_omics.types.reference_list.deserialize_json(
            data["references"]
        )
    else:
        out["references"] = []
    return out
