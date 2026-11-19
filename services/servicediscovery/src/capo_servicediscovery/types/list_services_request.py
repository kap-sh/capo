"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ListServicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.max_results
    import capo_servicediscovery.types.next_token
    import capo_servicediscovery.types.service_filters


class ListServicesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_servicediscovery.types.next_token.NextToken"]
    """<p>For the first <code>ListServices</code> request, omit this value.</p> <p>If the response contains <code>NextToken</code>, submit another <code>ListServices</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p> <note> <p>Cloud Map gets <code>MaxResults</code> services and then filters them based on the specified criteria. It's possible that no services in the first <code>MaxResults</code> services matched the specified criteria but that subsequent groups of <code>MaxResults</code> services do contain services that match the criteria.</p> </note>"""
    max_results: NotRequired["capo_servicediscovery.types.max_results.MaxResults"]
    """<p>The maximum number of services that you want Cloud Map to return in the response to a <code>ListServices</code> request. If you don't specify a value for <code>MaxResults</code>, Cloud Map returns up to 100 services.</p>"""
    filters: NotRequired["capo_servicediscovery.types.service_filters.ServiceFilters"]
    """<p>A complex type that contains specifications for the namespaces that you want to list services for. </p> <p>If you specify more than one filter, an operation must match all filters to be returned by <code>ListServices</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServicesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import capo_servicediscovery.types.service_filters

        out["Filters"] = (
            capo_servicediscovery.types.service_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServicesRequest:
    out: ListServicesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filters") is not None:
        import capo_servicediscovery.types.service_filters

        out["filters"] = (
            capo_servicediscovery.types.service_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListServicesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import capo_servicediscovery.types.service_filters

        out["Filters"] = capo_servicediscovery.types.service_filters.serialize_cbor(
            value["filters"]
        )
    return out


def deserialize_cbor(data: dict) -> ListServicesRequest:
    out: ListServicesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filters") is not None:
        import capo_servicediscovery.types.service_filters

        out["filters"] = capo_servicediscovery.types.service_filters.deserialize_cbor(
            data["Filters"]
        )
    return out
