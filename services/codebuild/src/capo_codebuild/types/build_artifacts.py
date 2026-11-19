"""Generated from Smithy shape ``com.amazonaws.codebuild#BuildArtifacts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.bucket_owner_access
    import capo_codebuild.types.string
    import capo_codebuild.types.wrapper_boolean


class BuildArtifacts(TypedDict, closed=True):
    location: NotRequired["capo_codebuild.types.string.String"]
    """<p>Information about the location of the build artifacts.</p>"""
    sha256sum: NotRequired["capo_codebuild.types.string.String"]
    """<p>The SHA-256 hash of the build artifact.</p> <p>You can use this hash along with a checksum tool to confirm file integrity and authenticity.</p> <note> <p>This value is available only if the build project's <code>packaging</code> value is set to <code>ZIP</code>.</p> </note>"""
    md5sum: NotRequired["capo_codebuild.types.string.String"]
    """<p>The MD5 hash of the build artifact.</p> <p>You can use this hash along with a checksum tool to confirm file integrity and authenticity.</p> <note> <p>This value is available only if the build project's <code>packaging</code> value is set to <code>ZIP</code>.</p> </note>"""
    override_artifact_name: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p> If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. </p>"""
    encryption_disabled: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p> Information that tells you if encryption for build artifacts is disabled. </p>"""
    artifact_identifier: NotRequired["capo_codebuild.types.string.String"]
    """<p> An identifier for this artifact definition. </p>"""
    bucket_owner_access: NotRequired[
        "capo_codebuild.types.bucket_owner_access.BucketOwnerAccess"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BuildArtifacts) -> dict:
    out: dict = {}
    if "location" in value:
        out["location"] = value["location"]
    if "sha256sum" in value:
        out["sha256sum"] = value["sha256sum"]
    if "md5sum" in value:
        out["md5sum"] = value["md5sum"]
    if "override_artifact_name" in value:
        out["overrideArtifactName"] = value["override_artifact_name"]
    if "encryption_disabled" in value:
        out["encryptionDisabled"] = value["encryption_disabled"]
    if "artifact_identifier" in value:
        out["artifactIdentifier"] = value["artifact_identifier"]
    if "bucket_owner_access" in value:
        import capo_codebuild.types.bucket_owner_access

        out["bucketOwnerAccess"] = (
            capo_codebuild.types.bucket_owner_access.serialize_aws_json_1_1(
                value["bucket_owner_access"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BuildArtifacts:
    out: BuildArtifacts = {}  # type: ignore[typeddict-item]
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("sha256sum") is not None:
        out["sha256sum"] = data["sha256sum"]
    if data.get("md5sum") is not None:
        out["md5sum"] = data["md5sum"]
    if data.get("overrideArtifactName") is not None:
        out["override_artifact_name"] = data["overrideArtifactName"]
    if data.get("encryptionDisabled") is not None:
        out["encryption_disabled"] = data["encryptionDisabled"]
    if data.get("artifactIdentifier") is not None:
        out["artifact_identifier"] = data["artifactIdentifier"]
    if data.get("bucketOwnerAccess") is not None:
        import capo_codebuild.types.bucket_owner_access

        out["bucket_owner_access"] = (
            capo_codebuild.types.bucket_owner_access.deserialize_aws_json_1_1(
                data["bucketOwnerAccess"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BuildArtifacts) -> dict:
    out: dict = {}
    if "location" in value:
        out["location"] = value["location"]
    if "sha256sum" in value:
        out["sha256sum"] = value["sha256sum"]
    if "md5sum" in value:
        out["md5sum"] = value["md5sum"]
    if "override_artifact_name" in value:
        out["overrideArtifactName"] = value["override_artifact_name"]
    if "encryption_disabled" in value:
        out["encryptionDisabled"] = value["encryption_disabled"]
    if "artifact_identifier" in value:
        out["artifactIdentifier"] = value["artifact_identifier"]
    if "bucket_owner_access" in value:
        import capo_codebuild.types.bucket_owner_access

        out["bucketOwnerAccess"] = (
            capo_codebuild.types.bucket_owner_access.serialize_cbor(
                value["bucket_owner_access"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BuildArtifacts:
    out: BuildArtifacts = {}  # type: ignore[typeddict-item]
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("sha256sum") is not None:
        out["sha256sum"] = data["sha256sum"]
    if data.get("md5sum") is not None:
        out["md5sum"] = data["md5sum"]
    if data.get("overrideArtifactName") is not None:
        out["override_artifact_name"] = data["overrideArtifactName"]
    if data.get("encryptionDisabled") is not None:
        out["encryption_disabled"] = data["encryptionDisabled"]
    if data.get("artifactIdentifier") is not None:
        out["artifact_identifier"] = data["artifactIdentifier"]
    if data.get("bucketOwnerAccess") is not None:
        import capo_codebuild.types.bucket_owner_access

        out["bucket_owner_access"] = (
            capo_codebuild.types.bucket_owner_access.deserialize_cbor(
                data["bucketOwnerAccess"]
            )
        )
    return out
