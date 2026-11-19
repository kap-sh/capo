"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectBuildBatchConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.batch_report_mode_type
    import capo_codebuild.types.batch_restrictions
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.wrapper_boolean
    import capo_codebuild.types.wrapper_int


class ProjectBuildBatchConfig(TypedDict, closed=True):
    service_role: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the service role ARN for the batch build project.</p>"""
    combine_artifacts: NotRequired[
        "capo_codebuild.types.wrapper_boolean.WrapperBoolean"
    ]
    """<p>Specifies if the build artifacts for the batch build should be combined into a single artifact location.</p>"""
    restrictions: NotRequired[
        "capo_codebuild.types.batch_restrictions.BatchRestrictions"
    ]
    """<p>A <code>BatchRestrictions</code> object that specifies the restrictions for the batch build.</p>"""
    timeout_in_mins: NotRequired["capo_codebuild.types.wrapper_int.WrapperInt"]
    """<p>Specifies the maximum amount of time, in minutes, that the batch build must be completed in.</p>"""
    batch_report_mode: NotRequired[
        "capo_codebuild.types.batch_report_mode_type.BatchReportModeType"
    ]
    """<p>Specifies how build status reports are sent to the source provider for the batch build. This property is only used when the source provider for your project is Bitbucket, GitHub, or GitHub Enterprise, and your project is configured to report build statuses to the source provider.</p> <dl> <dt>REPORT_AGGREGATED_BATCH</dt> <dd> <p>(Default) Aggregate all of the build statuses into a single status report.</p> </dd> <dt>REPORT_INDIVIDUAL_BUILDS</dt> <dd> <p>Send a separate status report for each individual build.</p> </dd> </dl>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectBuildBatchConfig) -> dict:
    out: dict = {}
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "combine_artifacts" in value:
        out["combineArtifacts"] = value["combine_artifacts"]
    if "restrictions" in value:
        import capo_codebuild.types.batch_restrictions

        out["restrictions"] = (
            capo_codebuild.types.batch_restrictions.serialize_aws_json_1_1(
                value["restrictions"]
            )
        )
    if "timeout_in_mins" in value:
        out["timeoutInMins"] = value["timeout_in_mins"]
    if "batch_report_mode" in value:
        import capo_codebuild.types.batch_report_mode_type

        out["batchReportMode"] = (
            capo_codebuild.types.batch_report_mode_type.serialize_aws_json_1_1(
                value["batch_report_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectBuildBatchConfig:
    out: ProjectBuildBatchConfig = {}  # type: ignore[typeddict-item]
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("combineArtifacts") is not None:
        out["combine_artifacts"] = data["combineArtifacts"]
    if data.get("restrictions") is not None:
        import capo_codebuild.types.batch_restrictions

        out["restrictions"] = (
            capo_codebuild.types.batch_restrictions.deserialize_aws_json_1_1(
                data["restrictions"]
            )
        )
    if data.get("timeoutInMins") is not None:
        out["timeout_in_mins"] = data["timeoutInMins"]
    if data.get("batchReportMode") is not None:
        import capo_codebuild.types.batch_report_mode_type

        out["batch_report_mode"] = (
            capo_codebuild.types.batch_report_mode_type.deserialize_aws_json_1_1(
                data["batchReportMode"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProjectBuildBatchConfig) -> dict:
    out: dict = {}
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "combine_artifacts" in value:
        out["combineArtifacts"] = value["combine_artifacts"]
    if "restrictions" in value:
        import capo_codebuild.types.batch_restrictions

        out["restrictions"] = capo_codebuild.types.batch_restrictions.serialize_cbor(
            value["restrictions"]
        )
    if "timeout_in_mins" in value:
        out["timeoutInMins"] = value["timeout_in_mins"]
    if "batch_report_mode" in value:
        import capo_codebuild.types.batch_report_mode_type

        out["batchReportMode"] = (
            capo_codebuild.types.batch_report_mode_type.serialize_cbor(
                value["batch_report_mode"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ProjectBuildBatchConfig:
    out: ProjectBuildBatchConfig = {}  # type: ignore[typeddict-item]
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("combineArtifacts") is not None:
        out["combine_artifacts"] = data["combineArtifacts"]
    if data.get("restrictions") is not None:
        import capo_codebuild.types.batch_restrictions

        out["restrictions"] = capo_codebuild.types.batch_restrictions.deserialize_cbor(
            data["restrictions"]
        )
    if data.get("timeoutInMins") is not None:
        out["timeout_in_mins"] = data["timeoutInMins"]
    if data.get("batchReportMode") is not None:
        import capo_codebuild.types.batch_report_mode_type

        out["batch_report_mode"] = (
            capo_codebuild.types.batch_report_mode_type.deserialize_cbor(
                data["batchReportMode"]
            )
        )
    return out
