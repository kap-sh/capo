"""Generated from Smithy shape ``com.amazonaws.invoicing#ProcurementPortal``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string
    import capo_invoicing.types.feature_configurations
    import capo_invoicing.types.procurement_portal_id_string
    import capo_invoicing.types.procurement_portal_name


class ProcurementPortal(TypedDict, closed=True):
    portal_identifier: (
        "capo_invoicing.types.procurement_portal_id_string.ProcurementPortalIdString"
    )
    """<p>The unique identifier of the procurement portal.</p>"""
    portal_name: "capo_invoicing.types.procurement_portal_name.ProcurementPortalName"
    """<p>The name of the procurement portal.</p>"""
    portal_display_name: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p>The display name of the procurement portal.</p>"""
    default_feature_configurations: NotRequired[
        "capo_invoicing.types.feature_configurations.FeatureConfigurations"
    ]
    """<p>The default feature configurations for the procurement portal.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProcurementPortal) -> dict:
    out: dict = {}
    out["PortalIdentifier"] = value["portal_identifier"]
    import capo_invoicing.types.procurement_portal_name

    out["PortalName"] = (
        capo_invoicing.types.procurement_portal_name.serialize_aws_json_1_0(
            value["portal_name"]
        )
    )
    if "portal_display_name" in value:
        out["PortalDisplayName"] = value["portal_display_name"]
    if "default_feature_configurations" in value:
        import capo_invoicing.types.feature_configurations

        out["DefaultFeatureConfigurations"] = (
            capo_invoicing.types.feature_configurations.serialize_aws_json_1_0(
                value["default_feature_configurations"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProcurementPortal:
    out: ProcurementPortal = {}  # type: ignore[typeddict-item]
    if data.get("PortalIdentifier") is not None:
        out["portal_identifier"] = data["PortalIdentifier"]
    else:
        out["portal_identifier"] = ""
    if data.get("PortalName") is not None:
        import capo_invoicing.types.procurement_portal_name

        out["portal_name"] = (
            capo_invoicing.types.procurement_portal_name.deserialize_aws_json_1_0(
                data["PortalName"]
            )
        )
    else:
        import typing

        out["portal_name"] = typing.cast(
            "capo_invoicing.types.procurement_portal_name.ProcurementPortalName", ""
        )
    if data.get("PortalDisplayName") is not None:
        out["portal_display_name"] = data["PortalDisplayName"]
    if data.get("DefaultFeatureConfigurations") is not None:
        import capo_invoicing.types.feature_configurations

        out["default_feature_configurations"] = (
            capo_invoicing.types.feature_configurations.deserialize_aws_json_1_0(
                data["DefaultFeatureConfigurations"]
            )
        )
    return out
