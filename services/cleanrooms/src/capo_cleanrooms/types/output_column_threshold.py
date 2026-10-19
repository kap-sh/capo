"""Generated from Smithy shape ``com.amazonaws.cleanrooms#OutputColumnThreshold``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_rule_column_name


class OutputColumnThreshold(TypedDict, closed=True):
    output_column_name: (
        "capo_cleanrooms.types.analysis_rule_column_name.AnalysisRuleColumnName"
    )
    """<p>The name of the output column that the override applies to. You can specify each column only once.</p>"""
    minimum_identity_count: "int"
    """<p>The minimum number of distinct identities that each query output group must represent for this column. Specify 0 to exempt the column from the threshold, or a value of 2 or greater to enforce a threshold.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputColumnThreshold) -> dict:
    out: dict = {}
    out["outputColumnName"] = value["output_column_name"]
    out["minimumIdentityCount"] = value["minimum_identity_count"]
    return out


def deserialize_json(data: dict) -> OutputColumnThreshold:
    out: OutputColumnThreshold = {}  # type: ignore[typeddict-item]
    if data.get("outputColumnName") is not None:
        out["output_column_name"] = data["outputColumnName"]
    else:
        out["output_column_name"] = ""
    if data.get("minimumIdentityCount") is not None:
        out["minimum_identity_count"] = data["minimumIdentityCount"]
    else:
        out["minimum_identity_count"] = 0
    return out
