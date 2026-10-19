"""Generated from Smithy shape ``com.amazonaws.iam#GetServiceLinkedRoleDeletionStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.deletion_task_failure_reason_type
    import capo_iam.types.deletion_task_status_type


class GetServiceLinkedRoleDeletionStatusResponse(TypedDict, closed=True):
    status: "capo_iam.types.deletion_task_status_type.DeletionTaskStatusType"
    """<p>The status of the deletion.</p>"""
    reason: NotRequired[
        "capo_iam.types.deletion_task_failure_reason_type.DeletionTaskFailureReasonType"
    ]
    """<p>An object that contains details about the reason the deletion failed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetServiceLinkedRoleDeletionStatusResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_iam.types.deletion_task_status_type

    capo_iam.types.deletion_task_status_type.serialize_query(
        value["status"], pairs, f"{key_prefix}Status"
    )
    if "reason" in value:
        import capo_iam.types.deletion_task_failure_reason_type

        capo_iam.types.deletion_task_failure_reason_type.serialize_query(
            value["reason"], pairs, f"{key_prefix}Reason"
        )


def deserialize_query(el: Element) -> GetServiceLinkedRoleDeletionStatusResponse:
    out: GetServiceLinkedRoleDeletionStatusResponse = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        import capo_iam.types.deletion_task_status_type

        out["status"] = capo_iam.types.deletion_task_status_type.deserialize_query(
            child_status
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_iam.types.deletion_task_status_type.DeletionTaskStatusType", ""
        )
    child_reason = el.find("Reason")
    if child_reason is not None:
        import capo_iam.types.deletion_task_failure_reason_type

        out["reason"] = (
            capo_iam.types.deletion_task_failure_reason_type.deserialize_query(
                child_reason
            )
        )
    return out
