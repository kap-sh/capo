"""Generated from Smithy shape ``com.amazonaws.m2#S3BatchJobIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.job_identifier


class S3BatchJobIdentifier(TypedDict, closed=True):
    bucket: "str"
    """<p>The Amazon S3 bucket that contains the batch job definitions.</p>"""
    key_prefix: NotRequired["str"]
    """<p>The key prefix that specifies the path to the folder in the S3 bucket that has the batch job definitions.</p>"""
    identifier: "capo_m2.types.job_identifier.JobIdentifier"
    """<p>Identifies the batch job definition. This identifier can also point to any batch job definition that already exists in the application or to one of the batch job definitions within the directory that is specified in <code>keyPrefix</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BatchJobIdentifier) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    import capo_m2.types.job_identifier

    out["identifier"] = capo_m2.types.job_identifier.serialize_json(value["identifier"])
    return out


def deserialize_json(data: dict) -> S3BatchJobIdentifier:
    out: S3BatchJobIdentifier = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("keyPrefix") is not None:
        out["key_prefix"] = data["keyPrefix"]
    if data.get("identifier") is not None:
        import capo_m2.types.job_identifier

        out["identifier"] = capo_m2.types.job_identifier.deserialize_json(
            data["identifier"]
        )
    else:
        import capo_m2.types._unknown

        out["identifier"] = capo_m2.types._unknown.UnknownUnionMember("")
    return out
