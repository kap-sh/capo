"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#VariantResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.confidence_interval


class VariantResult(TypedDict, closed=True):
    variant_name: "str"
    """<p>The name of the treatment variant.</p>"""
    sample_size: "int"
    """<p>The number of sessions evaluated for this variant.</p>"""
    mean: "float"
    """<p>The mean evaluation score for this variant.</p>"""
    absolute_change: NotRequired["float"]
    """<p>The absolute change in mean score compared to the control variant.</p>"""
    percent_change: NotRequired["float"]
    """<p>The percentage change in mean score compared to the control variant.</p>"""
    p_value: NotRequired["float"]
    """<p>The p-value indicating the statistical significance of the observed difference.</p>"""
    confidence_interval: NotRequired[
        "capo_bedrock_agentcore.types.confidence_interval.ConfidenceInterval"
    ]
    """<p>The confidence interval for the observed difference.</p>"""
    is_significant: "bool"
    """<p>Whether the observed difference is statistically significant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VariantResult) -> dict:
    out: dict = {}
    out["variantName"] = value["variant_name"]
    out["sampleSize"] = value["sample_size"]
    out["mean"] = (
        "NaN"
        if value["mean"] != value["mean"]
        else "Infinity"
        if value["mean"] == float("inf")
        else "-Infinity"
        if value["mean"] == float("-inf")
        else value["mean"]
    )
    if "absolute_change" in value:
        out["absoluteChange"] = (
            "NaN"
            if value["absolute_change"] != value["absolute_change"]
            else "Infinity"
            if value["absolute_change"] == float("inf")
            else "-Infinity"
            if value["absolute_change"] == float("-inf")
            else value["absolute_change"]
        )
    if "percent_change" in value:
        out["percentChange"] = (
            "NaN"
            if value["percent_change"] != value["percent_change"]
            else "Infinity"
            if value["percent_change"] == float("inf")
            else "-Infinity"
            if value["percent_change"] == float("-inf")
            else value["percent_change"]
        )
    if "p_value" in value:
        out["pValue"] = (
            "NaN"
            if value["p_value"] != value["p_value"]
            else "Infinity"
            if value["p_value"] == float("inf")
            else "-Infinity"
            if value["p_value"] == float("-inf")
            else value["p_value"]
        )
    if "confidence_interval" in value:
        import capo_bedrock_agentcore.types.confidence_interval

        out["confidenceInterval"] = (
            capo_bedrock_agentcore.types.confidence_interval.serialize_json(
                value["confidence_interval"]
            )
        )
    out["isSignificant"] = value["is_significant"]
    return out


def deserialize_json(data: dict) -> VariantResult:
    out: VariantResult = {}  # type: ignore[typeddict-item]
    if data.get("variantName") is not None:
        out["variant_name"] = data["variantName"]
    else:
        out["variant_name"] = ""
    if data.get("sampleSize") is not None:
        out["sample_size"] = data["sampleSize"]
    else:
        out["sample_size"] = 0
    if data.get("mean") is not None:
        out["mean"] = float(data["mean"])
    else:
        out["mean"] = 0.0
    if data.get("absoluteChange") is not None:
        out["absolute_change"] = float(data["absoluteChange"])
    if data.get("percentChange") is not None:
        out["percent_change"] = float(data["percentChange"])
    if data.get("pValue") is not None:
        out["p_value"] = float(data["pValue"])
    if data.get("confidenceInterval") is not None:
        import capo_bedrock_agentcore.types.confidence_interval

        out["confidence_interval"] = (
            capo_bedrock_agentcore.types.confidence_interval.deserialize_json(
                data["confidenceInterval"]
            )
        )
    if data.get("isSignificant") is not None:
        out["is_significant"] = data["isSignificant"]
    else:
        out["is_significant"] = False
    return out
