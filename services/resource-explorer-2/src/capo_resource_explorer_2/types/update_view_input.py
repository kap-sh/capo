"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#UpdateViewInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resource_explorer_2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.included_property_list
    import capo_resource_explorer_2.types.search_filter


class UpdateViewInput(TypedDict, closed=True):
    view_arn: "str"
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view that you want to modify.</p>"""
    included_properties: NotRequired[
        "capo_resource_explorer_2.types.included_property_list.IncludedPropertyList"
    ]
    """<p>Specifies optional fields that you want included in search results from this view. It is a list of objects that each describe a field to include.</p> <p>The default is an empty list, with no optional fields included in the results.</p>"""
    filters: NotRequired["capo_resource_explorer_2.types.search_filter.SearchFilter"]
    """<p>An array of strings that specify which resources are included in the results of queries made using this view. When you use this view in a <a>Search</a> operation, the filter string is combined with the search's <code>QueryString</code> parameter using a logical <code>AND</code> operator.</p> <p>For information about the supported syntax, see <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html">Search query reference for Resource Explorer</a> in the <i>Amazon Web Services Resource Explorer User Guide</i>.</p> <important> <p>This query string in the context of this operation supports only <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-filters">filter prefixes</a> with optional <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/using-search-query-syntax.html#query-syntax-operators">operators</a>. It doesn't support free-form text. For example, the string <code>region:us* service:ec2 -tag:stage=prod</code> includes all Amazon EC2 resources in any Amazon Web Services Region that begins with the letters <code>us</code> and is <i>not</i> tagged with a key <code>Stage</code> that has the value <code>prod</code>.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateViewInput) -> dict:
    out: dict = {}
    out["ViewArn"] = value["view_arn"]
    if "included_properties" in value:
        import capo_resource_explorer_2.types.included_property_list

        out["IncludedProperties"] = (
            capo_resource_explorer_2.types.included_property_list.serialize_json(
                value["included_properties"]
            )
        )
    if "filters" in value:
        import capo_resource_explorer_2.types.search_filter

        out["Filters"] = capo_resource_explorer_2.types.search_filter.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> UpdateViewInput:
    out: UpdateViewInput = {}  # type: ignore[typeddict-item]
    if data.get("ViewArn") is not None:
        out["view_arn"] = data["ViewArn"]
    else:
        raise DeserializationError("UpdateViewInput.view_arn required")
    if data.get("IncludedProperties") is not None:
        import capo_resource_explorer_2.types.included_property_list

        out["included_properties"] = (
            capo_resource_explorer_2.types.included_property_list.deserialize_json(
                data["IncludedProperties"]
            )
        )
    if data.get("Filters") is not None:
        import capo_resource_explorer_2.types.search_filter

        out["filters"] = capo_resource_explorer_2.types.search_filter.deserialize_json(
            data["Filters"]
        )
    return out
