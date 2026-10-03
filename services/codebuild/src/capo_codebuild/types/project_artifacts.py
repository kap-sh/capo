"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectArtifacts``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.artifact_namespace
    import capo_codebuild.types.artifact_packaging
    import capo_codebuild.types.artifacts_type
    import capo_codebuild.types.bucket_owner_access
    import capo_codebuild.types.string
    import capo_codebuild.types.wrapper_boolean


class ProjectArtifacts(TypedDict, closed=True):
    type: "capo_codebuild.types.artifacts_type.ArtifactsType"
    """<p>The type of build output artifact. Valid values include:</p> <ul> <li> <p> <code>CODEPIPELINE</code>: The build project has build output generated through CodePipeline. </p> <note> <p>The <code>CODEPIPELINE</code> type is not supported for <code>secondaryArtifacts</code>.</p> </note> </li> <li> <p> <code>NO_ARTIFACTS</code>: The build project does not produce any build output.</p> </li> <li> <p> <code>S3</code>: The build project stores build output in Amazon S3.</p> </li> </ul>"""
    location: NotRequired["capo_codebuild.types.string.String"]
    """<p>Information about the build output artifact location:</p> <ul> <li> <p>If <code>type</code> is set to <code>CODEPIPELINE</code>, CodePipeline ignores this value if specified. This is because CodePipeline manages its build output locations instead of CodeBuild.</p> </li> <li> <p>If <code>type</code> is set to <code>NO_ARTIFACTS</code>, this value is ignored if specified, because no build output is produced.</p> </li> <li> <p>If <code>type</code> is set to <code>S3</code>, this is the name of the output bucket.</p> </li> </ul>"""
    path: NotRequired["capo_codebuild.types.string.String"]
    """<p>Along with <code>namespaceType</code> and <code>name</code>, the pattern that CodeBuild uses to name and store the output artifact:</p> <ul> <li> <p>If <code>type</code> is set to <code>CODEPIPELINE</code>, CodePipeline ignores this value if specified. This is because CodePipeline manages its build output names instead of CodeBuild.</p> </li> <li> <p>If <code>type</code> is set to <code>NO_ARTIFACTS</code>, this value is ignored if specified, because no build output is produced.</p> </li> <li> <p>If <code>type</code> is set to <code>S3</code>, this is the path to the output artifact. If <code>path</code> is not specified, <code>path</code> is not used.</p> </li> </ul> <p>For example, if <code>path</code> is set to <code>MyArtifacts</code>, <code>namespaceType</code> is set to <code>NONE</code>, and <code>name</code> is set to <code>MyArtifact.zip</code>, the output artifact is stored in the output bucket at <code>MyArtifacts/MyArtifact.zip</code>.</p>"""
    namespace_type: NotRequired[
        "capo_codebuild.types.artifact_namespace.ArtifactNamespace"
    ]
    """<p>Along with <code>path</code> and <code>name</code>, the pattern that CodeBuild uses to determine the name and location to store the output artifact:</p> <ul> <li> <p>If <code>type</code> is set to <code>CODEPIPELINE</code>, CodePipeline ignores this value if specified. This is because CodePipeline manages its build output names instead of CodeBuild.</p> </li> <li> <p>If <code>type</code> is set to <code>NO_ARTIFACTS</code>, this value is ignored if specified, because no build output is produced.</p> </li> <li> <p>If <code>type</code> is set to <code>S3</code>, valid values include:</p> <ul> <li> <p> <code>BUILD_ID</code>: Include the build ID in the location of the build output artifact.</p> </li> <li> <p> <code>NONE</code>: Do not include the build ID. This is the default if <code>namespaceType</code> is not specified.</p> </li> </ul> </li> </ul> <p>For example, if <code>path</code> is set to <code>MyArtifacts</code>, <code>namespaceType</code> is set to <code>BUILD_ID</code>, and <code>name</code> is set to <code>MyArtifact.zip</code>, the output artifact is stored in <code>MyArtifacts/<build-ID>/MyArtifact.zip</code>.</p>"""
    name: NotRequired["capo_codebuild.types.string.String"]
    """<p>Along with <code>path</code> and <code>namespaceType</code>, the pattern that CodeBuild uses to name and store the output artifact:</p> <ul> <li> <p>If <code>type</code> is set to <code>CODEPIPELINE</code>, CodePipeline ignores this value if specified. This is because CodePipeline manages its build output names instead of CodeBuild.</p> </li> <li> <p>If <code>type</code> is set to <code>NO_ARTIFACTS</code>, this value is ignored if specified, because no build output is produced.</p> </li> <li> <p>If <code>type</code> is set to <code>S3</code>, this is the name of the output artifact object. If you set the name to be a forward slash ("/"), the artifact is stored in the root of the output bucket.</p> </li> </ul> <p>For example:</p> <ul> <li> <p> If <code>path</code> is set to <code>MyArtifacts</code>, <code>namespaceType</code> is set to <code>BUILD_ID</code>, and <code>name</code> is set to <code>MyArtifact.zip</code>, then the output artifact is stored in <code>MyArtifacts/<build-ID>/MyArtifact.zip</code>. </p> </li> <li> <p> If <code>path</code> is empty, <code>namespaceType</code> is set to <code>NONE</code>, and <code>name</code> is set to "<code>/</code>", the output artifact is stored in the root of the output bucket. </p> </li> <li> <p> If <code>path</code> is set to <code>MyArtifacts</code>, <code>namespaceType</code> is set to <code>BUILD_ID</code>, and <code>name</code> is set to "<code>/</code>", the output artifact is stored in <code>MyArtifacts/<build-ID></code>. </p> </li> </ul>"""
    packaging: NotRequired["capo_codebuild.types.artifact_packaging.ArtifactPackaging"]
    """<p>The type of build output artifact to create:</p> <ul> <li> <p>If <code>type</code> is set to <code>CODEPIPELINE</code>, CodePipeline ignores this value if specified. This is because CodePipeline manages its build output artifacts instead of CodeBuild.</p> </li> <li> <p>If <code>type</code> is set to <code>NO_ARTIFACTS</code>, this value is ignored if specified, because no build output is produced.</p> </li> <li> <p>If <code>type</code> is set to <code>S3</code>, valid values include:</p> <ul> <li> <p> <code>NONE</code>: CodeBuild creates in the output bucket a folder that contains the build output. This is the default if <code>packaging</code> is not specified.</p> </li> <li> <p> <code>ZIP</code>: CodeBuild creates in the output bucket a ZIP file that contains the build output.</p> </li> </ul> </li> </ul>"""
    override_artifact_name: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p> If this flag is set, a name specified in the buildspec file overrides the artifact name. The name specified in a buildspec file is calculated at build time and uses the Shell Command Language. For example, you can append a date and time to your artifact name so that it is always unique. </p>"""
    encryption_disabled: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p> Set to true if you do not want your output artifacts encrypted. This option is valid only if your artifacts type is Amazon S3. If this is set with another artifacts type, an invalidInputException is thrown. </p>"""
    artifact_identifier: NotRequired["capo_codebuild.types.string.String"]
    """<p> An identifier for this artifact definition. </p>"""
    bucket_owner_access: NotRequired[
        "capo_codebuild.types.bucket_owner_access.BucketOwnerAccess"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectArtifacts) -> dict:
    out: dict = {}
    import capo_codebuild.types.artifacts_type

    out["type"] = capo_codebuild.types.artifacts_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "location" in value:
        out["location"] = value["location"]
    if "path" in value:
        out["path"] = value["path"]
    if "namespace_type" in value:
        import capo_codebuild.types.artifact_namespace

        out["namespaceType"] = (
            capo_codebuild.types.artifact_namespace.serialize_aws_json_1_1(
                value["namespace_type"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "packaging" in value:
        import capo_codebuild.types.artifact_packaging

        out["packaging"] = (
            capo_codebuild.types.artifact_packaging.serialize_aws_json_1_1(
                value["packaging"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> ProjectArtifacts:
    out: ProjectArtifacts = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codebuild.types.artifacts_type

        out["type"] = capo_codebuild.types.artifacts_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("ProjectArtifacts.type required")
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("path") is not None:
        out["path"] = data["path"]
    if data.get("namespaceType") is not None:
        import capo_codebuild.types.artifact_namespace

        out["namespace_type"] = (
            capo_codebuild.types.artifact_namespace.deserialize_aws_json_1_1(
                data["namespaceType"]
            )
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("packaging") is not None:
        import capo_codebuild.types.artifact_packaging

        out["packaging"] = (
            capo_codebuild.types.artifact_packaging.deserialize_aws_json_1_1(
                data["packaging"]
            )
        )
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
