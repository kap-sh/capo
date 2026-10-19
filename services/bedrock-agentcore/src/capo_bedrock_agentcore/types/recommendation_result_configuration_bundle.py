"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RecommendationResultConfigurationBundle``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.configuration_bundle_arn
    import capo_bedrock_agentcore.types.configuration_bundle_version_id


class RecommendationResultConfigurationBundle(TypedDict, closed=True):
    bundle_arn: (
        "capo_bedrock_agentcore.types.configuration_bundle_arn.ConfigurationBundleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the configuration bundle.</p>"""
    version_id: "capo_bedrock_agentcore.types.configuration_bundle_version_id.ConfigurationBundleVersionId"
    """<p>The version identifier of the configuration bundle containing the recommendation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationResultConfigurationBundle) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["versionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> RecommendationResultConfigurationBundle:
    out: RecommendationResultConfigurationBundle = {}  # type: ignore[typeddict-item]
    if data.get("bundleArn") is not None:
        out["bundle_arn"] = data["bundleArn"]
    else:
        out["bundle_arn"] = ""
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    else:
        out["version_id"] = ""
    return out
