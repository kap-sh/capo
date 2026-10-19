"""Generated from Smithy shape ``com.amazonaws.taxsettings#PutTaxExemptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_taxsettings.errors import DeserializationError

if TYPE_CHECKING:
    import capo_taxsettings.types.account_ids
    import capo_taxsettings.types.authority
    import capo_taxsettings.types.exemption_certificate
    import capo_taxsettings.types.generic_string


class PutTaxExemptionRequest(TypedDict, closed=True):
    account_ids: "capo_taxsettings.types.account_ids.AccountIds"
    """<p> The list of unique account identifiers. </p>"""
    authority: "capo_taxsettings.types.authority.Authority"
    exemption_type: "capo_taxsettings.types.generic_string.GenericString"
    """<p>The exemption type. Use the supported tax exemption type description. </p>"""
    exemption_certificate: (
        "capo_taxsettings.types.exemption_certificate.ExemptionCertificate"
    )


# --- restJson1 ser/de ---
def serialize_json(value: PutTaxExemptionRequest) -> dict:
    out: dict = {}
    import capo_taxsettings.types.account_ids

    out["accountIds"] = capo_taxsettings.types.account_ids.serialize_json(
        value["account_ids"]
    )
    import capo_taxsettings.types.authority

    out["authority"] = capo_taxsettings.types.authority.serialize_json(
        value["authority"]
    )
    out["exemptionType"] = value["exemption_type"]
    import capo_taxsettings.types.exemption_certificate

    out["exemptionCertificate"] = (
        capo_taxsettings.types.exemption_certificate.serialize_json(
            value["exemption_certificate"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTaxExemptionRequest:
    out: PutTaxExemptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountIds") is not None:
        import capo_taxsettings.types.account_ids

        out["account_ids"] = capo_taxsettings.types.account_ids.deserialize_json(
            data["accountIds"]
        )
    else:
        out["account_ids"] = []
    if data.get("authority") is not None:
        import capo_taxsettings.types.authority

        out["authority"] = capo_taxsettings.types.authority.deserialize_json(
            data["authority"]
        )
    else:
        raise DeserializationError("PutTaxExemptionRequest.authority required")
    if data.get("exemptionType") is not None:
        out["exemption_type"] = data["exemptionType"]
    else:
        out["exemption_type"] = ""
    if data.get("exemptionCertificate") is not None:
        import capo_taxsettings.types.exemption_certificate

        out["exemption_certificate"] = (
            capo_taxsettings.types.exemption_certificate.deserialize_json(
                data["exemptionCertificate"]
            )
        )
    else:
        raise DeserializationError(
            "PutTaxExemptionRequest.exemption_certificate required"
        )
    return out
