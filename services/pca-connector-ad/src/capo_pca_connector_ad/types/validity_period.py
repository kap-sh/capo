"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ValidityPeriod``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.validity_period_type


class ValidityPeriod(TypedDict, closed=True):
    period_type: "capo_pca_connector_ad.types.validity_period_type.ValidityPeriodType"
    """<p>The unit of time. You can select hours, days, weeks, months, and years.</p>"""
    period: "int"
    """<p>The numeric value for the validity period.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidityPeriod) -> dict:
    out: dict = {}
    import capo_pca_connector_ad.types.validity_period_type

    out["PeriodType"] = capo_pca_connector_ad.types.validity_period_type.serialize_json(
        value["period_type"]
    )
    out["Period"] = value["period"]
    return out


def deserialize_json(data: dict) -> ValidityPeriod:
    out: ValidityPeriod = {}  # type: ignore[typeddict-item]
    if data.get("PeriodType") is not None:
        import capo_pca_connector_ad.types.validity_period_type

        out["period_type"] = (
            capo_pca_connector_ad.types.validity_period_type.deserialize_json(
                data["PeriodType"]
            )
        )
    else:
        import typing

        out["period_type"] = typing.cast(
            "capo_pca_connector_ad.types.validity_period_type.ValidityPeriodType", ""
        )
    if data.get("Period") is not None:
        out["period"] = data["Period"]
    else:
        out["period"] = 0
    return out
