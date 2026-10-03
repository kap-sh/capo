"""Generated from Smithy shape ``com.amazonaws.codebuild#StartBuildBatchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.build_time_out
    import capo_codebuild.types.compute_type
    import capo_codebuild.types.environment_type
    import capo_codebuild.types.environment_variables
    import capo_codebuild.types.git_clone_depth
    import capo_codebuild.types.git_submodules_config
    import capo_codebuild.types.image_pull_credentials_type
    import capo_codebuild.types.logs_config
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.project_artifacts
    import capo_codebuild.types.project_artifacts_list
    import capo_codebuild.types.project_build_batch_config
    import capo_codebuild.types.project_cache
    import capo_codebuild.types.project_secondary_source_versions
    import capo_codebuild.types.project_sources
    import capo_codebuild.types.registry_credential
    import capo_codebuild.types.source_auth
    import capo_codebuild.types.source_type
    import capo_codebuild.types.string
    import capo_codebuild.types.time_out
    import capo_codebuild.types.wrapper_boolean


class StartBuildBatchInput(TypedDict, closed=True):
    project_name: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The name of the project.</p>"""
    secondary_sources_override: NotRequired[
        "capo_codebuild.types.project_sources.ProjectSources"
    ]
    """<p>An array of <code>ProjectSource</code> objects that override the secondary sources defined in the batch build project.</p>"""
    secondary_sources_version_override: NotRequired[
        "capo_codebuild.types.project_secondary_source_versions.ProjectSecondarySourceVersions"
    ]
    """<p>An array of <code>ProjectSourceVersion</code> objects that override the secondary source versions in the batch build project.</p>"""
    source_version: NotRequired["capo_codebuild.types.string.String"]
    """<p>The version of the batch build input to be built, for this build only. If not specified, the latest version is used. If specified, the contents depends on the source provider:</p> <dl> <dt>CodeCommit</dt> <dd> <p>The commit ID, branch, or Git tag to use.</p> </dd> <dt>GitHub</dt> <dd> <p>The commit ID, pull request ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a pull request ID is specified, it must use the format <code>pr/pull-request-ID</code> (for example <code>pr/25</code>). If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </dd> <dt>Bitbucket</dt> <dd> <p>The commit ID, branch name, or tag name that corresponds to the version of the source code you want to build. If a branch name is specified, the branch's HEAD commit ID is used. If not specified, the default branch's HEAD commit ID is used.</p> </dd> <dt>Amazon S3</dt> <dd> <p>The version ID of the object that represents the build input ZIP file to use.</p> </dd> </dl> <p>If <code>sourceVersion</code> is specified at the project level, then this <code>sourceVersion</code> (at the build level) takes precedence. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/sample-source-version.html">Source Version Sample with CodeBuild</a> in the <i>CodeBuild User Guide</i>. </p>"""
    artifacts_override: NotRequired[
        "capo_codebuild.types.project_artifacts.ProjectArtifacts"
    ]
    """<p>An array of <code>ProjectArtifacts</code> objects that contains information about the build output artifact overrides for the build project.</p>"""
    secondary_artifacts_override: NotRequired[
        "capo_codebuild.types.project_artifacts_list.ProjectArtifactsList"
    ]
    """<p>An array of <code>ProjectArtifacts</code> objects that override the secondary artifacts defined in the batch build project.</p>"""
    environment_variables_override: NotRequired[
        "capo_codebuild.types.environment_variables.EnvironmentVariables"
    ]
    """<p>An array of <code>EnvironmentVariable</code> objects that override, or add to, the environment variables defined in the batch build project.</p>"""
    source_type_override: NotRequired["capo_codebuild.types.source_type.SourceType"]
    """<p>The source input type that overrides the source input defined in the batch build project.</p>"""
    source_location_override: NotRequired["capo_codebuild.types.string.String"]
    """<p>A location that overrides, for this batch build, the source location defined in the batch build project.</p>"""
    source_auth_override: NotRequired["capo_codebuild.types.source_auth.SourceAuth"]
    """<p>A <code>SourceAuth</code> object that overrides the one defined in the batch build project. This override applies only if the build project's source is BitBucket or GitHub.</p>"""
    git_clone_depth_override: NotRequired[
        "capo_codebuild.types.git_clone_depth.GitCloneDepth"
    ]
    """<p>The user-defined depth of history, with a minimum value of 0, that overrides, for this batch build only, any previous depth of history defined in the batch build project.</p>"""
    git_submodules_config_override: NotRequired[
        "capo_codebuild.types.git_submodules_config.GitSubmodulesConfig"
    ]
    """<p>A <code>GitSubmodulesConfig</code> object that overrides the Git submodules configuration for this batch build.</p>"""
    buildspec_override: NotRequired["capo_codebuild.types.string.String"]
    """<p>A buildspec file declaration that overrides, for this build only, the latest one already defined in the build project.</p> <p>If this value is set, it can be either an inline buildspec definition, the path to an alternate buildspec file relative to the value of the built-in <code>CODEBUILD_SRC_DIR</code> environment variable, or the path to an S3 bucket. The bucket must be in the same Amazon Web Services Region as the build project. Specify the buildspec file using its ARN (for example, <code>arn:aws:s3:::my-codebuild-sample2/buildspec.yml</code>). If this value is not provided or is set to an empty string, the source code must contain a buildspec file in its root directory. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec-ref-name-storage">Buildspec File Name and Storage Location</a>. </p>"""
    insecure_ssl_override: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p>Enable this flag to override the insecure SSL setting that is specified in the batch build project. The insecure SSL setting determines whether to ignore SSL warnings while connecting to the project source code. This override applies only if the build's source is GitHub Enterprise.</p>"""
    report_build_batch_status_override: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p>Set to <code>true</code> to report to your source provider the status of a batch build's start and completion. If you use this option with a source provider other than GitHub, GitHub Enterprise, or Bitbucket, an <code>invalidInputException</code> is thrown. </p> <note> <p>The status of a build triggered by a webhook is always reported to your source provider. </p> </note>"""
    environment_type_override: NotRequired[
        "capo_codebuild.types.environment_type.EnvironmentType"
    ]
    """<p>A container type for this batch build that overrides the one specified in the batch build project.</p>"""
    image_override: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The name of an image for this batch build that overrides the one specified in the batch build project.</p>"""
    compute_type_override: NotRequired["capo_codebuild.types.compute_type.ComputeType"]
    """<p>The name of a compute type for this batch build that overrides the one specified in the batch build project.</p>"""
    certificate_override: NotRequired["capo_codebuild.types.string.String"]
    """<p>The name of a certificate for this batch build that overrides the one specified in the batch build project.</p>"""
    cache_override: NotRequired["capo_codebuild.types.project_cache.ProjectCache"]
    """<p>A <code>ProjectCache</code> object that specifies cache overrides.</p>"""
    service_role_override: NotRequired[
        "capo_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of a service role for this batch build that overrides the one specified in the batch build project.</p>"""
    privileged_mode_override: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p>Enable this flag to override privileged mode in the batch build project.</p>"""
    build_timeout_in_minutes_override: NotRequired[
        "capo_codebuild.types.build_time_out.BuildTimeOut"
    ]
    """<p>Overrides the build timeout specified in the batch build project.</p>"""
    queued_timeout_in_minutes_override: NotRequired[
        "capo_codebuild.types.time_out.TimeOut"
    ]
    """<p>The number of minutes a batch build is allowed to be queued before it times out.</p>"""
    encryption_key_override: NotRequired[
        "capo_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Key Management Service customer master key (CMK) that overrides the one specified in the batch build project. The CMK key encrypts the build output artifacts.</p> <note> <p>You can use a cross-account KMS key to encrypt the build output artifacts if your service role has permission to that key. </p> </note> <p>You can specify either the Amazon Resource Name (ARN) of the CMK or, if available, the CMK's alias (using the format <code>alias/<alias-name></code>).</p>"""
    idempotency_token: NotRequired["capo_codebuild.types.string.String"]
    """<p>A unique, case sensitive identifier you provide to ensure the idempotency of the <code>StartBuildBatch</code> request. The token is included in the <code>StartBuildBatch</code> request and is valid for five minutes. If you repeat the <code>StartBuildBatch</code> request with the same token, but change a parameter, CodeBuild returns a parameter mismatch error.</p>"""
    logs_config_override: NotRequired["capo_codebuild.types.logs_config.LogsConfig"]
    """<p>A <code>LogsConfig</code> object that override the log settings defined in the batch build project.</p>"""
    registry_credential_override: NotRequired[
        "capo_codebuild.types.registry_credential.RegistryCredential"
    ]
    """<p>A <code>RegistryCredential</code> object that overrides credentials for access to a private registry.</p>"""
    image_pull_credentials_type_override: NotRequired[
        "capo_codebuild.types.image_pull_credentials_type.ImagePullCredentialsType"
    ]
    """<p>The type of credentials CodeBuild uses to pull images in your batch build. There are two valid values: </p> <dl> <dt>CODEBUILD</dt> <dd> <p>Specifies that CodeBuild uses its own credentials. This requires that you modify your ECR repository policy to trust CodeBuild's service principal.</p> </dd> <dt>SERVICE_ROLE</dt> <dd> <p>Specifies that CodeBuild uses your build project's service role. </p> </dd> </dl> <p>When using a cross-account or private registry image, you must use <code>SERVICE_ROLE</code> credentials. When using an CodeBuild curated image, you must use <code>CODEBUILD</code> credentials. </p>"""
    build_batch_config_override: NotRequired[
        "capo_codebuild.types.project_build_batch_config.ProjectBuildBatchConfig"
    ]
    """<p>A <code>BuildBatchConfigOverride</code> object that contains batch build configuration overrides.</p>"""
    debug_session_enabled: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p>Specifies if session debugging is enabled for this batch build. For more information, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/session-manager.html">Viewing a running build in Session Manager</a>. Batch session debugging is not supported for matrix batch builds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartBuildBatchInput) -> dict:
    out: dict = {}
    out["projectName"] = value["project_name"]
    if "secondary_sources_override" in value:
        import capo_codebuild.types.project_sources

        out["secondarySourcesOverride"] = (
            capo_codebuild.types.project_sources.serialize_aws_json_1_1(
                value["secondary_sources_override"]
            )
        )
    if "secondary_sources_version_override" in value:
        import capo_codebuild.types.project_secondary_source_versions

        out["secondarySourcesVersionOverride"] = (
            capo_codebuild.types.project_secondary_source_versions.serialize_aws_json_1_1(
                value["secondary_sources_version_override"]
            )
        )
    if "source_version" in value:
        out["sourceVersion"] = value["source_version"]
    if "artifacts_override" in value:
        import capo_codebuild.types.project_artifacts

        out["artifactsOverride"] = (
            capo_codebuild.types.project_artifacts.serialize_aws_json_1_1(
                value["artifacts_override"]
            )
        )
    if "secondary_artifacts_override" in value:
        import capo_codebuild.types.project_artifacts_list

        out["secondaryArtifactsOverride"] = (
            capo_codebuild.types.project_artifacts_list.serialize_aws_json_1_1(
                value["secondary_artifacts_override"]
            )
        )
    if "environment_variables_override" in value:
        import capo_codebuild.types.environment_variables

        out["environmentVariablesOverride"] = (
            capo_codebuild.types.environment_variables.serialize_aws_json_1_1(
                value["environment_variables_override"]
            )
        )
    if "source_type_override" in value:
        import capo_codebuild.types.source_type

        out["sourceTypeOverride"] = (
            capo_codebuild.types.source_type.serialize_aws_json_1_1(
                value["source_type_override"]
            )
        )
    if "source_location_override" in value:
        out["sourceLocationOverride"] = value["source_location_override"]
    if "source_auth_override" in value:
        import capo_codebuild.types.source_auth

        out["sourceAuthOverride"] = (
            capo_codebuild.types.source_auth.serialize_aws_json_1_1(
                value["source_auth_override"]
            )
        )
    if "git_clone_depth_override" in value:
        out["gitCloneDepthOverride"] = value["git_clone_depth_override"]
    if "git_submodules_config_override" in value:
        import capo_codebuild.types.git_submodules_config

        out["gitSubmodulesConfigOverride"] = (
            capo_codebuild.types.git_submodules_config.serialize_aws_json_1_1(
                value["git_submodules_config_override"]
            )
        )
    if "buildspec_override" in value:
        out["buildspecOverride"] = value["buildspec_override"]
    if "insecure_ssl_override" in value:
        out["insecureSslOverride"] = value["insecure_ssl_override"]
    if "report_build_batch_status_override" in value:
        out["reportBuildBatchStatusOverride"] = value[
            "report_build_batch_status_override"
        ]
    if "environment_type_override" in value:
        import capo_codebuild.types.environment_type

        out["environmentTypeOverride"] = (
            capo_codebuild.types.environment_type.serialize_aws_json_1_1(
                value["environment_type_override"]
            )
        )
    if "image_override" in value:
        out["imageOverride"] = value["image_override"]
    if "compute_type_override" in value:
        import capo_codebuild.types.compute_type

        out["computeTypeOverride"] = (
            capo_codebuild.types.compute_type.serialize_aws_json_1_1(
                value["compute_type_override"]
            )
        )
    if "certificate_override" in value:
        out["certificateOverride"] = value["certificate_override"]
    if "cache_override" in value:
        import capo_codebuild.types.project_cache

        out["cacheOverride"] = (
            capo_codebuild.types.project_cache.serialize_aws_json_1_1(
                value["cache_override"]
            )
        )
    if "service_role_override" in value:
        out["serviceRoleOverride"] = value["service_role_override"]
    if "privileged_mode_override" in value:
        out["privilegedModeOverride"] = value["privileged_mode_override"]
    if "build_timeout_in_minutes_override" in value:
        out["buildTimeoutInMinutesOverride"] = value[
            "build_timeout_in_minutes_override"
        ]
    if "queued_timeout_in_minutes_override" in value:
        out["queuedTimeoutInMinutesOverride"] = value[
            "queued_timeout_in_minutes_override"
        ]
    if "encryption_key_override" in value:
        out["encryptionKeyOverride"] = value["encryption_key_override"]
    if "idempotency_token" in value:
        out["idempotencyToken"] = value["idempotency_token"]
    if "logs_config_override" in value:
        import capo_codebuild.types.logs_config

        out["logsConfigOverride"] = (
            capo_codebuild.types.logs_config.serialize_aws_json_1_1(
                value["logs_config_override"]
            )
        )
    if "registry_credential_override" in value:
        import capo_codebuild.types.registry_credential

        out["registryCredentialOverride"] = (
            capo_codebuild.types.registry_credential.serialize_aws_json_1_1(
                value["registry_credential_override"]
            )
        )
    if "image_pull_credentials_type_override" in value:
        import capo_codebuild.types.image_pull_credentials_type

        out["imagePullCredentialsTypeOverride"] = (
            capo_codebuild.types.image_pull_credentials_type.serialize_aws_json_1_1(
                value["image_pull_credentials_type_override"]
            )
        )
    if "build_batch_config_override" in value:
        import capo_codebuild.types.project_build_batch_config

        out["buildBatchConfigOverride"] = (
            capo_codebuild.types.project_build_batch_config.serialize_aws_json_1_1(
                value["build_batch_config_override"]
            )
        )
    if "debug_session_enabled" in value:
        out["debugSessionEnabled"] = value["debug_session_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartBuildBatchInput:
    out: StartBuildBatchInput = {}  # type: ignore[typeddict-item]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        raise DeserializationError("StartBuildBatchInput.project_name required")
    if data.get("secondarySourcesOverride") is not None:
        import capo_codebuild.types.project_sources

        out["secondary_sources_override"] = (
            capo_codebuild.types.project_sources.deserialize_aws_json_1_1(
                data["secondarySourcesOverride"]
            )
        )
    if data.get("secondarySourcesVersionOverride") is not None:
        import capo_codebuild.types.project_secondary_source_versions

        out["secondary_sources_version_override"] = (
            capo_codebuild.types.project_secondary_source_versions.deserialize_aws_json_1_1(
                data["secondarySourcesVersionOverride"]
            )
        )
    if data.get("sourceVersion") is not None:
        out["source_version"] = data["sourceVersion"]
    if data.get("artifactsOverride") is not None:
        import capo_codebuild.types.project_artifacts

        out["artifacts_override"] = (
            capo_codebuild.types.project_artifacts.deserialize_aws_json_1_1(
                data["artifactsOverride"]
            )
        )
    if data.get("secondaryArtifactsOverride") is not None:
        import capo_codebuild.types.project_artifacts_list

        out["secondary_artifacts_override"] = (
            capo_codebuild.types.project_artifacts_list.deserialize_aws_json_1_1(
                data["secondaryArtifactsOverride"]
            )
        )
    if data.get("environmentVariablesOverride") is not None:
        import capo_codebuild.types.environment_variables

        out["environment_variables_override"] = (
            capo_codebuild.types.environment_variables.deserialize_aws_json_1_1(
                data["environmentVariablesOverride"]
            )
        )
    if data.get("sourceTypeOverride") is not None:
        import capo_codebuild.types.source_type

        out["source_type_override"] = (
            capo_codebuild.types.source_type.deserialize_aws_json_1_1(
                data["sourceTypeOverride"]
            )
        )
    if data.get("sourceLocationOverride") is not None:
        out["source_location_override"] = data["sourceLocationOverride"]
    if data.get("sourceAuthOverride") is not None:
        import capo_codebuild.types.source_auth

        out["source_auth_override"] = (
            capo_codebuild.types.source_auth.deserialize_aws_json_1_1(
                data["sourceAuthOverride"]
            )
        )
    if data.get("gitCloneDepthOverride") is not None:
        out["git_clone_depth_override"] = data["gitCloneDepthOverride"]
    if data.get("gitSubmodulesConfigOverride") is not None:
        import capo_codebuild.types.git_submodules_config

        out["git_submodules_config_override"] = (
            capo_codebuild.types.git_submodules_config.deserialize_aws_json_1_1(
                data["gitSubmodulesConfigOverride"]
            )
        )
    if data.get("buildspecOverride") is not None:
        out["buildspec_override"] = data["buildspecOverride"]
    if data.get("insecureSslOverride") is not None:
        out["insecure_ssl_override"] = data["insecureSslOverride"]
    if data.get("reportBuildBatchStatusOverride") is not None:
        out["report_build_batch_status_override"] = data[
            "reportBuildBatchStatusOverride"
        ]
    if data.get("environmentTypeOverride") is not None:
        import capo_codebuild.types.environment_type

        out["environment_type_override"] = (
            capo_codebuild.types.environment_type.deserialize_aws_json_1_1(
                data["environmentTypeOverride"]
            )
        )
    if data.get("imageOverride") is not None:
        out["image_override"] = data["imageOverride"]
    if data.get("computeTypeOverride") is not None:
        import capo_codebuild.types.compute_type

        out["compute_type_override"] = (
            capo_codebuild.types.compute_type.deserialize_aws_json_1_1(
                data["computeTypeOverride"]
            )
        )
    if data.get("certificateOverride") is not None:
        out["certificate_override"] = data["certificateOverride"]
    if data.get("cacheOverride") is not None:
        import capo_codebuild.types.project_cache

        out["cache_override"] = (
            capo_codebuild.types.project_cache.deserialize_aws_json_1_1(
                data["cacheOverride"]
            )
        )
    if data.get("serviceRoleOverride") is not None:
        out["service_role_override"] = data["serviceRoleOverride"]
    if data.get("privilegedModeOverride") is not None:
        out["privileged_mode_override"] = data["privilegedModeOverride"]
    if data.get("buildTimeoutInMinutesOverride") is not None:
        out["build_timeout_in_minutes_override"] = data["buildTimeoutInMinutesOverride"]
    if data.get("queuedTimeoutInMinutesOverride") is not None:
        out["queued_timeout_in_minutes_override"] = data[
            "queuedTimeoutInMinutesOverride"
        ]
    if data.get("encryptionKeyOverride") is not None:
        out["encryption_key_override"] = data["encryptionKeyOverride"]
    if data.get("idempotencyToken") is not None:
        out["idempotency_token"] = data["idempotencyToken"]
    if data.get("logsConfigOverride") is not None:
        import capo_codebuild.types.logs_config

        out["logs_config_override"] = (
            capo_codebuild.types.logs_config.deserialize_aws_json_1_1(
                data["logsConfigOverride"]
            )
        )
    if data.get("registryCredentialOverride") is not None:
        import capo_codebuild.types.registry_credential

        out["registry_credential_override"] = (
            capo_codebuild.types.registry_credential.deserialize_aws_json_1_1(
                data["registryCredentialOverride"]
            )
        )
    if data.get("imagePullCredentialsTypeOverride") is not None:
        import capo_codebuild.types.image_pull_credentials_type

        out["image_pull_credentials_type_override"] = (
            capo_codebuild.types.image_pull_credentials_type.deserialize_aws_json_1_1(
                data["imagePullCredentialsTypeOverride"]
            )
        )
    if data.get("buildBatchConfigOverride") is not None:
        import capo_codebuild.types.project_build_batch_config

        out["build_batch_config_override"] = (
            capo_codebuild.types.project_build_batch_config.deserialize_aws_json_1_1(
                data["buildBatchConfigOverride"]
            )
        )
    if data.get("debugSessionEnabled") is not None:
        out["debug_session_enabled"] = data["debugSessionEnabled"]
    return out
