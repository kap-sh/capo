"""Generated from Smithy shape ``com.amazonaws.iot#AwsJobAbortConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_job_abort_criteria_list


class AwsJobAbortConfig(TypedDict, closed=True):
    abort_criteria_list: (
        "capo_iot.types.aws_job_abort_criteria_list.AwsJobAbortCriteriaList"
    )
    """<p>The list of criteria that determine when and how to abort the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsJobAbortConfig) -> dict:
    out: dict = {}
    import capo_iot.types.aws_job_abort_criteria_list

    out["abortCriteriaList"] = (
        capo_iot.types.aws_job_abort_criteria_list.serialize_json(
            value["abort_criteria_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> AwsJobAbortConfig:
    out: AwsJobAbortConfig = {}  # type: ignore[typeddict-item]
    if data.get("abortCriteriaList") is not None:
        import capo_iot.types.aws_job_abort_criteria_list

        out["abort_criteria_list"] = (
            capo_iot.types.aws_job_abort_criteria_list.deserialize_json(
                data["abortCriteriaList"]
            )
        )
    else:
        out["abort_criteria_list"] = []
    return out
