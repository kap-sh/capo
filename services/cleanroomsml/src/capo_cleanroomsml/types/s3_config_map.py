"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#S3ConfigMap``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.s3_path


class S3ConfigMap(TypedDict, closed=True):
    s3_uri: "capo_cleanroomsml.types.s3_path.S3Path"
    """<p>The Amazon S3 location URI.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ConfigMap) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> S3ConfigMap:
    out: S3ConfigMap = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    return out
