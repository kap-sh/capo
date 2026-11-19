"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ListNamespacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.max_results
    import capo_servicediscovery.types.namespace_filters
    import capo_servicediscovery.types.next_token


class ListNamespacesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_servicediscovery.types.next_token.NextToken"]
    """<p>For the first <code>ListNamespaces</code> request, omit this value.</p> <p>If the response contains <code>NextToken</code>, submit another <code>ListNamespaces</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p> <note> <p>Cloud Map gets <code>MaxResults</code> namespaces and then filters them based on the specified criteria. It's possible that no namespaces in the first <code>MaxResults</code> namespaces matched the specified criteria but that subsequent groups of <code>MaxResults</code> namespaces do contain namespaces that match the criteria.</p> </note>"""
    max_results: NotRequired["capo_servicediscovery.types.max_results.MaxResults"]
    """<p>The maximum number of namespaces that you want Cloud Map to return in the response to a <code>ListNamespaces</code> request. If you don't specify a value for <code>MaxResults</code>, Cloud Map returns up to 100 namespaces.</p>"""
    filters: NotRequired[
        "capo_servicediscovery.types.namespace_filters.NamespaceFilters"
    ]
    """<p>A complex type that contains specifications for the namespaces that you want to list.</p> <p>If you specify more than one filter, a namespace must match all filters to be returned by <code>ListNamespaces</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNamespacesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import capo_servicediscovery.types.namespace_filters

        out["Filters"] = (
            capo_servicediscovery.types.namespace_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNamespacesRequest:
    out: ListNamespacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filters") is not None:
        import capo_servicediscovery.types.namespace_filters

        out["filters"] = (
            capo_servicediscovery.types.namespace_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListNamespacesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import capo_servicediscovery.types.namespace_filters

        out["Filters"] = capo_servicediscovery.types.namespace_filters.serialize_cbor(
            value["filters"]
        )
    return out


def deserialize_cbor(data: dict) -> ListNamespacesRequest:
    out: ListNamespacesRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filters") is not None:
        import capo_servicediscovery.types.namespace_filters

        out["filters"] = capo_servicediscovery.types.namespace_filters.deserialize_cbor(
            data["Filters"]
        )
    return out
