"""Generated from Smithy shape ``com.amazonaws.bedrock#GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_build_result_assets
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_id


class GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse(
    TypedDict, closed=True
):
    policy_arn: (
        "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
    )
    """<p>The Amazon Resource Name (ARN) of the Automated Reasoning policy.</p>"""
    build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId"
    """<p>The unique identifier of the build workflow.</p>"""
    build_workflow_assets: NotRequired[
        "capo_bedrock.types.automated_reasoning_policy_build_result_assets.AutomatedReasoningPolicyBuildResultAssets"
    ]
    """<p>The requested build workflow asset. This is a union type that returns only one of the available asset types (logs, reports, or generated artifacts) based on the specific asset type requested in the API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse,
) -> dict:
    out: dict = {}
    out["policyArn"] = value["policy_arn"]
    out["buildWorkflowId"] = value["build_workflow_id"]
    if "build_workflow_assets" in value:
        import capo_bedrock.types.automated_reasoning_policy_build_result_assets

        out["buildWorkflowAssets"] = (
            capo_bedrock.types.automated_reasoning_policy_build_result_assets.serialize_json(
                value["build_workflow_assets"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse:
    out: GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse = {}  # type: ignore[typeddict-item]
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        out["policy_arn"] = ""
    if data.get("buildWorkflowId") is not None:
        out["build_workflow_id"] = data["buildWorkflowId"]
    else:
        out["build_workflow_id"] = ""
    if data.get("buildWorkflowAssets") is not None:
        import capo_bedrock.types.automated_reasoning_policy_build_result_assets

        out["build_workflow_assets"] = (
            capo_bedrock.types.automated_reasoning_policy_build_result_assets.deserialize_json(
                data["buildWorkflowAssets"]
            )
        )
    return out


def redact_sensitive(
    value: GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "build_workflow_assets" in value:
        import capo_bedrock.types.automated_reasoning_policy_build_result_assets

        out["build_workflow_assets"] = (
            capo_bedrock.types.automated_reasoning_policy_build_result_assets.redact_sensitive(
                value["build_workflow_assets"]
            )
        )
    return out
