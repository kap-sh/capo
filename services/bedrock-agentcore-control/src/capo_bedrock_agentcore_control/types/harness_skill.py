"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSkill``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_skill_aws_skills_source
    import capo_bedrock_agentcore_control.types.harness_skill_git_source
    import capo_bedrock_agentcore_control.types.harness_skill_path
    import capo_bedrock_agentcore_control.types.harness_skill_s3_source


class _HarnessSkill_path(TypedDict, closed=True):
    path: "capo_bedrock_agentcore_control.types.harness_skill_path.HarnessSkillPath"


class _HarnessSkill_s3(TypedDict, closed=True):
    s3: "capo_bedrock_agentcore_control.types.harness_skill_s3_source.HarnessSkillS3Source"


class _HarnessSkill_git(TypedDict, closed=True):
    git: "capo_bedrock_agentcore_control.types.harness_skill_git_source.HarnessSkillGitSource"


class _HarnessSkill_awsSkills(TypedDict, closed=True):
    awsSkills: "capo_bedrock_agentcore_control.types.harness_skill_aws_skills_source.HarnessSkillAwsSkillsSource"


HarnessSkill: TypeAlias = (
    _HarnessSkill_path
    | _HarnessSkill_s3
    | _HarnessSkill_git
    | _HarnessSkill_awsSkills
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSkill) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"HarnessSkill: cannot serialize unknown variant {value.name!r}"
        )
    elif "path" in value:
        return {"path": value["path"]}
    elif "s3" in value:
        import capo_bedrock_agentcore_control.types.harness_skill_s3_source

        return {
            "s3": capo_bedrock_agentcore_control.types.harness_skill_s3_source.serialize_json(
                value["s3"]
            )
        }
    elif "git" in value:
        import capo_bedrock_agentcore_control.types.harness_skill_git_source

        return {
            "git": capo_bedrock_agentcore_control.types.harness_skill_git_source.serialize_json(
                value["git"]
            )
        }
    elif "awsSkills" in value:
        import capo_bedrock_agentcore_control.types.harness_skill_aws_skills_source

        return {
            "awsSkills": capo_bedrock_agentcore_control.types.harness_skill_aws_skills_source.serialize_json(
                value["awsSkills"]
            )
        }
    else:
        raise SerializationError("HarnessSkill: no variant present")


def deserialize_json(data: dict) -> HarnessSkill:
    if data.get("path") is not None:
        return {"path": data["path"]}
    elif data.get("s3") is not None:
        import capo_bedrock_agentcore_control.types.harness_skill_s3_source

        return {
            "s3": capo_bedrock_agentcore_control.types.harness_skill_s3_source.deserialize_json(
                data["s3"]
            )
        }
    elif data.get("git") is not None:
        import capo_bedrock_agentcore_control.types.harness_skill_git_source

        return {
            "git": capo_bedrock_agentcore_control.types.harness_skill_git_source.deserialize_json(
                data["git"]
            )
        }
    elif data.get("awsSkills") is not None:
        import capo_bedrock_agentcore_control.types.harness_skill_aws_skills_source

        return {
            "awsSkills": capo_bedrock_agentcore_control.types.harness_skill_aws_skills_source.deserialize_json(
                data["awsSkills"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("HarnessSkill: no recognized variant key")
