"""Generated from Smithy shape ``com.amazonaws.licensemanager#Entitlement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.box_boolean
    import capo_license_manager.types.entitlement_unit
    import capo_license_manager.types.long
    import capo_license_manager.types.string


class Entitlement(TypedDict, closed=True):
    name: "capo_license_manager.types.string.String"
    """<p>Entitlement name.</p>"""
    value: NotRequired["capo_license_manager.types.string.String"]
    """<p>Entitlement resource. Use only if the unit is None.</p>"""
    max_count: NotRequired["capo_license_manager.types.long.Long"]
    """<p>Maximum entitlement count. Use if the unit is not None.</p>"""
    overage: NotRequired["capo_license_manager.types.box_boolean.BoxBoolean"]
    """<p>Indicates whether overages are allowed.</p>"""
    unit: "capo_license_manager.types.entitlement_unit.EntitlementUnit"
    """<p>Entitlement unit.</p>"""
    allow_check_in: NotRequired["capo_license_manager.types.box_boolean.BoxBoolean"]
    """<p>Indicates whether check-ins are allowed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Entitlement) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    if "max_count" in value:
        out["MaxCount"] = value["max_count"]
    if "overage" in value:
        out["Overage"] = value["overage"]
    import capo_license_manager.types.entitlement_unit

    out["Unit"] = capo_license_manager.types.entitlement_unit.serialize_aws_json_1_1(
        value["unit"]
    )
    if "allow_check_in" in value:
        out["AllowCheckIn"] = value["allow_check_in"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Entitlement:
    out: Entitlement = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    if data.get("MaxCount") is not None:
        out["max_count"] = data["MaxCount"]
    if data.get("Overage") is not None:
        out["overage"] = data["Overage"]
    if data.get("Unit") is not None:
        import capo_license_manager.types.entitlement_unit

        out["unit"] = (
            capo_license_manager.types.entitlement_unit.deserialize_aws_json_1_1(
                data["Unit"]
            )
        )
    else:
        import typing

        out["unit"] = typing.cast(
            "capo_license_manager.types.entitlement_unit.EntitlementUnit", ""
        )
    if data.get("AllowCheckIn") is not None:
        out["allow_check_in"] = data["AllowCheckIn"]
    return out
