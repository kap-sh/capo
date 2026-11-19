"""Generated from Smithy shape ``com.amazonaws.securityhub#GcpProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.gcp_region_list
    import capo_securityhub.types.gcp_scope_configuration
    import capo_securityhub.types.non_empty_string


class GcpProviderConfiguration(TypedDict, closed=True):
    aws_config_connector_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the multi-cloud configuration connector used to establish the connection to GCP.</p>"""
    scope_configuration: NotRequired[
        "capo_securityhub.types.gcp_scope_configuration.GcpScopeConfiguration"
    ]
    """<p>The scope configuration that defines which GCP resources are monitored.</p>"""
    gcp_regions: NotRequired["capo_securityhub.types.gcp_region_list.GcpRegionList"]
    """<p>The list of GCP regions to monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GcpProviderConfiguration) -> dict:
    out: dict = {}
    if "aws_config_connector_arn" in value:
        out["AWSConfigConnectorArn"] = value["aws_config_connector_arn"]
    if "scope_configuration" in value:
        import capo_securityhub.types.gcp_scope_configuration

        out["ScopeConfiguration"] = (
            capo_securityhub.types.gcp_scope_configuration.serialize_json(
                value["scope_configuration"]
            )
        )
    if "gcp_regions" in value:
        import capo_securityhub.types.gcp_region_list

        out["GCPRegions"] = capo_securityhub.types.gcp_region_list.serialize_json(
            value["gcp_regions"]
        )
    return out


def deserialize_json(data: dict) -> GcpProviderConfiguration:
    out: GcpProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AWSConfigConnectorArn") is not None:
        out["aws_config_connector_arn"] = data["AWSConfigConnectorArn"]
    if data.get("ScopeConfiguration") is not None:
        import capo_securityhub.types.gcp_scope_configuration

        out["scope_configuration"] = (
            capo_securityhub.types.gcp_scope_configuration.deserialize_json(
                data["ScopeConfiguration"]
            )
        )
    if data.get("GCPRegions") is not None:
        import capo_securityhub.types.gcp_region_list

        out["gcp_regions"] = capo_securityhub.types.gcp_region_list.deserialize_json(
            data["GCPRegions"]
        )
    return out
