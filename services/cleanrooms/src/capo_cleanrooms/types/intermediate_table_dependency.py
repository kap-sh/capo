"""Generated from Smithy shape ``com.amazonaws.cleanrooms#IntermediateTableDependency``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.base_table_dependency_type
    import capo_cleanrooms.types.base_table_parent_type
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.uuid


class IntermediateTableDependency(TypedDict, closed=True):
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the dependency table.</p>"""
    name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The name of the dependency table.</p>"""
    type: "capo_cleanrooms.types.base_table_dependency_type.BaseTableDependencyType"
    """<p>The type of the dependency table.</p>"""
    parent_type: "capo_cleanrooms.types.base_table_parent_type.BaseTableParentType"
    """<p>The type of dependency, either direct or indirect. A direct dependency is a table explicitly referenced in the stored query. An indirect dependency is a table referenced through another intermediate table.</p>"""
    creator_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the member who owns the dependency table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntermediateTableDependency) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_cleanrooms.types.base_table_dependency_type

    out["type"] = capo_cleanrooms.types.base_table_dependency_type.serialize_json(
        value["type"]
    )
    import capo_cleanrooms.types.base_table_parent_type

    out["parentType"] = capo_cleanrooms.types.base_table_parent_type.serialize_json(
        value["parent_type"]
    )
    out["creatorAccountId"] = value["creator_account_id"]
    return out


def deserialize_json(data: dict) -> IntermediateTableDependency:
    out: IntermediateTableDependency = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_cleanrooms.types.base_table_dependency_type

        out["type"] = capo_cleanrooms.types.base_table_dependency_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_cleanrooms.types.base_table_dependency_type.BaseTableDependencyType",
            "",
        )
    if data.get("parentType") is not None:
        import capo_cleanrooms.types.base_table_parent_type

        out["parent_type"] = (
            capo_cleanrooms.types.base_table_parent_type.deserialize_json(
                data["parentType"]
            )
        )
    else:
        import typing

        out["parent_type"] = typing.cast(
            "capo_cleanrooms.types.base_table_parent_type.BaseTableParentType", ""
        )
    if data.get("creatorAccountId") is not None:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        out["creator_account_id"] = ""
    return out
