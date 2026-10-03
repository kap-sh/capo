"""Generated from Smithy shape ``com.amazonaws.uxc#UpdateAccountCustomizationsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_uxc.types.account_color
    import capo_uxc.types.regions_list
    import capo_uxc.types.service_list


class UpdateAccountCustomizationsInput(TypedDict, closed=True):
    account_color: NotRequired["capo_uxc.types.account_color.AccountColor"]
    """<p>The account color preference to set. Set to <code>none</code> to reset to the default (no color).</p>"""
    visible_services: NotRequired["capo_uxc.types.service_list.ServiceList"]
    """<p>The list of Amazon Web Services service identifiers to make visible in the Amazon Web Services Management Console. Set to <code>null</code> to reset to the default, which makes all services visible. For valid service identifiers, call <a href="https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_ListServices.html">ListServices</a>.</p>"""
    visible_regions: NotRequired["capo_uxc.types.regions_list.RegionsList"]
    """<p>The list of Amazon Web Services Region codes to make visible in the Amazon Web Services Management Console. Set to <code>null</code> to reset to the default, which makes all Regions visible. For a list of valid Region codes, see <a href="https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html">Amazon Web Services Regions</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountCustomizationsInput) -> dict:
    out: dict = {}
    if "account_color" in value:
        import capo_uxc.types.account_color

        out["accountColor"] = capo_uxc.types.account_color.serialize_json(
            value["account_color"]
        )
    if "visible_services" in value:
        import capo_uxc.types.service_list

        out["visibleServices"] = capo_uxc.types.service_list.serialize_json(
            value["visible_services"]
        )
    if "visible_regions" in value:
        import capo_uxc.types.regions_list

        out["visibleRegions"] = capo_uxc.types.regions_list.serialize_json(
            value["visible_regions"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAccountCustomizationsInput:
    out: UpdateAccountCustomizationsInput = {}  # type: ignore[typeddict-item]
    if data.get("accountColor") is not None:
        import capo_uxc.types.account_color

        out["account_color"] = capo_uxc.types.account_color.deserialize_json(
            data["accountColor"]
        )
    if data.get("visibleServices") is not None:
        import capo_uxc.types.service_list

        out["visible_services"] = capo_uxc.types.service_list.deserialize_json(
            data["visibleServices"]
        )
    if data.get("visibleRegions") is not None:
        import capo_uxc.types.regions_list

        out["visible_regions"] = capo_uxc.types.regions_list.deserialize_json(
            data["visibleRegions"]
        )
    return out
