"""Generated from Smithy shape ``com.amazonaws.s3vectors#UpdateMetadataConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3vectors.types.index_arn


class UpdateMetadataConfigurationOutput(TypedDict, closed=True):
    index_arn: NotRequired["capo_s3vectors.types.index_arn.IndexArn"]
    """<p>The Amazon Resource Name (ARN) of the updated vector index.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMetadataConfigurationOutput) -> dict:
    out: dict = {}
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    return out


def deserialize_json(data: dict) -> UpdateMetadataConfigurationOutput:
    out: UpdateMetadataConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("indexArn") is not None:
        out["index_arn"] = data["indexArn"]
    return out
