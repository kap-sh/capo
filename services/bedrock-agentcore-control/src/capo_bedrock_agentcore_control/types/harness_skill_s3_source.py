"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSkillS3Source``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_skill_s3_uri


class HarnessSkillS3Source(TypedDict, closed=True):
    uri: "capo_bedrock_agentcore_control.types.harness_skill_s3_uri.HarnessSkillS3Uri"
    """<p>The S3 URI pointing to the skill directory (e.g., s3://bucket/skills/my-skill/).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSkillS3Source) -> dict:
    out: dict = {}
    out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> HarnessSkillS3Source:
    out: HarnessSkillS3Source = {}  # type: ignore[typeddict-item]
    if data.get("uri") is not None:
        out["uri"] = data["uri"]
    else:
        out["uri"] = ""
    return out
