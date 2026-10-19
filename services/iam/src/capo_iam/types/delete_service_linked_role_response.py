"""Generated from Smithy shape ``com.amazonaws.iam#DeleteServiceLinkedRoleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.deletion_task_id_type


class DeleteServiceLinkedRoleResponse(TypedDict, closed=True):
    deletion_task_id: "capo_iam.types.deletion_task_id_type.DeletionTaskIdType"
    """<p>The deletion task identifier that you can use to check the status of the deletion. This identifier is returned in the format <code>task/aws-service-role/<service-principal-name>/<role-name>/<task-uuid></code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteServiceLinkedRoleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}DeletionTaskId", str(value["deletion_task_id"])))


def deserialize_query(el: Element) -> DeleteServiceLinkedRoleResponse:
    out: DeleteServiceLinkedRoleResponse = {}  # type: ignore[typeddict-item]
    child_deletion_task_id = el.find("DeletionTaskId")
    if child_deletion_task_id is not None:
        out["deletion_task_id"] = str(child_deletion_task_id.text or "")
    else:
        out["deletion_task_id"] = ""
    return out
