"""Generated from Smithy shape ``com.amazonaws.configservice#ConnectorFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.connector_filter_name
    import capo_config_service.types.filter_value_list


class ConnectorFilter(TypedDict, closed=True):
    filter_name: NotRequired[
        "capo_config_service.types.connector_filter_name.ConnectorFilterName"
    ]
    """<p>The name of the filter. Currently, only <code>provider</code> is supported.</p>"""
    filter_values: NotRequired[
        "capo_config_service.types.filter_value_list.FilterValueList"
    ]
    """<p>The value of the filter. For <code>provider</code>, valid values include:</p> <ul> <li> <p> <code>AZURE</code> – The connector is for Microsoft Azure</p> </li> <li> <p> <code>GCP</code> – The connector is for Google Cloud</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorFilter) -> dict:
    out: dict = {}
    if "filter_name" in value:
        import capo_config_service.types.connector_filter_name

        out["filterName"] = (
            capo_config_service.types.connector_filter_name.serialize_aws_json_1_1(
                value["filter_name"]
            )
        )
    if "filter_values" in value:
        import capo_config_service.types.filter_value_list

        out["filterValues"] = (
            capo_config_service.types.filter_value_list.serialize_aws_json_1_1(
                value["filter_values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectorFilter:
    out: ConnectorFilter = {}  # type: ignore[typeddict-item]
    if data.get("filterName") is not None:
        import capo_config_service.types.connector_filter_name

        out["filter_name"] = (
            capo_config_service.types.connector_filter_name.deserialize_aws_json_1_1(
                data["filterName"]
            )
        )
    if data.get("filterValues") is not None:
        import capo_config_service.types.filter_value_list

        out["filter_values"] = (
            capo_config_service.types.filter_value_list.deserialize_aws_json_1_1(
                data["filterValues"]
            )
        )
    return out
