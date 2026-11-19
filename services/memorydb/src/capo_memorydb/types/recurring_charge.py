"""Generated from Smithy shape ``com.amazonaws.memorydb#RecurringCharge``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.double
    import capo_memorydb.types.string


class RecurringCharge(TypedDict, closed=True):
    recurring_charge_amount: "capo_memorydb.types.double.Double"
    """<p>The amount of the recurring charge to run this reserved node.</p>"""
    recurring_charge_frequency: NotRequired["capo_memorydb.types.string.String"]
    """<p>The frequency of the recurring price charged to run this reserved node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecurringCharge) -> dict:
    out: dict = {}
    out["RecurringChargeAmount"] = (
        "NaN"
        if value.get("recurring_charge_amount", 0)
        != value.get("recurring_charge_amount", 0)
        else "Infinity"
        if value.get("recurring_charge_amount", 0) == float("inf")
        else "-Infinity"
        if value.get("recurring_charge_amount", 0) == float("-inf")
        else value.get("recurring_charge_amount", 0)
    )
    if "recurring_charge_frequency" in value:
        out["RecurringChargeFrequency"] = value["recurring_charge_frequency"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecurringCharge:
    out: RecurringCharge = {}  # type: ignore[typeddict-item]
    if data.get("RecurringChargeAmount") is not None:
        out["recurring_charge_amount"] = float(data["RecurringChargeAmount"])
    else:
        out["recurring_charge_amount"] = 0
    if data.get("RecurringChargeFrequency") is not None:
        out["recurring_charge_frequency"] = data["RecurringChargeFrequency"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecurringCharge) -> dict:
    out: dict = {}
    out["RecurringChargeAmount"] = value.get("recurring_charge_amount", 0)
    if "recurring_charge_frequency" in value:
        out["RecurringChargeFrequency"] = value["recurring_charge_frequency"]
    return out


def deserialize_cbor(data: dict) -> RecurringCharge:
    out: RecurringCharge = {}  # type: ignore[typeddict-item]
    if data.get("RecurringChargeAmount") is not None:
        out["recurring_charge_amount"] = float(data["RecurringChargeAmount"])
    else:
        out["recurring_charge_amount"] = 0
    if data.get("RecurringChargeFrequency") is not None:
        out["recurring_charge_frequency"] = data["RecurringChargeFrequency"]
    return out
