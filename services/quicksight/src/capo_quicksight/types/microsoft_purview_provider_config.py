"""Generated from Smithy shape ``com.amazonaws.quicksight#MicrosoftPurviewProviderConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.dlp_action
    import capo_quicksight.types.label_action_mapping_list
    import capo_quicksight.types.microsoft_purview_credentials


class MicrosoftPurviewProviderConfig(TypedDict, closed=True):
    credentials: "capo_quicksight.types.microsoft_purview_credentials.MicrosoftPurviewCredentials"
    """<p>The credentials used to authenticate with Microsoft Purview.</p>"""
    label_action_mappings: (
        "capo_quicksight.types.label_action_mapping_list.LabelActionMappingList"
    )
    """<p>The mappings from Microsoft Purview sensitivity labels to enforcement actions.</p>"""
    unmapped_action: "capo_quicksight.types.dlp_action.DlpAction"
    """<p>The default action to apply to content that has no sensitivity label or whose label is not mapped. Valid values are <code>ALLOW</code>, <code>BLOCK</code>, and <code>WARN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MicrosoftPurviewProviderConfig) -> dict:
    out: dict = {}
    import capo_quicksight.types.microsoft_purview_credentials

    out["Credentials"] = (
        capo_quicksight.types.microsoft_purview_credentials.serialize_json(
            value["credentials"]
        )
    )
    import capo_quicksight.types.label_action_mapping_list

    out["LabelActionMappings"] = (
        capo_quicksight.types.label_action_mapping_list.serialize_json(
            value["label_action_mappings"]
        )
    )
    import capo_quicksight.types.dlp_action

    out["UnmappedAction"] = capo_quicksight.types.dlp_action.serialize_json(
        value["unmapped_action"]
    )
    return out


def deserialize_json(data: dict) -> MicrosoftPurviewProviderConfig:
    out: MicrosoftPurviewProviderConfig = {}  # type: ignore[typeddict-item]
    if data.get("Credentials") is not None:
        import capo_quicksight.types.microsoft_purview_credentials

        out["credentials"] = (
            capo_quicksight.types.microsoft_purview_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    else:
        raise DeserializationError(
            "MicrosoftPurviewProviderConfig.credentials required"
        )
    if data.get("LabelActionMappings") is not None:
        import capo_quicksight.types.label_action_mapping_list

        out["label_action_mappings"] = (
            capo_quicksight.types.label_action_mapping_list.deserialize_json(
                data["LabelActionMappings"]
            )
        )
    else:
        out["label_action_mappings"] = []
    if data.get("UnmappedAction") is not None:
        import capo_quicksight.types.dlp_action

        out["unmapped_action"] = capo_quicksight.types.dlp_action.deserialize_json(
            data["UnmappedAction"]
        )
    else:
        import typing

        out["unmapped_action"] = typing.cast(
            "capo_quicksight.types.dlp_action.DlpAction", ""
        )
    return out
