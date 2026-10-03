"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DeleteServiceAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn
    import capo_servicediscovery.types.service_attribute_key_list


class DeleteServiceAttributesRequest(TypedDict, closed=True):
    service_id: "capo_servicediscovery.types.arn.Arn"
    """<p>The ID or Amazon Resource Name (ARN) of the service from which the attributes will be deleted. For services created in a namespace shared with your Amazon Web Services account, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""
    attributes: (
        "capo_servicediscovery.types.service_attribute_key_list.ServiceAttributeKeyList"
    )
    """<p>A list of keys corresponding to each attribute that you want to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteServiceAttributesRequest) -> dict:
    out: dict = {}
    out["ServiceId"] = value["service_id"]
    import capo_servicediscovery.types.service_attribute_key_list

    out["Attributes"] = (
        capo_servicediscovery.types.service_attribute_key_list.serialize_aws_json_1_1(
            value["attributes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteServiceAttributesRequest:
    out: DeleteServiceAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceId") is not None:
        out["service_id"] = data["ServiceId"]
    else:
        raise DeserializationError("DeleteServiceAttributesRequest.service_id required")
    if data.get("Attributes") is not None:
        import capo_servicediscovery.types.service_attribute_key_list

        out["attributes"] = (
            capo_servicediscovery.types.service_attribute_key_list.deserialize_aws_json_1_1(
                data["Attributes"]
            )
        )
    else:
        raise DeserializationError("DeleteServiceAttributesRequest.attributes required")
    return out
