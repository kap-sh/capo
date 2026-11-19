"""Generated from Smithy shape ``com.amazonaws.translate#TextTranslationJobFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_translate.types.job_name
    import capo_translate.types.job_status
    import capo_translate.types.timestamp


class TextTranslationJobFilter(TypedDict, closed=True):
    job_name: NotRequired["capo_translate.types.job_name.JobName"]
    """<p>Filters the list of jobs by name.</p>"""
    job_status: NotRequired["capo_translate.types.job_status.JobStatus"]
    """<p>Filters the list of jobs based by job status.</p>"""
    submitted_before_time: NotRequired["capo_translate.types.timestamp.Timestamp"]
    """<p>Filters the list of jobs based on the time that the job was submitted for processing and returns only the jobs submitted before the specified time. Jobs are returned in ascending order, oldest to newest.</p>"""
    submitted_after_time: NotRequired["capo_translate.types.timestamp.Timestamp"]
    """<p>Filters the list of jobs based on the time that the job was submitted for processing and returns only the jobs submitted after the specified time. Jobs are returned in descending order, newest to oldest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TextTranslationJobFilter) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import capo_translate.types.job_status

        out["JobStatus"] = capo_translate.types.job_status.serialize_aws_json_1_1(
            value["job_status"]
        )
    if "submitted_before_time" in value:
        import capo_translate.types.timestamp

        out["SubmittedBeforeTime"] = (
            capo_translate.types.timestamp.serialize_aws_json_1_1(
                value["submitted_before_time"]
            )
        )
    if "submitted_after_time" in value:
        import capo_translate.types.timestamp

        out["SubmittedAfterTime"] = (
            capo_translate.types.timestamp.serialize_aws_json_1_1(
                value["submitted_after_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TextTranslationJobFilter:
    out: TextTranslationJobFilter = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobStatus") is not None:
        import capo_translate.types.job_status

        out["job_status"] = capo_translate.types.job_status.deserialize_aws_json_1_1(
            data["JobStatus"]
        )
    if data.get("SubmittedBeforeTime") is not None:
        import capo_translate.types.timestamp

        out["submitted_before_time"] = (
            capo_translate.types.timestamp.deserialize_aws_json_1_1(
                data["SubmittedBeforeTime"]
            )
        )
    if data.get("SubmittedAfterTime") is not None:
        import capo_translate.types.timestamp

        out["submitted_after_time"] = (
            capo_translate.types.timestamp.deserialize_aws_json_1_1(
                data["SubmittedAfterTime"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TextTranslationJobFilter) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "job_status" in value:
        import capo_translate.types.job_status

        out["JobStatus"] = capo_translate.types.job_status.serialize_cbor(
            value["job_status"]
        )
    if "submitted_before_time" in value:
        import capo_translate.types.timestamp

        out["SubmittedBeforeTime"] = capo_translate.types.timestamp.serialize_cbor(
            value["submitted_before_time"]
        )
    if "submitted_after_time" in value:
        import capo_translate.types.timestamp

        out["SubmittedAfterTime"] = capo_translate.types.timestamp.serialize_cbor(
            value["submitted_after_time"]
        )
    return out


def deserialize_cbor(data: dict) -> TextTranslationJobFilter:
    out: TextTranslationJobFilter = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    if data.get("JobStatus") is not None:
        import capo_translate.types.job_status

        out["job_status"] = capo_translate.types.job_status.deserialize_cbor(
            data["JobStatus"]
        )
    if data.get("SubmittedBeforeTime") is not None:
        import capo_translate.types.timestamp

        out["submitted_before_time"] = capo_translate.types.timestamp.deserialize_cbor(
            data["SubmittedBeforeTime"]
        )
    if data.get("SubmittedAfterTime") is not None:
        import capo_translate.types.timestamp

        out["submitted_after_time"] = capo_translate.types.timestamp.deserialize_cbor(
            data["SubmittedAfterTime"]
        )
    return out
