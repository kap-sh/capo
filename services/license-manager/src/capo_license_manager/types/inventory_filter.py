"""Generated from Smithy shape ``com.amazonaws.licensemanager#InventoryFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.inventory_filter_condition
    import capo_license_manager.types.string


class InventoryFilter(TypedDict, closed=True):
    name: "capo_license_manager.types.string.String"
    """<p>Name of the filter.</p>"""
    condition: (
        "capo_license_manager.types.inventory_filter_condition.InventoryFilterCondition"
    )
    """<p>Condition of the filter.</p>"""
    value: NotRequired["capo_license_manager.types.string.String"]
    """<p>Value of the filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryFilter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_license_manager.types.inventory_filter_condition

    out["Condition"] = (
        capo_license_manager.types.inventory_filter_condition.serialize_aws_json_1_1(
            value["condition"]
        )
    )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryFilter:
    out: InventoryFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Condition") is not None:
        import capo_license_manager.types.inventory_filter_condition

        out["condition"] = (
            capo_license_manager.types.inventory_filter_condition.deserialize_aws_json_1_1(
                data["Condition"]
            )
        )
    else:
        import typing

        out["condition"] = typing.cast(
            "capo_license_manager.types.inventory_filter_condition.InventoryFilterCondition",
            "",
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
