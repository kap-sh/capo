"""Generated from Smithy shape ``com.amazonaws.cloudsearchdomain#FieldStats``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudsearch_domain.types.double
    import capo_cloudsearch_domain.types.long
    import capo_cloudsearch_domain.types.string


class FieldStats(TypedDict, closed=True):
    min: NotRequired["capo_cloudsearch_domain.types.string.String"]
    """<p>The minimum value found in the specified field in the result set.</p> <p>If the field is numeric (<code>int</code>, <code>int-array</code>, <code>double</code>, or <code>double-array</code>), <code>min</code> is the string representation of a double-precision 64-bit floating point value. If the field is <code>date</code> or <code>date-array</code>, <code>min</code> is the string representation of a date with the format specified in <a href="http://tools.ietf.org/html/rfc3339">IETF RFC3339</a>: yyyy-mm-ddTHH:mm:ss.SSSZ.</p>"""
    max: NotRequired["capo_cloudsearch_domain.types.string.String"]
    """<p>The maximum value found in the specified field in the result set.</p> <p>If the field is numeric (<code>int</code>, <code>int-array</code>, <code>double</code>, or <code>double-array</code>), <code>max</code> is the string representation of a double-precision 64-bit floating point value. If the field is <code>date</code> or <code>date-array</code>, <code>max</code> is the string representation of a date with the format specified in <a href="http://tools.ietf.org/html/rfc3339">IETF RFC3339</a>: yyyy-mm-ddTHH:mm:ss.SSSZ.</p>"""
    count: "capo_cloudsearch_domain.types.long.Long"
    """<p>The number of documents that contain a value in the specified field in the result set.</p>"""
    missing: "capo_cloudsearch_domain.types.long.Long"
    """<p>The number of documents that do not contain a value in the specified field in the result set.</p>"""
    sum: "capo_cloudsearch_domain.types.double.Double"
    """<p>The sum of the field values across the documents in the result set. <code>null</code> for date fields.</p>"""
    sum_of_squares: "capo_cloudsearch_domain.types.double.Double"
    """<p>The sum of all field values in the result set squared.</p>"""
    mean: NotRequired["capo_cloudsearch_domain.types.string.String"]
    """<p>The average of the values found in the specified field in the result set.</p> <p>If the field is numeric (<code>int</code>, <code>int-array</code>, <code>double</code>, or <code>double-array</code>), <code>mean</code> is the string representation of a double-precision 64-bit floating point value. If the field is <code>date</code> or <code>date-array</code>, <code>mean</code> is the string representation of a date with the format specified in <a href="http://tools.ietf.org/html/rfc3339">IETF RFC3339</a>: yyyy-mm-ddTHH:mm:ss.SSSZ.</p>"""
    stddev: "capo_cloudsearch_domain.types.double.Double"
    """<p>The standard deviation of the values in the specified field in the result set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldStats) -> dict:
    out: dict = {}
    if "min" in value:
        out["min"] = value["min"]
    if "max" in value:
        out["max"] = value["max"]
    out["count"] = value.get("count", 0)
    out["missing"] = value.get("missing", 0)
    out["sum"] = (
        "NaN"
        if value.get("sum", 0) != value.get("sum", 0)
        else "Infinity"
        if value.get("sum", 0) == float("inf")
        else "-Infinity"
        if value.get("sum", 0) == float("-inf")
        else value.get("sum", 0)
    )
    out["sumOfSquares"] = (
        "NaN"
        if value.get("sum_of_squares", 0) != value.get("sum_of_squares", 0)
        else "Infinity"
        if value.get("sum_of_squares", 0) == float("inf")
        else "-Infinity"
        if value.get("sum_of_squares", 0) == float("-inf")
        else value.get("sum_of_squares", 0)
    )
    if "mean" in value:
        out["mean"] = value["mean"]
    out["stddev"] = (
        "NaN"
        if value.get("stddev", 0) != value.get("stddev", 0)
        else "Infinity"
        if value.get("stddev", 0) == float("inf")
        else "-Infinity"
        if value.get("stddev", 0) == float("-inf")
        else value.get("stddev", 0)
    )
    return out


def deserialize_json(data: dict) -> FieldStats:
    out: FieldStats = {}  # type: ignore[typeddict-item]
    if data.get("min") is not None:
        out["min"] = data["min"]
    if data.get("max") is not None:
        out["max"] = data["max"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    else:
        out["count"] = 0
    if data.get("missing") is not None:
        out["missing"] = data["missing"]
    else:
        out["missing"] = 0
    if data.get("sum") is not None:
        out["sum"] = float(data["sum"])
    else:
        out["sum"] = 0
    if data.get("sumOfSquares") is not None:
        out["sum_of_squares"] = float(data["sumOfSquares"])
    else:
        out["sum_of_squares"] = 0
    if data.get("mean") is not None:
        out["mean"] = data["mean"]
    if data.get("stddev") is not None:
        out["stddev"] = float(data["stddev"])
    else:
        out["stddev"] = 0
    return out
