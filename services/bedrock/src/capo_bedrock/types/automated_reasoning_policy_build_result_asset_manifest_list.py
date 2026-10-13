"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildResultAssetManifestList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry

AutomatedReasoningPolicyBuildResultAssetManifestList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry.AutomatedReasoningPolicyBuildResultAssetManifestEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildResultAssetManifestList) -> list:
    import capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AutomatedReasoningPolicyBuildResultAssetManifestList:
    import capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry

    out: AutomatedReasoningPolicyBuildResultAssetManifestList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyBuildResultAssetManifestList,
) -> list[Any]:
    import capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry

    return [
        capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_entry.redact_sensitive(
            item
        )
        for item in value
    ]
