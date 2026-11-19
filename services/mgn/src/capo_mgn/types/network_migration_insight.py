"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationInsight``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mgn.types.construct_id
    import capo_mgn.types.insight_id
    import capo_mgn.types.insight_level
    import capo_mgn.types.insight_message
    import capo_mgn.types.insight_producer_id
    import capo_mgn.types.insight_producer_name
    import capo_mgn.types.insight_producer_type
    import capo_mgn.types.insight_type
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id
    import capo_mgn.types.segment_id


class NetworkMigrationInsight(TypedDict, closed=True):
    network_migration_definition_id: NotRequired[
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    ]
    """<p>The unique identifier of the network migration definition the insight belongs to.</p>"""
    network_migration_execution_id: NotRequired[
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    ]
    """<p>The unique identifier of the network migration execution the insight belongs to.</p>"""
    producer_id: NotRequired["capo_mgn.types.insight_producer_id.InsightProducerID"]
    """<p>The identifier of the job or API request that produced the insight.</p>"""
    producer_type: NotRequired[
        "capo_mgn.types.insight_producer_type.InsightProducerType"
    ]
    """<p>Whether the insight was produced by a job or by an API request.</p>"""
    producer_name: NotRequired[
        "capo_mgn.types.insight_producer_name.InsightProducerName"
    ]
    """<p>The job type or API name that produced the insight.</p>"""
    segment_id: NotRequired["capo_mgn.types.segment_id.SegmentID"]
    """<p>The unique identifier of the segment the insight relates to; absent for run-level insights.</p>"""
    construct_id: NotRequired["capo_mgn.types.construct_id.ConstructID"]
    """<p>The unique identifier of the construct the insight relates to; absent for run-level and segment-level insights.</p>"""
    insight_id: NotRequired["capo_mgn.types.insight_id.InsightID"]
    """<p>The unique identifier of the insight.</p>"""
    insight_level: NotRequired["capo_mgn.types.insight_level.InsightLevel"]
    """<p>The level that the insight applies to: the run, a segment, or a construct.</p>"""
    insight_type: NotRequired["capo_mgn.types.insight_type.InsightType"]
    """<p>The type of the insight.</p>"""
    insight_message: NotRequired["capo_mgn.types.insight_message.InsightMessage"]
    """<p>The content of the insight.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the insight was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationInsight) -> dict:
    out: dict = {}
    if "network_migration_definition_id" in value:
        out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "network_migration_execution_id" in value:
        out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    if "producer_id" in value:
        out["producerID"] = value["producer_id"]
    if "producer_type" in value:
        out["producerType"] = value["producer_type"]
    if "producer_name" in value:
        out["producerName"] = value["producer_name"]
    if "segment_id" in value:
        out["segmentID"] = value["segment_id"]
    if "construct_id" in value:
        out["constructID"] = value["construct_id"]
    if "insight_id" in value:
        out["insightID"] = value["insight_id"]
    if "insight_level" in value:
        out["insightLevel"] = value["insight_level"]
    if "insight_type" in value:
        out["insightType"] = value["insight_type"]
    if "insight_message" in value:
        import capo_mgn.types.insight_message

        out["insightMessage"] = capo_mgn.types.insight_message.serialize_json(
            value["insight_message"]
        )
    if "created_at" in value:
        import capo_mgn.types._prelude.timestamp

        out["createdAt"] = capo_mgn.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    return out


def deserialize_json(data: dict) -> NetworkMigrationInsight:
    out: NetworkMigrationInsight = {}  # type: ignore[typeddict-item]
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    if data.get("networkMigrationExecutionID") is not None:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    if data.get("producerID") is not None:
        out["producer_id"] = data["producerID"]
    if data.get("producerType") is not None:
        out["producer_type"] = data["producerType"]
    if data.get("producerName") is not None:
        out["producer_name"] = data["producerName"]
    if data.get("segmentID") is not None:
        out["segment_id"] = data["segmentID"]
    if data.get("constructID") is not None:
        out["construct_id"] = data["constructID"]
    if data.get("insightID") is not None:
        out["insight_id"] = data["insightID"]
    if data.get("insightLevel") is not None:
        out["insight_level"] = data["insightLevel"]
    if data.get("insightType") is not None:
        out["insight_type"] = data["insightType"]
    if data.get("insightMessage") is not None:
        import capo_mgn.types.insight_message

        out["insight_message"] = capo_mgn.types.insight_message.deserialize_json(
            data["insightMessage"]
        )
    if data.get("createdAt") is not None:
        import capo_mgn.types._prelude.timestamp

        out["created_at"] = capo_mgn.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    return out
