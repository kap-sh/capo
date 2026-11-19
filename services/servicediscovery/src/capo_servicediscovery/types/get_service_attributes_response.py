"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetServiceAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.service_attributes


class GetServiceAttributesResponse(TypedDict, closed=True):
    service_attributes: NotRequired[
        "capo_servicediscovery.types.service_attributes.ServiceAttributes"
    ]
    """<p>A complex type that contains the service ARN and a list of attribute key-value pairs associated with the service.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetServiceAttributesResponse) -> dict:
    out: dict = {}
    if "service_attributes" in value:
        import capo_servicediscovery.types.service_attributes

        out["ServiceAttributes"] = (
            capo_servicediscovery.types.service_attributes.serialize_aws_json_1_1(
                value["service_attributes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetServiceAttributesResponse:
    out: GetServiceAttributesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ServiceAttributes") is not None:
        import capo_servicediscovery.types.service_attributes

        out["service_attributes"] = (
            capo_servicediscovery.types.service_attributes.deserialize_aws_json_1_1(
                data["ServiceAttributes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetServiceAttributesResponse) -> dict:
    out: dict = {}
    if "service_attributes" in value:
        import capo_servicediscovery.types.service_attributes

        out["ServiceAttributes"] = (
            capo_servicediscovery.types.service_attributes.serialize_cbor(
                value["service_attributes"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetServiceAttributesResponse:
    out: GetServiceAttributesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ServiceAttributes") is not None:
        import capo_servicediscovery.types.service_attributes

        out["service_attributes"] = (
            capo_servicediscovery.types.service_attributes.deserialize_cbor(
                data["ServiceAttributes"]
            )
        )
    return out
