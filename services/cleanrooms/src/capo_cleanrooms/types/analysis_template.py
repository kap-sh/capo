"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisTemplate``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.analysis_format
    import capo_cleanrooms.types.analysis_parameter_list
    import capo_cleanrooms.types.analysis_schema
    import capo_cleanrooms.types.analysis_source
    import capo_cleanrooms.types.analysis_source_metadata
    import capo_cleanrooms.types.analysis_template_arn
    import capo_cleanrooms.types.analysis_template_identifier
    import capo_cleanrooms.types.analysis_template_validation_status_detail_list
    import capo_cleanrooms.types.collaboration_arn
    import capo_cleanrooms.types.error_message_configuration
    import capo_cleanrooms.types.membership_arn
    import capo_cleanrooms.types.resource_alias
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.synthetic_data_parameters
    import capo_cleanrooms.types.uuid


class AnalysisTemplate(TypedDict, closed=True):
    id: "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier"
    """<p>The identifier for the analysis template.</p>"""
    arn: "capo_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    """<p>The Amazon Resource Name (ARN) of the analysis template.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique ID for the associated collaboration of the analysis template.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique ARN for the analysis template’s associated collaboration.</p>"""
    membership_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>The identifier of a member who created the analysis template.</p>"""
    membership_arn: "capo_cleanrooms.types.membership_arn.MembershipArn"
    """<p>The Amazon Resource Name (ARN) of the member who created the analysis template.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the analysis template.</p>"""
    name: "capo_cleanrooms.types.resource_alias.ResourceAlias"
    """<p>The name of the analysis template.</p>"""
    create_time: "datetime.datetime"
    """<p>The time that the analysis template was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time that the analysis template was last updated.</p>"""
    schema: "capo_cleanrooms.types.analysis_schema.AnalysisSchema"
    """<p>The entire schema object.</p>"""
    format: "capo_cleanrooms.types.analysis_format.AnalysisFormat"
    """<p>The format of the analysis template.</p>"""
    source: "capo_cleanrooms.types.analysis_source.AnalysisSource"
    """<p>The source of the analysis template.</p>"""
    source_metadata: NotRequired[
        "capo_cleanrooms.types.analysis_source_metadata.AnalysisSourceMetadata"
    ]
    """<p> The source metadata for the analysis template.</p>"""
    analysis_parameters: NotRequired[
        "capo_cleanrooms.types.analysis_parameter_list.AnalysisParameterList"
    ]
    """<p>The parameters of the analysis template.</p>"""
    validations: NotRequired[
        "capo_cleanrooms.types.analysis_template_validation_status_detail_list.AnalysisTemplateValidationStatusDetailList"
    ]
    """<p>Information about the validations performed on the analysis template.</p>"""
    error_message_configuration: NotRequired[
        "capo_cleanrooms.types.error_message_configuration.ErrorMessageConfiguration"
    ]
    """<p>The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to <code>DETAILED</code>, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.</p>"""
    synthetic_data_parameters: NotRequired[
        "capo_cleanrooms.types.synthetic_data_parameters.SyntheticDataParameters"
    ]
    """<p>The parameters used to generate synthetic data for this analysis template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisTemplate) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    out["membershipId"] = value["membership_id"]
    out["membershipArn"] = value["membership_arn"]
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    import capo_cleanrooms.types._prelude.timestamp

    out["createTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanrooms.types._prelude.timestamp

    out["updateTime"] = capo_cleanrooms.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    import capo_cleanrooms.types.analysis_schema

    out["schema"] = capo_cleanrooms.types.analysis_schema.serialize_json(
        value["schema"]
    )
    import capo_cleanrooms.types.analysis_format

    out["format"] = capo_cleanrooms.types.analysis_format.serialize_json(
        value["format"]
    )
    import capo_cleanrooms.types.analysis_source

    out["source"] = capo_cleanrooms.types.analysis_source.serialize_json(
        value["source"]
    )
    if "source_metadata" in value:
        import capo_cleanrooms.types.analysis_source_metadata

        out["sourceMetadata"] = (
            capo_cleanrooms.types.analysis_source_metadata.serialize_json(
                value["source_metadata"]
            )
        )
    if "analysis_parameters" in value:
        import capo_cleanrooms.types.analysis_parameter_list

        out["analysisParameters"] = (
            capo_cleanrooms.types.analysis_parameter_list.serialize_json(
                value["analysis_parameters"]
            )
        )
    if "validations" in value:
        import capo_cleanrooms.types.analysis_template_validation_status_detail_list

        out["validations"] = (
            capo_cleanrooms.types.analysis_template_validation_status_detail_list.serialize_json(
                value["validations"]
            )
        )
    if "error_message_configuration" in value:
        import capo_cleanrooms.types.error_message_configuration

        out["errorMessageConfiguration"] = (
            capo_cleanrooms.types.error_message_configuration.serialize_json(
                value["error_message_configuration"]
            )
        )
    if "synthetic_data_parameters" in value:
        import capo_cleanrooms.types.synthetic_data_parameters

        out["syntheticDataParameters"] = (
            capo_cleanrooms.types.synthetic_data_parameters.serialize_json(
                value["synthetic_data_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisTemplate:
    out: AnalysisTemplate = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("AnalysisTemplate.id required")
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AnalysisTemplate.arn required")
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    else:
        raise DeserializationError("AnalysisTemplate.collaboration_id required")
    if data.get("collaborationArn") is not None:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        raise DeserializationError("AnalysisTemplate.collaboration_arn required")
    if data.get("membershipId") is not None:
        out["membership_id"] = data["membershipId"]
    else:
        raise DeserializationError("AnalysisTemplate.membership_id required")
    if data.get("membershipArn") is not None:
        out["membership_arn"] = data["membershipArn"]
    else:
        raise DeserializationError("AnalysisTemplate.membership_arn required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AnalysisTemplate.name required")
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        raise DeserializationError("AnalysisTemplate.create_time required")
    if data.get("updateTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        raise DeserializationError("AnalysisTemplate.update_time required")
    if data.get("schema") is not None:
        import capo_cleanrooms.types.analysis_schema

        out["schema"] = capo_cleanrooms.types.analysis_schema.deserialize_json(
            data["schema"]
        )
    else:
        raise DeserializationError("AnalysisTemplate.schema required")
    if data.get("format") is not None:
        import capo_cleanrooms.types.analysis_format

        out["format"] = capo_cleanrooms.types.analysis_format.deserialize_json(
            data["format"]
        )
    else:
        raise DeserializationError("AnalysisTemplate.format required")
    if data.get("source") is not None:
        import capo_cleanrooms.types.analysis_source

        out["source"] = capo_cleanrooms.types.analysis_source.deserialize_json(
            data["source"]
        )
    else:
        raise DeserializationError("AnalysisTemplate.source required")
    if data.get("sourceMetadata") is not None:
        import capo_cleanrooms.types.analysis_source_metadata

        out["source_metadata"] = (
            capo_cleanrooms.types.analysis_source_metadata.deserialize_json(
                data["sourceMetadata"]
            )
        )
    if data.get("analysisParameters") is not None:
        import capo_cleanrooms.types.analysis_parameter_list

        out["analysis_parameters"] = (
            capo_cleanrooms.types.analysis_parameter_list.deserialize_json(
                data["analysisParameters"]
            )
        )
    if data.get("validations") is not None:
        import capo_cleanrooms.types.analysis_template_validation_status_detail_list

        out["validations"] = (
            capo_cleanrooms.types.analysis_template_validation_status_detail_list.deserialize_json(
                data["validations"]
            )
        )
    if data.get("errorMessageConfiguration") is not None:
        import capo_cleanrooms.types.error_message_configuration

        out["error_message_configuration"] = (
            capo_cleanrooms.types.error_message_configuration.deserialize_json(
                data["errorMessageConfiguration"]
            )
        )
    if data.get("syntheticDataParameters") is not None:
        import capo_cleanrooms.types.synthetic_data_parameters

        out["synthetic_data_parameters"] = (
            capo_cleanrooms.types.synthetic_data_parameters.deserialize_json(
                data["syntheticDataParameters"]
            )
        )
    return out


def redact_sensitive(value: AnalysisTemplate) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source" in value:
        import capo_cleanrooms.types.analysis_source

        out["source"] = capo_cleanrooms.types.analysis_source.redact_sensitive(
            value["source"]
        )
    if "analysis_parameters" in value:
        import capo_cleanrooms.types.analysis_parameter_list

        out["analysis_parameters"] = (
            capo_cleanrooms.types.analysis_parameter_list.redact_sensitive(
                value["analysis_parameters"]
            )
        )
    return out
