"""Generated from Smithy shape ``com.amazonaws.taxsettings#UkraineAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.ukraine_trn_type


class UkraineAdditionalInfo(TypedDict, closed=True):
    ukraine_trn_type: "capo_taxsettings.types.ukraine_trn_type.UkraineTrnType"
    """<p> The tax registration type. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UkraineAdditionalInfo) -> dict:
    out: dict = {}
    import capo_taxsettings.types.ukraine_trn_type

    out["ukraineTrnType"] = capo_taxsettings.types.ukraine_trn_type.serialize_json(
        value["ukraine_trn_type"]
    )
    return out


def deserialize_json(data: dict) -> UkraineAdditionalInfo:
    out: UkraineAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("ukraineTrnType") is not None:
        import capo_taxsettings.types.ukraine_trn_type

        out["ukraine_trn_type"] = (
            capo_taxsettings.types.ukraine_trn_type.deserialize_json(
                data["ukraineTrnType"]
            )
        )
    else:
        import typing

        out["ukraine_trn_type"] = typing.cast(
            "capo_taxsettings.types.ukraine_trn_type.UkraineTrnType", ""
        )
    return out
