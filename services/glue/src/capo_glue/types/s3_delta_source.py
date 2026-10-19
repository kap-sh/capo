"""Generated from Smithy shape ``com.amazonaws.glue#S3DeltaSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.additional_options
    import capo_glue.types.enclosed_in_string_properties
    import capo_glue.types.glue_schemas
    import capo_glue.types.node_name
    import capo_glue.types.s3_direct_source_additional_options


class S3DeltaSource(TypedDict, closed=True):
    name: "capo_glue.types.node_name.NodeName"
    """<p>The name of the Delta Lake source.</p>"""
    paths: "capo_glue.types.enclosed_in_string_properties.EnclosedInStringProperties"
    """<p>A list of the Amazon S3 paths to read from.</p>"""
    additional_delta_options: NotRequired[
        "capo_glue.types.additional_options.AdditionalOptions"
    ]
    """<p>Specifies additional connection options.</p>"""
    additional_options: NotRequired[
        "capo_glue.types.s3_direct_source_additional_options.S3DirectSourceAdditionalOptions"
    ]
    """<p>Specifies additional options for the connector.</p>"""
    output_schemas: NotRequired["capo_glue.types.glue_schemas.GlueSchemas"]
    """<p>Specifies the data schema for the Delta Lake source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3DeltaSource) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_glue.types.enclosed_in_string_properties

    out["Paths"] = capo_glue.types.enclosed_in_string_properties.serialize_aws_json_1_1(
        value["paths"]
    )
    if "additional_delta_options" in value:
        import capo_glue.types.additional_options

        out["AdditionalDeltaOptions"] = (
            capo_glue.types.additional_options.serialize_aws_json_1_1(
                value["additional_delta_options"]
            )
        )
    if "additional_options" in value:
        import capo_glue.types.s3_direct_source_additional_options

        out["AdditionalOptions"] = (
            capo_glue.types.s3_direct_source_additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "output_schemas" in value:
        import capo_glue.types.glue_schemas

        out["OutputSchemas"] = capo_glue.types.glue_schemas.serialize_aws_json_1_1(
            value["output_schemas"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> S3DeltaSource:
    out: S3DeltaSource = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Paths") is not None:
        import capo_glue.types.enclosed_in_string_properties

        out["paths"] = (
            capo_glue.types.enclosed_in_string_properties.deserialize_aws_json_1_1(
                data["Paths"]
            )
        )
    else:
        out["paths"] = []
    if data.get("AdditionalDeltaOptions") is not None:
        import capo_glue.types.additional_options

        out["additional_delta_options"] = (
            capo_glue.types.additional_options.deserialize_aws_json_1_1(
                data["AdditionalDeltaOptions"]
            )
        )
    if data.get("AdditionalOptions") is not None:
        import capo_glue.types.s3_direct_source_additional_options

        out["additional_options"] = (
            capo_glue.types.s3_direct_source_additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if data.get("OutputSchemas") is not None:
        import capo_glue.types.glue_schemas

        out["output_schemas"] = capo_glue.types.glue_schemas.deserialize_aws_json_1_1(
            data["OutputSchemas"]
        )
    return out
