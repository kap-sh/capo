"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.dataset_config
    import capo_iotsitewise.types.dataset_enrichment
    import capo_iotsitewise.types.dataset_source
    import capo_iotsitewise.types.dataset_status
    import capo_iotsitewise.types.dataset_type_enum
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.metadata
    import capo_iotsitewise.types.restricted_name
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.version
    import capo_iotsitewise.types.workspace_name


class DescribeDatasetResponse(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""
    dataset_arn: "capo_iotsitewise.types.arn.ARN"
    """<p>The <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">ARN</a> of the dataset. The format is <code>arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}</code>.</p>"""
    dataset_name: "capo_iotsitewise.types.restricted_name.RestrictedName"
    """<p>The name of the dataset.</p>"""
    dataset_description: "capo_iotsitewise.types.description.Description"
    """<p>A description about the dataset, and its functionality.</p>"""
    dataset_type: NotRequired[
        "capo_iotsitewise.types.dataset_type_enum.DatasetTypeEnum"
    ]
    """<p>The type of dataset: a session dataset, a curated dataset, or a connection to an external datasource.</p>"""
    dataset_config: NotRequired["capo_iotsitewise.types.dataset_config.DatasetConfig"]
    """<p>The configuration for the dataset.</p>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace that contains the dataset.</p>"""
    metadata: NotRequired["capo_iotsitewise.types.metadata.Metadata"]
    """<p>The metadata for the dataset.</p>"""
    dataset_source: "capo_iotsitewise.types.dataset_source.DatasetSource"
    """<p>The data source for the dataset.</p>"""
    dataset_status: "capo_iotsitewise.types.dataset_status.DatasetStatus"
    """<p>The status of the dataset. This contains the state and any error messages. State is <code>CREATING</code> after a successfull call to this API, and any associated error message. The state is <code>ACTIVE</code> when ready to use.</p>"""
    dataset_creation_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The dataset creation date, in Unix epoch time.</p>"""
    dataset_last_update_date: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The date the dataset was last updated, in Unix epoch time.</p>"""
    dataset_version: NotRequired["capo_iotsitewise.types.version.Version"]
    """<p>The version of the dataset.</p>"""
    enrichment_status: NotRequired[
        "capo_iotsitewise.types.dataset_enrichment.DatasetEnrichment"
    ]
    """<p>The enrichment status of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDatasetResponse) -> dict:
    out: dict = {}
    out["datasetId"] = value["dataset_id"]
    out["datasetArn"] = value["dataset_arn"]
    out["datasetName"] = value["dataset_name"]
    out["datasetDescription"] = value["dataset_description"]
    if "dataset_type" in value:
        import capo_iotsitewise.types.dataset_type_enum

        out["datasetType"] = capo_iotsitewise.types.dataset_type_enum.serialize_json(
            value["dataset_type"]
        )
    if "dataset_config" in value:
        import capo_iotsitewise.types.dataset_config

        out["datasetConfig"] = capo_iotsitewise.types.dataset_config.serialize_json(
            value["dataset_config"]
        )
    if "workspace_name" in value:
        out["workspaceName"] = value["workspace_name"]
    if "metadata" in value:
        import capo_iotsitewise.types.metadata

        out["metadata"] = capo_iotsitewise.types.metadata.serialize_json(
            value["metadata"]
        )
    import capo_iotsitewise.types.dataset_source

    out["datasetSource"] = capo_iotsitewise.types.dataset_source.serialize_json(
        value["dataset_source"]
    )
    import capo_iotsitewise.types.dataset_status

    out["datasetStatus"] = capo_iotsitewise.types.dataset_status.serialize_json(
        value["dataset_status"]
    )
    import capo_iotsitewise.types.timestamp

    out["datasetCreationDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["dataset_creation_date"]
    )
    import capo_iotsitewise.types.timestamp

    out["datasetLastUpdateDate"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["dataset_last_update_date"]
    )
    if "dataset_version" in value:
        out["datasetVersion"] = value["dataset_version"]
    if "enrichment_status" in value:
        import capo_iotsitewise.types.dataset_enrichment

        out["enrichmentStatus"] = (
            capo_iotsitewise.types.dataset_enrichment.serialize_json(
                value["enrichment_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeDatasetResponse:
    out: DescribeDatasetResponse = {}  # type: ignore[typeddict-item]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("DescribeDatasetResponse.dataset_id required")
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("DescribeDatasetResponse.dataset_arn required")
    if data.get("datasetName") is not None:
        out["dataset_name"] = data["datasetName"]
    else:
        raise DeserializationError("DescribeDatasetResponse.dataset_name required")
    if data.get("datasetDescription") is not None:
        out["dataset_description"] = data["datasetDescription"]
    else:
        raise DeserializationError(
            "DescribeDatasetResponse.dataset_description required"
        )
    if data.get("datasetType") is not None:
        import capo_iotsitewise.types.dataset_type_enum

        out["dataset_type"] = capo_iotsitewise.types.dataset_type_enum.deserialize_json(
            data["datasetType"]
        )
    if data.get("datasetConfig") is not None:
        import capo_iotsitewise.types.dataset_config

        out["dataset_config"] = capo_iotsitewise.types.dataset_config.deserialize_json(
            data["datasetConfig"]
        )
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    if data.get("metadata") is not None:
        import capo_iotsitewise.types.metadata

        out["metadata"] = capo_iotsitewise.types.metadata.deserialize_json(
            data["metadata"]
        )
    if data.get("datasetSource") is not None:
        import capo_iotsitewise.types.dataset_source

        out["dataset_source"] = capo_iotsitewise.types.dataset_source.deserialize_json(
            data["datasetSource"]
        )
    else:
        raise DeserializationError("DescribeDatasetResponse.dataset_source required")
    if data.get("datasetStatus") is not None:
        import capo_iotsitewise.types.dataset_status

        out["dataset_status"] = capo_iotsitewise.types.dataset_status.deserialize_json(
            data["datasetStatus"]
        )
    else:
        raise DeserializationError("DescribeDatasetResponse.dataset_status required")
    if data.get("datasetCreationDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["dataset_creation_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["datasetCreationDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDatasetResponse.dataset_creation_date required"
        )
    if data.get("datasetLastUpdateDate") is not None:
        import capo_iotsitewise.types.timestamp

        out["dataset_last_update_date"] = (
            capo_iotsitewise.types.timestamp.deserialize_json(
                data["datasetLastUpdateDate"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDatasetResponse.dataset_last_update_date required"
        )
    if data.get("datasetVersion") is not None:
        out["dataset_version"] = data["datasetVersion"]
    if data.get("enrichmentStatus") is not None:
        import capo_iotsitewise.types.dataset_enrichment

        out["enrichment_status"] = (
            capo_iotsitewise.types.dataset_enrichment.deserialize_json(
                data["enrichmentStatus"]
            )
        )
    return out
