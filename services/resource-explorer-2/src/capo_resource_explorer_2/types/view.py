"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#View``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resource_explorer_2.types.included_property_list
    import capo_resource_explorer_2.types.search_filter
    import capo_resource_explorer_2.types.view_name


class View(TypedDict, closed=True):
    view_arn: NotRequired["str"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the view.</p>"""
    view_name: NotRequired["capo_resource_explorer_2.types.view_name.ViewName"]
    """<p>The name of the view.</p>"""
    owner: NotRequired["str"]
    """<p>The Amazon Web Services account that owns this view.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when this view was last modified.</p>"""
    scope: NotRequired["str"]
    """<p>An <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of an Amazon Web Services account, an organization, or an organizational unit (OU) that specifies whether this view includes resources from only the specified Amazon Web Services account, all accounts in the specified organization, or all accounts in the specified OU.</p> <p>If not specified, the value defaults to the Amazon Web Services account used to call this operation.</p>"""
    included_properties: NotRequired[
        "capo_resource_explorer_2.types.included_property_list.IncludedPropertyList"
    ]
    """<p>A structure that contains additional information about the view.</p>"""
    filters: NotRequired["capo_resource_explorer_2.types.search_filter.SearchFilter"]
    """<p>An array of <a>SearchFilter</a> objects that specify which resources can be included in the results of queries made using this view.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: View) -> dict:
    out: dict = {}
    if "view_arn" in value:
        out["ViewArn"] = value["view_arn"]
    if "view_name" in value:
        out["ViewName"] = value["view_name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "last_updated_at" in value:
        import capo_resource_explorer_2._protocol.serialize

        out["LastUpdatedAt"] = (
            capo_resource_explorer_2._protocol.serialize.fmt_date_time(
                value["last_updated_at"]
            )
        )
    if "scope" in value:
        out["Scope"] = value["scope"]
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


def deserialize_json(data: dict) -> View:
    out: View = {}  # type: ignore[typeddict-item]
    if data.get("ViewArn") is not None:
        out["view_arn"] = data["ViewArn"]
    if data.get("ViewName") is not None:
        out["view_name"] = data["ViewName"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("LastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["LastUpdatedAt"].replace("Z", "+00:00")
        )
    if data.get("Scope") is not None:
        out["scope"] = data["Scope"]
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
