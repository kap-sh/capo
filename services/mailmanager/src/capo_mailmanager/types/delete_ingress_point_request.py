"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteIngressPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_point_id


class DeleteIngressPointRequest(TypedDict, closed=True):
    ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId"
    """<p>The identifier of the ingress endpoint resource that you want to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteIngressPointRequest) -> dict:
    out: dict = {}
    out["IngressPointId"] = value["ingress_point_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteIngressPointRequest:
    out: DeleteIngressPointRequest = {}  # type: ignore[typeddict-item]
    if data.get("IngressPointId") is not None:
        out["ingress_point_id"] = data["IngressPointId"]
    else:
        out["ingress_point_id"] = ""
    return out
