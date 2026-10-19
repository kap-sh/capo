"""Generated from Smithy shape ``com.amazonaws.cleanrooms#InheritedAllowedAdditionalAnalysesSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.allowed_additional_analyses
    import capo_cleanrooms.types.base_table_dependency_type
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.uuid


class InheritedAllowedAdditionalAnalysesSource(TypedDict, closed=True):
    name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The name of the parent table.</p>"""
    id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the parent table.</p>"""
    type: "capo_cleanrooms.types.base_table_dependency_type.BaseTableDependencyType"
    """<p>The type of the parent table.</p>"""
    value: "capo_cleanrooms.types.allowed_additional_analyses.AllowedAdditionalAnalyses"
    """<p>The allowed additional analyses defined on the parent table.</p>"""
    source_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the member who owns the parent table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InheritedAllowedAdditionalAnalysesSource) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["id"] = value["id"]
    import capo_cleanrooms.types.base_table_dependency_type

    out["type"] = capo_cleanrooms.types.base_table_dependency_type.serialize_json(
        value["type"]
    )
    import capo_cleanrooms.types.allowed_additional_analyses

    out["value"] = capo_cleanrooms.types.allowed_additional_analyses.serialize_json(
        value["value"]
    )
    out["sourceAccountId"] = value["source_account_id"]
    return out


def deserialize_json(data: dict) -> InheritedAllowedAdditionalAnalysesSource:
    out: InheritedAllowedAdditionalAnalysesSource = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
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
    if data.get("value") is not None:
        import capo_cleanrooms.types.allowed_additional_analyses

        out["value"] = (
            capo_cleanrooms.types.allowed_additional_analyses.deserialize_json(
                data["value"]
            )
        )
    else:
        out["value"] = []
    if data.get("sourceAccountId") is not None:
        out["source_account_id"] = data["sourceAccountId"]
    else:
        out["source_account_id"] = ""
    return out
