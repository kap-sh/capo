"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.dataset_config
    import capo_iotsitewise.types.dataset_source
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.metadata
    import capo_iotsitewise.types.restricted_name
    import capo_iotsitewise.types.workspace_name


class UpdateDatasetRequest(TypedDict, closed=True):
    dataset_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the dataset.</p>"""
    workspace_name: NotRequired["capo_iotsitewise.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace that contains the dataset.</p>"""
    dataset_name: "capo_iotsitewise.types.restricted_name.RestrictedName"
    """<p>The name of the dataset.</p>"""
    dataset_description: NotRequired["capo_iotsitewise.types.description.Description"]
    """<p>A description about the dataset, and its functionality.</p>"""
    dataset_config: NotRequired["capo_iotsitewise.types.dataset_config.DatasetConfig"]
    """<p>The updated configuration for the dataset.</p>"""
    metadata: NotRequired["capo_iotsitewise.types.metadata.Metadata"]
    """<p>The updated metadata for the dataset.</p>"""
    dataset_source: "capo_iotsitewise.types.dataset_source.DatasetSource"
    """<p>The data source for the dataset.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDatasetRequest) -> dict:
    out: dict = {}
    if "workspace_name" in value:
        out["workspaceName"] = value["workspace_name"]
    out["datasetName"] = value["dataset_name"]
    if "dataset_description" in value:
        out["datasetDescription"] = value["dataset_description"]
    if "dataset_config" in value:
        import capo_iotsitewise.types.dataset_config

        out["datasetConfig"] = capo_iotsitewise.types.dataset_config.serialize_json(
            value["dataset_config"]
        )
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
    return out


def deserialize_json(data: dict) -> UpdateDatasetRequest:
    out: UpdateDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("workspaceName") is not None:
        out["workspace_name"] = data["workspaceName"]
    if data.get("datasetName") is not None:
        out["dataset_name"] = data["datasetName"]
    else:
        out["dataset_name"] = ""
    if data.get("datasetDescription") is not None:
        out["dataset_description"] = data["datasetDescription"]
    if data.get("datasetConfig") is not None:
        import capo_iotsitewise.types.dataset_config

        out["dataset_config"] = capo_iotsitewise.types.dataset_config.deserialize_json(
            data["datasetConfig"]
        )
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
        raise DeserializationError("UpdateDatasetRequest.dataset_source required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
