"""Generated from Smithy shape ``com.amazonaws.b2bi#TransformerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_b2bi.types.created_date
    import capo_b2bi.types.edi_type
    import capo_b2bi.types.file_format
    import capo_b2bi.types.file_location
    import capo_b2bi.types.input_conversion
    import capo_b2bi.types.mapping
    import capo_b2bi.types.mapping_template
    import capo_b2bi.types.modified_date
    import capo_b2bi.types.output_conversion
    import capo_b2bi.types.sample_documents
    import capo_b2bi.types.transformer_id
    import capo_b2bi.types.transformer_name
    import capo_b2bi.types.transformer_status


class TransformerSummary(TypedDict, closed=True):
    transformer_id: "capo_b2bi.types.transformer_id.TransformerId"
    """<p>Returns the system-assigned unique identifier for the transformer.</p>"""
    name: "capo_b2bi.types.transformer_name.TransformerName"
    """<p>Returns the descriptive name for the transformer.</p>"""
    status: "capo_b2bi.types.transformer_status.TransformerStatus"
    """<p>Returns the state of the newly created transformer. The transformer can be either <code>active</code> or <code>inactive</code>. For the transformer to be used in a capability, its status must <code>active</code>.</p>"""
    created_at: "capo_b2bi.types.created_date.CreatedDate"
    """<p>Returns a timestamp indicating when the transformer was created. For example, <code>2023-07-20T19:58:44.624Z</code>.</p>"""
    modified_at: NotRequired["capo_b2bi.types.modified_date.ModifiedDate"]
    """<p>Returns a timestamp representing the date and time for the most recent change for the transformer object.</p>"""
    file_format: "capo_b2bi.types.file_format.FileFormat"
    """<p>Returns that the currently supported file formats for EDI transformations are <code>JSON</code> and <code>XML</code>.</p>"""
    mapping_template: "capo_b2bi.types.mapping_template.MappingTemplate"
    """<p>Returns the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.</p>"""
    edi_type: NotRequired["capo_b2bi.types.edi_type.EdiType"]
    """<p>Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.</p>"""
    sample_document: NotRequired["capo_b2bi.types.file_location.FileLocation"]
    """<p>Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.</p>"""
    input_conversion: NotRequired["capo_b2bi.types.input_conversion.InputConversion"]
    """<p>Returns a structure that contains the format options for the transformation.</p>"""
    mapping: NotRequired["capo_b2bi.types.mapping.Mapping"]
    """<p>Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).</p>"""
    output_conversion: NotRequired["capo_b2bi.types.output_conversion.OutputConversion"]
    """<p>Returns the <code>OutputConversion</code> object, which contains the format options for the outbound transformation.</p>"""
    sample_documents: NotRequired["capo_b2bi.types.sample_documents.SampleDocuments"]
    """<p>Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransformerSummary) -> dict:
    out: dict = {}
    out["transformerId"] = value["transformer_id"]
    out["name"] = value["name"]
    import capo_b2bi.types.transformer_status

    out["status"] = capo_b2bi.types.transformer_status.serialize_aws_json_1_0(
        value["status"]
    )
    import capo_b2bi.types.created_date

    out["createdAt"] = capo_b2bi.types.created_date.serialize_aws_json_1_0(
        value["created_at"]
    )
    if "modified_at" in value:
        import capo_b2bi.types.modified_date

        out["modifiedAt"] = capo_b2bi.types.modified_date.serialize_aws_json_1_0(
            value["modified_at"]
        )
    import capo_b2bi.types.file_format

    out["fileFormat"] = capo_b2bi.types.file_format.serialize_aws_json_1_0(
        value.get("file_format", "NOT_USED")
    )
    out["mappingTemplate"] = value.get("mapping_template", "NOT_USED")
    if "edi_type" in value:
        import capo_b2bi.types.edi_type

        out["ediType"] = capo_b2bi.types.edi_type.serialize_aws_json_1_0(
            value["edi_type"]
        )
    if "sample_document" in value:
        out["sampleDocument"] = value["sample_document"]
    if "input_conversion" in value:
        import capo_b2bi.types.input_conversion

        out["inputConversion"] = (
            capo_b2bi.types.input_conversion.serialize_aws_json_1_0(
                value["input_conversion"]
            )
        )
    if "mapping" in value:
        import capo_b2bi.types.mapping

        out["mapping"] = capo_b2bi.types.mapping.serialize_aws_json_1_0(
            value["mapping"]
        )
    if "output_conversion" in value:
        import capo_b2bi.types.output_conversion

        out["outputConversion"] = (
            capo_b2bi.types.output_conversion.serialize_aws_json_1_0(
                value["output_conversion"]
            )
        )
    if "sample_documents" in value:
        import capo_b2bi.types.sample_documents

        out["sampleDocuments"] = (
            capo_b2bi.types.sample_documents.serialize_aws_json_1_0(
                value["sample_documents"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TransformerSummary:
    out: TransformerSummary = {}  # type: ignore[typeddict-item]
    if data.get("transformerId") is not None:
        out["transformer_id"] = data["transformerId"]
    else:
        out["transformer_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_b2bi.types.transformer_status

        out["status"] = capo_b2bi.types.transformer_status.deserialize_aws_json_1_0(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_b2bi.types.transformer_status.TransformerStatus", ""
        )
    if data.get("createdAt") is not None:
        import capo_b2bi.types.created_date

        out["created_at"] = capo_b2bi.types.created_date.deserialize_aws_json_1_0(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("modifiedAt") is not None:
        import capo_b2bi.types.modified_date

        out["modified_at"] = capo_b2bi.types.modified_date.deserialize_aws_json_1_0(
            data["modifiedAt"]
        )
    if data.get("fileFormat") is not None:
        import capo_b2bi.types.file_format

        out["file_format"] = capo_b2bi.types.file_format.deserialize_aws_json_1_0(
            data["fileFormat"]
        )
    else:
        out["file_format"] = "NOT_USED"
    if data.get("mappingTemplate") is not None:
        out["mapping_template"] = data["mappingTemplate"]
    else:
        out["mapping_template"] = "NOT_USED"
    if data.get("ediType") is not None:
        import capo_b2bi.types.edi_type

        out["edi_type"] = capo_b2bi.types.edi_type.deserialize_aws_json_1_0(
            data["ediType"]
        )
    if data.get("sampleDocument") is not None:
        out["sample_document"] = data["sampleDocument"]
    if data.get("inputConversion") is not None:
        import capo_b2bi.types.input_conversion

        out["input_conversion"] = (
            capo_b2bi.types.input_conversion.deserialize_aws_json_1_0(
                data["inputConversion"]
            )
        )
    if data.get("mapping") is not None:
        import capo_b2bi.types.mapping

        out["mapping"] = capo_b2bi.types.mapping.deserialize_aws_json_1_0(
            data["mapping"]
        )
    if data.get("outputConversion") is not None:
        import capo_b2bi.types.output_conversion

        out["output_conversion"] = (
            capo_b2bi.types.output_conversion.deserialize_aws_json_1_0(
                data["outputConversion"]
            )
        )
    if data.get("sampleDocuments") is not None:
        import capo_b2bi.types.sample_documents

        out["sample_documents"] = (
            capo_b2bi.types.sample_documents.deserialize_aws_json_1_0(
                data["sampleDocuments"]
            )
        )
    return out
