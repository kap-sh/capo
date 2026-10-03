"""Generated from Smithy shape ``com.amazonaws.ec2#ApplicationStatusCheckResponseObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.aggregation_status_enum
    import capo_ec2.types.application_status_check_id
    import capo_ec2.types.custom_key_value_pair_response_set
    import capo_ec2.types.health_check_path_response_list
    import capo_ec2.types.initialization_grace_period_seconds
    import capo_ec2.types.integer
    import capo_ec2.types.ip_scope_enum
    import capo_ec2.types.ip_version_enum
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.network_protocol_enum
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class ApplicationStatusCheckResponseObject(TypedDict, closed=True):
    application_status_check_id: NotRequired[
        "capo_ec2.types.application_status_check_id.ApplicationStatusCheckId"
    ]
    """<p>The ID of the application status check.</p>"""
    aggregation: NotRequired[
        "capo_ec2.types.aggregation_status_enum.AggregationStatusEnum"
    ]
    """<p>The aggregation setting for the application status check. When set to <code>included</code>, the result of this check contributes to the instance-level application status. When set to <code>excluded</code>, the check runs independently and does not affect the instance-level status.</p>"""
    health_check_paths: NotRequired[
        "capo_ec2.types.health_check_path_response_list.HealthCheckPathResponseList"
    ]
    """<p>The health check paths for the application status check.</p>"""
    protocol: NotRequired["capo_ec2.types.network_protocol_enum.NetworkProtocolEnum"]
    """<p>The protocol used for the health check.</p>"""
    port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The port used for the health check.</p>"""
    path: NotRequired["capo_ec2.types.string.String"]
    """<p>The URL path used for the health check HTTP request.</p>"""
    device_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the network device used for the health check. The value is greater than or equal to 0.</p>"""
    ip_version: NotRequired["capo_ec2.types.ip_version_enum.IpVersionEnum"]
    """<p>The IP version used for the health check.</p>"""
    ip_scope: NotRequired["capo_ec2.types.ip_scope_enum.IpScopeEnum"]
    """<p>The IP scope used for the health check.</p>"""
    interval: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The interval, in seconds, between health checks. Valid value: 60.</p>"""
    timeout: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The amount of time, in seconds, to wait for a health check response. Valid values: 1 to 30.</p>"""
    failure_threshold: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of consecutive failed health checks before the application status is considered impaired. The value must be greater than 0.</p>"""
    success_threshold: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of consecutive successful health checks before the application status is considered healthy. The value must be greater than 0.</p>"""
    status_code_matcher: NotRequired["capo_ec2.types.string.String"]
    """<p>The comma-separated list of individual HTTP status codes or ranges that indicate a successful health check response.</p>"""
    initialization_grace_period_seconds: NotRequired[
        "capo_ec2.types.initialization_grace_period_seconds.InitializationGracePeriodSeconds"
    ]
    """<p>The number of seconds to wait before starting health checks after an instance is launched. Valid values: 1 to 600.</p>"""
    last_updated_at: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the application status check was last updated.</p>"""
    target_tag_associations: NotRequired[
        "capo_ec2.types.custom_key_value_pair_response_set.CustomKeyValuePairResponseSet"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html">tags</a> associated with the application status check. Instances with these tags are automatically monitored by this check.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags assigned to the application status check.</p>"""
    creation_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the application status check was created.</p>"""
    modify_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>The date and time when the application status check was last modified.</p>"""
    deletion_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the application status check was deleted.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ApplicationStatusCheckResponseObject,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_status_check_id" in value:
        pairs.append(
            (
                f"{key_prefix}ApplicationStatusCheckId",
                str(value["application_status_check_id"]),
            )
        )
    if "aggregation" in value:
        import capo_ec2.types.aggregation_status_enum

        capo_ec2.types.aggregation_status_enum.serialize_ec2_query(
            value["aggregation"], pairs, f"{key_prefix}Aggregation"
        )
    if "health_check_paths" in value:
        import capo_ec2.types.health_check_path_response_list

        capo_ec2.types.health_check_path_response_list.serialize_ec2_query(
            value["health_check_paths"], pairs, f"{key_prefix}HealthCheckPathSet"
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
    if "last_updated_at" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["last_updated_at"], pairs, f"{key_prefix}LastUpdatedAt"
        )
    if "target_tag_associations" in value:
        import capo_ec2.types.custom_key_value_pair_response_set

        capo_ec2.types.custom_key_value_pair_response_set.serialize_ec2_query(
            value["target_tag_associations"],
            pairs,
            f"{key_prefix}TargetTagAssociationSet",
        )
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "creation_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["creation_time"], pairs, f"{key_prefix}CreationTime"
        )
    if "modify_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["modify_time"], pairs, f"{key_prefix}ModifyTime"
        )
    if "deletion_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["deletion_time"], pairs, f"{key_prefix}DeletionTime"
        )


def deserialize_ec2_query(el: Element) -> ApplicationStatusCheckResponseObject:
    out: ApplicationStatusCheckResponseObject = {}  # type: ignore[typeddict-item]
    child_application_status_check_id = el.find("applicationStatusCheckId")
    if child_application_status_check_id is not None:
        out["application_status_check_id"] = str(
            child_application_status_check_id.text or ""
        )
    child_aggregation = el.find("aggregation")
    if child_aggregation is not None:
        import capo_ec2.types.aggregation_status_enum

        out["aggregation"] = (
            capo_ec2.types.aggregation_status_enum.deserialize_ec2_query(
                child_aggregation
            )
        )
    child_health_check_paths = el.find("healthCheckPathSet")
    if child_health_check_paths is not None:
        import capo_ec2.types.health_check_path_response_list

        out["health_check_paths"] = (
            capo_ec2.types.health_check_path_response_list.deserialize_ec2_query(
                child_health_check_paths
            )
        )
    child_protocol = el.find("protocol")
    if child_protocol is not None:
        import capo_ec2.types.network_protocol_enum

        out["protocol"] = capo_ec2.types.network_protocol_enum.deserialize_ec2_query(
            child_protocol
        )
    child_port = el.find("port")
    if child_port is not None:
        out["port"] = int(child_port.text or "")
    child_path = el.find("path")
    if child_path is not None:
        out["path"] = str(child_path.text or "")
    child_device_index = el.find("deviceIndex")
    if child_device_index is not None:
        out["device_index"] = int(child_device_index.text or "")
    child_ip_version = el.find("ipVersion")
    if child_ip_version is not None:
        import capo_ec2.types.ip_version_enum

        out["ip_version"] = capo_ec2.types.ip_version_enum.deserialize_ec2_query(
            child_ip_version
        )
    child_ip_scope = el.find("ipScope")
    if child_ip_scope is not None:
        import capo_ec2.types.ip_scope_enum

        out["ip_scope"] = capo_ec2.types.ip_scope_enum.deserialize_ec2_query(
            child_ip_scope
        )
    child_interval = el.find("interval")
    if child_interval is not None:
        out["interval"] = int(child_interval.text or "")
    child_timeout = el.find("timeout")
    if child_timeout is not None:
        out["timeout"] = int(child_timeout.text or "")
    child_failure_threshold = el.find("failureThreshold")
    if child_failure_threshold is not None:
        out["failure_threshold"] = int(child_failure_threshold.text or "")
    child_success_threshold = el.find("successThreshold")
    if child_success_threshold is not None:
        out["success_threshold"] = int(child_success_threshold.text or "")
    child_status_code_matcher = el.find("statusCodeMatcher")
    if child_status_code_matcher is not None:
        out["status_code_matcher"] = str(child_status_code_matcher.text or "")
    child_initialization_grace_period_seconds = el.find(
        "initializationGracePeriodSeconds"
    )
    if child_initialization_grace_period_seconds is not None:
        out["initialization_grace_period_seconds"] = int(
            child_initialization_grace_period_seconds.text or ""
        )
    child_last_updated_at = el.find("lastUpdatedAt")
    if child_last_updated_at is not None:
        import capo_ec2.types.millisecond_date_time

        out["last_updated_at"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_last_updated_at
            )
        )
    child_target_tag_associations = el.find("targetTagAssociationSet")
    if child_target_tag_associations is not None:
        import capo_ec2.types.custom_key_value_pair_response_set

        out["target_tag_associations"] = (
            capo_ec2.types.custom_key_value_pair_response_set.deserialize_ec2_query(
                child_target_tag_associations
            )
        )
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_creation_time = el.find("creationTime")
    if child_creation_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["creation_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_creation_time
            )
        )
    child_modify_time = el.find("modifyTime")
    if child_modify_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["modify_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_modify_time
        )
    child_deletion_time = el.find("deletionTime")
    if child_deletion_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["deletion_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_deletion_time
            )
        )
    return out
