"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#GetBenefitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.catalog_name


class GetBenefitInput(TypedDict, closed=True):
    catalog: "capo_partnercentral_benefits.types.catalog_name.CatalogName"
    """<p>The catalog identifier that specifies which benefit catalog to query.</p>"""
    identifier: "str"
    """<p>The unique identifier of the benefit to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBenefitInput) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBenefitInput:
    out: GetBenefitInput = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    return out
