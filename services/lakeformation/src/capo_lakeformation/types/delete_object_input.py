"""Generated from Smithy shape ``com.amazonaws.lakeformation#DeleteObjectInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.e_tag_string
    import capo_lakeformation.types.partition_values_list
    import capo_lakeformation.types.uri


class DeleteObjectInput(TypedDict, closed=True):
    uri: "capo_lakeformation.types.uri.URI"
    """<p>The Amazon S3 location of the object to delete.</p>"""
    e_tag: NotRequired["capo_lakeformation.types.e_tag_string.ETagString"]
    """<p>The Amazon S3 ETag of the object. Returned by <code>GetTableObjects</code> for validation and used to identify changes to the underlying data.</p>"""
    partition_values: NotRequired[
        "capo_lakeformation.types.partition_values_list.PartitionValuesList"
    ]
    """<p>A list of partition values for the object. A value must be specified for each partition key associated with the governed table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteObjectInput) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "partition_values" in value:
        import capo_lakeformation.types.partition_values_list

        out["PartitionValues"] = (
            capo_lakeformation.types.partition_values_list.serialize_json(
                value["partition_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteObjectInput:
    out: DeleteObjectInput = {}  # type: ignore[typeddict-item]
    if data.get("Uri") is not None:
        out["uri"] = data["Uri"]
    else:
        out["uri"] = ""
    if data.get("ETag") is not None:
        out["e_tag"] = data["ETag"]
    if data.get("PartitionValues") is not None:
        import capo_lakeformation.types.partition_values_list

        out["partition_values"] = (
            capo_lakeformation.types.partition_values_list.deserialize_json(
                data["PartitionValues"]
            )
        )
    return out
