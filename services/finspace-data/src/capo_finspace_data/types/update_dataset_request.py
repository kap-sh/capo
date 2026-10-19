"""Generated from Smithy shape ``com.amazonaws.finspacedata#UpdateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.alias_string
    import capo_finspace_data.types.client_token
    import capo_finspace_data.types.dataset_description
    import capo_finspace_data.types.dataset_id
    import capo_finspace_data.types.dataset_kind
    import capo_finspace_data.types.dataset_title
    import capo_finspace_data.types.schema_union


class UpdateDatasetRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_finspace_data.types.client_token.ClientToken"]
    """<p>A token that ensures idempotency. This token expires in 10 minutes.</p>"""
    dataset_id: "capo_finspace_data.types.dataset_id.DatasetId"
    """<p>The unique identifier for the Dataset to update.</p>"""
    dataset_title: "capo_finspace_data.types.dataset_title.DatasetTitle"
    """<p>A display title for the Dataset.</p>"""
    kind: "capo_finspace_data.types.dataset_kind.DatasetKind"
    """<p>The format in which the Dataset data is structured.</p> <ul> <li> <p> <code>TABULAR</code> – Data is structured in a tabular format.</p> </li> <li> <p> <code>NON_TABULAR</code> – Data is structured in a non-tabular format.</p> </li> </ul>"""
    dataset_description: NotRequired[
        "capo_finspace_data.types.dataset_description.DatasetDescription"
    ]
    """<p>A description for the Dataset.</p>"""
    alias: NotRequired["capo_finspace_data.types.alias_string.AliasString"]
    """<p>The unique resource identifier for a Dataset.</p>"""
    schema_definition: NotRequired["capo_finspace_data.types.schema_union.SchemaUnion"]
    """<p>Definition for a schema on a tabular Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDatasetRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["datasetTitle"] = value["dataset_title"]
    import capo_finspace_data.types.dataset_kind

    out["kind"] = capo_finspace_data.types.dataset_kind.serialize_json(value["kind"])
    if "dataset_description" in value:
        out["datasetDescription"] = value["dataset_description"]
    if "alias" in value:
        out["alias"] = value["alias"]
    if "schema_definition" in value:
        import capo_finspace_data.types.schema_union

        out["schemaDefinition"] = capo_finspace_data.types.schema_union.serialize_json(
            value["schema_definition"]
        )
    return out


def deserialize_json(data: dict) -> UpdateDatasetRequest:
    out: UpdateDatasetRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("datasetTitle") is not None:
        out["dataset_title"] = data["datasetTitle"]
    else:
        out["dataset_title"] = ""
    if data.get("kind") is not None:
        import capo_finspace_data.types.dataset_kind

        out["kind"] = capo_finspace_data.types.dataset_kind.deserialize_json(
            data["kind"]
        )
    else:
        import typing

        out["kind"] = typing.cast(
            "capo_finspace_data.types.dataset_kind.DatasetKind", ""
        )
    if data.get("datasetDescription") is not None:
        out["dataset_description"] = data["datasetDescription"]
    if data.get("alias") is not None:
        out["alias"] = data["alias"]
    if data.get("schemaDefinition") is not None:
        import capo_finspace_data.types.schema_union

        out["schema_definition"] = (
            capo_finspace_data.types.schema_union.deserialize_json(
                data["schemaDefinition"]
            )
        )
    return out
