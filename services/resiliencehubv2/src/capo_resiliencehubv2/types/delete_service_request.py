"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteServiceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn


class DeleteServiceRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteServiceRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    return out


def deserialize_json(data: dict) -> DeleteServiceRequest:
    out: DeleteServiceRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    return out
