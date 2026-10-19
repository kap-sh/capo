"""Generated from Smithy shape ``com.amazonaws.braket#SearchQuantumTasksFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.search_quantum_tasks_filter_operator
    import capo_braket.types.string64
    import capo_braket.types.string256_list


class SearchQuantumTasksFilter(TypedDict, closed=True):
    name: "capo_braket.types.string64.String64"
    """<p>The name of the quantum task parameter to filter based on. Filter name can be either <code>quantumTaskArn</code>, <code>deviceArn</code>, <code>jobArn</code>, <code>status</code> or <code>createdAt</code>.</p>"""
    values: "capo_braket.types.string256_list.String256List"
    """<p>The values used to filter quantum tasks based on the filter name and operator.</p>"""
    operator: "capo_braket.types.search_quantum_tasks_filter_operator.SearchQuantumTasksFilterOperator"
    """<p>An operator to use for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchQuantumTasksFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_braket.types.string256_list

    out["values"] = capo_braket.types.string256_list.serialize_json(value["values"])
    out["operator"] = value["operator"]
    return out


def deserialize_json(data: dict) -> SearchQuantumTasksFilter:
    out: SearchQuantumTasksFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("values") is not None:
        import capo_braket.types.string256_list

        out["values"] = capo_braket.types.string256_list.deserialize_json(
            data["values"]
        )
    else:
        out["values"] = []
    if data.get("operator") is not None:
        out["operator"] = data["operator"]
    else:
        out["operator"] = ""
    return out
