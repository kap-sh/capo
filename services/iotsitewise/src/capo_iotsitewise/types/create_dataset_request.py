"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.dataset_config
    import capo_iotsitewise.types.dataset_source
    import capo_iotsitewise.types.dataset_type_enum
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.metadata
    import capo_iotsitewise.types.restricted_name
    import capo_iotsitewise.types.tag_map
    import capo_iotsitewise.types.workspace_name


class CreateDatasetRequest(TypedDict, closed=True):
    dataset_id: NotRequired["capo_iotsitewise.types.id.ID"]
    """<p>The ID of the dataset.</p>"""
    dataset_name: "capo_iotsitewise.types.restricted_name.RestrictedName"
    """<p>The name of the dataset.</p>"""
    dataset_description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>A description about the dataset, and its functionality.</p>"""
    dataset_type: NotRequired[
        "capo_iotsitewise.types.dataset_type_enum.DatasetTypeEnum"
    ]
    """<p>The type of dataset: a session dataset, a curated dataset, or a connection to an external datasource.</p>"""
    dataset_config: NotRequired["capo_iotsitewise.types.dataset_config.DatasetConfig"]
    """<p>The configuration for the dataset.</p>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace that contains the dataset. Required for session and curated datasets. Omit this field for datasets that connect to an external datasource.</p>"""
    metadata: NotRequired["capo_iotsitewise.types.metadata.Metadata"]
    """<p>The metadata for the dataset, provided as key-value pairs.</p>"""
    dataset_source: "capo_iotsitewise.types.dataset_source.DatasetSource"
    """<p>The data source for the dataset.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""
    tags: NotRequired["capo_iotsitewise.types.tag_map.TagMap"]
    """<p>A list of key-value pairs that contain metadata for the access policy. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetRequest) -> dict:
    out: dict = {}
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    out["datasetName"] = value["dataset_name"]
    if "dataset_description" in value:
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    if data.get("datasetName") is not None:
        out["dataset_name"] = data["datasetName"]
    else:
        raise DeserializationError("CreateDatasetRequest.dataset_name required")
    if data.get("datasetDescription") is not None:
        out["dataset_description"] = data["datasetDescription"]
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
        raise DeserializationError("CreateDatasetRequest.dataset_source required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_iotsitewise.types.tag_map

        out["tags"] = capo_iotsitewise.types.tag_map.deserialize_json(data["tags"])
    return out
