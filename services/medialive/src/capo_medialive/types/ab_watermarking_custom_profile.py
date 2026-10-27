"""Generated from Smithy shape ``com.amazonaws.medialive#AbWatermarkingCustomProfile``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double
    import capo_medialive.types.__double_min32_max46
    import capo_medialive.types.__double_min_negative1_max5


class AbWatermarkingCustomProfile(TypedDict, closed=True):
    embedding_frequency: NotRequired["capo_medialive.types.__double.__double"]
    """The frequency with which watermarks will be embedded, in milliseconds."""
    scene_cut: NotRequired[
        "capo_medialive.types.__double_min_negative1_max5.__doubleMinNegative1Max5"
    ]
    """The number of frames after scene-cut to embed the watermark."""
    target_psnr: NotRequired[
        "capo_medialive.types.__double_min32_max46.__doubleMin32Max46"
    ]
    """The target PSNR of the watermarked frame"""


# --- restJson1 ser/de ---
def serialize_json(value: AbWatermarkingCustomProfile) -> dict:
    out: dict = {}
    if "embedding_frequency" in value:
        out["embeddingFrequency"] = (
            "NaN"
            if value["embedding_frequency"] != value["embedding_frequency"]
            else "Infinity"
            if value["embedding_frequency"] == float("inf")
            else "-Infinity"
            if value["embedding_frequency"] == float("-inf")
            else value["embedding_frequency"]
        )
    if "scene_cut" in value:
        out["sceneCut"] = (
            "NaN"
            if value["scene_cut"] != value["scene_cut"]
            else "Infinity"
            if value["scene_cut"] == float("inf")
            else "-Infinity"
            if value["scene_cut"] == float("-inf")
            else value["scene_cut"]
        )
    if "target_psnr" in value:
        out["targetPsnr"] = (
            "NaN"
            if value["target_psnr"] != value["target_psnr"]
            else "Infinity"
            if value["target_psnr"] == float("inf")
            else "-Infinity"
            if value["target_psnr"] == float("-inf")
            else value["target_psnr"]
        )
    return out


def deserialize_json(data: dict) -> AbWatermarkingCustomProfile:
    out: AbWatermarkingCustomProfile = {}  # type: ignore[typeddict-item]
    if data.get("embeddingFrequency") is not None:
        out["embedding_frequency"] = float(data["embeddingFrequency"])
    if data.get("sceneCut") is not None:
        out["scene_cut"] = float(data["sceneCut"])
    if data.get("targetPsnr") is not None:
        out["target_psnr"] = float(data["targetPsnr"])
    return out
