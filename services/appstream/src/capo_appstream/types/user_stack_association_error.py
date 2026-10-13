"""Generated from Smithy shape ``com.amazonaws.appstream#UserStackAssociationError``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.string
    import capo_appstream.types.user_stack_association
    import capo_appstream.types.user_stack_association_error_code


class UserStackAssociationError(TypedDict, closed=True):
    user_stack_association: NotRequired[
        "capo_appstream.types.user_stack_association.UserStackAssociation"
    ]
    """<p>Information about the user and associated stack.</p>"""
    error_code: NotRequired[
        "capo_appstream.types.user_stack_association_error_code.UserStackAssociationErrorCode"
    ]
    """<p>The error code for the error that is returned when a user can’t be associated with or disassociated from a stack.</p>"""
    error_message: NotRequired["capo_appstream.types.string.String"]
    """<p>The error message for the error that is returned when a user can’t be associated with or disassociated from a stack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserStackAssociationError) -> dict:
    out: dict = {}
    if "user_stack_association" in value:
        import capo_appstream.types.user_stack_association

        out["UserStackAssociation"] = (
            capo_appstream.types.user_stack_association.serialize_aws_json_1_1(
                value["user_stack_association"]
            )
        )
    if "error_code" in value:
        import capo_appstream.types.user_stack_association_error_code

        out["ErrorCode"] = (
            capo_appstream.types.user_stack_association_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UserStackAssociationError:
    out: UserStackAssociationError = {}  # type: ignore[typeddict-item]
    if data.get("UserStackAssociation") is not None:
        import capo_appstream.types.user_stack_association

        out["user_stack_association"] = (
            capo_appstream.types.user_stack_association.deserialize_aws_json_1_1(
                data["UserStackAssociation"]
            )
        )
    if data.get("ErrorCode") is not None:
        import capo_appstream.types.user_stack_association_error_code

        out["error_code"] = (
            capo_appstream.types.user_stack_association_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


def redact_sensitive(value: UserStackAssociationError) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "user_stack_association" in value:
        import capo_appstream.types.user_stack_association

        out["user_stack_association"] = (
            capo_appstream.types.user_stack_association.redact_sensitive(
                value["user_stack_association"]
            )
        )
    return out
