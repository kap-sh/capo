"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#IdleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.idle_finding
    import capo_compute_optimizer.types.summary_value


class IdleSummary(TypedDict, closed=True):
    name: NotRequired["capo_compute_optimizer.types.idle_finding.IdleFinding"]
    """<p>The name of the finding group for the idle resources.</p>"""
    value: "capo_compute_optimizer.types.summary_value.SummaryValue"
    """<p>The count of idle resources in the finding group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdleSummary) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.idle_finding

        out["name"] = capo_compute_optimizer.types.idle_finding.serialize_aws_json_1_0(
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
    return out


def deserialize_aws_json_1_0(data: dict) -> IdleSummary:
    out: IdleSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.idle_finding

        out["name"] = (
            capo_compute_optimizer.types.idle_finding.deserialize_aws_json_1_0(
                data["name"]
            )
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IdleSummary) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_compute_optimizer.types.idle_finding

        out["name"] = capo_compute_optimizer.types.idle_finding.serialize_cbor(
            value["name"]
        )
    out["value"] = value.get("value", 0)
    return out


def deserialize_cbor(data: dict) -> IdleSummary:
    out: IdleSummary = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_compute_optimizer.types.idle_finding

        out["name"] = capo_compute_optimizer.types.idle_finding.deserialize_cbor(
            data["name"]
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0
    return out
