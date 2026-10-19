"""Generated from Smithy shape ``com.amazonaws.glue#BatchStopJobRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.batch_stop_job_run_job_run_id_list
    import capo_glue.types.name_string


class BatchStopJobRunRequest(TypedDict, closed=True):
    job_name: "capo_glue.types.name_string.NameString"
    """<p>The name of the job definition for which to stop job runs.</p>"""
    job_run_ids: (
        "capo_glue.types.batch_stop_job_run_job_run_id_list.BatchStopJobRunJobRunIdList"
    )
    """<p>A list of the <code>JobRunIds</code> that should be stopped for that job definition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchStopJobRunRequest) -> dict:
    out: dict = {}
    out["JobName"] = value["job_name"]
    import capo_glue.types.batch_stop_job_run_job_run_id_list

    out["JobRunIds"] = (
        capo_glue.types.batch_stop_job_run_job_run_id_list.serialize_aws_json_1_1(
            value["job_run_ids"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchStopJobRunRequest:
    out: BatchStopJobRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("JobName") is not None:
        out["job_name"] = data["JobName"]
    else:
        out["job_name"] = ""
    if data.get("JobRunIds") is not None:
        import capo_glue.types.batch_stop_job_run_job_run_id_list

        out["job_run_ids"] = (
            capo_glue.types.batch_stop_job_run_job_run_id_list.deserialize_aws_json_1_1(
                data["JobRunIds"]
            )
        )
    else:
        out["job_run_ids"] = []
    return out
