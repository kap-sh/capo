"""Generated from Smithy shape ``com.amazonaws.dsql#CreateStreamOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dsql.types.cluster_id
    import capo_dsql.types.stream_arn
    import capo_dsql.types.stream_creation_time
    import capo_dsql.types.stream_format
    import capo_dsql.types.stream_id
    import capo_dsql.types.stream_ordering
    import capo_dsql.types.stream_status


class CreateStreamOutput(TypedDict, closed=True):
    cluster_identifier: "capo_dsql.types.cluster_id.ClusterId"
    """<p>The ID of the cluster for the created stream.</p>"""
    stream_identifier: "capo_dsql.types.stream_id.StreamId"
    """<p>The ID of the created stream.</p>"""
    arn: "capo_dsql.types.stream_arn.StreamArn"
    """<p>The ARN of the created stream.</p>"""
    status: "capo_dsql.types.stream_status.StreamStatus"
    """<p>The status of the created stream.</p>"""
    creation_time: "capo_dsql.types.stream_creation_time.StreamCreationTime"
    """<p>The time when created the stream.</p>"""
    ordering: "capo_dsql.types.stream_ordering.StreamOrdering"
    """<p>The ordering mode of the created stream.</p>"""
    format: "capo_dsql.types.stream_format.StreamFormat"
    """<p>The format of the created stream records.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamOutput) -> dict:
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
    return out


def deserialize_json(data: dict) -> CreateStreamOutput:
    out: CreateStreamOutput = {}  # type: ignore[typeddict-item]
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
    return out
