"""Generated from Smithy shape ``com.amazonaws.neptunegraph#NeptuneImportOptions``."""

from typing_extensions import NotRequired, TypedDict


class NeptuneImportOptions(TypedDict, closed=True):
    s3_export_path: "str"
    """<p>The path to an S3 bucket from which to import data.</p>"""
    s3_export_kms_key_id: "str"
    """<p>The KMS key to use to encrypt data in the S3 bucket where the graph data is exported</p>"""
    preserve_default_vertex_labels: NotRequired["bool"]
    """<p>Neptune Analytics supports label-less vertices and no labels are assigned unless one is explicitly provided. Neptune assigns default labels when none is explicitly provided. When importing the data into Neptune Analytics, the default vertex labels can be omitted by setting <i>preserveDefaultVertexLabels</i> to false. Note that if the vertex only has default labels, and has no other properties or edges, then the vertex will effectively not get imported into Neptune Analytics when preserveDefaultVertexLabels is set to false.</p>"""
    preserve_edge_ids: NotRequired["bool"]
    """<p>Neptune Analytics currently does not support user defined edge ids. The edge ids are not imported by default. They are imported if <i>preserveEdgeIds</i> is set to true, and ids are stored as properties on the relationships with the property name <i>neptuneEdgeId</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NeptuneImportOptions) -> dict:
    out: dict = {}
    out["s3ExportPath"] = value["s3_export_path"]
    out["s3ExportKmsKeyId"] = value["s3_export_kms_key_id"]
    if "preserve_default_vertex_labels" in value:
        out["preserveDefaultVertexLabels"] = value["preserve_default_vertex_labels"]
    if "preserve_edge_ids" in value:
        out["preserveEdgeIds"] = value["preserve_edge_ids"]
    return out


def deserialize_json(data: dict) -> NeptuneImportOptions:
    out: NeptuneImportOptions = {}  # type: ignore[typeddict-item]
    if data.get("s3ExportPath") is not None:
        out["s3_export_path"] = data["s3ExportPath"]
    else:
        out["s3_export_path"] = ""
    if data.get("s3ExportKmsKeyId") is not None:
        out["s3_export_kms_key_id"] = data["s3ExportKmsKeyId"]
    else:
        out["s3_export_kms_key_id"] = ""
    if data.get("preserveDefaultVertexLabels") is not None:
        out["preserve_default_vertex_labels"] = data["preserveDefaultVertexLabels"]
    if data.get("preserveEdgeIds") is not None:
        out["preserve_edge_ids"] = data["preserveEdgeIds"]
    return out
