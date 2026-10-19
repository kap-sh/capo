"""Generated from Smithy shape ``com.amazonaws.lakeformation#UpdateRLSPolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.predicate_string


class UpdateRLSPolicyRequest(TypedDict, closed=True):
    name: "capo_lakeformation.types.name_string.NameString"
    """<p>The name of the row-level security policy to update.</p>"""
    filter_expression: NotRequired[
        "capo_lakeformation.types.predicate_string.PredicateString"
    ]
    """<p>The new filter predicate, written in a SQL-like syntax, that replaces the policy's current filter expression.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRLSPolicyRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "filter_expression" in value:
        out["FilterExpression"] = value["filter_expression"]
    return out


def deserialize_json(data: dict) -> UpdateRLSPolicyRequest:
    out: UpdateRLSPolicyRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("FilterExpression") is not None:
        out["filter_expression"] = data["FilterExpression"]
    return out
