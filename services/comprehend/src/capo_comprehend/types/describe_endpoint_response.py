"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.endpoint_properties


class DescribeEndpointResponse(TypedDict, closed=True):
    endpoint_properties: NotRequired[
        "capo_comprehend.types.endpoint_properties.EndpointProperties"
    ]
    """<p>Describes information associated with the specific endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint_properties" in value:
        import capo_comprehend.types.endpoint_properties

        out["EndpointProperties"] = (
            capo_comprehend.types.endpoint_properties.serialize_aws_json_1_1(
                value["endpoint_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointResponse:
    out: DescribeEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("EndpointProperties") is not None:
        import capo_comprehend.types.endpoint_properties

        out["endpoint_properties"] = (
            capo_comprehend.types.endpoint_properties.deserialize_aws_json_1_1(
                data["EndpointProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint_properties" in value:
        import capo_comprehend.types.endpoint_properties

        out["EndpointProperties"] = (
            capo_comprehend.types.endpoint_properties.serialize_cbor(
                value["endpoint_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeEndpointResponse:
    out: DescribeEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("EndpointProperties") is not None:
        import capo_comprehend.types.endpoint_properties

        out["endpoint_properties"] = (
            capo_comprehend.types.endpoint_properties.deserialize_cbor(
                data["EndpointProperties"]
            )
        )
    return out
