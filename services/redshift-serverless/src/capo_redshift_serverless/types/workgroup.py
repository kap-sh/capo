"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#Workgroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_redshift_serverless.types.config_parameter_list
    import capo_redshift_serverless.types.custom_domain_certificate_arn_string
    import capo_redshift_serverless.types.custom_domain_name
    import capo_redshift_serverless.types.endpoint
    import capo_redshift_serverless.types.ip_address_type
    import capo_redshift_serverless.types.performance_target
    import capo_redshift_serverless.types.security_group_id_list
    import capo_redshift_serverless.types.subnet_id_list
    import capo_redshift_serverless.types.track_name
    import capo_redshift_serverless.types.vpc_ids
    import capo_redshift_serverless.types.workgroup_name
    import capo_redshift_serverless.types.workgroup_status


class Workgroup(TypedDict, closed=True):
    workgroup_id: NotRequired["str"]
    """<p>The unique identifier of the workgroup.</p>"""
    workgroup_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) that links to the workgroup.</p>"""
    workgroup_name: NotRequired[
        "capo_redshift_serverless.types.workgroup_name.WorkgroupName"
    ]
    """<p>The name of the workgroup.</p>"""
    namespace_name: NotRequired["str"]
    """<p>The namespace the workgroup is associated with.</p>"""
    base_capacity: NotRequired["int"]
    """<p>The base data warehouse capacity of the workgroup in Redshift Processing Units (RPUs).</p>"""
    enhanced_vpc_routing: NotRequired["bool"]
    """<p>The value that specifies whether to enable enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.</p>"""
    config_parameters: NotRequired[
        "capo_redshift_serverless.types.config_parameter_list.ConfigParameterList"
    ]
    """<p>An array of parameters to set for advanced control over a database. The options are <code>auto_mv</code>, <code>datestyle</code>, <code>enable_case_sensitive_identifier</code>, <code>enable_user_activity_logging</code>, <code>query_group</code>, <code>search_path</code>, <code>require_ssl</code>, <code>use_fips_ssl</code>, and either <code>wlm_json_configuration</code> or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as <code>max_scan_row_count</code>, <code>max_query_execution_time</code>) or use <code>wlm_json_configuration</code> to define query queues with rules, but not both. If you're using <code>wlm_json_configuration</code>, the maximum size of <code>parameterValue</code> is 8000 characters. For more information about query monitoring rules and available metrics, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless"> Query monitoring metrics for Amazon Redshift Serverless</a>.</p>"""
    security_group_ids: NotRequired[
        "capo_redshift_serverless.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>An array of security group IDs to associate with the workgroup.</p>"""
    subnet_ids: NotRequired[
        "capo_redshift_serverless.types.subnet_id_list.SubnetIdList"
    ]
    """<p>An array of subnet IDs the workgroup is associated with.</p>"""
    status: NotRequired[
        "capo_redshift_serverless.types.workgroup_status.WorkgroupStatus"
    ]
    """<p>The status of the workgroup.</p>"""
    endpoint: NotRequired["capo_redshift_serverless.types.endpoint.Endpoint"]
    """<p>The endpoint that is created from the workgroup.</p>"""
    publicly_accessible: NotRequired["bool"]
    """<p>A value that specifies whether the workgroup can be accessible from a public network.</p>"""
    creation_date: NotRequired["datetime.datetime"]
    """<p>The creation date of the workgroup.</p>"""
    port: NotRequired["int"]
    """<p>The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.</p>"""
    custom_domain_name: NotRequired[
        "capo_redshift_serverless.types.custom_domain_name.CustomDomainName"
    ]
    """<p>The custom domain name associated with the workgroup.</p>"""
    custom_domain_certificate_arn: NotRequired[
        "capo_redshift_serverless.types.custom_domain_certificate_arn_string.CustomDomainCertificateArnString"
    ]
    """<p>The custom domain name’s certificate Amazon resource name (ARN).</p>"""
    custom_domain_certificate_expiry_time: NotRequired["datetime.datetime"]
    """<p>The expiration time for the certificate.</p>"""
    workgroup_version: NotRequired["str"]
    """<p>The Amazon Redshift Serverless version of your workgroup. For more information about Amazon Redshift Serverless versions, see<a href="https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html">Cluster versions for Amazon Redshift</a>.</p>"""
    patch_version: NotRequired["str"]
    """<p>The patch version of your Amazon Redshift Serverless workgroup. For more information about patch versions, see <a href="https://docs.aws.amazon.com/redshift/latest/mgmt/cluster-versions.html">Cluster versions for Amazon Redshift</a>.</p>"""
    max_capacity: NotRequired["int"]
    """<p>The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.</p>"""
    cross_account_vpcs: NotRequired["capo_redshift_serverless.types.vpc_ids.VpcIds"]
    """<p>A list of VPCs. Each entry is the unique identifier of a virtual private cloud with access to Amazon Redshift Serverless. If all of the VPCs for the grantee are allowed, it shows an asterisk.</p>"""
    ip_address_type: NotRequired[
        "capo_redshift_serverless.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type that the workgroup supports. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>"""
    price_performance_target: NotRequired[
        "capo_redshift_serverless.types.performance_target.PerformanceTarget"
    ]
    """<p>An object that represents the price performance target settings for the workgroup.</p>"""
    track_name: NotRequired["capo_redshift_serverless.types.track_name.TrackName"]
    """<p>The name of the track for the workgroup.</p>"""
    pending_track_name: NotRequired[
        "capo_redshift_serverless.types.track_name.TrackName"
    ]
    """<p>The name for the track that you want to assign to the workgroup. When the track changes, the workgroup is switched to the latest workgroup release available for the track. At this point, the track name is applied.</p>"""
    extra_compute_for_automatic_optimization: NotRequired["bool"]
    """<p>A boolean value that, if <code>true</code>, indicates that the workgroup allocates additional compute resources to run automatic optimization operations.</p> <p>Default: false</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Workgroup) -> dict:
    out: dict = {}
    if "workgroup_id" in value:
        out["workgroupId"] = value["workgroup_id"]
    if "workgroup_arn" in value:
        out["workgroupArn"] = value["workgroup_arn"]
    if "workgroup_name" in value:
        out["workgroupName"] = value["workgroup_name"]
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "base_capacity" in value:
        out["baseCapacity"] = value["base_capacity"]
    if "enhanced_vpc_routing" in value:
        out["enhancedVpcRouting"] = value["enhanced_vpc_routing"]
    if "config_parameters" in value:
        import capo_redshift_serverless.types.config_parameter_list

        out["configParameters"] = (
            capo_redshift_serverless.types.config_parameter_list.serialize_aws_json_1_1(
                value["config_parameters"]
            )
        )
    if "security_group_ids" in value:
        import capo_redshift_serverless.types.security_group_id_list

        out["securityGroupIds"] = (
            capo_redshift_serverless.types.security_group_id_list.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "subnet_ids" in value:
        import capo_redshift_serverless.types.subnet_id_list

        out["subnetIds"] = (
            capo_redshift_serverless.types.subnet_id_list.serialize_aws_json_1_1(
                value["subnet_ids"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "endpoint" in value:
        import capo_redshift_serverless.types.endpoint

        out["endpoint"] = (
            capo_redshift_serverless.types.endpoint.serialize_aws_json_1_1(
                value["endpoint"]
            )
        )
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "creation_date" in value:
        import capo_redshift_serverless._protocol.serialize

        out["creationDate"] = (
            capo_redshift_serverless._protocol.serialize.fmt_date_time(
                value["creation_date"]
            )
        )
    if "port" in value:
        out["port"] = value["port"]
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "custom_domain_certificate_arn" in value:
        out["customDomainCertificateArn"] = value["custom_domain_certificate_arn"]
    if "custom_domain_certificate_expiry_time" in value:
        import capo_redshift_serverless._protocol.serialize

        out["customDomainCertificateExpiryTime"] = (
            capo_redshift_serverless._protocol.serialize.fmt_date_time(
                value["custom_domain_certificate_expiry_time"]
            )
        )
    if "workgroup_version" in value:
        out["workgroupVersion"] = value["workgroup_version"]
    if "patch_version" in value:
        out["patchVersion"] = value["patch_version"]
    if "max_capacity" in value:
        out["maxCapacity"] = value["max_capacity"]
    if "cross_account_vpcs" in value:
        import capo_redshift_serverless.types.vpc_ids

        out["crossAccountVpcs"] = (
            capo_redshift_serverless.types.vpc_ids.serialize_aws_json_1_1(
                value["cross_account_vpcs"]
            )
        )
    if "ip_address_type" in value:
        out["ipAddressType"] = value["ip_address_type"]
    if "price_performance_target" in value:
        import capo_redshift_serverless.types.performance_target

        out["pricePerformanceTarget"] = (
            capo_redshift_serverless.types.performance_target.serialize_aws_json_1_1(
                value["price_performance_target"]
            )
        )
    if "track_name" in value:
        out["trackName"] = value["track_name"]
    if "pending_track_name" in value:
        out["pendingTrackName"] = value["pending_track_name"]
    if "extra_compute_for_automatic_optimization" in value:
        out["extraComputeForAutomaticOptimization"] = value[
            "extra_compute_for_automatic_optimization"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> Workgroup:
    out: Workgroup = {}  # type: ignore[typeddict-item]
    if data.get("workgroupId") is not None:
        out["workgroup_id"] = data["workgroupId"]
    if data.get("workgroupArn") is not None:
        out["workgroup_arn"] = data["workgroupArn"]
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    if data.get("namespaceName") is not None:
        out["namespace_name"] = data["namespaceName"]
    if data.get("baseCapacity") is not None:
        out["base_capacity"] = data["baseCapacity"]
    if data.get("enhancedVpcRouting") is not None:
        out["enhanced_vpc_routing"] = data["enhancedVpcRouting"]
    if data.get("configParameters") is not None:
        import capo_redshift_serverless.types.config_parameter_list

        out["config_parameters"] = (
            capo_redshift_serverless.types.config_parameter_list.deserialize_aws_json_1_1(
                data["configParameters"]
            )
        )
    if data.get("securityGroupIds") is not None:
        import capo_redshift_serverless.types.security_group_id_list

        out["security_group_ids"] = (
            capo_redshift_serverless.types.security_group_id_list.deserialize_aws_json_1_1(
                data["securityGroupIds"]
            )
        )
    if data.get("subnetIds") is not None:
        import capo_redshift_serverless.types.subnet_id_list

        out["subnet_ids"] = (
            capo_redshift_serverless.types.subnet_id_list.deserialize_aws_json_1_1(
                data["subnetIds"]
            )
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    if data.get("endpoint") is not None:
        import capo_redshift_serverless.types.endpoint

        out["endpoint"] = (
            capo_redshift_serverless.types.endpoint.deserialize_aws_json_1_1(
                data["endpoint"]
            )
        )
    if data.get("publiclyAccessible") is not None:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if data.get("creationDate") is not None:
        import datetime

        out["creation_date"] = datetime.datetime.fromisoformat(
            data["creationDate"].replace("Z", "+00:00")
        )
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("customDomainName") is not None:
        out["custom_domain_name"] = data["customDomainName"]
    if data.get("customDomainCertificateArn") is not None:
        out["custom_domain_certificate_arn"] = data["customDomainCertificateArn"]
    if data.get("customDomainCertificateExpiryTime") is not None:
        import datetime

        out["custom_domain_certificate_expiry_time"] = datetime.datetime.fromisoformat(
            data["customDomainCertificateExpiryTime"].replace("Z", "+00:00")
        )
    if data.get("workgroupVersion") is not None:
        out["workgroup_version"] = data["workgroupVersion"]
    if data.get("patchVersion") is not None:
        out["patch_version"] = data["patchVersion"]
    if data.get("maxCapacity") is not None:
        out["max_capacity"] = data["maxCapacity"]
    if data.get("crossAccountVpcs") is not None:
        import capo_redshift_serverless.types.vpc_ids

        out["cross_account_vpcs"] = (
            capo_redshift_serverless.types.vpc_ids.deserialize_aws_json_1_1(
                data["crossAccountVpcs"]
            )
        )
    if data.get("ipAddressType") is not None:
        out["ip_address_type"] = data["ipAddressType"]
    if data.get("pricePerformanceTarget") is not None:
        import capo_redshift_serverless.types.performance_target

        out["price_performance_target"] = (
            capo_redshift_serverless.types.performance_target.deserialize_aws_json_1_1(
                data["pricePerformanceTarget"]
            )
        )
    if data.get("trackName") is not None:
        out["track_name"] = data["trackName"]
    if data.get("pendingTrackName") is not None:
        out["pending_track_name"] = data["pendingTrackName"]
    if data.get("extraComputeForAutomaticOptimization") is not None:
        out["extra_compute_for_automatic_optimization"] = data[
            "extraComputeForAutomaticOptimization"
        ]
    return out
