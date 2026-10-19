"""Generated from Smithy shape ``com.amazonaws.rtbfabric#OpenRtbAttributeModuleParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.action
    import capo_rtbfabric.types.filter_configuration
    import capo_rtbfabric.types.filter_type


class OpenRtbAttributeModuleParameters(TypedDict, closed=True):
    filter_type: "capo_rtbfabric.types.filter_type.FilterType"
    """<p>The filter type.</p>"""
    filter_configuration: (
        "capo_rtbfabric.types.filter_configuration.FilterConfiguration"
    )
    """<p>Describes the configuration of a filter.</p>"""
    action: "capo_rtbfabric.types.action.Action"
    """<p>Describes a bid action.</p>"""
    holdback_percentage: "float"
    """<p>The hold back percentage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenRtbAttributeModuleParameters) -> dict:
    out: dict = {}
    import capo_rtbfabric.types.filter_type

    out["filterType"] = capo_rtbfabric.types.filter_type.serialize_json(
        value["filter_type"]
    )
    import capo_rtbfabric.types.filter_configuration

    out["filterConfiguration"] = (
        capo_rtbfabric.types.filter_configuration.serialize_json(
            value["filter_configuration"]
        )
    )
    import capo_rtbfabric.types.action

    out["action"] = capo_rtbfabric.types.action.serialize_json(value["action"])
    out["holdbackPercentage"] = (
        "NaN"
        if value["holdback_percentage"] != value["holdback_percentage"]
        else "Infinity"
        if value["holdback_percentage"] == float("inf")
        else "-Infinity"
        if value["holdback_percentage"] == float("-inf")
        else value["holdback_percentage"]
    )
    return out


def deserialize_json(data: dict) -> OpenRtbAttributeModuleParameters:
    out: OpenRtbAttributeModuleParameters = {}  # type: ignore[typeddict-item]
    if data.get("filterType") is not None:
        import capo_rtbfabric.types.filter_type

        out["filter_type"] = capo_rtbfabric.types.filter_type.deserialize_json(
            data["filterType"]
        )
    else:
        import typing

        out["filter_type"] = typing.cast(
            "capo_rtbfabric.types.filter_type.FilterType", ""
        )
    if data.get("filterConfiguration") is not None:
        import capo_rtbfabric.types.filter_configuration

        out["filter_configuration"] = (
            capo_rtbfabric.types.filter_configuration.deserialize_json(
                data["filterConfiguration"]
            )
        )
    else:
        out["filter_configuration"] = []
    if data.get("action") is not None:
        import capo_rtbfabric.types.action

        out["action"] = capo_rtbfabric.types.action.deserialize_json(data["action"])
    else:
        import capo_rtbfabric.types._unknown

        out["action"] = capo_rtbfabric.types._unknown.UnknownUnionMember("")
    if data.get("holdbackPercentage") is not None:
        out["holdback_percentage"] = float(data["holdbackPercentage"])
    else:
        out["holdback_percentage"] = 0.0
    return out
