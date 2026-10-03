"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserHierarchyStructureRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_structure_update
    import capo_connect.types.instance_id


class UpdateUserHierarchyStructureRequest(TypedDict, closed=True):
    hierarchy_structure: (
        "capo_connect.types.hierarchy_structure_update.HierarchyStructureUpdate"
    )
    """<p>The hierarchy levels to update.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserHierarchyStructureRequest) -> dict:
    out: dict = {}
    import capo_connect.types.hierarchy_structure_update

    out["HierarchyStructure"] = (
        capo_connect.types.hierarchy_structure_update.serialize_json(
            value["hierarchy_structure"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateUserHierarchyStructureRequest:
    out: UpdateUserHierarchyStructureRequest = {}  # type: ignore[typeddict-item]
    if data.get("HierarchyStructure") is not None:
        import capo_connect.types.hierarchy_structure_update

        out["hierarchy_structure"] = (
            capo_connect.types.hierarchy_structure_update.deserialize_json(
                data["HierarchyStructure"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateUserHierarchyStructureRequest.hierarchy_structure required"
        )
    return out
