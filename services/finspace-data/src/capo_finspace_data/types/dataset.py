"""Generated from Smithy shape ``com.amazonaws.finspacedata#Dataset``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace_data.types.alias_string
    import capo_finspace_data.types.dataset_arn
    import capo_finspace_data.types.dataset_description
    import capo_finspace_data.types.dataset_id
    import capo_finspace_data.types.dataset_kind
    import capo_finspace_data.types.dataset_owner_info
    import capo_finspace_data.types.dataset_title
    import capo_finspace_data.types.schema_union
    import capo_finspace_data.types.timestamp_epoch


class Dataset(TypedDict, closed=True):
    dataset_id: NotRequired["capo_finspace_data.types.dataset_id.DatasetId"]
    """<p>An identifier for a Dataset.</p>"""
    dataset_arn: NotRequired["capo_finspace_data.types.dataset_arn.DatasetArn"]
    """<p>The ARN identifier of the Dataset.</p>"""
    dataset_title: NotRequired["capo_finspace_data.types.dataset_title.DatasetTitle"]
    """<p>Display title for a Dataset.</p>"""
    kind: NotRequired["capo_finspace_data.types.dataset_kind.DatasetKind"]
    """<p>The format in which Dataset data is structured.</p> <ul> <li> <p> <code>TABULAR</code> – Data is structured in a tabular format.</p> </li> <li> <p> <code>NON_TABULAR</code> – Data is structured in a non-tabular format.</p> </li> </ul>"""
    dataset_description: NotRequired[
        "capo_finspace_data.types.dataset_description.DatasetDescription"
    ]
    """<p>Description for a Dataset.</p>"""
    owner_info: NotRequired[
        "capo_finspace_data.types.dataset_owner_info.DatasetOwnerInfo"
    ]
    """<p>Contact information for a Dataset owner.</p>"""
    create_time: "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>The timestamp at which the Dataset was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    last_modified_time: "capo_finspace_data.types.timestamp_epoch.TimestampEpoch"
    """<p>The last time that the Dataset was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    schema_definition: NotRequired["capo_finspace_data.types.schema_union.SchemaUnion"]
    """<p>Definition for a schema on a tabular Dataset.</p>"""
    alias: NotRequired["capo_finspace_data.types.alias_string.AliasString"]
    """<p>The unique resource identifier for a Dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dataset) -> dict:
    out: dict = {}
    if "dataset_id" in value:
        out["datasetId"] = value["dataset_id"]
    if "dataset_arn" in value:
        out["datasetArn"] = value["dataset_arn"]
    if "dataset_title" in value:
        out["datasetTitle"] = value["dataset_title"]
    if "kind" in value:
        import capo_finspace_data.types.dataset_kind

        out["kind"] = capo_finspace_data.types.dataset_kind.serialize_json(
            value["kind"]
        )
    if "dataset_description" in value:
        out["datasetDescription"] = value["dataset_description"]
    if "owner_info" in value:
        import capo_finspace_data.types.dataset_owner_info

        out["ownerInfo"] = capo_finspace_data.types.dataset_owner_info.serialize_json(
            value["owner_info"]
        )
    out["createTime"] = value.get("create_time", 0)
    out["lastModifiedTime"] = value.get("last_modified_time", 0)
    if "schema_definition" in value:
        import capo_finspace_data.types.schema_union

        out["schemaDefinition"] = capo_finspace_data.types.schema_union.serialize_json(
            value["schema_definition"]
        )
    if "alias" in value:
        out["alias"] = value["alias"]
    return out


def deserialize_json(data: dict) -> Dataset:
    out: Dataset = {}  # type: ignore[typeddict-item]
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    if data.get("datasetTitle") is not None:
        out["dataset_title"] = data["datasetTitle"]
    if data.get("kind") is not None:
        import capo_finspace_data.types.dataset_kind

        out["kind"] = capo_finspace_data.types.dataset_kind.deserialize_json(
            data["kind"]
        )
    if data.get("datasetDescription") is not None:
        out["dataset_description"] = data["datasetDescription"]
    if data.get("ownerInfo") is not None:
        import capo_finspace_data.types.dataset_owner_info

        out["owner_info"] = (
            capo_finspace_data.types.dataset_owner_info.deserialize_json(
                data["ownerInfo"]
            )
        )
    if data.get("createTime") is not None:
        out["create_time"] = data["createTime"]
    else:
        out["create_time"] = 0
    if data.get("lastModifiedTime") is not None:
        out["last_modified_time"] = data["lastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if data.get("schemaDefinition") is not None:
        import capo_finspace_data.types.schema_union

        out["schema_definition"] = (
            capo_finspace_data.types.schema_union.deserialize_json(
                data["schemaDefinition"]
            )
        )
    if data.get("alias") is not None:
        out["alias"] = data["alias"]
    return out


def redact_sensitive(value: Dataset) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "owner_info" in value:
        import capo_finspace_data.types.dataset_owner_info

        out["owner_info"] = (
            capo_finspace_data.types.dataset_owner_info.redact_sensitive(
                value["owner_info"]
            )
        )
    return out
