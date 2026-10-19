"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateIngressPointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_point_id


class CreateIngressPointResponse(TypedDict, closed=True):
    ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId"
    """<p>The unique identifier for a previously created ingress endpoint.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateIngressPointResponse) -> dict:
    out: dict = {}
    out["IngressPointId"] = value["ingress_point_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateIngressPointResponse:
    out: CreateIngressPointResponse = {}  # type: ignore[typeddict-item]
    if data.get("IngressPointId") is not None:
        out["ingress_point_id"] = data["IngressPointId"]
    else:
        out["ingress_point_id"] = ""
    return out
