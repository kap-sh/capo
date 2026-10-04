"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteConfigurationBundleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.configuration_bundle_arn
    import capo_bedrock_agentcore_control.types.configuration_bundle_id
    import capo_bedrock_agentcore_control.types.configuration_bundle_status


class DeleteConfigurationBundleResponse(TypedDict, closed=True):
    bundle_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.configuration_bundle_arn.ConfigurationBundleArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the deleted configuration bundle.</p>"""
    bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId"
    """<p>The unique identifier of the deleted configuration bundle.</p>"""
    status: "capo_bedrock_agentcore_control.types.configuration_bundle_status.ConfigurationBundleStatus"
    """<p>The status of the configuration bundle deletion operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfigurationBundleResponse) -> dict:
    out: dict = {}
    if "bundle_arn" in value:
        out["bundleArn"] = value["bundle_arn"]
    out["bundleId"] = value["bundle_id"]
    import capo_bedrock_agentcore_control.types.configuration_bundle_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.configuration_bundle_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteConfigurationBundleResponse:
    out: DeleteConfigurationBundleResponse = {}  # type: ignore[typeddict-item]
    if data.get("bundleArn") is not None:
        out["bundle_arn"] = data["bundleArn"]
    if data.get("bundleId") is not None:
        out["bundle_id"] = data["bundleId"]
    else:
        raise DeserializationError(
            "DeleteConfigurationBundleResponse.bundle_id required"
        )
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.configuration_bundle_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.configuration_bundle_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteConfigurationBundleResponse.status required")
    return out
