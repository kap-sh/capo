"""Generated from Smithy shape ``com.amazonaws.s3#S3TablesDestinationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.s3_tables_arn
    import capo_s3.types.s3_tables_bucket_arn
    import capo_s3.types.s3_tables_name
    import capo_s3.types.s3_tables_namespace


class S3TablesDestinationResult(TypedDict, closed=True):
    table_bucket_arn: "capo_s3.types.s3_tables_bucket_arn.S3TablesBucketArn"
    """<p> The Amazon Resource Name (ARN) for the table bucket that's specified as the destination in the metadata table configuration. The destination table bucket must be in the same Region and Amazon Web Services account as the general purpose bucket. </p>"""
    table_name: "capo_s3.types.s3_tables_name.S3TablesName"
    """<p> The name for the metadata table in your metadata table configuration. The specified metadata table name must be unique within the <code>aws_s3_metadata</code> namespace in the destination table bucket. </p>"""
    table_arn: "capo_s3.types.s3_tables_arn.S3TablesArn"
    """<p> The Amazon Resource Name (ARN) for the metadata table in the metadata table configuration. The specified metadata table name must be unique within the <code>aws_s3_metadata</code> namespace in the destination table bucket. </p>"""
    table_namespace: "capo_s3.types.s3_tables_namespace.S3TablesNamespace"
    """<p> The table bucket namespace for the metadata table in your metadata table configuration. This value is always <code>aws_s3_metadata</code>. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3TablesDestinationResult, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "TableBucketArn").text = str(value["table_bucket_arn"])
    SubElement(el, "TableName").text = str(value["table_name"])
    SubElement(el, "TableArn").text = str(value["table_arn"])
    SubElement(el, "TableNamespace").text = str(value["table_namespace"])


def deserialize_xml(el: Element) -> S3TablesDestinationResult:
    out: S3TablesDestinationResult = {}  # type: ignore[typeddict-item]
    child_table_bucket_arn = el.find("TableBucketArn")
    if child_table_bucket_arn is not None:
        out["table_bucket_arn"] = str(child_table_bucket_arn.text or "")
    else:
        out["table_bucket_arn"] = ""
    child_table_name = el.find("TableName")
    if child_table_name is not None:
        out["table_name"] = str(child_table_name.text or "")
    else:
        out["table_name"] = ""
    child_table_arn = el.find("TableArn")
    if child_table_arn is not None:
        out["table_arn"] = str(child_table_arn.text or "")
    else:
        out["table_arn"] = ""
    child_table_namespace = el.find("TableNamespace")
    if child_table_namespace is not None:
        out["table_namespace"] = str(child_table_namespace.text or "")
    else:
        out["table_namespace"] = ""
    return out
