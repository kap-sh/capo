"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateWorkgroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.config_parameter_list
    import capo_redshift_serverless.types.ip_address_type
    import capo_redshift_serverless.types.performance_target
    import capo_redshift_serverless.types.security_group_id_list
    import capo_redshift_serverless.types.subnet_id_list
    import capo_redshift_serverless.types.track_name
    import capo_redshift_serverless.types.workgroup_name


class UpdateWorkgroupRequest(TypedDict, closed=True):
    workgroup_name: "capo_redshift_serverless.types.workgroup_name.WorkgroupName"
    """<p>The name of the workgroup to update. You can't update the name of a workgroup once it is created.</p>"""
    base_capacity: NotRequired["int"]
    """<p>The new base data warehouse capacity in Redshift Processing Units (RPUs).</p>"""
    enhanced_vpc_routing: NotRequired["bool"]
    """<p>The value that specifies whether to turn on enhanced virtual private cloud (VPC) routing, which forces Amazon Redshift Serverless to route traffic through your VPC.</p>"""
    config_parameters: NotRequired[
        "capo_redshift_serverless.types.config_parameter_list.ConfigParameterList"
    ]
    """<p>An array of parameters to set for advanced control over a database. The options are <code>auto_mv</code>, <code>datestyle</code>, <code>enable_case_sensitive_identifier</code>, <code>enable_user_activity_logging</code>, <code>query_group</code>, <code>search_path</code>, <code>require_ssl</code>, <code>use_fips_ssl</code>, and either <code>wlm_json_configuration</code> or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as <code>max_scan_row_count</code>, <code>max_query_execution_time</code>) or use <code>wlm_json_configuration</code> to define query queues with rules, but not both. If you're using <code>wlm_json_configuration</code>, the maximum size of <code>parameterValue</code> is 8000 characters. For more information about query monitoring rules and available metrics, see <a href="https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless"> Query monitoring metrics for Amazon Redshift Serverless</a>.</p>"""
    publicly_accessible: NotRequired["bool"]
    """<p>A value that specifies whether the workgroup can be accessible from a public network.</p>"""
    subnet_ids: NotRequired[
        "capo_redshift_serverless.types.subnet_id_list.SubnetIdList"
    ]
    """<p>An array of VPC subnet IDs to associate with the workgroup.</p>"""
    security_group_ids: NotRequired[
        "capo_redshift_serverless.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>An array of security group IDs to associate with the workgroup.</p>"""
    port: NotRequired["int"]
    """<p>The custom port to use when connecting to a workgroup. Valid port ranges are 5431-5455 and 8191-8215. The default is 5439.</p>"""
    max_capacity: NotRequired["int"]
    """<p>The maximum data-warehouse capacity Amazon Redshift Serverless uses to serve queries. The max capacity is specified in RPUs.</p>"""
    ip_address_type: NotRequired[
        "capo_redshift_serverless.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type that the workgroup supports. Possible values are <code>ipv4</code> and <code>dualstack</code>.</p>"""
    price_performance_target: NotRequired[
        "capo_redshift_serverless.types.performance_target.PerformanceTarget"
    ]
    """<p>An object that represents the price performance target settings for the workgroup.</p>"""
    track_name: NotRequired["capo_redshift_serverless.types.track_name.TrackName"]
    """<p>An optional parameter for the name of the track for the workgroup. If you don't provide a track name, the workgroup is assigned to the <code>current</code> track.</p>"""
    extra_compute_for_automatic_optimization: NotRequired["bool"]
    """<p>If <code>true</code>, allocates additional compute resources for running automatic optimization operations.</p> <p>Default: false</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWorkgroupRequest) -> dict:
    out: dict = {}
    out["workgroupName"] = value["workgroup_name"]
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
    if "publicly_accessible" in value:
        out["publiclyAccessible"] = value["publicly_accessible"]
    if "subnet_ids" in value:
        import capo_redshift_serverless.types.subnet_id_list

        out["subnetIds"] = (
            capo_redshift_serverless.types.subnet_id_list.serialize_aws_json_1_1(
                value["subnet_ids"]
            )
        )
    if "security_group_ids" in value:
        import capo_redshift_serverless.types.security_group_id_list

        out["securityGroupIds"] = (
            capo_redshift_serverless.types.security_group_id_list.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "port" in value:
        out["port"] = value["port"]
    if "max_capacity" in value:
        out["maxCapacity"] = value["max_capacity"]
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
    if "extra_compute_for_automatic_optimization" in value:
        out["extraComputeForAutomaticOptimization"] = value[
            "extra_compute_for_automatic_optimization"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWorkgroupRequest:
    out: UpdateWorkgroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("workgroupName") is not None:
        out["workgroup_name"] = data["workgroupName"]
    else:
        raise DeserializationError("UpdateWorkgroupRequest.workgroup_name required")
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
    if data.get("publiclyAccessible") is not None:
        out["publicly_accessible"] = data["publiclyAccessible"]
    if data.get("subnetIds") is not None:
        import capo_redshift_serverless.types.subnet_id_list

        out["subnet_ids"] = (
            capo_redshift_serverless.types.subnet_id_list.deserialize_aws_json_1_1(
                data["subnetIds"]
            )
        )
    if data.get("securityGroupIds") is not None:
        import capo_redshift_serverless.types.security_group_id_list

        out["security_group_ids"] = (
            capo_redshift_serverless.types.security_group_id_list.deserialize_aws_json_1_1(
                data["securityGroupIds"]
            )
        )
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("maxCapacity") is not None:
        out["max_capacity"] = data["maxCapacity"]
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
    if data.get("extraComputeForAutomaticOptimization") is not None:
        out["extra_compute_for_automatic_optimization"] = data[
            "extraComputeForAutomaticOptimization"
        ]
    return out
