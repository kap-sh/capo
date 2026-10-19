"""Generated from Smithy shape ``com.amazonaws.s3tables#UpdateTableMetadataLocationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.metadata_location
    import capo_s3tables.types.namespace_list
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_name
    import capo_s3tables.types.version_token


class UpdateTableMetadataLocationResponse(TypedDict, closed=True):
    name: "capo_s3tables.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    namespace: "capo_s3tables.types.namespace_list.NamespaceList"
    """<p>The namespace the table is associated with.</p>"""
    version_token: "capo_s3tables.types.version_token.VersionToken"
    """<p>The version token of the table.</p>"""
    metadata_location: "capo_s3tables.types.metadata_location.MetadataLocation"
    """<p>The metadata location of the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTableMetadataLocationResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["tableARN"] = value["table_arn"]
    import capo_s3tables.types.namespace_list

    out["namespace"] = capo_s3tables.types.namespace_list.serialize_json(
        value["namespace"]
    )
    out["versionToken"] = value["version_token"]
    out["metadataLocation"] = value["metadata_location"]
    return out


def deserialize_json(data: dict) -> UpdateTableMetadataLocationResponse:
    out: UpdateTableMetadataLocationResponse = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("tableARN") is not None:
        out["table_arn"] = data["tableARN"]
    else:
        out["table_arn"] = ""
    if data.get("namespace") is not None:
        import capo_s3tables.types.namespace_list

        out["namespace"] = capo_s3tables.types.namespace_list.deserialize_json(
            data["namespace"]
        )
    else:
        out["namespace"] = []
    if data.get("versionToken") is not None:
        out["version_token"] = data["versionToken"]
    else:
        out["version_token"] = ""
    if data.get("metadataLocation") is not None:
        out["metadata_location"] = data["metadataLocation"]
    else:
        out["metadata_location"] = ""
    return out
