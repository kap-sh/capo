"""Generated from Smithy shape ``com.amazonaws.kendra#IndexConfigurationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.index_edition
    import capo_kendra.types.index_id
    import capo_kendra.types.index_name
    import capo_kendra.types.index_status
    import capo_kendra.types.timestamp


class IndexConfigurationSummary(TypedDict, closed=True):
    name: NotRequired["capo_kendra.types.index_name.IndexName"]
    """<p>The name of the index.</p>"""
    id: NotRequired["capo_kendra.types.index_id.IndexId"]
    """<p>A identifier for the index. Use this to identify the index when you are using APIs such as <code>Query</code>, <code>DescribeIndex</code>, <code>UpdateIndex</code>, and <code>DeleteIndex</code>.</p>"""
    edition: NotRequired["capo_kendra.types.index_edition.IndexEdition"]
    """<p>Indicates whether the index is a Enterprise Edition index or a Developer Edition index. </p>"""
    created_at: "capo_kendra.types.timestamp.Timestamp"
    """<p>The Unix timestamp when the index was created.</p>"""
    updated_at: "capo_kendra.types.timestamp.Timestamp"
    """<p>The Unix timestamp when the index was last updated.</p>"""
    status: "capo_kendra.types.index_status.IndexStatus"
    """<p>The current status of the index. When the status is <code>ACTIVE</code>, the index is ready to search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IndexConfigurationSummary) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "edition" in value:
        import capo_kendra.types.index_edition

        out["Edition"] = capo_kendra.types.index_edition.serialize_aws_json_1_1(
            value["edition"]
        )
    import capo_kendra.types.timestamp

    out["CreatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
        value["created_at"]
    )
    import capo_kendra.types.timestamp

    out["UpdatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
        value["updated_at"]
    )
    import capo_kendra.types.index_status

    out["Status"] = capo_kendra.types.index_status.serialize_aws_json_1_1(
        value["status"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IndexConfigurationSummary:
    out: IndexConfigurationSummary = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Edition") is not None:
        import capo_kendra.types.index_edition

        out["edition"] = capo_kendra.types.index_edition.deserialize_aws_json_1_1(
            data["Edition"]
        )
    if data.get("CreatedAt") is not None:
        import capo_kendra.types.timestamp

        out["created_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("UpdatedAt") is not None:
        import capo_kendra.types.timestamp

        out["updated_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Status") is not None:
        import capo_kendra.types.index_status

        out["status"] = capo_kendra.types.index_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    else:
        import typing

        out["status"] = typing.cast("capo_kendra.types.index_status.IndexStatus", "")
    return out
