"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSkillGitSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_skill_git_auth
    import capo_bedrock_agentcore_control.types.harness_skill_git_url


class HarnessSkillGitSource(TypedDict, closed=True):
    url: "capo_bedrock_agentcore_control.types.harness_skill_git_url.HarnessSkillGitUrl"
    """<p>The HTTPS URL of the git repository.</p>"""
    path: NotRequired["str"]
    """<p>Subdirectory within the repository containing the skill.</p>"""
    auth: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_skill_git_auth.HarnessSkillGitAuth"
    ]
    """<p>Authentication configuration for private repositories.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSkillGitSource) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    if "path" in value:
        out["path"] = value["path"]
    if "auth" in value:
        import capo_bedrock_agentcore_control.types.harness_skill_git_auth

        out["auth"] = (
            capo_bedrock_agentcore_control.types.harness_skill_git_auth.serialize_json(
                value["auth"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessSkillGitSource:
    out: HarnessSkillGitSource = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    if data.get("path") is not None:
        out["path"] = data["path"]
    if data.get("auth") is not None:
        import capo_bedrock_agentcore_control.types.harness_skill_git_auth

        out["auth"] = (
            capo_bedrock_agentcore_control.types.harness_skill_git_auth.deserialize_json(
                data["auth"]
            )
        )
    return out
