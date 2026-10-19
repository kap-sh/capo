"""Generated from Smithy shape ``com.amazonaws.iot#JobExecutionsRetryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.retry_criteria_list


class JobExecutionsRetryConfig(TypedDict, closed=True):
    criteria_list: "capo_iot.types.retry_criteria_list.RetryCriteriaList"
    """<p>The list of criteria that determines how many retries are allowed for each failure type for a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobExecutionsRetryConfig) -> dict:
    out: dict = {}
    import capo_iot.types.retry_criteria_list

    out["criteriaList"] = capo_iot.types.retry_criteria_list.serialize_json(
        value["criteria_list"]
    )
    return out


def deserialize_json(data: dict) -> JobExecutionsRetryConfig:
    out: JobExecutionsRetryConfig = {}  # type: ignore[typeddict-item]
    if data.get("criteriaList") is not None:
        import capo_iot.types.retry_criteria_list

        out["criteria_list"] = capo_iot.types.retry_criteria_list.deserialize_json(
            data["criteriaList"]
        )
    else:
        out["criteria_list"] = []
    return out
