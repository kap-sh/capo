"""Generated from Smithy shape ``com.amazonaws.directoryservice#DeleteTrustRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_directory_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_directory_service.types.delete_associated_conditional_forwarder
    import capo_directory_service.types.trust_id


class DeleteTrustRequest(TypedDict, closed=True):
    trust_id: "capo_directory_service.types.trust_id.TrustId"
    """<p>The Trust ID of the trust relationship to be deleted.</p>"""
    delete_associated_conditional_forwarder: NotRequired[
        "capo_directory_service.types.delete_associated_conditional_forwarder.DeleteAssociatedConditionalForwarder"
    ]
    """<p>Delete a conditional forwarder as part of a DeleteTrustRequest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTrustRequest) -> dict:
    out: dict = {}
    out["TrustId"] = value["trust_id"]
    if "delete_associated_conditional_forwarder" in value:
        out["DeleteAssociatedConditionalForwarder"] = value[
            "delete_associated_conditional_forwarder"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTrustRequest:
    out: DeleteTrustRequest = {}  # type: ignore[typeddict-item]
    if data.get("TrustId") is not None:
        out["trust_id"] = data["TrustId"]
    else:
        raise DeserializationError("DeleteTrustRequest.trust_id required")
    if data.get("DeleteAssociatedConditionalForwarder") is not None:
        out["delete_associated_conditional_forwarder"] = data[
            "DeleteAssociatedConditionalForwarder"
        ]
    return out
