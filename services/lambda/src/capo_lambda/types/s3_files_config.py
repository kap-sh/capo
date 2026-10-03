"""Generated from Smithy shape ``com.amazonaws.lambda#S3FilesConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.direct_s3_read


class S3FilesConfig(TypedDict, closed=True):
    direct_s3_read: NotRequired["capo_lambda.types.direct_s3_read.DirectS3Read"]
    """<p>Specifies if a function reads from the file system for the lowest latency, or through Amazon S3 Files feature "direct Amazon S3 bucket reads" for the highest throughput. Valid values:</p> <ul> <li> <p> <code>AUTO</code> (default) – Direct reads are active for functions you configure with 512 MB or more of memory.</p> </li> <li> <p> <code>ENABLED</code> – Enforces all reads are directly from the Amazon S3 bucket, regardless of available memory (less than 512 MB).</p> </li> <li> <p> <code>DISABLED</code> – Routes all reads through the file system, regardless of memory configuration.</p> </li> </ul> <p>To use direct reads, you must grant the execution role the <code>s3:GetObject</code> and <code>s3:GetObjectVersion</code> permissions. If a direct read fails, Lambda automatically falls back to reading through the file system.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3FilesConfig) -> dict:
    out: dict = {}
    if "direct_s3_read" in value:
        import capo_lambda.types.direct_s3_read

        out["DirectS3Read"] = capo_lambda.types.direct_s3_read.serialize_json(
            value["direct_s3_read"]
        )
    return out


def deserialize_json(data: dict) -> S3FilesConfig:
    out: S3FilesConfig = {}  # type: ignore[typeddict-item]
    if data.get("DirectS3Read") is not None:
        import capo_lambda.types.direct_s3_read

        out["direct_s3_read"] = capo_lambda.types.direct_s3_read.deserialize_json(
            data["DirectS3Read"]
        )
    return out
