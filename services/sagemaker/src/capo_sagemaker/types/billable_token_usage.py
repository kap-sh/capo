"""Generated from Smithy shape ``com.amazonaws.sagemaker#BillableTokenUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.java_long


class BillableTokenUsage(TypedDict, closed=True):
    prefill_token_count: NotRequired["capo_sagemaker.types.java_long.JavaLong"]
    """<p>The number of prefill tokens consumed.</p>"""
    sample_token_count: NotRequired["capo_sagemaker.types.java_long.JavaLong"]
    """<p>The number of sample tokens consumed.</p>"""
    training_token_count: NotRequired["capo_sagemaker.types.java_long.JavaLong"]
    """<p>The number of training tokens consumed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BillableTokenUsage) -> dict:
    out: dict = {}
    if "prefill_token_count" in value:
        out["PrefillTokenCount"] = value["prefill_token_count"]
    if "sample_token_count" in value:
        out["SampleTokenCount"] = value["sample_token_count"]
    if "training_token_count" in value:
        out["TrainingTokenCount"] = value["training_token_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BillableTokenUsage:
    out: BillableTokenUsage = {}  # type: ignore[typeddict-item]
    if data.get("PrefillTokenCount") is not None:
        out["prefill_token_count"] = data["PrefillTokenCount"]
    if data.get("SampleTokenCount") is not None:
        out["sample_token_count"] = data["SampleTokenCount"]
    if data.get("TrainingTokenCount") is not None:
        out["training_token_count"] = data["TrainingTokenCount"]
    return out
