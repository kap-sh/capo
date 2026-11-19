"""Generated from Smithy shape ``com.amazonaws.route53domains#ListOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.list_operations_sort_attribute_name
    import capo_route_53_domains.types.operation_status_list
    import capo_route_53_domains.types.operation_type_list
    import capo_route_53_domains.types.page_marker
    import capo_route_53_domains.types.page_max_items
    import capo_route_53_domains.types.sort_order
    import capo_route_53_domains.types.timestamp


class ListOperationsRequest(TypedDict, closed=True):
    submitted_since: NotRequired["capo_route_53_domains.types.timestamp.Timestamp"]
    """<p>An optional parameter that lets you get information about all the operations that you submitted after a specified date and time. Specify the date and time in Unix time format and Coordinated Universal time (UTC).</p>"""
    marker: NotRequired["capo_route_53_domains.types.page_marker.PageMarker"]
    """<p>For an initial request for a list of operations, omit this element. If the number of operations that are not yet complete is greater than the value that you specified for <code>MaxItems</code>, you can use <code>Marker</code> to return additional operations. Get the value of <code>NextPageMarker</code> from the previous response, and submit another request that includes the value of <code>NextPageMarker</code> in the <code>Marker</code> element.</p>"""
    max_items: NotRequired["capo_route_53_domains.types.page_max_items.PageMaxItems"]
    """<p>Number of domains to be returned.</p> <p>Default: 20</p>"""
    status: NotRequired[
        "capo_route_53_domains.types.operation_status_list.OperationStatusList"
    ]
    """<p> The status of the operations. </p>"""
    type: NotRequired[
        "capo_route_53_domains.types.operation_type_list.OperationTypeList"
    ]
    """<p> An arrays of the domains operation types. </p>"""
    sort_by: NotRequired[
        "capo_route_53_domains.types.list_operations_sort_attribute_name.ListOperationsSortAttributeName"
    ]
    """<p> The sort type for returned values. </p>"""
    sort_order: NotRequired["capo_route_53_domains.types.sort_order.SortOrder"]
    """<p> The sort order for returned values, either ascending or descending. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOperationsRequest) -> dict:
    out: dict = {}
    if "submitted_since" in value:
        import capo_route_53_domains.types.timestamp

        out["SubmittedSince"] = (
            capo_route_53_domains.types.timestamp.serialize_aws_json_1_1(
                value["submitted_since"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    if "status" in value:
        import capo_route_53_domains.types.operation_status_list

        out["Status"] = (
            capo_route_53_domains.types.operation_status_list.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "type" in value:
        import capo_route_53_domains.types.operation_type_list

        out["Type"] = (
            capo_route_53_domains.types.operation_type_list.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "sort_by" in value:
        import capo_route_53_domains.types.list_operations_sort_attribute_name

        out["SortBy"] = (
            capo_route_53_domains.types.list_operations_sort_attribute_name.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_route_53_domains.types.sort_order

        out["SortOrder"] = (
            capo_route_53_domains.types.sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOperationsRequest:
    out: ListOperationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubmittedSince") is not None:
        import capo_route_53_domains.types.timestamp

        out["submitted_since"] = (
            capo_route_53_domains.types.timestamp.deserialize_aws_json_1_1(
                data["SubmittedSince"]
            )
        )
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    if data.get("Status") is not None:
        import capo_route_53_domains.types.operation_status_list

        out["status"] = (
            capo_route_53_domains.types.operation_status_list.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("Type") is not None:
        import capo_route_53_domains.types.operation_type_list

        out["type"] = (
            capo_route_53_domains.types.operation_type_list.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("SortBy") is not None:
        import capo_route_53_domains.types.list_operations_sort_attribute_name

        out["sort_by"] = (
            capo_route_53_domains.types.list_operations_sort_attribute_name.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_route_53_domains.types.sort_order

        out["sort_order"] = (
            capo_route_53_domains.types.sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOperationsRequest) -> dict:
    out: dict = {}
    if "submitted_since" in value:
        import capo_route_53_domains.types.timestamp

        out["SubmittedSince"] = capo_route_53_domains.types.timestamp.serialize_cbor(
            value["submitted_since"]
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    if "status" in value:
        import capo_route_53_domains.types.operation_status_list

        out["Status"] = (
            capo_route_53_domains.types.operation_status_list.serialize_cbor(
                value["status"]
            )
        )
    if "type" in value:
        import capo_route_53_domains.types.operation_type_list

        out["Type"] = capo_route_53_domains.types.operation_type_list.serialize_cbor(
            value["type"]
        )
    if "sort_by" in value:
        import capo_route_53_domains.types.list_operations_sort_attribute_name

        out["SortBy"] = (
            capo_route_53_domains.types.list_operations_sort_attribute_name.serialize_cbor(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_route_53_domains.types.sort_order

        out["SortOrder"] = capo_route_53_domains.types.sort_order.serialize_cbor(
            value["sort_order"]
        )
    return out


def deserialize_cbor(data: dict) -> ListOperationsRequest:
    out: ListOperationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("SubmittedSince") is not None:
        import capo_route_53_domains.types.timestamp

        out["submitted_since"] = capo_route_53_domains.types.timestamp.deserialize_cbor(
            data["SubmittedSince"]
        )
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    if data.get("Status") is not None:
        import capo_route_53_domains.types.operation_status_list

        out["status"] = (
            capo_route_53_domains.types.operation_status_list.deserialize_cbor(
                data["Status"]
            )
        )
    if data.get("Type") is not None:
        import capo_route_53_domains.types.operation_type_list

        out["type"] = capo_route_53_domains.types.operation_type_list.deserialize_cbor(
            data["Type"]
        )
    if data.get("SortBy") is not None:
        import capo_route_53_domains.types.list_operations_sort_attribute_name

        out["sort_by"] = (
            capo_route_53_domains.types.list_operations_sort_attribute_name.deserialize_cbor(
                data["SortBy"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_route_53_domains.types.sort_order

        out["sort_order"] = capo_route_53_domains.types.sort_order.deserialize_cbor(
            data["SortOrder"]
        )
    return out
