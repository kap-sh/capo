"""Generated from Smithy shape ``com.amazonaws.pi#ResponsePartitionKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pi.types.dimension_map


class ResponsePartitionKey(TypedDict, closed=True):
    dimensions: "capo_pi.types.dimension_map.DimensionMap"
    """<p>A dimension map that contains the dimensions for this partition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponsePartitionKey) -> dict:
    out: dict = {}
    import capo_pi.types.dimension_map

    out["Dimensions"] = capo_pi.types.dimension_map.serialize_aws_json_1_1(
        value["dimensions"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponsePartitionKey:
    out: ResponsePartitionKey = {}  # type: ignore[typeddict-item]
    if data.get("Dimensions") is not None:
        import capo_pi.types.dimension_map

        out["dimensions"] = capo_pi.types.dimension_map.deserialize_aws_json_1_1(
            data["Dimensions"]
        )
    else:
        out["dimensions"] = {}
    return out
