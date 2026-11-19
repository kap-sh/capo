"""Generated from Smithy shape ``com.amazonaws.servicediscovery#ListServicesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.next_token
    import capo_servicediscovery.types.service_summaries_list


class ListServicesResponse(TypedDict, closed=True):
    services: NotRequired[
        "capo_servicediscovery.types.service_summaries_list.ServiceSummariesList"
    ]
    """<p>An array that contains one <code>ServiceSummary</code> object for each service that matches the specified filter criteria.</p>"""
    next_token: NotRequired["capo_servicediscovery.types.next_token.NextToken"]
    """<p>If the response contains <code>NextToken</code>, submit another <code>ListServices</code> request to get the next group of results. Specify the value of <code>NextToken</code> from the previous response in the next request.</p> <note> <p>Cloud Map gets <code>MaxResults</code> services and then filters them based on the specified criteria. It's possible that no services in the first <code>MaxResults</code> services matched the specified criteria but that subsequent groups of <code>MaxResults</code> services do contain services that match the criteria.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListServicesResponse) -> dict:
    out: dict = {}
    if "services" in value:
        import capo_servicediscovery.types.service_summaries_list

        out["Services"] = (
            capo_servicediscovery.types.service_summaries_list.serialize_aws_json_1_1(
                value["services"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListServicesResponse:
    out: ListServicesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Services") is not None:
        import capo_servicediscovery.types.service_summaries_list

        out["services"] = (
            capo_servicediscovery.types.service_summaries_list.deserialize_aws_json_1_1(
                data["Services"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListServicesResponse) -> dict:
    out: dict = {}
    if "services" in value:
        import capo_servicediscovery.types.service_summaries_list

        out["Services"] = (
            capo_servicediscovery.types.service_summaries_list.serialize_cbor(
                value["services"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListServicesResponse:
    out: ListServicesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Services") is not None:
        import capo_servicediscovery.types.service_summaries_list

        out["services"] = (
            capo_servicediscovery.types.service_summaries_list.deserialize_cbor(
                data["Services"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
