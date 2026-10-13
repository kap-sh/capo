"""Generated from Smithy shape ``com.amazonaws.appstream#BatchAssociateUserStackResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.user_stack_association_error_list


class BatchAssociateUserStackResult(TypedDict, closed=True):
    errors: NotRequired[
        "capo_appstream.types.user_stack_association_error_list.UserStackAssociationErrorList"
    ]
    """<p>The list of UserStackAssociationError objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchAssociateUserStackResult) -> dict:
    out: dict = {}
    if "errors" in value:
        import capo_appstream.types.user_stack_association_error_list

        out["errors"] = (
            capo_appstream.types.user_stack_association_error_list.serialize_aws_json_1_1(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchAssociateUserStackResult:
    out: BatchAssociateUserStackResult = {}  # type: ignore[typeddict-item]
    if data.get("errors") is not None:
        import capo_appstream.types.user_stack_association_error_list

        out["errors"] = (
            capo_appstream.types.user_stack_association_error_list.deserialize_aws_json_1_1(
                data["errors"]
            )
        )
    return out


def redact_sensitive(value: BatchAssociateUserStackResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "errors" in value:
        import capo_appstream.types.user_stack_association_error_list

        out["errors"] = (
            capo_appstream.types.user_stack_association_error_list.redact_sensitive(
                value["errors"]
            )
        )
    return out
