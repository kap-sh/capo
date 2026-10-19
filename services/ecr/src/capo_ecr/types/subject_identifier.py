"""Generated from Smithy shape ``com.amazonaws.ecr#SubjectIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.image_digest


class SubjectIdentifier(TypedDict, closed=True):
    image_digest: "capo_ecr.types.image_digest.ImageDigest"
    """<p>The digest of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubjectIdentifier) -> dict:
    out: dict = {}
    out["imageDigest"] = value["image_digest"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubjectIdentifier:
    out: SubjectIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("imageDigest") is not None:
        out["image_digest"] = data["imageDigest"]
    else:
        out["image_digest"] = ""
    return out
