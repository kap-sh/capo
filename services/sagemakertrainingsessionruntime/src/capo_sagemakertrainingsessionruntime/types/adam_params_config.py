"""Generated from Smithy shape ``com.amazonaws.sagemakertrainingsessionruntime#AdamParamsConfig``."""

from typing_extensions import NotRequired, TypedDict


class AdamParamsConfig(TypedDict, closed=True):
    learning_rate: "float"
    """<p>The learning rate for the optimizer. Must be greater than 0.</p>"""
    beta1: "float"
    """<p>The exponential decay rate for the first moment estimates.</p>"""
    beta2: "float"
    """<p>The exponential decay rate for the second moment estimates.</p>"""
    eps: "float"
    """<p>A small constant added to the denominator for numerical stability.</p>"""
    weight_decay: "float"
    """<p>The weight decay (L2 regularization) coefficient.</p>"""
    grad_clip_norm: "float"
    """<p>The maximum gradient norm for gradient clipping. Gradients are scaled down if their norm exceeds this value.</p>"""
    lora_plus_lr_ratio: NotRequired["float"]
    """<p>The learning rate multiplier for LoRA+ B matrices relative to A matrices. When set, B matrices use <code>learningRate * loraPlusLrRatio</code> while A matrices use the base learning rate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdamParamsConfig) -> dict:
    out: dict = {}
    out["learningRate"] = (
        "NaN"
        if value["learning_rate"] != value["learning_rate"]
        else "Infinity"
        if value["learning_rate"] == float("inf")
        else "-Infinity"
        if value["learning_rate"] == float("-inf")
        else value["learning_rate"]
    )
    out["beta1"] = (
        "NaN"
        if value.get("beta1", 0.9) != value.get("beta1", 0.9)
        else "Infinity"
        if value.get("beta1", 0.9) == float("inf")
        else "-Infinity"
        if value.get("beta1", 0.9) == float("-inf")
        else value.get("beta1", 0.9)
    )
    out["beta2"] = (
        "NaN"
        if value.get("beta2", 0.95) != value.get("beta2", 0.95)
        else "Infinity"
        if value.get("beta2", 0.95) == float("inf")
        else "-Infinity"
        if value.get("beta2", 0.95) == float("-inf")
        else value.get("beta2", 0.95)
    )
    out["eps"] = (
        "NaN"
        if value.get("eps", 1e-08) != value.get("eps", 1e-08)
        else "Infinity"
        if value.get("eps", 1e-08) == float("inf")
        else "-Infinity"
        if value.get("eps", 1e-08) == float("-inf")
        else value.get("eps", 1e-08)
    )
    out["weightDecay"] = (
        "NaN"
        if value.get("weight_decay", 0) != value.get("weight_decay", 0)
        else "Infinity"
        if value.get("weight_decay", 0) == float("inf")
        else "-Infinity"
        if value.get("weight_decay", 0) == float("-inf")
        else value.get("weight_decay", 0)
    )
    out["gradClipNorm"] = (
        "NaN"
        if value.get("grad_clip_norm", 1) != value.get("grad_clip_norm", 1)
        else "Infinity"
        if value.get("grad_clip_norm", 1) == float("inf")
        else "-Infinity"
        if value.get("grad_clip_norm", 1) == float("-inf")
        else value.get("grad_clip_norm", 1)
    )
    if "lora_plus_lr_ratio" in value:
        out["loraPlusLrRatio"] = (
            "NaN"
            if value["lora_plus_lr_ratio"] != value["lora_plus_lr_ratio"]
            else "Infinity"
            if value["lora_plus_lr_ratio"] == float("inf")
            else "-Infinity"
            if value["lora_plus_lr_ratio"] == float("-inf")
            else value["lora_plus_lr_ratio"]
        )
    return out


def deserialize_json(data: dict) -> AdamParamsConfig:
    out: AdamParamsConfig = {}  # type: ignore[typeddict-item]
    if data.get("learningRate") is not None:
        out["learning_rate"] = float(data["learningRate"])
    else:
        out["learning_rate"] = 0.0
    if data.get("beta1") is not None:
        out["beta1"] = float(data["beta1"])
    else:
        out["beta1"] = 0.9
    if data.get("beta2") is not None:
        out["beta2"] = float(data["beta2"])
    else:
        out["beta2"] = 0.95
    if data.get("eps") is not None:
        out["eps"] = float(data["eps"])
    else:
        out["eps"] = 1e-08
    if data.get("weightDecay") is not None:
        out["weight_decay"] = float(data["weightDecay"])
    else:
        out["weight_decay"] = 0
    if data.get("gradClipNorm") is not None:
        out["grad_clip_norm"] = float(data["gradClipNorm"])
    else:
        out["grad_clip_norm"] = 1
    if data.get("loraPlusLrRatio") is not None:
        out["lora_plus_lr_ratio"] = float(data["loraPlusLrRatio"])
    return out
