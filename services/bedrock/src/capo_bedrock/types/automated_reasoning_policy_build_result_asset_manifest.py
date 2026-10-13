"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildResultAssetManifest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list


class AutomatedReasoningPolicyBuildResultAssetManifest(TypedDict, closed=True):
    entries: "capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list.AutomatedReasoningPolicyBuildResultAssetManifestList"
    """<p>The list of asset entries in the manifest, each describing an available artifact that can be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildResultAssetManifest) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list

    out["entries"] = (
        capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list.serialize_json(
            value["entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildResultAssetManifest:
    out: AutomatedReasoningPolicyBuildResultAssetManifest = {}  # type: ignore[typeddict-item]
    if data.get("entries") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list

        out["entries"] = (
            capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list.deserialize_json(
                data["entries"]
            )
        )
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyBuildResultAssetManifest.entries required"
        )
    return out


def redact_sensitive(
    value: AutomatedReasoningPolicyBuildResultAssetManifest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entries" in value:
        import capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list

        out["entries"] = (
            capo_bedrock.types.automated_reasoning_policy_build_result_asset_manifest_list.redact_sensitive(
                value["entries"]
            )
        )
    return out
