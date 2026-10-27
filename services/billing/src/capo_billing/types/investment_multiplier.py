"""Generated from Smithy shape ``com.amazonaws.billing#InvestmentMultiplier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.multiplier_type


class InvestmentMultiplier(TypedDict, closed=True):
    value: "str"
    """<p>The multiplier value, expressed as a decimal string to preserve precision. The value is digits with an optional decimal point and is 1–1000 characters. The terms of the contract define this value.</p>"""
    investment_attestation_input_unit: "str"
    """<p>The unit of the attestation input that the multiplier applies to, such as <code>workloads migrated</code>. This value is 1–1000 characters. The terms of the contract define this value.</p>"""
    multiplier_type: "capo_billing.types.multiplier_type.MultiplierType"
    """<p>The type of the multiplier. A value of <code>PERCENTAGE</code> applies a percentage of a value. A value of <code>CURRENCY_AMOUNT</code> applies a currency amount per unit of attestation input. The terms of the contract define this value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvestmentMultiplier) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    out["investmentAttestationInputUnit"] = value["investment_attestation_input_unit"]
    import capo_billing.types.multiplier_type

    out["multiplierType"] = capo_billing.types.multiplier_type.serialize_aws_json_1_0(
        value["multiplier_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvestmentMultiplier:
    out: InvestmentMultiplier = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("investmentAttestationInputUnit") is not None:
        out["investment_attestation_input_unit"] = data[
            "investmentAttestationInputUnit"
        ]
    else:
        out["investment_attestation_input_unit"] = ""
    if data.get("multiplierType") is not None:
        import capo_billing.types.multiplier_type

        out["multiplier_type"] = (
            capo_billing.types.multiplier_type.deserialize_aws_json_1_0(
                data["multiplierType"]
            )
        )
    else:
        import typing

        out["multiplier_type"] = typing.cast(
            "capo_billing.types.multiplier_type.MultiplierType", ""
        )
    return out
