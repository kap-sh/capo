"""Generated from Smithy shape ``com.amazonaws.braket#SearchJobsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.search_jobs_filter_operator
    import capo_braket.types.string64
    import capo_braket.types.string256_list


class SearchJobsFilter(TypedDict, closed=True):
    name: "capo_braket.types.string64.String64"
    """<p>The name of the hybrid job parameter to filter based on. Filter name can be either <code>jobArn</code> or <code>createdAt</code>. </p>"""
    values: "capo_braket.types.string256_list.String256List"
    """<p>The values used to filter hybrid jobs based on the filter name and operator.</p>"""
    operator: "capo_braket.types.search_jobs_filter_operator.SearchJobsFilterOperator"
    """<p>An operator to use for the filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobsFilter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_braket.types.string256_list

    out["values"] = capo_braket.types.string256_list.serialize_json(value["values"])
    out["operator"] = value["operator"]
    return out


def deserialize_json(data: dict) -> SearchJobsFilter:
    out: SearchJobsFilter = {}  # type: ignore[typeddict-item]
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
