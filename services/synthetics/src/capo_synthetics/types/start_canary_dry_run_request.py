"""Generated from Smithy shape ``com.amazonaws.synthetics#StartCanaryDryRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.artifact_config_input
    import capo_synthetics.types.browser_configs
    import capo_synthetics.types.canary_code_input
    import capo_synthetics.types.canary_name
    import capo_synthetics.types.canary_run_config_input
    import capo_synthetics.types.max_size1024
    import capo_synthetics.types.provisioned_resource_cleanup_setting
    import capo_synthetics.types.role_arn
    import capo_synthetics.types.string
    import capo_synthetics.types.visual_reference_input
    import capo_synthetics.types.visual_references
    import capo_synthetics.types.vpc_config_input


class StartCanaryDryRunRequest(TypedDict, closed=True):
    name: "capo_synthetics.types.canary_name.CanaryName"
    """<p>The name of the canary that you want to dry run. To find canary names, use <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DescribeCanaries.html">DescribeCanaries</a>.</p>"""
    code: NotRequired["capo_synthetics.types.canary_code_input.CanaryCodeInput"]
    runtime_version: NotRequired["capo_synthetics.types.string.String"]
    """<p>Specifies the runtime version to use for the canary. For a list of valid runtime versions and for more information about runtime versions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html"> Canary Runtime Versions</a>.</p>"""
    run_config: NotRequired[
        "capo_synthetics.types.canary_run_config_input.CanaryRunConfigInput"
    ]
    vpc_config: NotRequired["capo_synthetics.types.vpc_config_input.VpcConfigInput"]
    execution_role_arn: NotRequired["capo_synthetics.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role to be used to run the canary. This role must already exist, and must include <code>lambda.amazonaws.com</code> as a principal in the trust policy. The role must also have the following permissions:</p>"""
    success_retention_period_in_days: NotRequired[
        "capo_synthetics.types.max_size1024.MaxSize1024"
    ]
    """<p>The number of days to retain data about successful runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.</p> <p>This setting affects the range of information returned by <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>"""
    failure_retention_period_in_days: NotRequired[
        "capo_synthetics.types.max_size1024.MaxSize1024"
    ]
    """<p>The number of days to retain data about failed runs of this canary. If you omit this field, the default of 31 days is used. The valid range is 1 to 455 days.</p> <p>This setting affects the range of information returned by <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GetCanaryRuns.html">GetCanaryRuns</a>, as well as the range of information displayed in the Synthetics console. </p>"""
    visual_reference: NotRequired[
        "capo_synthetics.types.visual_reference_input.VisualReferenceInput"
    ]
    artifact_s3_location: NotRequired["capo_synthetics.types.string.String"]
    """<p>The location in Amazon S3 where Synthetics stores artifacts from the test runs of this canary. Artifacts include the log file, screenshots, and HAR files. The name of the Amazon S3 bucket can't include a period (.).</p>"""
    artifact_config: NotRequired[
        "capo_synthetics.types.artifact_config_input.ArtifactConfigInput"
    ]
    provisioned_resource_cleanup: NotRequired[
        "capo_synthetics.types.provisioned_resource_cleanup_setting.ProvisionedResourceCleanupSetting"
    ]
    """<p>Specifies whether to also delete the Lambda functions and layers used by this canary when the canary is deleted. If you omit this parameter, the default of <code>AUTOMATIC</code> is used, which means that the Lambda functions and layers will be deleted when the canary is deleted.</p> <p>If the value of this parameter is <code>OFF</code>, then the value of the <code>DeleteLambda</code> parameter of the <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_DeleteCanary.html">DeleteCanary</a> operation determines whether the Lambda functions and layers will be deleted.</p>"""
    browser_configs: NotRequired["capo_synthetics.types.browser_configs.BrowserConfigs"]
    """<p>A structure that specifies the browser type to use for a canary run. CloudWatch Synthetics supports running canaries on both <code>CHROME</code> and <code>FIREFOX</code> browsers.</p> <note> <p>If not specified, <code>browserConfigs</code> defaults to Chrome.</p> </note>"""
    visual_references: NotRequired[
        "capo_synthetics.types.visual_references.VisualReferences"
    ]
    """<p>A list of visual reference configurations for the canary, one for each browser type that the canary is configured to run on. Visual references are used for visual monitoring comparisons.</p> <p> <code>syn-nodejs-puppeteer-11.0</code> and above, and <code>syn-nodejs-playwright-3.0</code> and above, only supports <code>visualReferences</code>. <code>visualReference</code> field is not supported.</p> <p>Versions older than <code>syn-nodejs-puppeteer-11.0</code> supports both <code>visualReference</code> and <code>visualReferences</code> for backward compatibility. It is recommended to use <code>visualReferences</code> for consistency and future compatibility.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCanaryDryRunRequest) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_synthetics.types.canary_code_input

        out["Code"] = capo_synthetics.types.canary_code_input.serialize_json(
            value["code"]
        )
    if "runtime_version" in value:
        out["RuntimeVersion"] = value["runtime_version"]
    if "run_config" in value:
        import capo_synthetics.types.canary_run_config_input

        out["RunConfig"] = capo_synthetics.types.canary_run_config_input.serialize_json(
            value["run_config"]
        )
    if "vpc_config" in value:
        import capo_synthetics.types.vpc_config_input

        out["VpcConfig"] = capo_synthetics.types.vpc_config_input.serialize_json(
            value["vpc_config"]
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "success_retention_period_in_days" in value:
        out["SuccessRetentionPeriodInDays"] = value["success_retention_period_in_days"]
    if "failure_retention_period_in_days" in value:
        out["FailureRetentionPeriodInDays"] = value["failure_retention_period_in_days"]
    if "visual_reference" in value:
        import capo_synthetics.types.visual_reference_input

        out["VisualReference"] = (
            capo_synthetics.types.visual_reference_input.serialize_json(
                value["visual_reference"]
            )
        )
    if "artifact_s3_location" in value:
        out["ArtifactS3Location"] = value["artifact_s3_location"]
    if "artifact_config" in value:
        import capo_synthetics.types.artifact_config_input

        out["ArtifactConfig"] = (
            capo_synthetics.types.artifact_config_input.serialize_json(
                value["artifact_config"]
            )
        )
    if "provisioned_resource_cleanup" in value:
        import capo_synthetics.types.provisioned_resource_cleanup_setting

        out["ProvisionedResourceCleanup"] = (
            capo_synthetics.types.provisioned_resource_cleanup_setting.serialize_json(
                value["provisioned_resource_cleanup"]
            )
        )
    if "browser_configs" in value:
        import capo_synthetics.types.browser_configs

        out["BrowserConfigs"] = capo_synthetics.types.browser_configs.serialize_json(
            value["browser_configs"]
        )
    if "visual_references" in value:
        import capo_synthetics.types.visual_references

        out["VisualReferences"] = (
            capo_synthetics.types.visual_references.serialize_json(
                value["visual_references"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartCanaryDryRunRequest:
    out: StartCanaryDryRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_synthetics.types.canary_code_input

        out["code"] = capo_synthetics.types.canary_code_input.deserialize_json(
            data["Code"]
        )
    if data.get("RuntimeVersion") is not None:
        out["runtime_version"] = data["RuntimeVersion"]
    if data.get("RunConfig") is not None:
        import capo_synthetics.types.canary_run_config_input

        out["run_config"] = (
            capo_synthetics.types.canary_run_config_input.deserialize_json(
                data["RunConfig"]
            )
        )
    if data.get("VpcConfig") is not None:
        import capo_synthetics.types.vpc_config_input

        out["vpc_config"] = capo_synthetics.types.vpc_config_input.deserialize_json(
            data["VpcConfig"]
        )
    if data.get("ExecutionRoleArn") is not None:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if data.get("SuccessRetentionPeriodInDays") is not None:
        out["success_retention_period_in_days"] = data["SuccessRetentionPeriodInDays"]
    if data.get("FailureRetentionPeriodInDays") is not None:
        out["failure_retention_period_in_days"] = data["FailureRetentionPeriodInDays"]
    if data.get("VisualReference") is not None:
        import capo_synthetics.types.visual_reference_input

        out["visual_reference"] = (
            capo_synthetics.types.visual_reference_input.deserialize_json(
                data["VisualReference"]
            )
        )
    if data.get("ArtifactS3Location") is not None:
        out["artifact_s3_location"] = data["ArtifactS3Location"]
    if data.get("ArtifactConfig") is not None:
        import capo_synthetics.types.artifact_config_input

        out["artifact_config"] = (
            capo_synthetics.types.artifact_config_input.deserialize_json(
                data["ArtifactConfig"]
            )
        )
    if data.get("ProvisionedResourceCleanup") is not None:
        import capo_synthetics.types.provisioned_resource_cleanup_setting

        out["provisioned_resource_cleanup"] = (
            capo_synthetics.types.provisioned_resource_cleanup_setting.deserialize_json(
                data["ProvisionedResourceCleanup"]
            )
        )
    if data.get("BrowserConfigs") is not None:
        import capo_synthetics.types.browser_configs

        out["browser_configs"] = capo_synthetics.types.browser_configs.deserialize_json(
            data["BrowserConfigs"]
        )
    if data.get("VisualReferences") is not None:
        import capo_synthetics.types.visual_references

        out["visual_references"] = (
            capo_synthetics.types.visual_references.deserialize_json(
                data["VisualReferences"]
            )
        )
    return out
