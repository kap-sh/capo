"""Generated from Smithy shape ``com.amazonaws.m2#GetApplicationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.application_lifecycle
    import capo_m2.types.application_version_summary
    import capo_m2.types.arn
    import capo_m2.types.arn_list
    import capo_m2.types.deployed_version_summary
    import capo_m2.types.engine_type
    import capo_m2.types.entity_description
    import capo_m2.types.entity_name
    import capo_m2.types.identifier
    import capo_m2.types.log_group_summaries
    import capo_m2.types.port_list
    import capo_m2.types.string100
    import capo_m2.types.tag_map
    import capo_m2.types.timestamp


class GetApplicationResponse(TypedDict, closed=True):
    name: "capo_m2.types.entity_name.EntityName"
    """<p>The unique identifier of the application.</p>"""
    description: NotRequired["capo_m2.types.entity_description.EntityDescription"]
    """<p>The description of the application.</p>"""
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The identifier of the application.</p>"""
    application_arn: "capo_m2.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""
    status: "capo_m2.types.application_lifecycle.ApplicationLifecycle"
    """<p>The status of the application.</p>"""
    latest_version: (
        "capo_m2.types.application_version_summary.ApplicationVersionSummary"
    )
    """<p>The latest version of the application.</p>"""
    deployed_version: NotRequired[
        "capo_m2.types.deployed_version_summary.DeployedVersionSummary"
    ]
    """<p>The version of the application that is deployed.</p>"""
    engine_type: "capo_m2.types.engine_type.EngineType"
    """<p>The type of the target platform for the application.</p>"""
    log_groups: NotRequired["capo_m2.types.log_group_summaries.LogGroupSummaries"]
    """<p>The list of log summaries. Each log summary includes the log type as well as the log group identifier. These are CloudWatch logs. Amazon Web Services Mainframe Modernization pushes the application log to CloudWatch under the customer's account.</p>"""
    creation_time: "capo_m2.types.timestamp.Timestamp"
    """<p>The timestamp when this application was created.</p>"""
    last_start_time: NotRequired["capo_m2.types.timestamp.Timestamp"]
    """<p>The timestamp when you last started the application. Null until the application runs for the first time.</p>"""
    tags: NotRequired["capo_m2.types.tag_map.TagMap"]
    """<p>A list of tags associated with the application.</p>"""
    environment_id: NotRequired["capo_m2.types.identifier.Identifier"]
    """<p>The identifier of the runtime environment where you want to deploy the application.</p>"""
    target_group_arns: NotRequired["capo_m2.types.arn_list.ArnList"]
    """<p>Returns the Amazon Resource Names (ARNs) of the target groups that are attached to the network load balancer.</p>"""
    listener_arns: NotRequired["capo_m2.types.arn_list.ArnList"]
    """<p>The Amazon Resource Name (ARN) for the network load balancer listener created in your Amazon Web Services account. Amazon Web Services Mainframe Modernization creates this listener for you the first time you deploy an application.</p>"""
    listener_ports: NotRequired["capo_m2.types.port_list.PortList"]
    """<p>The port associated with the network load balancer listener created in your Amazon Web Services account.</p>"""
    load_balancer_dns_name: NotRequired["capo_m2.types.string100.String100"]
    """<p>The public DNS name of the load balancer created in your Amazon Web Services account.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the reported status.</p>"""
    kms_key_id: NotRequired["str"]
    """<p>The identifier of a customer managed key.</p>"""
    role_arn: NotRequired["capo_m2.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the role associated with the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["applicationId"] = value["application_id"]
    out["applicationArn"] = value["application_arn"]
    out["status"] = value["status"]
    import capo_m2.types.application_version_summary

    out["latestVersion"] = capo_m2.types.application_version_summary.serialize_json(
        value["latest_version"]
    )
    if "deployed_version" in value:
        import capo_m2.types.deployed_version_summary

        out["deployedVersion"] = capo_m2.types.deployed_version_summary.serialize_json(
            value["deployed_version"]
        )
    out["engineType"] = value["engine_type"]
    if "log_groups" in value:
        import capo_m2.types.log_group_summaries

        out["logGroups"] = capo_m2.types.log_group_summaries.serialize_json(
            value["log_groups"]
        )
    import capo_m2.types.timestamp

    out["creationTime"] = capo_m2.types.timestamp.serialize_json(value["creation_time"])
    if "last_start_time" in value:
        import capo_m2.types.timestamp

        out["lastStartTime"] = capo_m2.types.timestamp.serialize_json(
            value["last_start_time"]
        )
    if "tags" in value:
        import capo_m2.types.tag_map

        out["tags"] = capo_m2.types.tag_map.serialize_json(value["tags"])
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "target_group_arns" in value:
        import capo_m2.types.arn_list

        out["targetGroupArns"] = capo_m2.types.arn_list.serialize_json(
            value["target_group_arns"]
        )
    if "listener_arns" in value:
        import capo_m2.types.arn_list

        out["listenerArns"] = capo_m2.types.arn_list.serialize_json(
            value["listener_arns"]
        )
    if "listener_ports" in value:
        import capo_m2.types.port_list

        out["listenerPorts"] = capo_m2.types.port_list.serialize_json(
            value["listener_ports"]
        )
    if "load_balancer_dns_name" in value:
        out["loadBalancerDnsName"] = value["load_balancer_dns_name"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> GetApplicationResponse:
    out: GetApplicationResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("applicationArn") is not None:
        out["application_arn"] = data["applicationArn"]
    else:
        out["application_arn"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("latestVersion") is not None:
        import capo_m2.types.application_version_summary

        out["latest_version"] = (
            capo_m2.types.application_version_summary.deserialize_json(
                data["latestVersion"]
            )
        )
    else:
        raise DeserializationError("GetApplicationResponse.latest_version required")
    if data.get("deployedVersion") is not None:
        import capo_m2.types.deployed_version_summary

        out["deployed_version"] = (
            capo_m2.types.deployed_version_summary.deserialize_json(
                data["deployedVersion"]
            )
        )
    if data.get("engineType") is not None:
        out["engine_type"] = data["engineType"]
    else:
        out["engine_type"] = ""
    if data.get("logGroups") is not None:
        import capo_m2.types.log_group_summaries

        out["log_groups"] = capo_m2.types.log_group_summaries.deserialize_json(
            data["logGroups"]
        )
    if data.get("creationTime") is not None:
        import capo_m2.types.timestamp

        out["creation_time"] = capo_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastStartTime") is not None:
        import capo_m2.types.timestamp

        out["last_start_time"] = capo_m2.types.timestamp.deserialize_json(
            data["lastStartTime"]
        )
    if data.get("tags") is not None:
        import capo_m2.types.tag_map

        out["tags"] = capo_m2.types.tag_map.deserialize_json(data["tags"])
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    if data.get("targetGroupArns") is not None:
        import capo_m2.types.arn_list

        out["target_group_arns"] = capo_m2.types.arn_list.deserialize_json(
            data["targetGroupArns"]
        )
    if data.get("listenerArns") is not None:
        import capo_m2.types.arn_list

        out["listener_arns"] = capo_m2.types.arn_list.deserialize_json(
            data["listenerArns"]
        )
    if data.get("listenerPorts") is not None:
        import capo_m2.types.port_list

        out["listener_ports"] = capo_m2.types.port_list.deserialize_json(
            data["listenerPorts"]
        )
    if data.get("loadBalancerDnsName") is not None:
        out["load_balancer_dns_name"] = data["loadBalancerDnsName"]
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    return out
