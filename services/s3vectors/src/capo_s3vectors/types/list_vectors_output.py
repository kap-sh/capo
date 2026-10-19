"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListVectorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.list_vectors_next_token
    import capo_s3vectors.types.list_vectors_output_list


class ListVectorsOutput(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_s3vectors.types.list_vectors_next_token.ListVectorsNextToken"
    ]
    """<p>Pagination token to be used in the subsequent request. The field is empty if no further pagination is required.</p>"""
    vectors: "capo_s3vectors.types.list_vectors_output_list.ListVectorsOutputList"
    """<p>Vectors in the current segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVectorsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_s3vectors.types.list_vectors_output_list

    out["vectors"] = capo_s3vectors.types.list_vectors_output_list.serialize_json(
        value["vectors"]
    )
    return out


def deserialize_json(data: dict) -> ListVectorsOutput:
    out: ListVectorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("vectors") is not None:
        import capo_s3vectors.types.list_vectors_output_list

        out["vectors"] = capo_s3vectors.types.list_vectors_output_list.deserialize_json(
            data["vectors"]
        )
    else:
        out["vectors"] = []
    return out
