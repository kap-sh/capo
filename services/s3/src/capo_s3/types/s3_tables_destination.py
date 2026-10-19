"""Generated from Smithy shape ``com.amazonaws.s3#S3TablesDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.s3_tables_bucket_arn
    import capo_s3.types.s3_tables_name


class S3TablesDestination(TypedDict, closed=True):
    table_bucket_arn: "capo_s3.types.s3_tables_bucket_arn.S3TablesBucketArn"
    """<p> The Amazon Resource Name (ARN) for the table bucket that's specified as the destination in the metadata table configuration. The destination table bucket must be in the same Region and Amazon Web Services account as the general purpose bucket. </p>"""
    table_name: "capo_s3.types.s3_tables_name.S3TablesName"
    """<p> The name for the metadata table in your metadata table configuration. The specified metadata table name must be unique within the <code>aws_s3_metadata</code> namespace in the destination table bucket. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3TablesDestination, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "TableBucketArn").text = str(value["table_bucket_arn"])
    SubElement(el, "TableName").text = str(value["table_name"])


def deserialize_xml(el: Element) -> S3TablesDestination:
    out: S3TablesDestination = {}  # type: ignore[typeddict-item]
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
    return out
