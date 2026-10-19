"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessSkillGitAuth``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.api_key_arn


class HarnessSkillGitAuth(TypedDict, closed=True):
    credential_arn: "capo_bedrock_agentcore.types.api_key_arn.ApiKeyArn"
    """<p>The ARN of the credential in AgentCore Identity containing the password or personal access token.</p>"""
    username: NotRequired["str"]
    """<p>Username for authentication. Defaults to 'oauth2' if not specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSkillGitAuth) -> dict:
    out: dict = {}
    out["credentialArn"] = value["credential_arn"]
    if "username" in value:
        out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> HarnessSkillGitAuth:
    out: HarnessSkillGitAuth = {}  # type: ignore[typeddict-item]
    if data.get("credentialArn") is not None:
        out["credential_arn"] = data["credentialArn"]
    else:
        out["credential_arn"] = ""
    if data.get("username") is not None:
        out["username"] = data["username"]
    return out
