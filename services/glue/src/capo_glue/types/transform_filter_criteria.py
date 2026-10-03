"""Generated from Smithy shape ``com.amazonaws.glue#TransformFilterCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glue_version_string
    import capo_glue.types.name_string
    import capo_glue.types.timestamp
    import capo_glue.types.transform_schema
    import capo_glue.types.transform_status_type
    import capo_glue.types.transform_type


class TransformFilterCriteria(TypedDict, closed=True):
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>A unique transform name that is used to filter the machine learning transforms.</p>"""
    transform_type: NotRequired["capo_glue.types.transform_type.TransformType"]
    """<p>The type of machine learning transform that is used to filter the machine learning transforms.</p>"""
    status: NotRequired["capo_glue.types.transform_status_type.TransformStatusType"]
    """<p>Filters the list of machine learning transforms by the last known status of the transforms (to indicate whether a transform can be used or not). One of "NOT_READY", "READY", or "DELETING".</p>"""
    glue_version: NotRequired["capo_glue.types.glue_version_string.GlueVersionString"]
    """<p>This value determines which version of Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see <a href="https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions">Glue Versions</a> in the developer guide.</p>"""
    created_before: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time and date before which the transforms were created.</p>"""
    created_after: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>The time and date after which the transforms were created.</p>"""
    last_modified_before: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>Filter on transforms last modified before this date.</p>"""
    last_modified_after: NotRequired["capo_glue.types.timestamp.Timestamp"]
    """<p>Filter on transforms last modified after this date.</p>"""
    schema: NotRequired["capo_glue.types.transform_schema.TransformSchema"]
    """<p>Filters on datasets with a specific schema. The <code>Map<Column, Type></code> object is an array of key-value pairs representing the schema this transform accepts, where <code>Column</code> is the name of a column, and <code>Type</code> is the type of the data such as an integer or string. Has an upper bound of 100 columns.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformFilterCriteria) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "transform_type" in value:
        import capo_glue.types.transform_type

        out["TransformType"] = capo_glue.types.transform_type.serialize_aws_json_1_1(
            value["transform_type"]
        )
    if "status" in value:
        import capo_glue.types.transform_status_type

        out["Status"] = capo_glue.types.transform_status_type.serialize_aws_json_1_1(
            value["status"]
        )
    if "glue_version" in value:
        out["GlueVersion"] = value["glue_version"]
    if "created_before" in value:
        import capo_glue.types.timestamp

        out["CreatedBefore"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "created_after" in value:
        import capo_glue.types.timestamp

        out["CreatedAfter"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "last_modified_before" in value:
        import capo_glue.types.timestamp

        out["LastModifiedBefore"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_before"]
        )
    if "last_modified_after" in value:
        import capo_glue.types.timestamp

        out["LastModifiedAfter"] = capo_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_modified_after"]
        )
    if "schema" in value:
        import capo_glue.types.transform_schema

        out["Schema"] = capo_glue.types.transform_schema.serialize_aws_json_1_1(
            value["schema"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TransformFilterCriteria:
    out: TransformFilterCriteria = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("TransformType") is not None:
        import capo_glue.types.transform_type

        out["transform_type"] = capo_glue.types.transform_type.deserialize_aws_json_1_1(
            data["TransformType"]
        )
    if data.get("Status") is not None:
        import capo_glue.types.transform_status_type

        out["status"] = capo_glue.types.transform_status_type.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("GlueVersion") is not None:
        out["glue_version"] = data["GlueVersion"]
    if data.get("CreatedBefore") is not None:
        import capo_glue.types.timestamp

        out["created_before"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedBefore"]
        )
    if data.get("CreatedAfter") is not None:
        import capo_glue.types.timestamp

        out["created_after"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAfter"]
        )
    if data.get("LastModifiedBefore") is not None:
        import capo_glue.types.timestamp

        out["last_modified_before"] = (
            capo_glue.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedBefore"]
            )
        )
    if data.get("LastModifiedAfter") is not None:
        import capo_glue.types.timestamp

        out["last_modified_after"] = capo_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastModifiedAfter"]
        )
    if data.get("Schema") is not None:
        import capo_glue.types.transform_schema

        out["schema"] = capo_glue.types.transform_schema.deserialize_aws_json_1_1(
            data["Schema"]
        )
    return out
