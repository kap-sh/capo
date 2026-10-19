"""Generated from Smithy shape ``com.amazonaws.iot#AbortConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.abort_criteria_list


class AbortConfig(TypedDict, closed=True):
    criteria_list: "capo_iot.types.abort_criteria_list.AbortCriteriaList"
    """<p>The list of criteria that determine when and how to abort the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AbortConfig) -> dict:
    out: dict = {}
    import capo_iot.types.abort_criteria_list

    out["criteriaList"] = capo_iot.types.abort_criteria_list.serialize_json(
        value["criteria_list"]
    )
    return out


def deserialize_json(data: dict) -> AbortConfig:
    out: AbortConfig = {}  # type: ignore[typeddict-item]
    if data.get("criteriaList") is not None:
        import capo_iot.types.abort_criteria_list

        out["criteria_list"] = capo_iot.types.abort_criteria_list.deserialize_json(
            data["criteriaList"]
        )
    else:
        out["criteria_list"] = []
    return out
