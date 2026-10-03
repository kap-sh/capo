"""Generated from Smithy shape ``com.amazonaws.ec2#CreateApplicationStatusCheckRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.aggregation_status_enum
    import capo_ec2.types.boolean
    import capo_ec2.types.health_check_path_request_list
    import capo_ec2.types.initialization_grace_period_seconds
    import capo_ec2.types.integer
    import capo_ec2.types.ip_scope_enum
    import capo_ec2.types.ip_version_enum
    import capo_ec2.types.network_protocol_enum
    import capo_ec2.types.port_number
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list


class CreateApplicationStatusCheckRequest(TypedDict, closed=True):
    health_check_paths: NotRequired[
        "capo_ec2.types.health_check_path_request_list.HealthCheckPathRequestList"
    ]
    """<p>The health check paths to use for the application status check. Health check paths define the network path from a source subnet to one or more destination subnets for cross-Availability Zone or Availability Zone to Local Zone health checking. If omitted, health checks are performed in the same subnet as the instance.</p>"""
    aggregation: NotRequired[
        "capo_ec2.types.aggregation_status_enum.AggregationStatusEnum"
    ]
    """<p>The aggregation setting for the application status check. When set to <code>included</code>, the result of this check contributes to the instance-level application status reported by <code>DescribeApplicationStatus</code>. When set to <code>excluded</code>, the check runs independently and does not affect the instance-level status. Valid values: <code>included</code> | <code>excluded</code>.</p>"""
    protocol: NotRequired["capo_ec2.types.network_protocol_enum.NetworkProtocolEnum"]
    """<p>The protocol to use for the health check. Valid values: <code>http</code> | <code>https</code>.</p>"""
    port: NotRequired["capo_ec2.types.port_number.PortNumber"]
    """<p>The port to use for the health check. Valid values: 1 to 65535.</p>"""
    path: NotRequired["capo_ec2.types.string.String"]
    """<p>The URL path to use for the health check HTTP request (for example, <code>/health</code> or <code>/status</code>).</p>"""
    device_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the network device to use for the health check. The value must be greater than or equal to 0.</p>"""
    ip_version: NotRequired["capo_ec2.types.ip_version_enum.IpVersionEnum"]
    """<p>The IP version to use for the health check. Valid values: <code>ipv4</code> and <code>ipv6</code>.</p>"""
    ip_scope: NotRequired["capo_ec2.types.ip_scope_enum.IpScopeEnum"]
    """<p>The IP scope to use for the health check. Valid value: <code>private</code>.</p>"""
    interval: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The interval, in seconds, between health checks. Valid value: 60.</p>"""
    timeout: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The amount of time, in seconds, to wait for a health check response before considering it failed. Valid values: 1 to 30. The value must be less than <code>Interval</code>.</p>"""
    failure_threshold: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of consecutive failed health checks before the application status is considered impaired. The value must be greater than 0.</p>"""
    success_threshold: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of consecutive successful health checks before the application status is considered healthy. The value must be greater than 0.</p>"""
    status_code_matcher: NotRequired["capo_ec2.types.string.String"]
    """<p>The HTTP status codes that indicate a successful health check response. Specify a comma-separated list of individual status codes or ranges, for example, <code>200,202,300-399</code>. For a range, the first value must be less than the second value. Maximum length: 64 characters. Default: <code>200</code>.</p>"""
    initialization_grace_period_seconds: NotRequired[
        "capo_ec2.types.initialization_grace_period_seconds.InitializationGracePeriodSeconds"
    ]
    """<p>The number of seconds to wait before starting health checks after an instance is launched. Valid values: 1 to 600.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the application status check.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive identifier that you provide to ensure that the operation completes no more than one time. If you retry a request with the same token, the service ignores the request but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateApplicationStatusCheckRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "health_check_paths" in value:
        import capo_ec2.types.health_check_path_request_list

        capo_ec2.types.health_check_path_request_list.serialize_ec2_query(
            value["health_check_paths"], pairs, f"{key_prefix}HealthCheckPath"
        )
    if "aggregation" in value:
        import capo_ec2.types.aggregation_status_enum

        capo_ec2.types.aggregation_status_enum.serialize_ec2_query(
            value["aggregation"], pairs, f"{key_prefix}Aggregation"
        )
    if "protocol" in value:
        import capo_ec2.types.network_protocol_enum

        capo_ec2.types.network_protocol_enum.serialize_ec2_query(
            value["protocol"], pairs, f"{key_prefix}Protocol"
        )
    if "port" in value:
        pairs.append((f"{key_prefix}Port", str(value["port"])))
    if "path" in value:
        pairs.append((f"{key_prefix}Path", str(value["path"])))
    if "device_index" in value:
        pairs.append((f"{key_prefix}DeviceIndex", str(value["device_index"])))
    if "ip_version" in value:
        import capo_ec2.types.ip_version_enum

        capo_ec2.types.ip_version_enum.serialize_ec2_query(
            value["ip_version"], pairs, f"{key_prefix}IpVersion"
        )
    if "ip_scope" in value:
        import capo_ec2.types.ip_scope_enum

        capo_ec2.types.ip_scope_enum.serialize_ec2_query(
            value["ip_scope"], pairs, f"{key_prefix}IpScope"
        )
    if "interval" in value:
        pairs.append((f"{key_prefix}Interval", str(value["interval"])))
    if "timeout" in value:
        pairs.append((f"{key_prefix}Timeout", str(value["timeout"])))
    if "failure_threshold" in value:
        pairs.append((f"{key_prefix}FailureThreshold", str(value["failure_threshold"])))
    if "success_threshold" in value:
        pairs.append((f"{key_prefix}SuccessThreshold", str(value["success_threshold"])))
    if "status_code_matcher" in value:
        pairs.append(
            (f"{key_prefix}StatusCodeMatcher", str(value["status_code_matcher"]))
        )
    if "initialization_grace_period_seconds" in value:
        pairs.append(
            (
                f"{key_prefix}InitializationGracePeriodSeconds",
                str(value["initialization_grace_period_seconds"]),
            )
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateApplicationStatusCheckRequest:
    out: CreateApplicationStatusCheckRequest = {}  # type: ignore[typeddict-item]
    child_health_check_paths = el.find("HealthCheckPath")
    if child_health_check_paths is not None:
        import capo_ec2.types.health_check_path_request_list

        out["health_check_paths"] = (
            capo_ec2.types.health_check_path_request_list.deserialize_ec2_query(
                child_health_check_paths
            )
        )
    child_aggregation = el.find("Aggregation")
    if child_aggregation is not None:
        import capo_ec2.types.aggregation_status_enum

        out["aggregation"] = (
            capo_ec2.types.aggregation_status_enum.deserialize_ec2_query(
                child_aggregation
            )
        )
    child_protocol = el.find("Protocol")
    if child_protocol is not None:
        import capo_ec2.types.network_protocol_enum

        out["protocol"] = capo_ec2.types.network_protocol_enum.deserialize_ec2_query(
            child_protocol
        )
    child_port = el.find("Port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_path = el.find("Path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_device_index = el.find("DeviceIndex")
    if child_device_index is not None:
        out["device_index"] = int(child_device_index.text or "")
    child_ip_version = el.find("IpVersion")
    if child_ip_version is not None:
        import capo_ec2.types.ip_version_enum

        out["ip_version"] = capo_ec2.types.ip_version_enum.deserialize_ec2_query(
            child_ip_version
        )
    child_ip_scope = el.find("IpScope")
    if child_ip_scope is not None:
        import capo_ec2.types.ip_scope_enum

        out["ip_scope"] = capo_ec2.types.ip_scope_enum.deserialize_ec2_query(
            child_ip_scope
        )
    child_interval = el.find("Interval")
    if child_interval is not None:
        out["interval"] = int(child_interval.text or "")
    child_timeout = el.find("Timeout")
    if child_timeout is not None:
        out["timeout"] = int(child_timeout.text or "")
    child_failure_threshold = el.find("FailureThreshold")
    if child_failure_threshold is not None:
        out["failure_threshold"] = int(child_failure_threshold.text or "")
    child_success_threshold = el.find("SuccessThreshold")
    if child_success_threshold is not None:
        out["success_threshold"] = int(child_success_threshold.text or "")
    child_status_code_matcher = el.find("StatusCodeMatcher")
    if child_status_code_matcher is not None:
        out["status_code_matcher"] = str(child_status_code_matcher.text or "")
    child_initialization_grace_period_seconds = el.find(
        "InitializationGracePeriodSeconds"
    )
    if child_initialization_grace_period_seconds is not None:
        out["initialization_grace_period_seconds"] = int(
            child_initialization_grace_period_seconds.text or ""
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
