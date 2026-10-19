"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.condition
    import capo_application_discovery_service.types.filter_values
    import capo_application_discovery_service.types.string


class Filter(TypedDict, closed=True):
    name: "capo_application_discovery_service.types.string.String"
    """<p>The name of the filter.</p>"""
    values: "capo_application_discovery_service.types.filter_values.FilterValues"
    """<p>A string value on which to filter. For example, if you choose the <code>destinationServer.osVersion</code> filter name, you could specify <code>Ubuntu</code> for the value.</p>"""
    condition: "capo_application_discovery_service.types.condition.Condition"
    """<p>A conditional operator. The following operators are valid: EQUALS, NOT_EQUALS, CONTAINS, NOT_CONTAINS. If you specify multiple filters, the system utilizes all filters as though concatenated by <i>AND</i>. If you specify multiple values for a particular filter, the system differentiates the values using <i>OR</i>. Calling either <i>DescribeConfigurations</i> or <i>ListConfigurations</i> returns attributes of matching configuration items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_application_discovery_service.types.filter_values

    out["values"] = (
        capo_application_discovery_service.types.filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    out["condition"] = value["condition"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("values") is not None:
        import capo_application_discovery_service.types.filter_values

        out["values"] = (
            capo_application_discovery_service.types.filter_values.deserialize_aws_json_1_1(
                data["values"]
            )
        )
    else:
        out["values"] = []
    if data.get("condition") is not None:
        out["condition"] = data["condition"]
    else:
        out["condition"] = ""
    return out
