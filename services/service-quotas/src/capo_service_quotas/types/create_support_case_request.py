"""Generated from Smithy shape ``com.amazonaws.servicequotas#CreateSupportCaseRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_service_quotas.types.request_id


class CreateSupportCaseRequest(TypedDict, closed=True):
    request_id: "capo_service_quotas.types.request_id.RequestId"
    """<p>The ID of the pending quota increase request for which you want to open a Support case. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSupportCaseRequest) -> dict:
    out: dict = {}
    out["RequestId"] = value["request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSupportCaseRequest:
    out: CreateSupportCaseRequest = {}  # type: ignore[typeddict-item]
    if data.get("RequestId") is not None:
        out["request_id"] = data["RequestId"]
    else:
        out["request_id"] = ""
    return out
