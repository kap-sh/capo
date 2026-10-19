"""Generated from Smithy shape ``com.amazonaws.licensemanager#EntitlementData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.entitlement_data_unit
    import capo_license_manager.types.string


class EntitlementData(TypedDict, closed=True):
    name: "capo_license_manager.types.string.String"
    """<p>Entitlement data name.</p>"""
    value: NotRequired["capo_license_manager.types.string.String"]
    """<p>Entitlement data value.</p>"""
    unit: "capo_license_manager.types.entitlement_data_unit.EntitlementDataUnit"
    """<p>Entitlement data unit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementData) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    import capo_license_manager.types.entitlement_data_unit

    out["Unit"] = (
        capo_license_manager.types.entitlement_data_unit.serialize_aws_json_1_1(
            value["unit"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntitlementData:
    out: EntitlementData = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("Unit") is not None:
        import capo_license_manager.types.entitlement_data_unit

        out["unit"] = (
            capo_license_manager.types.entitlement_data_unit.deserialize_aws_json_1_1(
                data["Unit"]
            )
        )
    else:
        import typing

        out["unit"] = typing.cast(
            "capo_license_manager.types.entitlement_data_unit.EntitlementDataUnit", ""
        )
    return out
