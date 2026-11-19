"""Generated from Smithy shape ``com.amazonaws.comprehend#ListEndpointsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.endpoint_properties_list
    import capo_comprehend.types.string


class ListEndpointsResponse(TypedDict, closed=True):
    endpoint_properties_list: NotRequired[
        "capo_comprehend.types.endpoint_properties_list.EndpointPropertiesList"
    ]
    """<p>Displays a list of endpoint properties being retrieved by the service in response to the request.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEndpointsResponse) -> dict:
    out: dict = {}
    if "endpoint_properties_list" in value:
        import capo_comprehend.types.endpoint_properties_list

        out["EndpointPropertiesList"] = (
            capo_comprehend.types.endpoint_properties_list.serialize_aws_json_1_1(
                value["endpoint_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEndpointsResponse:
    out: ListEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EndpointPropertiesList") is not None:
        import capo_comprehend.types.endpoint_properties_list

        out["endpoint_properties_list"] = (
            capo_comprehend.types.endpoint_properties_list.deserialize_aws_json_1_1(
                data["EndpointPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListEndpointsResponse) -> dict:
    out: dict = {}
    if "endpoint_properties_list" in value:
        import capo_comprehend.types.endpoint_properties_list

        out["EndpointPropertiesList"] = (
            capo_comprehend.types.endpoint_properties_list.serialize_cbor(
                value["endpoint_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListEndpointsResponse:
    out: ListEndpointsResponse = {}  # type: ignore[typeddict-item]
    if data.get("EndpointPropertiesList") is not None:
        import capo_comprehend.types.endpoint_properties_list

        out["endpoint_properties_list"] = (
            capo_comprehend.types.endpoint_properties_list.deserialize_cbor(
                data["EndpointPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
