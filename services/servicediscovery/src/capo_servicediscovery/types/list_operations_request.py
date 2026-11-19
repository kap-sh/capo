"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ListOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.max_results
    import capo_servicediscovery.types.next_token
    import capo_servicediscovery.types.operation_filters


class ListOperationsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_servicediscovery.types.next_token.NextToken"]
    """<p>For the first <code>ListOperations</code> request, omit this value.</p> <p>If the response contains <code>NextToken</code>, submit another <code>ListOperations</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p> <note> <p>Cloud Map gets <code>MaxResults</code> operations and then filters them based on the specified criteria. It's possible that no operations in the first <code>MaxResults</code> operations matched the specified criteria but that subsequent groups of <code>MaxResults</code> operations do contain operations that match the criteria.</p> </note>"""
    max_results: NotRequired["capo_servicediscovery.types.max_results.MaxResults"]
    """<p>The maximum number of items that you want Cloud Map to return in the response to a <code>ListOperations</code> request. If you don't specify a value for <code>MaxResults</code>, Cloud Map returns up to 100 operations.</p>"""
    filters: NotRequired[
        "capo_servicediscovery.types.operation_filters.OperationFilters"
    ]
    """<p>A complex type that contains specifications for the operations that you want to list, for example, operations that you started between a specified start date and end date.</p> <p>If you specify more than one filter, an operation must match all filters to be returned by <code>ListOperations</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOperationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import capo_servicediscovery.types.operation_filters

        out["Filters"] = (
            capo_servicediscovery.types.operation_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOperationsRequest:
    out: ListOperationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filters") is not None:
        import capo_servicediscovery.types.operation_filters

        out["filters"] = (
            capo_servicediscovery.types.operation_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOperationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import capo_servicediscovery.types.operation_filters

        out["Filters"] = capo_servicediscovery.types.operation_filters.serialize_cbor(
            value["filters"]
        )
    return out


def deserialize_cbor(data: dict) -> ListOperationsRequest:
    out: ListOperationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filters") is not None:
        import capo_servicediscovery.types.operation_filters

        out["filters"] = capo_servicediscovery.types.operation_filters.deserialize_cbor(
            data["Filters"]
        )
    return out
