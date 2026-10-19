"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisJobDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rekognition.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rekognition.types.date_time
    import capo_rekognition.types.kms_key_id
    import capo_rekognition.types.media_analysis_input
    import capo_rekognition.types.media_analysis_job_failure_details
    import capo_rekognition.types.media_analysis_job_id
    import capo_rekognition.types.media_analysis_job_name
    import capo_rekognition.types.media_analysis_job_status
    import capo_rekognition.types.media_analysis_manifest_summary
    import capo_rekognition.types.media_analysis_operations_config
    import capo_rekognition.types.media_analysis_output_config
    import capo_rekognition.types.media_analysis_results


class MediaAnalysisJobDescription(TypedDict, closed=True):
    job_id: "capo_rekognition.types.media_analysis_job_id.MediaAnalysisJobId"
    """<p>The identifier for a media analysis job.</p>"""
    job_name: NotRequired[
        "capo_rekognition.types.media_analysis_job_name.MediaAnalysisJobName"
    ]
    """<p>The name of a media analysis job.</p>"""
    operations_config: "capo_rekognition.types.media_analysis_operations_config.MediaAnalysisOperationsConfig"
    """<p>Operation configurations that were provided during job creation.</p>"""
    status: "capo_rekognition.types.media_analysis_job_status.MediaAnalysisJobStatus"
    """<p>The status of the media analysis job being retrieved.</p>"""
    failure_details: NotRequired[
        "capo_rekognition.types.media_analysis_job_failure_details.MediaAnalysisJobFailureDetails"
    ]
    """<p>Details about the error that resulted in failure of the job.</p>"""
    creation_timestamp: "capo_rekognition.types.date_time.DateTime"
    """<p>The Unix date and time when the job was started.</p>"""
    completion_timestamp: NotRequired["capo_rekognition.types.date_time.DateTime"]
    """<p>The Unix date and time when the job finished.</p>"""
    input: "capo_rekognition.types.media_analysis_input.MediaAnalysisInput"
    """<p>Reference to the input manifest that was provided in the job creation request.</p>"""
    output_config: (
        "capo_rekognition.types.media_analysis_output_config.MediaAnalysisOutputConfig"
    )
    """<p>Output configuration that was provided in the creation request.</p>"""
    kms_key_id: NotRequired["capo_rekognition.types.kms_key_id.KmsKeyId"]
    """<p>KMS Key that was provided in the creation request.</p>"""
    results: NotRequired[
        "capo_rekognition.types.media_analysis_results.MediaAnalysisResults"
    ]
    """<p>Output manifest that contains prediction results.</p>"""
    manifest_summary: NotRequired[
        "capo_rekognition.types.media_analysis_manifest_summary.MediaAnalysisManifestSummary"
    ]
    """<p>Provides statistics on input manifest and errors identified in the input manifest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaAnalysisJobDescription) -> dict:
    out: dict = {}
    out["JobId"] = value["job_id"]
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    import capo_rekognition.types.media_analysis_operations_config

    out["OperationsConfig"] = (
        capo_rekognition.types.media_analysis_operations_config.serialize_aws_json_1_1(
            value["operations_config"]
        )
    )
    import capo_rekognition.types.media_analysis_job_status

    out["Status"] = (
        capo_rekognition.types.media_analysis_job_status.serialize_aws_json_1_1(
            value["status"]
        )
    )
    if "failure_details" in value:
        import capo_rekognition.types.media_analysis_job_failure_details

        out["FailureDetails"] = (
            capo_rekognition.types.media_analysis_job_failure_details.serialize_aws_json_1_1(
                value["failure_details"]
            )
        )
    import capo_rekognition.types.date_time

    out["CreationTimestamp"] = capo_rekognition.types.date_time.serialize_aws_json_1_1(
        value["creation_timestamp"]
    )
    if "completion_timestamp" in value:
        import capo_rekognition.types.date_time

        out["CompletionTimestamp"] = (
            capo_rekognition.types.date_time.serialize_aws_json_1_1(
                value["completion_timestamp"]
            )
        )
    import capo_rekognition.types.media_analysis_input

    out["Input"] = capo_rekognition.types.media_analysis_input.serialize_aws_json_1_1(
        value["input"]
    )
    import capo_rekognition.types.media_analysis_output_config

    out["OutputConfig"] = (
        capo_rekognition.types.media_analysis_output_config.serialize_aws_json_1_1(
            value["output_config"]
        )
    )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "results" in value:
        import capo_rekognition.types.media_analysis_results

        out["Results"] = (
            capo_rekognition.types.media_analysis_results.serialize_aws_json_1_1(
                value["results"]
            )
        )
    if "manifest_summary" in value:
        import capo_rekognition.types.media_analysis_manifest_summary

        out["ManifestSummary"] = (
            capo_rekognition.types.media_analysis_manifest_summary.serialize_aws_json_1_1(
                value["manifest_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MediaAnalysisJobDescription:
    out: MediaAnalysisJobDescription = {}  # type: ignore[typeddict-item]
    if data.get("JobId") is not None:
        out["job_id"] = data["JobId"]
    else:
        out["job_id"] = ""
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("OperationsConfig") is not None:
        import capo_rekognition.types.media_analysis_operations_config

        out["operations_config"] = (
            capo_rekognition.types.media_analysis_operations_config.deserialize_aws_json_1_1(
                data["OperationsConfig"]
            )
        )
    else:
        raise DeserializationError(
            "MediaAnalysisJobDescription.operations_config required"
        )
    if data.get("Status") is not None:
        import capo_rekognition.types.media_analysis_job_status

        out["status"] = (
            capo_rekognition.types.media_analysis_job_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_rekognition.types.media_analysis_job_status.MediaAnalysisJobStatus",
            "",
        )
    if data.get("FailureDetails") is not None:
        import capo_rekognition.types.media_analysis_job_failure_details

        out["failure_details"] = (
            capo_rekognition.types.media_analysis_job_failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if data.get("CreationTimestamp") is not None:
        import capo_rekognition.types.date_time

        out["creation_timestamp"] = (
            capo_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["CreationTimestamp"]
            )
        )
    else:
        import datetime

        out["creation_timestamp"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("CompletionTimestamp") is not None:
        import capo_rekognition.types.date_time

        out["completion_timestamp"] = (
            capo_rekognition.types.date_time.deserialize_aws_json_1_1(
                data["CompletionTimestamp"]
            )
        )
    if data.get("Input") is not None:
        import capo_rekognition.types.media_analysis_input

        out["input"] = (
            capo_rekognition.types.media_analysis_input.deserialize_aws_json_1_1(
                data["Input"]
            )
        )
    else:
        raise DeserializationError("MediaAnalysisJobDescription.input required")
    if data.get("OutputConfig") is not None:
        import capo_rekognition.types.media_analysis_output_config

        out["output_config"] = (
            capo_rekognition.types.media_analysis_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    else:
        raise DeserializationError("MediaAnalysisJobDescription.output_config required")
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("Results") is not None:
        import capo_rekognition.types.media_analysis_results

        out["results"] = (
            capo_rekognition.types.media_analysis_results.deserialize_aws_json_1_1(
                data["Results"]
            )
        )
    if data.get("ManifestSummary") is not None:
        import capo_rekognition.types.media_analysis_manifest_summary

        out["manifest_summary"] = (
            capo_rekognition.types.media_analysis_manifest_summary.deserialize_aws_json_1_1(
                data["ManifestSummary"]
            )
        )
    return out
