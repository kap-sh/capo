"""Generated from Smithy shape ``com.amazonaws.quicksight#ResourcePermission``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.action_list
    import capo_quicksight.types.principal


class ResourcePermission(TypedDict, closed=True):
    principal: "capo_quicksight.types.principal.Principal"
    """<p>The Amazon Resource Name (ARN) of the principal. This can be one of the following:</p> <ul> <li> <p>The ARN of an Quick Sight user or group associated with a data source or dataset. (This is common.)</p> </li> <li> <p>The ARN of an Quick Sight user, group, or namespace associated with an analysis, dashboard, template, or theme. Namespace sharing is not supported for action connectors. (This is common.)</p> </li> <li> <p>The ARN of an Amazon Web Services account root: This is an IAM ARN rather than a Quick Sight ARN. Use this option only to share resources (templates) across Amazon Web Services accounts. Account root sharing is not supported for action connectors. (This is less common.) </p> </li> </ul>"""
    actions: "capo_quicksight.types.action_list.ActionList"
    """<p>The IAM action to grant or revoke permissions on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePermission) -> dict:
    out: dict = {}
    out["Principal"] = value["principal"]
    import capo_quicksight.types.action_list

    out["Actions"] = capo_quicksight.types.action_list.serialize_json(value["actions"])
    return out


def deserialize_json(data: dict) -> ResourcePermission:
    out: ResourcePermission = {}  # type: ignore[typeddict-item]
    if data.get("Principal") is not None:
        out["principal"] = data["Principal"]
    else:
        out["principal"] = ""
    if data.get("Actions") is not None:
        import capo_quicksight.types.action_list

        out["actions"] = capo_quicksight.types.action_list.deserialize_json(
            data["Actions"]
        )
    else:
        out["actions"] = []
    return out
