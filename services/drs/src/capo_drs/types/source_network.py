"""Generated from Smithy shape ``com.amazonaws.drs#SourceNetwork``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.account_id
    import capo_drs.types.arn
    import capo_drs.types.aws_region
    import capo_drs.types.cfn_stack_name
    import capo_drs.types.recovery_life_cycle
    import capo_drs.types.replication_status
    import capo_drs.types.sensitive_bounded_string
    import capo_drs.types.source_network_id
    import capo_drs.types.tags_map
    import capo_drs.types.vpc_id


class SourceNetwork(TypedDict, closed=True):
    source_network_id: NotRequired["capo_drs.types.source_network_id.SourceNetworkID"]
    """<p>Source Network ID.</p>"""
    source_vpc_id: NotRequired["capo_drs.types.vpc_id.VpcID"]
    """<p>VPC ID protected by the Source Network.</p>"""
    arn: NotRequired["capo_drs.types.arn.ARN"]
    """<p>The ARN of the Source Network.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>A list of tags associated with the Source Network.</p>"""
    replication_status: NotRequired[
        "capo_drs.types.replication_status.ReplicationStatus"
    ]
    """<p>Status of Source Network Replication. Possible values: (a) STOPPED - Source Network is not replicating. (b) IN_PROGRESS - Source Network is being replicated. (c) PROTECTED - Source Network was replicated successfully and is being synchronized for changes. (d) ERROR - Source Network replication has failed</p>"""
    replication_status_details: NotRequired[
        "capo_drs.types.sensitive_bounded_string.SensitiveBoundedString"
    ]
    """<p>Error details in case Source Network replication status is ERROR.</p>"""
    cfn_stack_name: NotRequired["capo_drs.types.cfn_stack_name.CfnStackName"]
    """<p>CloudFormation stack name that was deployed for recovering the Source Network.</p>"""
    source_region: NotRequired["capo_drs.types.aws_region.AwsRegion"]
    """<p>Region containing the VPC protected by the Source Network.</p>"""
    source_account_id: NotRequired["capo_drs.types.account_id.AccountID"]
    """<p>Account ID containing the VPC protected by the Source Network.</p>"""
    last_recovery: NotRequired["capo_drs.types.recovery_life_cycle.RecoveryLifeCycle"]
    """<p>An object containing information regarding the last recovery of the Source Network.</p>"""
    launched_vpc_id: NotRequired["capo_drs.types.vpc_id.VpcID"]
    """<p>ID of the recovered VPC following Source Network recovery.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceNetwork) -> dict:
    out: dict = {}
    if "source_network_id" in value:
        out["sourceNetworkID"] = value["source_network_id"]
    if "source_vpc_id" in value:
        out["sourceVpcID"] = value["source_vpc_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    if "replication_status" in value:
        out["replicationStatus"] = value["replication_status"]
    if "replication_status_details" in value:
        out["replicationStatusDetails"] = value["replication_status_details"]
    if "cfn_stack_name" in value:
        out["cfnStackName"] = value["cfn_stack_name"]
    if "source_region" in value:
        out["sourceRegion"] = value["source_region"]
    if "source_account_id" in value:
        out["sourceAccountID"] = value["source_account_id"]
    if "last_recovery" in value:
        import capo_drs.types.recovery_life_cycle

        out["lastRecovery"] = capo_drs.types.recovery_life_cycle.serialize_json(
            value["last_recovery"]
        )
    if "launched_vpc_id" in value:
        out["launchedVpcID"] = value["launched_vpc_id"]
    return out


def deserialize_json(data: dict) -> SourceNetwork:
    out: SourceNetwork = {}  # type: ignore[typeddict-item]
    if data.get("sourceNetworkID") is not None:
        out["source_network_id"] = data["sourceNetworkID"]
    if data.get("sourceVpcID") is not None:
        out["source_vpc_id"] = data["sourceVpcID"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    if data.get("replicationStatus") is not None:
        out["replication_status"] = data["replicationStatus"]
    if data.get("replicationStatusDetails") is not None:
        out["replication_status_details"] = data["replicationStatusDetails"]
    if data.get("cfnStackName") is not None:
        out["cfn_stack_name"] = data["cfnStackName"]
    if data.get("sourceRegion") is not None:
        out["source_region"] = data["sourceRegion"]
    if data.get("sourceAccountID") is not None:
        out["source_account_id"] = data["sourceAccountID"]
    if data.get("lastRecovery") is not None:
        import capo_drs.types.recovery_life_cycle

        out["last_recovery"] = capo_drs.types.recovery_life_cycle.deserialize_json(
            data["lastRecovery"]
        )
    if data.get("launchedVpcID") is not None:
        out["launched_vpc_id"] = data["launchedVpcID"]
    return out


def redact_sensitive(value: SourceNetwork) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    if "replication_status_details" in value:
        out["replication_status_details"] = "*** Sensitive Data Redacted ***"
    if "cfn_stack_name" in value:
        out["cfn_stack_name"] = "*** Sensitive Data Redacted ***"
    return out
