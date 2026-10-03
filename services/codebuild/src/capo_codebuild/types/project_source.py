"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.build_status_config
    import capo_codebuild.types.git_clone_depth
    import capo_codebuild.types.git_submodules_config
    import capo_codebuild.types.source_auth
    import capo_codebuild.types.source_type
    import capo_codebuild.types.string
    import capo_codebuild.types.wrapper_boolean


class ProjectSource(TypedDict, closed=True):
    type: "capo_codebuild.types.source_type.SourceType"
    """<p>The type of repository that contains the source code to be built. Valid values include:</p> <ul> <li> <p> <code>BITBUCKET</code>: The source code is in a Bitbucket repository.</p> </li> <li> <p> <code>CODECOMMIT</code>: The source code is in an CodeCommit repository.</p> </li> <li> <p> <code>CODEPIPELINE</code>: The source code settings are specified in the source action of a pipeline in CodePipeline.</p> </li> <li> <p> <code>GITHUB</code>: The source code is in a GitHub repository.</p> </li> <li> <p> <code>GITHUB_ENTERPRISE</code>: The source code is in a GitHub Enterprise Server repository.</p> </li> <li> <p> <code>GITLAB</code>: The source code is in a GitLab repository.</p> </li> <li> <p> <code>GITLAB_SELF_MANAGED</code>: The source code is in a self-managed GitLab repository.</p> </li> <li> <p> <code>NO_SOURCE</code>: The project does not have input source code.</p> </li> <li> <p> <code>S3</code>: The source code is in an Amazon S3 bucket.</p> </li> </ul>"""
    location: NotRequired["capo_codebuild.types.string.String"]
    """<p>Information about the location of the source code to be built. Valid values include:</p> <ul> <li> <p>For source code settings that are specified in the source action of a pipeline in CodePipeline, <code>location</code> should not be specified. If it is specified, CodePipeline ignores it. This is because CodePipeline uses the settings in a pipeline's source action instead of this value.</p> </li> <li> <p>For source code in an CodeCommit repository, the HTTPS clone URL to the repository that contains the source code and the buildspec file (for example, <code>https://git-codecommit.<region-ID>.amazonaws.com/v1/repos/<repo-name></code>).</p> </li> <li> <p>For source code in an Amazon S3 input bucket, one of the following. </p> <ul> <li> <p>The path to the ZIP file that contains the source code (for example, <code><bucket-name>/<path>/<object-name>.zip</code>). </p> </li> <li> <p>The path to the folder that contains the source code (for example, <code><bucket-name>/<path-to-source-code>/<folder>/</code>). </p> </li> </ul> </li> <li> <p>For source code in a GitHub repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your GitHub account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitHub, on the GitHub <b>Authorize application</b> page, for <b>Organization access</b>, choose <b>Request access</b> next to each repository you want to allow CodeBuild to have access to, and then choose <b>Authorize application</b>. (After you have connected to your GitHub account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to use this connection, in the <code>source</code> object, set the <code>auth</code> object's <code>type</code> value to <code>OAUTH</code>.</p> </li> <li> <p>For source code in an GitLab or self-managed GitLab repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your GitLab account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with GitLab, on the Connections <b>Authorize application</b> page, choose <b>Authorize</b>. Then on the CodeConnections <b>Create GitLab connection</b> page, choose <b>Connect to GitLab</b>. (After you have connected to your GitLab account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to override the default connection and use this connection instead, set the <code>auth</code> object's <code>type</code> value to <code>CODECONNECTIONS</code> in the <code>source</code> object.</p> </li> <li> <p>For source code in a Bitbucket repository, the HTTPS clone URL to the repository that contains the source and the buildspec file. You must connect your Amazon Web Services account to your Bitbucket account. Use the CodeBuild console to start creating a build project. When you use the console to connect (or reconnect) with Bitbucket, on the Bitbucket <b>Confirm access to your account</b> page, choose <b>Grant access</b>. (After you have connected to your Bitbucket account, you do not need to finish creating the build project. You can leave the CodeBuild console.) To instruct CodeBuild to use this connection, in the <code>source</code> object, set the <code>auth</code> object's <code>type</code> value to <code>OAUTH</code>.</p> </li> </ul> <p> If you specify <code>CODEPIPELINE</code> for the <code>Type</code> property, don't specify this property. For all of the other types, you must specify <code>Location</code>. </p>"""
    git_clone_depth: NotRequired["capo_codebuild.types.git_clone_depth.GitCloneDepth"]
    """<p>Information about the Git clone depth for the build project.</p>"""
    git_submodules_config: NotRequired[
        "capo_codebuild.types.git_submodules_config.GitSubmodulesConfig"
    ]
    """<p> Information about the Git submodules configuration for the build project. </p>"""
    buildspec: NotRequired["capo_codebuild.types.string.String"]
    """<p>The buildspec file declaration to use for the builds in this build project.</p> <p> If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in <code>CODEBUILD_SRC_DIR</code> environment variable, or the path to an S3 bucket. The bucket must be in the same Amazon Web Services Region as the build project. Specify the buildspec file using its ARN (for example, <code>arn:aws:s3:::my-codebuild-sample2/buildspec.yml</code>). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage">Buildspec File Name and Storage Location</a>. </p>"""
    auth: NotRequired["capo_codebuild.types.source_auth.SourceAuth"]
    """<p>Information about the authorization settings for CodeBuild to access the source code to be built.</p>"""
    report_build_status: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p> Set to true to report the status of a build's start and finish to your source provider. This option is valid only when your source provider is GitHub, GitHub Enterprise, GitLab, GitLab Self Managed, GitLab, GitLab Self Managed, or Bitbucket. If this is set and you use a different source provider, an <code>invalidInputException</code> is thrown. </p> <p>To be able to report the build status to the source provider, the user associated with the source provider must have write access to the repo. If the user does not have write access, the build status cannot be updated. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/access-tokens.html">Source provider access</a> in the <i>CodeBuild User Guide</i>.</p> <p>The status of a build triggered by a webhook is always reported to your source provider. </p> <p>If your project's builds are triggered by a webhook, you must push a new commit to the repo for a change to this property to take effect.</p>"""
    build_status_config: NotRequired[
        "capo_codebuild.types.build_status_config.BuildStatusConfig"
    ]
    """<p>Contains information that defines how the build project reports the build status to the source provider. This option is only used when the source provider is <code>GITHUB</code>, <code>GITHUB_ENTERPRISE</code>, or <code>BITBUCKET</code>.</p>"""
    insecure_ssl: NotRequired["capo_codebuild.types.wrapper_boolean.WrapperBoolean"]
    """<p>Enable this flag to ignore SSL warnings while connecting to the project source code.</p>"""
    source_identifier: NotRequired["capo_codebuild.types.string.String"]
    """<p>An identifier for this project source. The identifier can only contain alphanumeric characters and underscores, and must be less than 128 characters in length. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectSource) -> dict:
    out: dict = {}
    import capo_codebuild.types.source_type

    out["type"] = capo_codebuild.types.source_type.serialize_aws_json_1_1(value["type"])
    if "location" in value:
        out["location"] = value["location"]
    if "git_clone_depth" in value:
        out["gitCloneDepth"] = value["git_clone_depth"]
    if "git_submodules_config" in value:
        import capo_codebuild.types.git_submodules_config

        out["gitSubmodulesConfig"] = (
            capo_codebuild.types.git_submodules_config.serialize_aws_json_1_1(
                value["git_submodules_config"]
            )
        )
    if "buildspec" in value:
        out["buildspec"] = value["buildspec"]
    if "auth" in value:
        import capo_codebuild.types.source_auth

        out["auth"] = capo_codebuild.types.source_auth.serialize_aws_json_1_1(
            value["auth"]
        )
    if "report_build_status" in value:
        out["reportBuildStatus"] = value["report_build_status"]
    if "build_status_config" in value:
        import capo_codebuild.types.build_status_config

        out["buildStatusConfig"] = (
            capo_codebuild.types.build_status_config.serialize_aws_json_1_1(
                value["build_status_config"]
            )
        )
    if "insecure_ssl" in value:
        out["insecureSsl"] = value["insecure_ssl"]
    if "source_identifier" in value:
        out["sourceIdentifier"] = value["source_identifier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectSource:
    out: ProjectSource = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_codebuild.types.source_type

        out["type"] = capo_codebuild.types.source_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("ProjectSource.type required")
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("gitCloneDepth") is not None:
        out["git_clone_depth"] = data["gitCloneDepth"]
    if data.get("gitSubmodulesConfig") is not None:
        import capo_codebuild.types.git_submodules_config

        out["git_submodules_config"] = (
            capo_codebuild.types.git_submodules_config.deserialize_aws_json_1_1(
                data["gitSubmodulesConfig"]
            )
        )
    if data.get("buildspec") is not None:
        out["buildspec"] = data["buildspec"]
    if data.get("auth") is not None:
        import capo_codebuild.types.source_auth

        out["auth"] = capo_codebuild.types.source_auth.deserialize_aws_json_1_1(
            data["auth"]
        )
    if data.get("reportBuildStatus") is not None:
        out["report_build_status"] = data["reportBuildStatus"]
    if data.get("buildStatusConfig") is not None:
        import capo_codebuild.types.build_status_config

        out["build_status_config"] = (
            capo_codebuild.types.build_status_config.deserialize_aws_json_1_1(
                data["buildStatusConfig"]
            )
        )
    if data.get("insecureSsl") is not None:
        out["insecure_ssl"] = data["insecureSsl"]
    if data.get("sourceIdentifier") is not None:
        out["source_identifier"] = data["sourceIdentifier"]
    return out
