"""Generated from Smithy shape ``com.amazonaws.licensemanager#EntitlementUsage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.entitlement_data_unit
    import capo_license_manager.types.string


class EntitlementUsage(TypedDict, closed=True):
    name: "capo_license_manager.types.string.String"
    """<p>Entitlement usage name.</p>"""
    consumed_value: "capo_license_manager.types.string.String"
    """<p>Resource usage consumed.</p>"""
    max_count: NotRequired["capo_license_manager.types.string.String"]
    """<p>Maximum entitlement usage count.</p>"""
    unit: "capo_license_manager.types.entitlement_data_unit.EntitlementDataUnit"
    """<p>Entitlement usage unit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementUsage) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["ConsumedValue"] = value["consumed_value"]
    if "max_count" in value:
        out["MaxCount"] = value["max_count"]
    import capo_license_manager.types.entitlement_data_unit

    out["Unit"] = (
        capo_license_manager.types.entitlement_data_unit.serialize_aws_json_1_1(
            value["unit"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntitlementUsage:
    out: EntitlementUsage = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("ConsumedValue") is not None:
        out["consumed_value"] = data["ConsumedValue"]
    else:
        out["consumed_value"] = ""
    if data.get("MaxCount") is not None:
        out["max_count"] = data["MaxCount"]
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
