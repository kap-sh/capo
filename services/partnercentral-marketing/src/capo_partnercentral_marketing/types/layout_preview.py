"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#LayoutPreview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.layout_format
    import capo_partnercentral_marketing.types.layout_page_type
    import capo_partnercentral_marketing.types.layout_url


class LayoutPreview(TypedDict, closed=True):
    format: "capo_partnercentral_marketing.types.layout_format.LayoutFormat"
    """The format of the referenced object."""
    url: "capo_partnercentral_marketing.types.layout_url.LayoutUrl"
    """A stable URL serving the object. Not presigned, so it does not expire."""
    page_type: NotRequired[
        "capo_partnercentral_marketing.types.layout_page_type.LayoutPageType"
    ]
    """Which page of a multi-page layout this is. Present only for LANDING_PAGE, which genuinely has two layout objects — the page carrying the form, and the confirmation page shown after submit — and absent for every other category, which has one. A confirmation page is a second LAYOUT, never a second asset: modelling it as its own asset would give it a lifecycle, an activation and a state it does not have."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LayoutPreview) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.layout_format

    out["Format"] = capo_partnercentral_marketing.types.layout_format.serialize_cbor(
        value["format"]
    )
    out["Url"] = value["url"]
    if "page_type" in value:
        import capo_partnercentral_marketing.types.layout_page_type

        out["PageType"] = (
            capo_partnercentral_marketing.types.layout_page_type.serialize_cbor(
                value["page_type"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> LayoutPreview:
    out: LayoutPreview = {}  # type: ignore[typeddict-item]
    if data.get("Format") is not None:
        import capo_partnercentral_marketing.types.layout_format

        out["format"] = (
            capo_partnercentral_marketing.types.layout_format.deserialize_cbor(
                data["Format"]
            )
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_partnercentral_marketing.types.layout_format.LayoutFormat", ""
        )
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        out["url"] = ""
    if data.get("PageType") is not None:
        import capo_partnercentral_marketing.types.layout_page_type

        out["page_type"] = (
            capo_partnercentral_marketing.types.layout_page_type.deserialize_cbor(
                data["PageType"]
            )
        )
    return out
