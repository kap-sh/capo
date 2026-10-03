"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DatasetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.dataset_enrichment
    import capo_iotsitewise.types.dataset_source_type
    import capo_iotsitewise.types.dataset_status
    import capo_iotsitewise.types.dataset_type_enum
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.restricted_name
    import capo_iotsitewise.types.timestamp


class DatasetSummary(TypedDict, closed=True):
    id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""
    arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">ARN</a> of the dataset. The format is <code>arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}</code>.</p>"""
    name: "capo_iotsitewise.types.restricted_name.RestrictedName"
    """<p>The name of the dataset.</p>"""
    description: "capo_iotsitewise.types.description.Description"
    """<p>A description about the dataset, and its functionality.</p>"""
    source_type: NotRequired[
        "capo_iotsitewise.types.dataset_source_type.DatasetSourceType"
    ]
    """<p>The data source type of the dataset.</p>"""
    dataset_type: NotRequired[
        "capo_iotsitewise.types.dataset_type_enum.DatasetTypeEnum"
    ]
    """<p>The type of dataset: a session dataset, a curated dataset, or a connection to an external datasource.</p>"""
    creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The dataset creation date, in Unix epoch time.</p>"""
    last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the dataset was last updated, in Unix epoch time.</p>"""
    status: "capo_iotsitewise.types.dataset_status.DatasetStatus"
    """<p>The status of the dataset. This contains the state and any error messages. The state is <code>ACTIVE</code> when ready to use.</p>"""
    enrichment_status: NotRequired[
        "capo_iotsitewise.types.dataset_enrichment.DatasetEnrichment"
    ]
    """<p>The enrichment status of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    if "source_type" in value:
        import capo_iotsitewise.types.dataset_source_type

        out["sourceType"] = capo_iotsitewise.types.dataset_source_type.serialize_json(
            value["source_type"]
        )
    if "dataset_type" in value:
        import capo_iotsitewise.types.dataset_type_enum

        out["datasetType"] = capo_iotsitewise.types.dataset_type_enum.serialize_json(
            value["dataset_type"]
        )
    import capo_iotsitewise.types.timestamp

    out["creationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["lastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["last_update_date"]
    )
    import capo_iotsitewise.types.dataset_status

    out["status"] = capo_iotsitewise.types.dataset_status.serialize_json(
        value["status"]
    )
    if "enrichment_status" in value:
        import capo_iotsitewise.types.dataset_enrichment

        out["enrichmentStatus"] = (
            capo_iotsitewise.types.dataset_enrichment.serialize_json(
                value["enrichment_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DatasetSummary:
    out: DatasetSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("DatasetSummary.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DatasetSummary.arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DatasetSummary.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError("DatasetSummary.description required")
    if data.get("sourceType") is not None:
        import capo_iotsitewise.types.dataset_source_type

        out["source_type"] = (
            capo_iotsitewise.types.dataset_source_type.deserialize_json(
                data["sourceType"]
            )
        )
    if data.get("datasetType") is not None:
        import capo_iotsitewise.types.dataset_type_enum

        out["dataset_type"] = capo_iotsitewise.types.dataset_type_enum.deserialize_json(
            data["datasetType"]
        )
    if data.get("creationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["creation_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    else:
        raise DeserializationError("DatasetSummary.creation_date required")
    if data.get("lastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["last_update_date"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["lastUpdateDate"]
        )
    else:
        raise DeserializationError("DatasetSummary.last_update_date required")
    if data.get("status") is not None:
        import capo_iotsitewise.types.dataset_status

        out["status"] = capo_iotsitewise.types.dataset_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DatasetSummary.status required")
    if data.get("enrichmentStatus") is not None:
        import capo_iotsitewise.types.dataset_enrichment

        out["enrichment_status"] = (
            capo_iotsitewise.types.dataset_enrichment.deserialize_json(
                data["enrichmentStatus"]
            )
        )
    return out
