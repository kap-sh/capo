"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#Ec2RecommendationsExportPreferences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.excluded_instance_types
    import capo_application_discovery_service.types.export_enabled
    import capo_application_discovery_service.types.reserved_instance_options
    import capo_application_discovery_service.types.tenancy
    import capo_application_discovery_service.types.usage_metric_basis
    import capo_application_discovery_service.types.user_preferred_region


class Ec2RecommendationsExportPreferences(TypedDict, closed=True):
    enabled: "capo_application_discovery_service.types.export_enabled.ExportEnabled"
    """<p> If set to true, the export <a href="https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_StartExportTask.html#API_StartExportTask_RequestSyntax">preferences</a> is set to <code>Ec2RecommendationsExportPreferences</code>. </p>"""
    cpu_performance_metric_basis: NotRequired[
        "capo_application_discovery_service.types.usage_metric_basis.UsageMetricBasis"
    ]
    """<p> The recommended EC2 instance type that matches the CPU usage metric of server performance data. </p>"""
    ram_performance_metric_basis: NotRequired[
        "capo_application_discovery_service.types.usage_metric_basis.UsageMetricBasis"
    ]
    """<p> The recommended EC2 instance type that matches the Memory usage metric of server performance data. </p>"""
    tenancy: NotRequired["capo_application_discovery_service.types.tenancy.Tenancy"]
    """<p> The target tenancy to use for your recommended EC2 instances. </p>"""
    excluded_instance_types: NotRequired[
        "capo_application_discovery_service.types.excluded_instance_types.ExcludedInstanceTypes"
    ]
    """<p> An array of instance types to exclude from recommendations. </p>"""
    preferred_region: NotRequired[
        "capo_application_discovery_service.types.user_preferred_region.UserPreferredRegion"
    ]
    """<p> The target Amazon Web Services Region for the recommendations. You can use any of the Region codes available for the chosen service, as listed in <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html">Amazon Web Services service endpoints</a> in the <i>Amazon Web Services General Reference</i>. </p>"""
    reserved_instance_options: NotRequired[
        "capo_application_discovery_service.types.reserved_instance_options.ReservedInstanceOptions"
    ]
    """<p> The contract type for a reserved instance. If blank, we assume an On-Demand instance is preferred. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2RecommendationsExportPreferences) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "cpu_performance_metric_basis" in value:
        import capo_application_discovery_service.types.usage_metric_basis

        out["cpuPerformanceMetricBasis"] = (
            capo_application_discovery_service.types.usage_metric_basis.serialize_aws_json_1_1(
                value["cpu_performance_metric_basis"]
            )
        )
    if "ram_performance_metric_basis" in value:
        import capo_application_discovery_service.types.usage_metric_basis

        out["ramPerformanceMetricBasis"] = (
            capo_application_discovery_service.types.usage_metric_basis.serialize_aws_json_1_1(
                value["ram_performance_metric_basis"]
            )
        )
    if "tenancy" in value:
        import capo_application_discovery_service.types.tenancy

        out["tenancy"] = (
            capo_application_discovery_service.types.tenancy.serialize_aws_json_1_1(
                value["tenancy"]
            )
        )
    if "excluded_instance_types" in value:
        import capo_application_discovery_service.types.excluded_instance_types

        out["excludedInstanceTypes"] = (
            capo_application_discovery_service.types.excluded_instance_types.serialize_aws_json_1_1(
                value["excluded_instance_types"]
            )
        )
    if "preferred_region" in value:
        out["preferredRegion"] = value["preferred_region"]
    if "reserved_instance_options" in value:
        import capo_application_discovery_service.types.reserved_instance_options

        out["reservedInstanceOptions"] = (
            capo_application_discovery_service.types.reserved_instance_options.serialize_aws_json_1_1(
                value["reserved_instance_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Ec2RecommendationsExportPreferences:
    out: Ec2RecommendationsExportPreferences = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("cpuPerformanceMetricBasis") is not None:
        import capo_application_discovery_service.types.usage_metric_basis

        out["cpu_performance_metric_basis"] = (
            capo_application_discovery_service.types.usage_metric_basis.deserialize_aws_json_1_1(
                data["cpuPerformanceMetricBasis"]
            )
        )
    if data.get("ramPerformanceMetricBasis") is not None:
        import capo_application_discovery_service.types.usage_metric_basis

        out["ram_performance_metric_basis"] = (
            capo_application_discovery_service.types.usage_metric_basis.deserialize_aws_json_1_1(
                data["ramPerformanceMetricBasis"]
            )
        )
    if data.get("tenancy") is not None:
        import capo_application_discovery_service.types.tenancy

        out["tenancy"] = (
            capo_application_discovery_service.types.tenancy.deserialize_aws_json_1_1(
                data["tenancy"]
            )
        )
    if data.get("excludedInstanceTypes") is not None:
        import capo_application_discovery_service.types.excluded_instance_types

        out["excluded_instance_types"] = (
            capo_application_discovery_service.types.excluded_instance_types.deserialize_aws_json_1_1(
                data["excludedInstanceTypes"]
            )
        )
    if data.get("preferredRegion") is not None:
        out["preferred_region"] = data["preferredRegion"]
    if data.get("reservedInstanceOptions") is not None:
        import capo_application_discovery_service.types.reserved_instance_options

        out["reserved_instance_options"] = (
            capo_application_discovery_service.types.reserved_instance_options.deserialize_aws_json_1_1(
                data["reservedInstanceOptions"]
            )
        )
    return out
