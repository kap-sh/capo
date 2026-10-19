"""Generated from Smithy shape ``com.amazonaws.databrew#Dataset``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.account_id
    import capo_databrew.types.arn
    import capo_databrew.types.created_by
    import capo_databrew.types.dataset_name
    import capo_databrew.types.date
    import capo_databrew.types.format_options
    import capo_databrew.types.input
    import capo_databrew.types.input_format
    import capo_databrew.types.last_modified_by
    import capo_databrew.types.path_options
    import capo_databrew.types.source
    import capo_databrew.types.tag_map


class Dataset(TypedDict, closed=True):
    account_id: NotRequired["capo_databrew.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account that owns the dataset.</p>"""
    created_by: NotRequired["capo_databrew.types.created_by.CreatedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who created the dataset.</p>"""
    create_date: NotRequired["capo_databrew.types.date.Date"]
    """<p>The date and time that the dataset was created.</p>"""
    name: "capo_databrew.types.dataset_name.DatasetName"
    """<p>The unique name of the dataset.</p>"""
    format: NotRequired["capo_databrew.types.input_format.InputFormat"]
    """<p>The file format of a dataset that is created from an Amazon S3 file or folder.</p>"""
    format_options: NotRequired["capo_databrew.types.format_options.FormatOptions"]
    """<p>A set of options that define how DataBrew interprets the data in the dataset.</p>"""
    input: "capo_databrew.types.input.Input"
    """<p>Information on how DataBrew can find the dataset, in either the Glue Data Catalog or Amazon S3.</p>"""
    last_modified_date: NotRequired["capo_databrew.types.date.Date"]
    """<p>The last modification date and time of the dataset.</p>"""
    last_modified_by: NotRequired["capo_databrew.types.last_modified_by.LastModifiedBy"]
    """<p>The Amazon Resource Name (ARN) of the user who last modified the dataset.</p>"""
    source: NotRequired["capo_databrew.types.source.Source"]
    """<p>The location of the data for the dataset, either Amazon S3 or the Glue Data Catalog.</p>"""
    path_options: NotRequired["capo_databrew.types.path_options.PathOptions"]
    """<p>A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.</p>"""
    tags: NotRequired["capo_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags that have been applied to the dataset.</p>"""
    resource_arn: NotRequired["capo_databrew.types.arn.Arn"]
    """<p>The unique Amazon Resource Name (ARN) for the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dataset) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "create_date" in value:
        import capo_databrew.types.date

        out["CreateDate"] = capo_databrew.types.date.serialize_json(
            value["create_date"]
        )
    out["Name"] = value["name"]
    if "format" in value:
        import capo_databrew.types.input_format

        out["Format"] = capo_databrew.types.input_format.serialize_json(value["format"])
    if "format_options" in value:
        import capo_databrew.types.format_options

        out["FormatOptions"] = capo_databrew.types.format_options.serialize_json(
            value["format_options"]
        )
    import capo_databrew.types.input

    out["Input"] = capo_databrew.types.input.serialize_json(value["input"])
    if "last_modified_date" in value:
        import capo_databrew.types.date

        out["LastModifiedDate"] = capo_databrew.types.date.serialize_json(
            value["last_modified_date"]
        )
    if "last_modified_by" in value:
        out["LastModifiedBy"] = value["last_modified_by"]
    if "source" in value:
        import capo_databrew.types.source

        out["Source"] = capo_databrew.types.source.serialize_json(value["source"])
    if "path_options" in value:
        import capo_databrew.types.path_options

        out["PathOptions"] = capo_databrew.types.path_options.serialize_json(
            value["path_options"]
        )
    if "tags" in value:
        import capo_databrew.types.tag_map

        out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> Dataset:
    out: Dataset = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("CreateDate") is not None:
        import capo_databrew.types.date

        out["create_date"] = capo_databrew.types.date.deserialize_json(
            data["CreateDate"]
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Format") is not None:
        import capo_databrew.types.input_format

        out["format"] = capo_databrew.types.input_format.deserialize_json(
            data["Format"]
        )
    if data.get("FormatOptions") is not None:
        import capo_databrew.types.format_options

        out["format_options"] = capo_databrew.types.format_options.deserialize_json(
            data["FormatOptions"]
        )
    if data.get("Input") is not None:
        import capo_databrew.types.input

        out["input"] = capo_databrew.types.input.deserialize_json(data["Input"])
    else:
        raise DeserializationError("Dataset.input required")
    if data.get("LastModifiedDate") is not None:
        import capo_databrew.types.date

        out["last_modified_date"] = capo_databrew.types.date.deserialize_json(
            data["LastModifiedDate"]
        )
    if data.get("LastModifiedBy") is not None:
        out["last_modified_by"] = data["LastModifiedBy"]
    if data.get("Source") is not None:
        import capo_databrew.types.source

        out["source"] = capo_databrew.types.source.deserialize_json(data["Source"])
    if data.get("PathOptions") is not None:
        import capo_databrew.types.path_options

        out["path_options"] = capo_databrew.types.path_options.deserialize_json(
            data["PathOptions"]
        )
    if data.get("Tags") is not None:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    return out
