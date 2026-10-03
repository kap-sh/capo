"""Generated from Smithy shape ``com.amazonaws.internetmonitor#FilterParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.filter_list
    import capo_internetmonitor.types.operator


class FilterParameter(TypedDict, closed=True):
    field: NotRequired["str"]
    """<p>A data field that you want to filter, to further scope your application's Internet Monitor data in a repository that you created by running a query. A field might be <code>city</code>, for example. The field must be one of the fields that was returned by the specific query that you used to create the repository.</p>"""
    operator: NotRequired["capo_internetmonitor.types.operator.Operator"]
    """<p>The operator to use with the filter field and a value, such as <code>not_equals</code>.</p>"""
    values: NotRequired["capo_internetmonitor.types.filter_list.FilterList"]
    """<p>One or more values to be used, together with the specified operator, to filter data for a query. For example, you could specify an array of values such as <code>["Seattle", "Redmond"]</code>. Values in the array are separated by commas.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterParameter) -> dict:
    out: dict = {}
    if "field" in value:
        out["Field"] = value["field"]
    if "operator" in value:
        out["Operator"] = value["operator"]
    if "values" in value:
        import capo_internetmonitor.types.filter_list

        out["Values"] = capo_internetmonitor.types.filter_list.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> FilterParameter:
    out: FilterParameter = {}  # type: ignore[typeddict-item]
    if data.get("Field") is not None:
        out["field"] = data["Field"]
    if data.get("Operator") is not None:
        out["operator"] = data["Operator"]
    if data.get("Values") is not None:
        import capo_internetmonitor.types.filter_list

        out["values"] = capo_internetmonitor.types.filter_list.deserialize_json(
            data["Values"]
        )
    return out
