"""Generated from Smithy shape ``com.amazonaws.servicediscovery#GetNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_servicediscovery.errors import DeserializationError

if TYPE_CHECKING:
    import capo_servicediscovery.types.arn


class GetNamespaceRequest(TypedDict, closed=True):
    id: "capo_servicediscovery.types.arn.Arn"
    """<p>The ID or Amazon Resource Name (ARN) of the namespace that you want to get information about. For namespaces shared with your Amazon Web Services account, specify the namespace ARN. For more information about shared namespaces, see <a href="https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html">Cross-account Cloud Map namespace sharing</a> in the <i>Cloud Map Developer Guide</i> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNamespaceRequest) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNamespaceRequest:
    out: GetNamespaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("GetNamespaceRequest.id required")
    return out
