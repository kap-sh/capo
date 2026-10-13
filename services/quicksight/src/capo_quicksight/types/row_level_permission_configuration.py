"""Generated from Smithy shape ``com.amazonaws.quicksight#RowLevelPermissionConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.row_level_permission_data_set
    import capo_quicksight.types.row_level_permission_tag_configuration


class RowLevelPermissionConfiguration(TypedDict, closed=True):
    tag_configuration: NotRequired[
        "capo_quicksight.types.row_level_permission_tag_configuration.RowLevelPermissionTagConfiguration"
    ]
    row_level_permission_data_set: NotRequired[
        "capo_quicksight.types.row_level_permission_data_set.RowLevelPermissionDataSet"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: RowLevelPermissionConfiguration) -> dict:
    out: dict = {}
    if "tag_configuration" in value:
        import capo_quicksight.types.row_level_permission_tag_configuration

        out["TagConfiguration"] = (
            capo_quicksight.types.row_level_permission_tag_configuration.serialize_json(
                value["tag_configuration"]
            )
        )
    if "row_level_permission_data_set" in value:
        import capo_quicksight.types.row_level_permission_data_set

        out["RowLevelPermissionDataSet"] = (
            capo_quicksight.types.row_level_permission_data_set.serialize_json(
                value["row_level_permission_data_set"]
            )
        )
    return out


def deserialize_json(data: dict) -> RowLevelPermissionConfiguration:
    out: RowLevelPermissionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TagConfiguration") is not None:
        import capo_quicksight.types.row_level_permission_tag_configuration

        out["tag_configuration"] = (
            capo_quicksight.types.row_level_permission_tag_configuration.deserialize_json(
                data["TagConfiguration"]
            )
        )
    if data.get("RowLevelPermissionDataSet") is not None:
        import capo_quicksight.types.row_level_permission_data_set

        out["row_level_permission_data_set"] = (
            capo_quicksight.types.row_level_permission_data_set.deserialize_json(
                data["RowLevelPermissionDataSet"]
            )
        )
    return out


def redact_sensitive(value: RowLevelPermissionConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tag_configuration" in value:
        import capo_quicksight.types.row_level_permission_tag_configuration

        out["tag_configuration"] = (
            capo_quicksight.types.row_level_permission_tag_configuration.redact_sensitive(
                value["tag_configuration"]
            )
        )
    return out
