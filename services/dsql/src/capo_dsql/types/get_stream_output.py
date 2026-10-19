"""Generated from Smithy shape ``com.amazonaws.dsql#GetStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.cluster_id
    import capo_dsql.types.status_reason
    import capo_dsql.types.stream_arn
    import capo_dsql.types.stream_creation_time
    import capo_dsql.types.stream_format
    import capo_dsql.types.stream_id
    import capo_dsql.types.stream_ordering
    import capo_dsql.types.stream_status
    import capo_dsql.types.tag_map
    import capo_dsql.types.target_definition


class GetStreamOutput(TypedDict, closed=True):
    cluster_identifier: "capo_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster for the retrieved stream.</p>"""
    stream_identifier: "capo_dsql.types.stream_id.StreamId"
    """<p>The ID of the retrieved stream.</p>"""
    arn: "capo_dsql.types.stream_arn.StreamArn"
    """<p>The ARN of the retrieved stream.</p>"""
    status: "capo_dsql.types.stream_status.StreamStatus"
    """<p>The current status of the retrieved stream.</p>"""
    creation_time: "capo_dsql.types.stream_creation_time.StreamCreationTime"
    """<p>The time when the stream was created.</p>"""
    ordering: "capo_dsql.types.stream_ordering.StreamOrdering"
    """<p>The ordering mode of the stream.</p>"""
    format: "capo_dsql.types.stream_format.StreamFormat"
    """<p>The format of the stream records.</p>"""
    target_definition: NotRequired["capo_dsql.types.target_definition.TargetDefinition"]
    """<p>The target definition for the stream destination.</p>"""
    status_reason: NotRequired["capo_dsql.types.status_reason.StatusReason"]
    """<p>Stream status reason with error code and timestamp (if applicable).</p>"""
    tags: NotRequired["capo_dsql.types.tag_map.TagMap"]
    """<p>A map of tags associated with the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStreamOutput) -> dict:
    out: dict = {}
    out["clusterIdentifier"] = value["cluster_identifier"]
    out["streamIdentifier"] = value["stream_identifier"]
    out["arn"] = value["arn"]
    import capo_dsql.types.stream_status

    out["status"] = capo_dsql.types.stream_status.serialize_json(value["status"])
    import capo_dsql.types.stream_creation_time

    out["creationTime"] = capo_dsql.types.stream_creation_time.serialize_json(
        value["creation_time"]
    )
    import capo_dsql.types.stream_ordering

    out["ordering"] = capo_dsql.types.stream_ordering.serialize_json(value["ordering"])
    import capo_dsql.types.stream_format

    out["format"] = capo_dsql.types.stream_format.serialize_json(value["format"])
    if "target_definition" in value:
        import capo_dsql.types.target_definition

        out["targetDefinition"] = capo_dsql.types.target_definition.serialize_json(
            value["target_definition"]
        )
    if "status_reason" in value:
        import capo_dsql.types.status_reason

        out["statusReason"] = capo_dsql.types.status_reason.serialize_json(
            value["status_reason"]
        )
    if "tags" in value:
        import capo_dsql.types.tag_map

        out["tags"] = capo_dsql.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetStreamOutput:
    out: GetStreamOutput = {}  # type: ignore[typeddict-item]
    if data.get("clusterIdentifier") is not None:
        out["cluster_identifier"] = data["clusterIdentifier"]
    else:
        out["cluster_identifier"] = ""
    if data.get("streamIdentifier") is not None:
        out["stream_identifier"] = data["streamIdentifier"]
    else:
        out["stream_identifier"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_dsql.types.stream_status

        out["status"] = capo_dsql.types.stream_status.deserialize_json(data["status"])
    else:
        import typing

        out["status"] = typing.cast("capo_dsql.types.stream_status.StreamStatus", "")
    if data.get("creationTime") is not None:
        import capo_dsql.types.stream_creation_time

        out["creation_time"] = capo_dsql.types.stream_creation_time.deserialize_json(
            data["creationTime"]
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("ordering") is not None:
        import capo_dsql.types.stream_ordering

        out["ordering"] = capo_dsql.types.stream_ordering.deserialize_json(
            data["ordering"]
        )
    else:
        import typing

        out["ordering"] = typing.cast(
            "capo_dsql.types.stream_ordering.StreamOrdering", ""
        )
    if data.get("format") is not None:
        import capo_dsql.types.stream_format

        out["format"] = capo_dsql.types.stream_format.deserialize_json(data["format"])
    else:
        import typing

        out["format"] = typing.cast("capo_dsql.types.stream_format.StreamFormat", "")
    if data.get("targetDefinition") is not None:
        import capo_dsql.types.target_definition

        out["target_definition"] = capo_dsql.types.target_definition.deserialize_json(
            data["targetDefinition"]
        )
    if data.get("statusReason") is not None:
        import capo_dsql.types.status_reason

        out["status_reason"] = capo_dsql.types.status_reason.deserialize_json(
            data["statusReason"]
        )
    if data.get("tags") is not None:
        import capo_dsql.types.tag_map

        out["tags"] = capo_dsql.types.tag_map.deserialize_json(data["tags"])
    return out
