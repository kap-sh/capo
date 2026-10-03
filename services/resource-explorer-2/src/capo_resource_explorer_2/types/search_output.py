"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#SearchOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.resource_count
    import capo_resource_explorer_2.types.resource_list


class SearchOutput(TypedDict, closed=True):
    resources: NotRequired["capo_resource_explorer_2.types.resource_list.ResourceList"]
    """<p>The list of structures that describe the resources that match the query.</p>"""
    next_token: NotRequired["str"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the <code>NextToken</code> response element comes back as <code>null</code>. The pagination tokens expire after 24 hours.</p>"""
    view_arn: NotRequired["str"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view that this operation used to perform the search.</p>"""
    count: NotRequired["capo_resource_explorer_2.types.resource_count.ResourceCount"]
    """<p>The number of resources that match the query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchOutput) -> dict:
    out: dict = {}
    if "resources" in value:
        import capo_resource_explorer_2.types.resource_list

        out["Resources"] = capo_resource_explorer_2.types.resource_list.serialize_json(
            value["resources"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "view_arn" in value:
        out["ViewArn"] = value["view_arn"]
    if "count" in value:
        import capo_resource_explorer_2.types.resource_count

        out["Count"] = capo_resource_explorer_2.types.resource_count.serialize_json(
            value["count"]
        )
    return out


def deserialize_json(data: dict) -> SearchOutput:
    out: SearchOutput = {}  # type: ignore[typeddict-item]
    if data.get("Resources") is not None:
        import capo_resource_explorer_2.types.resource_list

        out["resources"] = (
            capo_resource_explorer_2.types.resource_list.deserialize_json(
                data["Resources"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ViewArn") is not None:
        out["view_arn"] = data["ViewArn"]
    if data.get("Count") is not None:
        import capo_resource_explorer_2.types.resource_count

        out["count"] = capo_resource_explorer_2.types.resource_count.deserialize_json(
            data["Count"]
        )
    return out
