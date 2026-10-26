"""Generated from Smithy shape ``com.amazonaws.b2bi#CreateStarterMappingTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.mapping_type
    import capo_b2bi.types.s3_location
    import capo_b2bi.types.template_details


class CreateStarterMappingTemplateRequest(TypedDict, closed=True):
    output_sample_location: NotRequired["capo_b2bi.types.s3_location.S3Location"]
    """<p>Specify the location of the sample EDI file that is used to generate the mapping template.</p>"""
    mapping_type: "capo_b2bi.types.mapping_type.MappingType"
    """<p>Specify the format for the mapping template: either JSONATA or XSLT.</p>"""
    template_details: "capo_b2bi.types.template_details.TemplateDetails"
    """<p> Describes the details needed for generating the template. Specify the X12 transaction set and version for which the template is used: currently, we only support X12. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateStarterMappingTemplateRequest) -> dict:
    out: dict = {}
    if "output_sample_location" in value:
        import capo_b2bi.types.s3_location

        out["outputSampleLocation"] = (
            capo_b2bi.types.s3_location.serialize_aws_json_1_0(
                value["output_sample_location"]
            )
        )
    import capo_b2bi.types.mapping_type

    out["mappingType"] = capo_b2bi.types.mapping_type.serialize_aws_json_1_0(
        value["mapping_type"]
    )
    import capo_b2bi.types.template_details

    out["templateDetails"] = capo_b2bi.types.template_details.serialize_aws_json_1_0(
        value["template_details"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateStarterMappingTemplateRequest:
    out: CreateStarterMappingTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("outputSampleLocation") is not None:
        import capo_b2bi.types.s3_location

        out["output_sample_location"] = (
            capo_b2bi.types.s3_location.deserialize_aws_json_1_0(
                data["outputSampleLocation"]
            )
        )
    if data.get("mappingType") is not None:
        import capo_b2bi.types.mapping_type

        out["mapping_type"] = capo_b2bi.types.mapping_type.deserialize_aws_json_1_0(
            data["mappingType"]
        )
    else:
        import typing

        out["mapping_type"] = typing.cast(
            "capo_b2bi.types.mapping_type.MappingType", ""
        )
    if data.get("templateDetails") is not None:
        import capo_b2bi.types.template_details

        out["template_details"] = (
            capo_b2bi.types.template_details.deserialize_aws_json_1_0(
                data["templateDetails"]
            )
        )
    else:
        out["template_details"] = {"$unknown": {"name": ""}}
    return out
