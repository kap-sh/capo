"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#TargetAudience``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.company_size_list
    import capo_partnercentral_marketing.types.country_code_list
    import capo_partnercentral_marketing.types.industry_list


class TargetAudience(TypedDict, closed=True):
    industries: NotRequired[
        "capo_partnercentral_marketing.types.industry_list.IndustryList"
    ]
    """Target industries."""
    company_sizes: NotRequired[
        "capo_partnercentral_marketing.types.company_size_list.CompanySizeList"
    ]
    """Target company sizes."""
    countries: NotRequired[
        "capo_partnercentral_marketing.types.country_code_list.CountryCodeList"
    ]
    """Target countries, as ISO 3166-1 alpha-2 codes."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetAudience) -> dict:
    out: dict = {}
    if "industries" in value:
        import capo_partnercentral_marketing.types.industry_list

        out["Industries"] = (
            capo_partnercentral_marketing.types.industry_list.serialize_cbor(
                value["industries"]
            )
        )
    if "company_sizes" in value:
        import capo_partnercentral_marketing.types.company_size_list

        out["CompanySizes"] = (
            capo_partnercentral_marketing.types.company_size_list.serialize_cbor(
                value["company_sizes"]
            )
        )
    if "countries" in value:
        import capo_partnercentral_marketing.types.country_code_list

        out["Countries"] = (
            capo_partnercentral_marketing.types.country_code_list.serialize_cbor(
                value["countries"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> TargetAudience:
    out: TargetAudience = {}  # type: ignore[typeddict-item]
    if data.get("Industries") is not None:
        import capo_partnercentral_marketing.types.industry_list

        out["industries"] = (
            capo_partnercentral_marketing.types.industry_list.deserialize_cbor(
                data["Industries"]
            )
        )
    if data.get("CompanySizes") is not None:
        import capo_partnercentral_marketing.types.company_size_list

        out["company_sizes"] = (
            capo_partnercentral_marketing.types.company_size_list.deserialize_cbor(
                data["CompanySizes"]
            )
        )
    if data.get("Countries") is not None:
        import capo_partnercentral_marketing.types.country_code_list

        out["countries"] = (
            capo_partnercentral_marketing.types.country_code_list.deserialize_cbor(
                data["Countries"]
            )
        )
    return out
