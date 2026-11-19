"""Generated from Smithy shape ``com.amazonaws.braket#SearchJobsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_braket.types.search_jobs_filter_operator
    import capo_braket.types.string64
    import capo_braket.types.string256_list


class SearchJobsFilter(TypedDict, closed=True):
    name: "capo_braket.types.string64.String64"
    """<p>The name of the hybrid job parameter to filter based on. Supported filter names:</p> <p> <code>jobArn</code> — Filter by the job ARN. Supports the <code>EQUAL</code> operator only. Cannot be combined with other filters.</p> <p> <code>jobName</code> — Filter by the job name. Supports the <code>EQUAL</code> operator for exact match, or the <code>CONTAINS</code> operator for substring match. For example, use <code>CONTAINS</code> with a value of <code>my-experiment</code> to find all jobs whose name includes "my-experiment".</p> <p> <code>deviceArn</code> — Filter by the target device. Supports the <code>EQUAL</code> operator only. The value can be a device ARN (for example, <code>arn:aws:braket:us-east-1::device/qpu/ionq/Aria-1</code>) or a local simulator identifier (for example, <code>local:braket/default</code>).</p> <p> <code>createdAt</code> — Filter by the job creation time. Supports the <code>EQUAL</code>, <code>GT</code>, <code>GTE</code>, <code>LT</code>, <code>LTE</code>, and <code>BETWEEN</code> operators. Values must be in RFC 3339 date-time format.</p>"""
    values: "capo_braket.types.string256_list.String256List"
    """<p>The values used to filter hybrid jobs based on the filter name and operator. Each filter accepts an array of values. Most filters accept a single value, except <code>createdAt</code> with the <code>BETWEEN</code> operator, which requires exactly two values.</p>"""
    operator: "capo_braket.types.search_jobs_filter_operator.SearchJobsFilterOperator"
    """<p>An operator to use for the filter. The supported operators depend on the filter name. See the <code>name</code> parameter for details.</p>"""


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
