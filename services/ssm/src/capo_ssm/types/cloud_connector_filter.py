"""Generated from Smithy shape ``com.amazonaws.ssm#CloudConnectorFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.cloud_connector_filter_key
    import capo_ssm.types.cloud_connector_filter_values


class CloudConnectorFilter(TypedDict, closed=True):
    filter_key: NotRequired[
        "capo_ssm.types.cloud_connector_filter_key.CloudConnectorFilterKey"
    ]
    """<p>The name of the filter key.</p>"""
    filter_values: NotRequired[
        "capo_ssm.types.cloud_connector_filter_values.CloudConnectorFilterValues"
    ]
    """<p>The filter values. Valid values for each filter key are as follows:</p> <dl> <dt>SubscriptionId</dt> <dd> <p>The Azure subscription ID to filter by. To return only tenant-level connectors, specify <code>NONE</code>.</p> </dd> <dt>TenantId</dt> <dd> <p>The Azure tenant ID to filter by. Filters the results to connectors that target the specified tenant.</p> </dd> <dt>ProjectId</dt> <dd> <p>The Google Cloud Platform (GCP) project ID to filter by. Filters the results to connectors that target the specified project.</p> </dd> <dt>OrganizationId</dt> <dd> <p>The GCP organization ID to filter by. Filters the results to connectors that target the entire specified organization.</p> </dd> </dl> <p>You can't combine Azure filter keys (<code>SubscriptionId</code> and <code>TenantId</code>) with GCP filter keys (<code>ProjectId</code> and <code>OrganizationId</code>) in the same request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudConnectorFilter) -> dict:
    out: dict = {}
    if "filter_key" in value:
        import capo_ssm.types.cloud_connector_filter_key

        out["FilterKey"] = (
            capo_ssm.types.cloud_connector_filter_key.serialize_aws_json_1_1(
                value["filter_key"]
            )
        )
    if "filter_values" in value:
        import capo_ssm.types.cloud_connector_filter_values

        out["FilterValues"] = (
            capo_ssm.types.cloud_connector_filter_values.serialize_aws_json_1_1(
                value["filter_values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CloudConnectorFilter:
    out: CloudConnectorFilter = {}  # type: ignore[typeddict-item]
    if data.get("FilterKey") is not None:
        import capo_ssm.types.cloud_connector_filter_key

        out["filter_key"] = (
            capo_ssm.types.cloud_connector_filter_key.deserialize_aws_json_1_1(
                data["FilterKey"]
            )
        )
    if data.get("FilterValues") is not None:
        import capo_ssm.types.cloud_connector_filter_values

        out["filter_values"] = (
            capo_ssm.types.cloud_connector_filter_values.deserialize_aws_json_1_1(
                data["FilterValues"]
            )
        )
    return out
