"""Generated from Smithy shape ``com.amazonaws.wafv2#RateLimitLabelNamespace``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.label_namespace


class RateLimitLabelNamespace(TypedDict, closed=True):
    namespace: "capo_wafv2.types.label_namespace.LabelNamespace"
    """<p>The namespace to use for aggregation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RateLimitLabelNamespace) -> dict:
    out: dict = {}
    out["Namespace"] = value["namespace"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RateLimitLabelNamespace:
    out: RateLimitLabelNamespace = {}  # type: ignore[typeddict-item]
    if data.get("Namespace") is not None:
        out["namespace"] = data["Namespace"]
    else:
        out["namespace"] = ""
    return out
