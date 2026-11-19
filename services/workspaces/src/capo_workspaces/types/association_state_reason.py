"""Generated from Smithy shape ``com.amazonaws.workspaces#AssociationStateReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.association_error_code
    import capo_workspaces.types.string2048


class AssociationStateReason(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_workspaces.types.association_error_code.AssociationErrorCode"
    ]
    """<p>The error code of the association deployment failure.</p>"""
    error_message: NotRequired["capo_workspaces.types.string2048.String2048"]
    """<p>The error message of the association deployment failure.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationStateReason) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_workspaces.types.association_error_code

        out["ErrorCode"] = (
            capo_workspaces.types.association_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationStateReason:
    out: AssociationStateReason = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        import capo_workspaces.types.association_error_code

        out["error_code"] = (
            capo_workspaces.types.association_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociationStateReason) -> dict:
    out: dict = {}
    if "error_code" in value:
        import capo_workspaces.types.association_error_code

        out["ErrorCode"] = capo_workspaces.types.association_error_code.serialize_cbor(
            value["error_code"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> AssociationStateReason:
    out: AssociationStateReason = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        import capo_workspaces.types.association_error_code

        out["error_code"] = (
            capo_workspaces.types.association_error_code.deserialize_cbor(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
