"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#DeleteAssertionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.uuid


class DeleteAssertionRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    assertion_id: "capo_resiliencehubv2.types.uuid.Uuid"
    """<p>The unique identifier of the assertion to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAssertionRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["assertionId"] = value["assertion_id"]
    return out


def deserialize_json(data: dict) -> DeleteAssertionRequest:
    out: DeleteAssertionRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("assertionId") is not None:
        out["assertion_id"] = data["assertionId"]
    else:
        out["assertion_id"] = ""
    return out
