"""Generated from Smithy shape ``com.amazonaws.backup#ResourceSelection``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.resource_arns
    import capo_backup.types.resource_type
    import capo_backup.types.tiering_down_settings_in_days


class ResourceSelection(TypedDict, closed=True):
    resources: "capo_backup.types.resource_arns.ResourceArns"
    """<p>An array of strings that either contains ARNs of the associated resources or contains a wildcard <code>*</code> to specify all resources. You can specify up to 100 specific resources per tiering configuration.</p>"""
    tiering_down_settings_in_days: (
        "capo_backup.types.tiering_down_settings_in_days.TieringDownSettingsInDays"
    )
    """<p>The number of days after creation within a backup vault that an object can transition to the low cost warm storage tier. Must be a positive integer between 60 and 36500 days.</p>"""
    resource_type: "capo_backup.types.resource_type.ResourceType"
    """<p>The type of Amazon Web Services resource; for example, <code>S3</code> for Amazon S3. For tiering configurations, this is currently limited to <code>S3</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSelection) -> dict:
    out: dict = {}
    import capo_backup.types.resource_arns

    out["Resources"] = capo_backup.types.resource_arns.serialize_json(
        value["resources"]
    )
    out["TieringDownSettingsInDays"] = value["tiering_down_settings_in_days"]
    out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ResourceSelection:
    out: ResourceSelection = {}  # type: ignore[typeddict-item]
    if data.get("Resources") is not None:
        import capo_backup.types.resource_arns

        out["resources"] = capo_backup.types.resource_arns.deserialize_json(
            data["Resources"]
        )
    else:
        out["resources"] = []
    if data.get("TieringDownSettingsInDays") is not None:
        out["tiering_down_settings_in_days"] = data["TieringDownSettingsInDays"]
    else:
        out["tiering_down_settings_in_days"] = 0
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    return out
