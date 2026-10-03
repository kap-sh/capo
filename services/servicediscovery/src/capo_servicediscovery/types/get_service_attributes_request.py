"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetServiceAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn


class GetServiceAttributesRequest(TypedDict, closed=True):
    service_id: "capo_servicediscovery.types.arn.Arn"
    """<p>The ID or Amazon Resource Name (ARN) of the service that you want to get attributes for. For services created in a namespace shared with your Amazon Web Services account, specify the service ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetServiceAttributesRequest) -> dict:
    out: dict = {}
    out["ServiceId"] = value["service_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetServiceAttributesRequest:
    out: GetServiceAttributesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceId") is not None:
        out["service_id"] = data["ServiceId"]
    else:
        raise DeserializationError("GetServiceAttributesRequest.service_id required")
    return out
