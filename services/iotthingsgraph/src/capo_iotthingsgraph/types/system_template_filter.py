"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#SystemTemplateFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.system_template_filter_name
    import capo_iotthingsgraph.types.system_template_filter_values


class SystemTemplateFilter(TypedDict, closed=True):
    name: (
        "capo_iotthingsgraph.types.system_template_filter_name.SystemTemplateFilterName"
    )
    """<p>The name of the system search filter field.</p>"""
    value: "capo_iotthingsgraph.types.system_template_filter_values.SystemTemplateFilterValues"
    """<p>An array of string values for the search filter field. Multiple values function as AND criteria in the search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SystemTemplateFilter) -> dict:
    out: dict = {}
    import capo_iotthingsgraph.types.system_template_filter_name

    out["name"] = (
        capo_iotthingsgraph.types.system_template_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import capo_iotthingsgraph.types.system_template_filter_values

    out["value"] = (
        capo_iotthingsgraph.types.system_template_filter_values.serialize_aws_json_1_1(
            value["value"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SystemTemplateFilter:
    out: SystemTemplateFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_iotthingsgraph.types.system_template_filter_name

        out["name"] = (
            capo_iotthingsgraph.types.system_template_filter_name.deserialize_aws_json_1_1(
                data["name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_iotthingsgraph.types.system_template_filter_name.SystemTemplateFilterName",
            "",
        )
    if data.get("value") is not None:
        import capo_iotthingsgraph.types.system_template_filter_values

        out["value"] = (
            capo_iotthingsgraph.types.system_template_filter_values.deserialize_aws_json_1_1(
                data["value"]
            )
        )
    else:
        out["value"] = []
    return out
