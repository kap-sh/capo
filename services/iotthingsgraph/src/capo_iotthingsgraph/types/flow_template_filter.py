"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#FlowTemplateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.flow_template_filter_name
    import capo_iotthingsgraph.types.flow_template_filter_values


class FlowTemplateFilter(TypedDict, closed=True):
    name: "capo_iotthingsgraph.types.flow_template_filter_name.FlowTemplateFilterName"
    """<p>The name of the search filter field.</p>"""
    value: (
        "capo_iotthingsgraph.types.flow_template_filter_values.FlowTemplateFilterValues"
    )
    """<p>An array of string values for the search filter field. Multiple values function as AND criteria in the search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlowTemplateFilter) -> dict:
    out: dict = {}
    import capo_iotthingsgraph.types.flow_template_filter_name

    out["name"] = (
        capo_iotthingsgraph.types.flow_template_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import capo_iotthingsgraph.types.flow_template_filter_values

    out["value"] = (
        capo_iotthingsgraph.types.flow_template_filter_values.serialize_aws_json_1_1(
            value["value"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> FlowTemplateFilter:
    out: FlowTemplateFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_iotthingsgraph.types.flow_template_filter_name

        out["name"] = (
            capo_iotthingsgraph.types.flow_template_filter_name.deserialize_aws_json_1_1(
                data["name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_iotthingsgraph.types.flow_template_filter_name.FlowTemplateFilterName",
            "",
        )
    if data.get("value") is not None:
        import capo_iotthingsgraph.types.flow_template_filter_values

        out["value"] = (
            capo_iotthingsgraph.types.flow_template_filter_values.deserialize_aws_json_1_1(
                data["value"]
            )
        )
    else:
        out["value"] = []
    return out
