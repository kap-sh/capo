"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#ReasonCodeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.finding_reason_code
    import capo_compute_optimizer.types.summary_value


class ReasonCodeSummary(TypedDict, closed=True):
    name: NotRequired[
        "capo_compute_optimizer.types.finding_reason_code.FindingReasonCode"
    ]
    """<p>The name of the finding reason code.</p>"""
    value: "capo_compute_optimizer.types.summary_value.SummaryValue"
    """<p>The value of the finding reason code summary.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReasonCodeSummary) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.finding_reason_code

        out["name"] = (
            capo_compute_optimizer.types.finding_reason_code.serialize_aws_json_1_0(
                value["name"]
            )
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
    return out


def deserialize_aws_json_1_0(data: dict) -> ReasonCodeSummary:
    out: ReasonCodeSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.finding_reason_code

        out["name"] = (
            capo_compute_optimizer.types.finding_reason_code.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ReasonCodeSummary) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.finding_reason_code

        out["name"] = capo_compute_optimizer.types.finding_reason_code.serialize_cbor(
            value["name"]
        )
    out["value"] = value.get("value", 0)
    return out


def deserialize_cbor(data: dict) -> ReasonCodeSummary:
    out: ReasonCodeSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.finding_reason_code

        out["name"] = capo_compute_optimizer.types.finding_reason_code.deserialize_cbor(
            data["name"]
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0
    return out
