"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#ServiceView``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_resource_explorer_2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.included_property_list
    import capo_resource_explorer_2.types.search_filter
    import capo_resource_explorer_2.types.service_linked_recorder_info
    import capo_resource_explorer_2.types.service_view_name


class ServiceView(TypedDict, closed=True):
    service_view_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the service view.</p>"""
    service_view_name: NotRequired[
        "capo_resource_explorer_2.types.service_view_name.ServiceViewName"
    ]
    """<p>The name of the service view.</p>"""
    filters: NotRequired["capo_resource_explorer_2.types.search_filter.SearchFilter"]
    included_properties: NotRequired[
        "capo_resource_explorer_2.types.included_property_list.IncludedPropertyList"
    ]
    """<p>A list of additional resource properties that are included in this view for search and filtering purposes.</p>"""
    streaming_access_for_service: NotRequired["str"]
    """<p>The Amazon Web Services service that has streaming access to this view's data.</p>"""
    scope_type: NotRequired["str"]
    """<p>The scope type of the service view, which determines what resources are included.</p>"""
    service_linked_recorder: NotRequired[
        "capo_resource_explorer_2.types.service_linked_recorder_info.ServiceLinkedRecorderInfo"
    ]
    """<p>Information about the service-linked recorder associated with this service view. When a service view is paired with a service-linked recorder, Resource Explorer uses the recorder's resource type list to filter search results and streaming data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceView) -> dict:
    out: dict = {}
    out["ServiceViewArn"] = value["service_view_arn"]
    if "service_view_name" in value:
        out["ServiceViewName"] = value["service_view_name"]
    if "filters" in value:
        import capo_resource_explorer_2.types.search_filter

        out["Filters"] = capo_resource_explorer_2.types.search_filter.serialize_json(
            value["filters"]
        )
    if "included_properties" in value:
        import capo_resource_explorer_2.types.included_property_list

        out["IncludedProperties"] = (
            capo_resource_explorer_2.types.included_property_list.serialize_json(
                value["included_properties"]
            )
        )
    if "streaming_access_for_service" in value:
        out["StreamingAccessForService"] = value["streaming_access_for_service"]
    if "scope_type" in value:
        out["ScopeType"] = value["scope_type"]
    if "service_linked_recorder" in value:
        import capo_resource_explorer_2.types.service_linked_recorder_info

        out["ServiceLinkedRecorder"] = (
            capo_resource_explorer_2.types.service_linked_recorder_info.serialize_json(
                value["service_linked_recorder"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceView:
    out: ServiceView = {}  # type: ignore[typeddict-item]
    if data.get("ServiceViewArn") is not None:
        out["service_view_arn"] = data["ServiceViewArn"]
    else:
        raise DeserializationError("ServiceView.service_view_arn required")
    if data.get("ServiceViewName") is not None:
        out["service_view_name"] = data["ServiceViewName"]
    if data.get("Filters") is not None:
        import capo_resource_explorer_2.types.search_filter

        out["filters"] = capo_resource_explorer_2.types.search_filter.deserialize_json(
            data["Filters"]
        )
    if data.get("IncludedProperties") is not None:
        import capo_resource_explorer_2.types.included_property_list

        out["included_properties"] = (
            capo_resource_explorer_2.types.included_property_list.deserialize_json(
                data["IncludedProperties"]
            )
        )
    if data.get("StreamingAccessForService") is not None:
        out["streaming_access_for_service"] = data["StreamingAccessForService"]
    if data.get("ScopeType") is not None:
        out["scope_type"] = data["ScopeType"]
    if data.get("ServiceLinkedRecorder") is not None:
        import capo_resource_explorer_2.types.service_linked_recorder_info

        out["service_linked_recorder"] = (
            capo_resource_explorer_2.types.service_linked_recorder_info.deserialize_json(
                data["ServiceLinkedRecorder"]
            )
        )
    return out


def redact_sensitive(value: ServiceView) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "filters" in value:
        out["filters"] = "*** Sensitive Data Redacted ***"
    return out
