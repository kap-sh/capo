"""Generated from Smithy shape ``com.amazonaws.datazone#AssetTypesForRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.rule_asset_type_list
    import capo_datazone.types.rule_scope_selection_mode


class AssetTypesForRule(TypedDict, closed=True):
    selection_mode: (
        "capo_datazone.types.rule_scope_selection_mode.RuleScopeSelectionMode"
    )
    """<p>The selection mode for the rule.</p>"""
    specific_asset_types: NotRequired[
        "capo_datazone.types.rule_asset_type_list.RuleAssetTypeList"
    ]
    """<p>The specific asset types that are included in the rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssetTypesForRule) -> dict:
    out: dict = {}
    import capo_datazone.types.rule_scope_selection_mode

    out["selectionMode"] = capo_datazone.types.rule_scope_selection_mode.serialize_json(
        value["selection_mode"]
    )
    if "specific_asset_types" in value:
        import capo_datazone.types.rule_asset_type_list

        out["specificAssetTypes"] = (
            capo_datazone.types.rule_asset_type_list.serialize_json(
                value["specific_asset_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssetTypesForRule:
    out: AssetTypesForRule = {}  # type: ignore[typeddict-item]
    if data.get("selectionMode") is not None:
        import capo_datazone.types.rule_scope_selection_mode

        out["selection_mode"] = (
            capo_datazone.types.rule_scope_selection_mode.deserialize_json(
                data["selectionMode"]
            )
        )
    else:
        import typing

        out["selection_mode"] = typing.cast(
            "capo_datazone.types.rule_scope_selection_mode.RuleScopeSelectionMode", ""
        )
    if data.get("specificAssetTypes") is not None:
        import capo_datazone.types.rule_asset_type_list

        out["specific_asset_types"] = (
            capo_datazone.types.rule_asset_type_list.deserialize_json(
                data["specificAssetTypes"]
            )
        )
    return out
