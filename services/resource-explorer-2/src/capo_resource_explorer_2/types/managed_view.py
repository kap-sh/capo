"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ManagedView``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resource_explorer_2.types.included_property_list
    import capo_resource_explorer_2.types.search_filter


class ManagedView(TypedDict, closed=True):
    managed_view_arn: NotRequired["str"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of the managed view.</p>"""
    managed_view_name: NotRequired["str"]
    """<p>The name of the managed view. </p>"""
    trusted_service: NotRequired["str"]
    """<p>The service principal of the Amazon Web Services service that created and manages the managed view. </p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when this managed view was last modified.</p>"""
    owner: NotRequired["str"]
    """<p>The Amazon Web Services account that owns this managed view.</p>"""
    scope: NotRequired["str"]
    """<p>An <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon resource name (ARN)</a> of an Amazon Web Services account or organization that specifies whether this managed view includes resources from only the specified Amazon Web Services account or all accounts in the specified organization. </p>"""
    included_properties: NotRequired[
        "capo_resource_explorer_2.types.included_property_list.IncludedPropertyList"
    ]
    """<p>A structure that contains additional information about the managed view.</p>"""
    filters: NotRequired["capo_resource_explorer_2.types.search_filter.SearchFilter"]
    resource_policy: NotRequired["str"]
    """<p>The resource policy that defines access to the managed view. To learn more about this policy, review <a href="https://docs.aws.amazon.com/resource-explorer/latest/userguide/aws-managed-views.html">Managed views</a>.</p>"""
    version: NotRequired["str"]
    """<p>The version of the managed view. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedView) -> dict:
    out: dict = {}
    if "managed_view_arn" in value:
        out["ManagedViewArn"] = value["managed_view_arn"]
    if "managed_view_name" in value:
        out["ManagedViewName"] = value["managed_view_name"]
    if "trusted_service" in value:
        out["TrustedService"] = value["trusted_service"]
    if "last_updated_at" in value:
        import capo_resource_explorer_2._protocol.serialize

        out["LastUpdatedAt"] = (
            capo_resource_explorer_2._protocol.serialize.fmt_date_time(
                value["last_updated_at"]
            )
        )
    if "owner" in value:
        out["Owner"] = value["owner"]
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
    if "resource_policy" in value:
        out["ResourcePolicy"] = value["resource_policy"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ManagedView:
    out: ManagedView = {}  # type: ignore[typeddict-item]
    if data.get("ManagedViewArn") is not None:
        out["managed_view_arn"] = data["ManagedViewArn"]
    if data.get("ManagedViewName") is not None:
        out["managed_view_name"] = data["ManagedViewName"]
    if data.get("TrustedService") is not None:
        out["trusted_service"] = data["TrustedService"]
    if data.get("LastUpdatedAt") is not None:
        import datetime

        out["last_updated_at"] = datetime.datetime.fromisoformat(
            data["LastUpdatedAt"].replace("Z", "+00:00")
        )
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
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
    if data.get("ResourcePolicy") is not None:
        out["resource_policy"] = data["ResourcePolicy"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
