"""Generated from Smithy shape ``com.amazonaws.taxsettings#BatchGetTaxExemptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.account_ids


class BatchGetTaxExemptionsRequest(TypedDict, closed=True):
    account_ids: "capo_taxsettings.types.account_ids.AccountIds"
    """<p> List of unique account identifiers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTaxExemptionsRequest) -> dict:
    out: dict = {}
    import capo_taxsettings.types.account_ids

    out["accountIds"] = capo_taxsettings.types.account_ids.serialize_json(
        value["account_ids"]
    )
    return out


def deserialize_json(data: dict) -> BatchGetTaxExemptionsRequest:
    out: BatchGetTaxExemptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_taxsettings.types.account_ids

        out["account_ids"] = capo_taxsettings.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    else:
        out["account_ids"] = []
    return out
