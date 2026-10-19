"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ProjectListFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.comparison_operator
    import capo_codecatalyst.types.filter_key
    import capo_codecatalyst.types.string_list


class ProjectListFilter(TypedDict, closed=True):
    key: "capo_codecatalyst.types.filter_key.FilterKey"
    """<p>A key that can be used to sort results.</p>"""
    values: "capo_codecatalyst.types.string_list.StringList"
    """<p>The values of the key.</p>"""
    comparison_operator: NotRequired[
        "capo_codecatalyst.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The operator used to compare the fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectListFilter) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_codecatalyst.types.string_list

    out["values"] = capo_codecatalyst.types.string_list.serialize_json(value["values"])
    if "comparison_operator" in value:
        out["comparisonOperator"] = value["comparison_operator"]
    return out


def deserialize_json(data: dict) -> ProjectListFilter:
    out: ProjectListFilter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("values") is not None:
        import capo_codecatalyst.types.string_list

        out["values"] = capo_codecatalyst.types.string_list.deserialize_json(
            data["values"]
        )
    else:
        out["values"] = []
    if data.get("comparisonOperator") is not None:
        out["comparison_operator"] = data["comparisonOperator"]
    return out
