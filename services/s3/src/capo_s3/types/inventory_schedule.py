"""Generated from Smithy shape ``com.amazonaws.s3#InventorySchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.inventory_frequency


class InventorySchedule(TypedDict, closed=True):
    frequency: "capo_s3.types.inventory_frequency.InventoryFrequency"
    """<p>Specifies how frequently inventory results are produced.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: InventorySchedule, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.inventory_frequency

    capo_s3.types.inventory_frequency.serialize_xml(value["frequency"], el, "Frequency")


def deserialize_xml(el: Element) -> InventorySchedule:
    out: InventorySchedule = {}  # type: ignore[typeddict-item]
    child_frequency = el.find("Frequency")
    if child_frequency is not None:
        import capo_s3.types.inventory_frequency

        out["frequency"] = capo_s3.types.inventory_frequency.deserialize_xml(
            child_frequency
        )
    else:
        import typing

        out["frequency"] = typing.cast(
            "capo_s3.types.inventory_frequency.InventoryFrequency", ""
        )
    return out
