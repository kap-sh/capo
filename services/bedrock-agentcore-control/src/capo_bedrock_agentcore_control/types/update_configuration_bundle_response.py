"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateConfigurationBundleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.configuration_bundle_arn
    import capo_bedrock_agentcore_control.types.configuration_bundle_id
    import capo_bedrock_agentcore_control.types.configuration_bundle_version


class UpdateConfigurationBundleResponse(TypedDict, closed=True):
    bundle_arn: "capo_bedrock_agentcore_control.types.configuration_bundle_arn.ConfigurationBundleArn"
    """<p>The Amazon Resource Name (ARN) of the updated configuration bundle.</p>"""
    bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the updated configuration bundle.</p>"""
    version_id: "capo_bedrock_agentcore_control.types.configuration_bundle_version.ConfigurationBundleVersion"
    """<p>The new version identifier created by this update.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the configuration bundle was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationBundleResponse) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["bundleId"] = value["bundle_id"]
    out["versionId"] = value["version_id"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationBundleResponse:
    out: UpdateConfigurationBundleResponse = {}  # type: ignore[typeddict-item]
    if data.get("bundleArn") is not None:
        out["bundle_arn"] = data["bundleArn"]
    else:
        out["bundle_arn"] = ""
    if data.get("bundleId") is not None:
        out["bundle_id"] = data["bundleId"]
    else:
        out["bundle_id"] = ""
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    else:
        out["version_id"] = ""
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
