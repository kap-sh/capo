"""Generated from Smithy shape ``com.amazonaws.greengrassv2#IoTJobAbortConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_greengrassv2.types.io_t_job_abort_criteria_list


class IoTJobAbortConfig(TypedDict, closed=True):
    criteria_list: (
        "capo_greengrassv2.types.io_t_job_abort_criteria_list.IoTJobAbortCriteriaList"
    )
    """<p>The list of criteria that define when and how to cancel the configuration deployment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IoTJobAbortConfig) -> dict:
    out: dict = {}
    import capo_greengrassv2.types.io_t_job_abort_criteria_list

    out["criteriaList"] = (
        capo_greengrassv2.types.io_t_job_abort_criteria_list.serialize_json(
            value["criteria_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> IoTJobAbortConfig:
    out: IoTJobAbortConfig = {}  # type: ignore[typeddict-item]
    if data.get("criteriaList") is not None:
        import capo_greengrassv2.types.io_t_job_abort_criteria_list

        out["criteria_list"] = (
            capo_greengrassv2.types.io_t_job_abort_criteria_list.deserialize_json(
                data["criteriaList"]
            )
        )
    else:
        out["criteria_list"] = []
    return out
