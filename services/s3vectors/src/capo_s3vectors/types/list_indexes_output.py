"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListIndexesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.list_indexes_next_token
    import capo_s3vectors.types.list_indexes_output_list


class ListIndexesOutput(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_s3vectors.types.list_indexes_next_token.ListIndexesNextToken"
    ]
    """<p>The next pagination token.</p>"""
    indexes: "capo_s3vectors.types.list_indexes_output_list.ListIndexesOutputList"
    """<p>The attributes of the vector indexes</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndexesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_s3vectors.types.list_indexes_output_list

    out["indexes"] = capo_s3vectors.types.list_indexes_output_list.serialize_json(
        value["indexes"]
    )
    return out


def deserialize_json(data: dict) -> ListIndexesOutput:
    out: ListIndexesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("indexes") is not None:
        import capo_s3vectors.types.list_indexes_output_list

        out["indexes"] = capo_s3vectors.types.list_indexes_output_list.deserialize_json(
            data["indexes"]
        )
    else:
        out["indexes"] = []
    return out
