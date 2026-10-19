"""Generated from Smithy shape ``com.amazonaws.route53#ReusableDelegationSetLimit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.limit_value
    import capo_route_53.types.reusable_delegation_set_limit_type


class ReusableDelegationSetLimit(TypedDict, closed=True):
    type: "capo_route_53.types.reusable_delegation_set_limit_type.ReusableDelegationSetLimitType"
    """<p>The limit that you requested: <code>MAX_ZONES_BY_REUSABLE_DELEGATION_SET</code>, the maximum number of hosted zones that you can associate with the specified reusable delegation set.</p>"""
    value: "capo_route_53.types.limit_value.LimitValue"
    """<p>The current value for the <code>MAX_ZONES_BY_REUSABLE_DELEGATION_SET</code> limit.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: ReusableDelegationSetLimit, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.reusable_delegation_set_limit_type

    capo_route_53.types.reusable_delegation_set_limit_type.serialize_xml(
        value["type"], el, "Type"
    )
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> ReusableDelegationSetLimit:
    out: ReusableDelegationSetLimit = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_route_53.types.reusable_delegation_set_limit_type

        out["type"] = (
            capo_route_53.types.reusable_delegation_set_limit_type.deserialize_xml(
                child_type
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_route_53.types.reusable_delegation_set_limit_type.ReusableDelegationSetLimitType",
            "",
        )
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = int(child_value.text or "")
    else:
        out["value"] = 0
    return out
