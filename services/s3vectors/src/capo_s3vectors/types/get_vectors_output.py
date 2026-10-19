"""Generated from Smithy shape ``com.amazonaws.s3vectors#GetVectorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.get_vectors_output_list


class GetVectorsOutput(TypedDict, closed=True):
    vectors: "capo_s3vectors.types.get_vectors_output_list.GetVectorsOutputList"
    """<p>The attributes of the vectors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVectorsOutput) -> dict:
    out: dict = {}
    import capo_s3vectors.types.get_vectors_output_list

    out["vectors"] = capo_s3vectors.types.get_vectors_output_list.serialize_json(
        value["vectors"]
    )
    return out


def deserialize_json(data: dict) -> GetVectorsOutput:
    out: GetVectorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("vectors") is not None:
        import capo_s3vectors.types.get_vectors_output_list

        out["vectors"] = capo_s3vectors.types.get_vectors_output_list.deserialize_json(
            data["vectors"]
        )
    else:
        out["vectors"] = []
    return out
