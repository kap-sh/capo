"""Generated from Smithy shape ``com.amazonaws.devopsagent#SourceAwsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.role_arn
    import capo_devops_agent.types.source_account_type
    import capo_devops_agent.types.validation_status


class SourceAwsConfiguration(TypedDict, closed=True):
    account_id: "str"
    """<p>AWS Account Id corresponding to provided resources.</p>"""
    account_type: "capo_devops_agent.types.source_account_type.SourceAccountType"
    """<p>Account Type 'source' for AIDevOps monitoring.</p>"""
    assumable_role_arn: "capo_devops_agent.types.role_arn.RoleArn"
    """<p>Role ARN to be assumed by AIDevOps to operate on behalf of customer. To set this role ARN on AssociateService or UpdateAssociation, the caller must have at least the iam:PassRole permission on arn:aws:iam::&lt;account-id&gt;:role/* in the caller's own account, with the condition iam:PassedToService set to aidevops.amazonaws.com. A broader iam:PassRole grant also satisfies this requirement.</p>"""
    external_id: NotRequired["str"]
    """<p>External ID for additional security when assuming the role. Used to prevent the confused deputy problem.</p>"""
    agent_elevated_role_arn: NotRequired["capo_devops_agent.types.role_arn.RoleArn"]
    """<p>Optional IAM role ARN to be assumed by AIDevOps for elevated directed actions on behalf of the customer. Used for mutating operations gated by elevatedActionsEnabled on the AgentSpace. When not provided, only non-elevated directed actions are available for this AWS account. Setting this role is subject to the same minimum iam:PassRole requirement described on assumableRoleArn.</p>"""
    agent_elevated_role_arn_status: NotRequired[
        "capo_devops_agent.types.validation_status.ValidationStatus"
    ]
    """<p>Validation status of the agentElevatedRoleArn. Updated asynchronously after the customer registers an elevated role. Possible values: PENDING_CONFIRMATION (validation in progress), VALID (role validated), INVALID (validation failed).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceAwsConfiguration) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_devops_agent.types.source_account_type

    out["accountType"] = capo_devops_agent.types.source_account_type.serialize_json(
        value["account_type"]
    )
    out["assumableRoleArn"] = value["assumable_role_arn"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "agent_elevated_role_arn" in value:
        out["agentElevatedRoleArn"] = value["agent_elevated_role_arn"]
    if "agent_elevated_role_arn_status" in value:
        import capo_devops_agent.types.validation_status

        out["agentElevatedRoleArnStatus"] = (
            capo_devops_agent.types.validation_status.serialize_json(
                value["agent_elevated_role_arn_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> SourceAwsConfiguration:
    out: SourceAwsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("accountType") is not None:
        import capo_devops_agent.types.source_account_type

        out["account_type"] = (
            capo_devops_agent.types.source_account_type.deserialize_json(
                data["accountType"]
            )
        )
    else:
        import typing

        out["account_type"] = typing.cast(
            "capo_devops_agent.types.source_account_type.SourceAccountType", ""
        )
    if data.get("assumableRoleArn") is not None:
        out["assumable_role_arn"] = data["assumableRoleArn"]
    else:
        out["assumable_role_arn"] = ""
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("agentElevatedRoleArn") is not None:
        out["agent_elevated_role_arn"] = data["agentElevatedRoleArn"]
    if data.get("agentElevatedRoleArnStatus") is not None:
        import capo_devops_agent.types.validation_status

        out["agent_elevated_role_arn_status"] = (
            capo_devops_agent.types.validation_status.deserialize_json(
                data["agentElevatedRoleArnStatus"]
            )
        )
    return out
