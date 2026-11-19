"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#Summary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.finding
    import capo_compute_optimizer.types.reason_code_summaries
    import capo_compute_optimizer.types.summary_value


class Summary(TypedDict, closed=True):
    name: NotRequired["capo_compute_optimizer.types.finding.Finding"]
    """<p>The finding classification of the recommendation.</p>"""
    value: "capo_compute_optimizer.types.summary_value.SummaryValue"
    """<p>The value of the recommendation summary.</p>"""
    reason_code_summaries: NotRequired[
        "capo_compute_optimizer.types.reason_code_summaries.ReasonCodeSummaries"
    ]
    """<p>An array of objects that summarize a finding reason code.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Summary) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.finding

        out["name"] = capo_compute_optimizer.types.finding.serialize_aws_json_1_0(
            value["name"]
        )
    out["value"] = (
        "NaN"
        if value.get("value", 0) != value.get("value", 0)
        else "Infinity"
        if value.get("value", 0) == float("inf")
        else "-Infinity"
        if value.get("value", 0) == float("-inf")
        else value.get("value", 0)
    )
    if "reason_code_summaries" in value:
        import capo_compute_optimizer.types.reason_code_summaries

        out["reasonCodeSummaries"] = (
            capo_compute_optimizer.types.reason_code_summaries.serialize_aws_json_1_0(
                value["reason_code_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Summary:
    out: Summary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.finding

        out["name"] = capo_compute_optimizer.types.finding.deserialize_aws_json_1_0(
            data["name"]
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0
    if data.get("reasonCodeSummaries") is not None:
        import capo_compute_optimizer.types.reason_code_summaries

        out["reason_code_summaries"] = (
            capo_compute_optimizer.types.reason_code_summaries.deserialize_aws_json_1_0(
                data["reasonCodeSummaries"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Summary) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.finding

        out["name"] = capo_compute_optimizer.types.finding.serialize_cbor(value["name"])
    out["value"] = value.get("value", 0)
    if "reason_code_summaries" in value:
        import capo_compute_optimizer.types.reason_code_summaries

        out["reasonCodeSummaries"] = (
            capo_compute_optimizer.types.reason_code_summaries.serialize_cbor(
                value["reason_code_summaries"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> Summary:
    out: Summary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.finding

        out["name"] = capo_compute_optimizer.types.finding.deserialize_cbor(
            data["name"]
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0
    if data.get("reasonCodeSummaries") is not None:
        import capo_compute_optimizer.types.reason_code_summaries

        out["reason_code_summaries"] = (
            capo_compute_optimizer.types.reason_code_summaries.deserialize_cbor(
                data["reasonCodeSummaries"]
            )
        )
    return out
