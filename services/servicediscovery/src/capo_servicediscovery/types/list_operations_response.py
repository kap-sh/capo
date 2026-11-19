"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ListOperationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.next_token
    import capo_servicediscovery.types.operation_summary_list


class ListOperationsResponse(TypedDict, closed=True):
    operations: NotRequired[
        "capo_servicediscovery.types.operation_summary_list.OperationSummaryList"
    ]
    """<p>Summary information about the operations that match the specified criteria.</p>"""
    next_token: NotRequired["capo_servicediscovery.types.next_token.NextToken"]
    """<p>If the response contains <code>NextToken</code>, submit another <code>ListOperations</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p> <note> <p>Cloud Map gets <code>MaxResults</code> operations and then filters them based on the specified criteria. It's possible that no operations in the first <code>MaxResults</code> operations matched the specified criteria but that subsequent groups of <code>MaxResults</code> operations do contain operations that match the criteria.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOperationsResponse) -> dict:
    out: dict = {}
    if "operations" in value:
        import capo_servicediscovery.types.operation_summary_list

        out["Operations"] = (
            capo_servicediscovery.types.operation_summary_list.serialize_aws_json_1_1(
                value["operations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListOperationsResponse:
    out: ListOperationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Operations") is not None:
        import capo_servicediscovery.types.operation_summary_list

        out["operations"] = (
            capo_servicediscovery.types.operation_summary_list.deserialize_aws_json_1_1(
                data["Operations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListOperationsResponse) -> dict:
    out: dict = {}
    if "operations" in value:
        import capo_servicediscovery.types.operation_summary_list

        out["Operations"] = (
            capo_servicediscovery.types.operation_summary_list.serialize_cbor(
                value["operations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListOperationsResponse:
    out: ListOperationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Operations") is not None:
        import capo_servicediscovery.types.operation_summary_list

        out["operations"] = (
            capo_servicediscovery.types.operation_summary_list.deserialize_cbor(
                data["Operations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
