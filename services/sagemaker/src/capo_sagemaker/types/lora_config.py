"""Generated from Smithy shape ``com.amazonaws.sagemaker#LoraConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.lora_alpha
    import capo_sagemaker.types.rank


class LoraConfig(TypedDict, closed=True):
    rank: NotRequired["capo_sagemaker.types.rank.Rank"]
    """<p>The rank of the Low-Rank Adaptation (LoRA) adapter matrices.</p>"""
    alpha: NotRequired["capo_sagemaker.types.lora_alpha.LoraAlpha"]
    """<p>The Low-Rank Adaptation (LoRA) scaling factor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoraConfig) -> dict:
    out: dict = {}
    if "rank" in value:
        out["Rank"] = value["rank"]
    if "alpha" in value:
        out["Alpha"] = value["alpha"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LoraConfig:
    out: LoraConfig = {}  # type: ignore[typeddict-item]
    if data.get("Rank") is not None:
        out["rank"] = data["Rank"]
    if data.get("Alpha") is not None:
        out["alpha"] = data["Alpha"]
    return out
