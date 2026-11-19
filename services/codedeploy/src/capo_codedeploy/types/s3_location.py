"""Generated from Smithy shape ``com.amazonaws.codedeploy#S3Location``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.bundle_type
    import capo_codedeploy.types.e_tag
    import capo_codedeploy.types.s3_bucket
    import capo_codedeploy.types.s3_key
    import capo_codedeploy.types.version_id


class S3Location(TypedDict, closed=True):
    bucket: NotRequired["capo_codedeploy.types.s3_bucket.S3Bucket"]
    """<p>The name of the Amazon S3 bucket where the application revision is stored.</p>"""
    key: NotRequired["capo_codedeploy.types.s3_key.S3Key"]
    """<p>The name of the Amazon S3 object that represents the bundled artifacts for the application revision.</p>"""
    bundle_type: NotRequired["capo_codedeploy.types.bundle_type.BundleType"]
    """<p>The file type of the application revision. Must be one of the following:</p> <ul> <li> <p> <code>tar</code>: A tar archive file.</p> </li> <li> <p> <code>tgz</code>: A compressed tar archive file.</p> </li> <li> <p> <code>zip</code>: A zip archive file.</p> </li> <li> <p> <code>YAML</code>: A YAML-formatted file.</p> </li> <li> <p> <code>JSON</code>: A JSON-formatted file.</p> </li> </ul>"""
    version: NotRequired["capo_codedeploy.types.version_id.VersionId"]
    """<p>A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.</p> <p>If the version is not specified, the system uses the most recent version by default.</p>"""
    e_tag: NotRequired["capo_codedeploy.types.e_tag.ETag"]
    """<p>The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.</p> <p>If the ETag is not specified as an input parameter, ETag validation of the object is skipped.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3Location) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key" in value:
        out["key"] = value["key"]
    if "bundle_type" in value:
        import capo_codedeploy.types.bundle_type

        out["bundleType"] = capo_codedeploy.types.bundle_type.serialize_aws_json_1_1(
            value["bundle_type"]
        )
    if "version" in value:
        out["version"] = value["version"]
    if "e_tag" in value:
        out["eTag"] = value["e_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("bundleType") is not None:
        import capo_codedeploy.types.bundle_type

        out["bundle_type"] = capo_codedeploy.types.bundle_type.deserialize_aws_json_1_1(
            data["bundleType"]
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("eTag") is not None:
        out["e_tag"] = data["eTag"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3Location) -> dict:
    out: dict = {}
    if "bucket" in value:
        out["bucket"] = value["bucket"]
    if "key" in value:
        out["key"] = value["key"]
    if "bundle_type" in value:
        import capo_codedeploy.types.bundle_type

        out["bundleType"] = capo_codedeploy.types.bundle_type.serialize_cbor(
            value["bundle_type"]
        )
    if "version" in value:
        out["version"] = value["version"]
    if "e_tag" in value:
        out["eTag"] = value["e_tag"]
    return out


def deserialize_cbor(data: dict) -> S3Location:
    out: S3Location = {}  # type: ignore[typeddict-item]
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    if data.get("key") is not None:
        out["key"] = data["key"]
    if data.get("bundleType") is not None:
        import capo_codedeploy.types.bundle_type

        out["bundle_type"] = capo_codedeploy.types.bundle_type.deserialize_cbor(
            data["bundleType"]
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("eTag") is not None:
        out["e_tag"] = data["eTag"]
    return out
