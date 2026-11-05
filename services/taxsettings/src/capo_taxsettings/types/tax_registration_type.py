"""Generated from Smithy shape ``com.amazonaws.taxsettings#TaxRegistrationType``."""

from typing import Literal, TypeAlias, cast

TaxRegistrationType: TypeAlias = Literal[
    "VAT",
    "GST",
    "CPF",
    "CNPJ",
    "SST",
    "TIN",
    "NRIC",
    "PAN",
    "NIP",
    "CUIT",
    "CDI",
    "RUT",
    "NIE",
    "CI",
]


# --- restJson1 ser/de ---
def serialize_json(value: TaxRegistrationType) -> str:
    return value


def deserialize_json(data: str) -> TaxRegistrationType:
    return cast(TaxRegistrationType, data)
