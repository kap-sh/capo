"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#VpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.security_groups
    import capo_bedrock_agentcore_control.types.subnets


class VpcConfig(TypedDict, closed=True):
    security_groups: (
        "capo_bedrock_agentcore_control.types.security_groups.SecurityGroups"
    )
    """<p>The security groups associated with the VPC configuration.</p>"""
    subnets: "capo_bedrock_agentcore_control.types.subnets.Subnets"
    """<p>The subnets associated with the VPC configuration.</p>"""
    require_service_s3_endpoint: NotRequired["bool"]
    """<note> <p>This field applies only to Agent Runtimes. It is not applicable to Browsers or Code Interpreters.</p> </note> <p>Controls whether a service-managed Amazon S3 gateway endpoint is provisioned in the VPC network topology for the agent runtime. This gateway is used by Amazon Bedrock AgentCore Runtime to download code and container images during agent startup.</p> <p>Starting May 5, 2026, Amazon Bedrock AgentCore Runtime is gradually rolling out a change to how network isolation is configured for VPC mode agents. Agent runtimes created on or after this rollout will no longer include the service-managed Amazon S3 gateway. Instead, all network access, including to Amazon S3, is governed exclusively by your VPC configuration. This field cannot be set on agent runtimes created after the rollout. Passing this field in an <code>UpdateAgentRuntime</code> request for these agent runtimes returns a <code>ValidationException</code>.</p> <p>Agent runtimes created before the rollout are not affected and continue to operate with the service-managed Amazon S3 gateway. To enforce full VPC network isolation on these existing agent runtimes, set this field to <code>false</code> via the <code>UpdateAgentRuntime</code> API. Before opting out, ensure your VPC provides the Amazon S3 access required for agent startup. If this field is not specified or is set to <code>true</code>, the service-managed Amazon S3 gateway remains provisioned.</p> <p>This field is only supported in the <code>UpdateAgentRuntime</code> API for pre-rollout agent runtimes. Passing this field in a <code>CreateAgentRuntime</code> request returns a <code>ValidationException</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfig) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.security_groups

    out["securityGroups"] = (
        capo_bedrock_agentcore_control.types.security_groups.serialize_json(
            value["security_groups"]
        )
    )
    import capo_bedrock_agentcore_control.types.subnets

    out["subnets"] = capo_bedrock_agentcore_control.types.subnets.serialize_json(
        value["subnets"]
    )
    if "require_service_s3_endpoint" in value:
        out["requireServiceS3Endpoint"] = value["require_service_s3_endpoint"]
    return out


def deserialize_json(data: dict) -> VpcConfig:
    out: VpcConfig = {}  # type: ignore[typeddict-item]
    if data.get("securityGroups") is not None:
        import capo_bedrock_agentcore_control.types.security_groups

        out["security_groups"] = (
            capo_bedrock_agentcore_control.types.security_groups.deserialize_json(
                data["securityGroups"]
            )
        )
    else:
        out["security_groups"] = []
    if data.get("subnets") is not None:
        import capo_bedrock_agentcore_control.types.subnets

        out["subnets"] = capo_bedrock_agentcore_control.types.subnets.deserialize_json(
            data["subnets"]
        )
    else:
        out["subnets"] = []
    if data.get("requireServiceS3Endpoint") is not None:
        out["require_service_s3_endpoint"] = data["requireServiceS3Endpoint"]
    return out
