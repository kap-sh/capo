"""Generated from Smithy shape ``com.amazonaws.databrew#CreateDatasetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_databrew.errors import DeserializationError

if TYPE_CHECKING:
    import capo_databrew.types.dataset_name
    import capo_databrew.types.format_options
    import capo_databrew.types.input
    import capo_databrew.types.input_format
    import capo_databrew.types.path_options
    import capo_databrew.types.tag_map


class CreateDatasetRequest(TypedDict, closed=True):
    name: "capo_databrew.types.dataset_name.DatasetName"
    """<p>The name of the dataset to be created. Valid characters are alphanumeric (A-Z, a-z, 0-9), hyphen (-), period (.), and space.</p>"""
    format: NotRequired["capo_databrew.types.input_format.InputFormat"]
    """<p>The file format of a dataset that is created from an Amazon S3 file or folder.</p>"""
    format_options: NotRequired["capo_databrew.types.format_options.FormatOptions"]
    input: "capo_databrew.types.input.Input"
    path_options: NotRequired["capo_databrew.types.path_options.PathOptions"]
    """<p>A set of options that defines how DataBrew interprets an Amazon S3 path of the dataset.</p>"""
    tags: NotRequired["capo_databrew.types.tag_map.TagMap"]
    """<p>Metadata tags to apply to this dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetRequest) -> dict:
    out: dict = {}
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
    if "path_options" in value:
        import capo_databrew.types.path_options

        out["PathOptions"] = capo_databrew.types.path_options.serialize_json(
            value["path_options"]
        )
    if "tags" in value:
        import capo_databrew.types.tag_map

        out["Tags"] = capo_databrew.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDatasetRequest:
    out: CreateDatasetRequest = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("CreateDatasetRequest.input required")
    if data.get("PathOptions") is not None:
        import capo_databrew.types.path_options

        out["path_options"] = capo_databrew.types.path_options.deserialize_json(
            data["PathOptions"]
        )
    if data.get("Tags") is not None:
        import capo_databrew.types.tag_map

        out["tags"] = capo_databrew.types.tag_map.deserialize_json(data["Tags"])
    return out
