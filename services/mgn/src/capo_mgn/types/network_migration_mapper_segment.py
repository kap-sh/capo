"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationMapperSegment``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mgn.types.account_id
    import capo_mgn.types.checksum
    import capo_mgn.types.logical_id
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id
    import capo_mgn.types.network_migration_job_id
    import capo_mgn.types.network_migration_mapper_segment_type
    import capo_mgn.types.referenced_segments_list
    import capo_mgn.types.s3_configuration
    import capo_mgn.types.scope_tags_map
    import capo_mgn.types.segment_description
    import capo_mgn.types.segment_id
    import capo_mgn.types.segment_name


class NetworkMigrationMapperSegment(TypedDict, closed=True):
    job_id: NotRequired["capo_mgn.types.network_migration_job_id.NetworkMigrationJobID"]
    """<p>The unique identifier of the job that created this segment.</p>"""
    network_migration_execution_id: NotRequired[
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    ]
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: NotRequired[
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    ]
    """<p>The unique identifier of the network migration definition.</p>"""
    segment_id: NotRequired["capo_mgn.types.segment_id.SegmentID"]
    """<p>The unique identifier of the segment.</p>"""
    segment_type: NotRequired[
        "capo_mgn.types.network_migration_mapper_segment_type.NetworkMigrationMapperSegmentType"
    ]
    """<p>The category of the network migration segment. A segment groups the network constructs (such as VPCs, subnets, and security groups) that are migrated together. Valid values: <code>WORKLOAD</code>, <code>APPLIANCE</code>.</p>"""
    name: NotRequired["capo_mgn.types.segment_name.SegmentName"]
    """<p>The name of the segment.</p>"""
    description: NotRequired["capo_mgn.types.segment_description.SegmentDescription"]
    """<p>A description of the segment.</p>"""
    logical_id: NotRequired["capo_mgn.types.logical_id.LogicalID"]
    """<p>The logical identifier for the segment in the infrastructure code.</p>"""
    checksum: NotRequired["capo_mgn.types.checksum.Checksum"]
    """<p>The checksum of the segment data for integrity verification.</p>"""
    output_s3_configuration: NotRequired[
        "capo_mgn.types.s3_configuration.S3Configuration"
    ]
    """<p>The S3 location where segment artifacts are stored.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the segment was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the segment was last updated.</p>"""
    scope_tags: NotRequired["capo_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>Scope tags for the segment.</p>"""
    target_account: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>The target AWS account where this segment will be deployed.</p>"""
    referenced_segments: NotRequired[
        "capo_mgn.types.referenced_segments_list.referencedSegmentsList"
    ]
    """<p>A list of other segments that this segment depends on or references.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationMapperSegment) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    if "network_migration_execution_id" in value:
        out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    if "network_migration_definition_id" in value:
        out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "segment_id" in value:
        out["segmentID"] = value["segment_id"]
    if "segment_type" in value:
        out["segmentType"] = value["segment_type"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "logical_id" in value:
        out["logicalID"] = value["logical_id"]
    if "checksum" in value:
        import capo_mgn.types.checksum

        out["checksum"] = capo_mgn.types.checksum.serialize_json(value["checksum"])
    if "output_s3_configuration" in value:
        import capo_mgn.types.s3_configuration

        out["outputS3Configuration"] = capo_mgn.types.s3_configuration.serialize_json(
            value["output_s3_configuration"]
        )
    if "created_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["createdAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["updatedAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "scope_tags" in value:
        import capo_mgn.types.scope_tags_map

        out["scopeTags"] = capo_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    if "target_account" in value:
        out["targetAccount"] = value["target_account"]
    if "referenced_segments" in value:
        import capo_mgn.types.referenced_segments_list

        out["referencedSegments"] = (
            capo_mgn.types.referenced_segments_list.serialize_json(
                value["referenced_segments"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkMigrationMapperSegment:
    out: NetworkMigrationMapperSegment = {}  # type: ignore[typeddict-item]
    if data.get("jobID") is not None:
        out["job_id"] = data["jobID"]
    if data.get("networkMigrationExecutionID") is not None:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    if data.get("segmentID") is not None:
        out["segment_id"] = data["segmentID"]
    if data.get("segmentType") is not None:
        out["segment_type"] = data["segmentType"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("logicalID") is not None:
        out["logical_id"] = data["logicalID"]
    if data.get("checksum") is not None:
        import capo_mgn.types.checksum

        out["checksum"] = capo_mgn.types.checksum.deserialize_json(data["checksum"])
    if data.get("outputS3Configuration") is not None:
        import capo_mgn.types.s3_configuration

        out["output_s3_configuration"] = (
            capo_mgn.types.s3_configuration.deserialize_json(
                data["outputS3Configuration"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["created_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["updated_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("scopeTags") is not None:
        import capo_mgn.types.scope_tags_map

        out["scope_tags"] = capo_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    if data.get("targetAccount") is not None:
        out["target_account"] = data["targetAccount"]
    if data.get("referencedSegments") is not None:
        import capo_mgn.types.referenced_segments_list

        out["referenced_segments"] = (
            capo_mgn.types.referenced_segments_list.deserialize_json(
                data["referencedSegments"]
            )
        )
    return out


def redact_sensitive(value: NetworkMigrationMapperSegment) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "scope_tags" in value:
        out["scope_tags"] = "*** Sensitive Data Redacted ***"
    return out
