"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#S3BucketRepository``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguru_reviewer.types.name
    import capo_codeguru_reviewer.types.s3_repository_details


class S3BucketRepository(TypedDict, closed=True):
    name: "capo_codeguru_reviewer.types.name.Name"
    """<p>The name of the repository when the <code>ProviderType</code> is <code>S3Bucket</code>.</p>"""
    details: NotRequired[
        "capo_codeguru_reviewer.types.s3_repository_details.S3RepositoryDetails"
    ]
    """<p>An <code>S3RepositoryDetails</code> object that specifies the name of an S3 bucket and a <code>CodeArtifacts</code> object. The <code>CodeArtifacts</code> object includes the S3 object keys for a source code .zip file and for a build artifacts .zip file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3BucketRepository) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "details" in value:
        import capo_codeguru_reviewer.types.s3_repository_details

        out["Details"] = (
            capo_codeguru_reviewer.types.s3_repository_details.serialize_json(
                value["details"]
            )
        )
    return out


def deserialize_json(data: dict) -> S3BucketRepository:
    out: S3BucketRepository = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Details") is not None:
        import capo_codeguru_reviewer.types.s3_repository_details

        out["details"] = (
            capo_codeguru_reviewer.types.s3_repository_details.deserialize_json(
                data["Details"]
            )
        )
    return out
