"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EstimatedMonthlySavings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.currency
    import capo_compute_optimizer.types.value


class EstimatedMonthlySavings(TypedDict, closed=True):
    currency: NotRequired["capo_compute_optimizer.types.currency.Currency"]
    """<p>The currency of the estimated monthly savings.</p>"""
    value: "capo_compute_optimizer.types.value.Value"
    """<p>The value of the estimated monthly savings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EstimatedMonthlySavings) -> dict:
    out: dict = {}
    if "currency" in value:
        import capo_compute_optimizer.types.currency

        out["currency"] = capo_compute_optimizer.types.currency.serialize_aws_json_1_0(
            value["currency"]
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


def deserialize_aws_json_1_0(data: dict) -> EstimatedMonthlySavings:
    out: EstimatedMonthlySavings = {}  # type: ignore[typeddict-item]
    if data.get("currency") is not None:
        import capo_compute_optimizer.types.currency

        out["currency"] = (
            capo_compute_optimizer.types.currency.deserialize_aws_json_1_0(
                data["currency"]
            )
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EstimatedMonthlySavings) -> dict:
    out: dict = {}
    if "currency" in value:
        import capo_compute_optimizer.types.currency

        out["currency"] = capo_compute_optimizer.types.currency.serialize_cbor(
            value["currency"]
        )
    out["value"] = value.get("value", 0)
    return out


def deserialize_cbor(data: dict) -> EstimatedMonthlySavings:
    out: EstimatedMonthlySavings = {}  # type: ignore[typeddict-item]
    if data.get("currency") is not None:
        import capo_compute_optimizer.types.currency

        out["currency"] = capo_compute_optimizer.types.currency.deserialize_cbor(
            data["currency"]
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0
    return out
