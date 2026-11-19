"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ListNamespacesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.namespace_summaries_list
    import capo_servicediscovery.types.next_token


class ListNamespacesResponse(TypedDict, closed=True):
    namespaces: NotRequired[
        "capo_servicediscovery.types.namespace_summaries_list.NamespaceSummariesList"
    ]
    """<p>An array that contains one <code>NamespaceSummary</code> object for each namespace that matches the specified filter criteria.</p>"""
    next_token: NotRequired["capo_servicediscovery.types.next_token.NextToken"]
    """<p>If the response contains <code>NextToken</code>, submit another <code>ListNamespaces</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p> <note> <p>Cloud Map gets <code>MaxResults</code> namespaces and then filters them based on the specified criteria. It's possible that no namespaces in the first <code>MaxResults</code> namespaces matched the specified criteria but that subsequent groups of <code>MaxResults</code> namespaces do contain namespaces that match the criteria.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNamespacesResponse) -> dict:
    out: dict = {}
    if "namespaces" in value:
        import capo_servicediscovery.types.namespace_summaries_list

        out["Namespaces"] = (
            capo_servicediscovery.types.namespace_summaries_list.serialize_aws_json_1_1(
                value["namespaces"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNamespacesResponse:
    out: ListNamespacesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Namespaces") is not None:
        import capo_servicediscovery.types.namespace_summaries_list

        out["namespaces"] = (
            capo_servicediscovery.types.namespace_summaries_list.deserialize_aws_json_1_1(
                data["Namespaces"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListNamespacesResponse) -> dict:
    out: dict = {}
    if "namespaces" in value:
        import capo_servicediscovery.types.namespace_summaries_list

        out["Namespaces"] = (
            capo_servicediscovery.types.namespace_summaries_list.serialize_cbor(
                value["namespaces"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListNamespacesResponse:
    out: ListNamespacesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Namespaces") is not None:
        import capo_servicediscovery.types.namespace_summaries_list

        out["namespaces"] = (
            capo_servicediscovery.types.namespace_summaries_list.deserialize_cbor(
                data["Namespaces"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
