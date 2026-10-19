"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationAnalysisTemplate``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanrooms.types.account_id
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
    import capo_cleanrooms.types.resource_alias
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.synthetic_data_parameters
    import capo_cleanrooms.types.uuid


class CollaborationAnalysisTemplate(TypedDict, closed=True):
    id: "capo_cleanrooms.types.analysis_template_identifier.AnalysisTemplateIdentifier"
    """<p>The identifier of the analysis template.</p>"""
    arn: "capo_cleanrooms.types.analysis_template_arn.AnalysisTemplateArn"
    """<p>The Amazon Resource Name (ARN) of the analysis template.</p>"""
    collaboration_id: "capo_cleanrooms.types.uuid.UUID"
    """<p>A unique identifier for the collaboration that the analysis templates belong to. Currently accepts collaboration ID.</p>"""
    collaboration_arn: "capo_cleanrooms.types.collaboration_arn.CollaborationArn"
    """<p>The unique ARN for the analysis template’s associated collaboration.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the analysis template.</p>"""
    creator_account_id: "capo_cleanrooms.types.account_id.AccountId"
    """<p>The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.</p>"""
    name: "capo_cleanrooms.types.resource_alias.ResourceAlias"
    """<p>The name of the analysis template.</p>"""
    create_time: "datetime.datetime"
    """<p>The time that the analysis template within a collaboration was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The time that the analysis template in the collaboration was last updated.</p>"""
    schema: "capo_cleanrooms.types.analysis_schema.AnalysisSchema"
    """<p>The entire schema object.</p>"""
    format: "capo_cleanrooms.types.analysis_format.AnalysisFormat"
    """<p>The format of the analysis template in the collaboration.</p>"""
    source: NotRequired["capo_cleanrooms.types.analysis_source.AnalysisSource"]
    """<p>The source of the analysis template within a collaboration.</p>"""
    source_metadata: NotRequired[
        "capo_cleanrooms.types.analysis_source_metadata.AnalysisSourceMetadata"
    ]
    """<p> The source metadata for the collaboration analysis template.</p>"""
    analysis_parameters: NotRequired[
        "capo_cleanrooms.types.analysis_parameter_list.AnalysisParameterList"
    ]
    """<p>The analysis parameters that have been specified in the analysis template.</p>"""
    validations: NotRequired[
        "capo_cleanrooms.types.analysis_template_validation_status_detail_list.AnalysisTemplateValidationStatusDetailList"
    ]
    """<p>The validations that were performed.</p>"""
    error_message_configuration: NotRequired[
        "capo_cleanrooms.types.error_message_configuration.ErrorMessageConfiguration"
    ]
    """<p>The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to <code>DETAILED</code>, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.</p>"""
    synthetic_data_parameters: NotRequired[
        "capo_cleanrooms.types.synthetic_data_parameters.SyntheticDataParameters"
    ]
    """<p>The synthetic data generation parameters configured for this collaboration analysis template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationAnalysisTemplate) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["collaborationId"] = value["collaboration_id"]
    out["collaborationArn"] = value["collaboration_arn"]
    if "description" in value:
        out["description"] = value["description"]
    out["creatorAccountId"] = value["creator_account_id"]
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
    if "source" in value:
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


def deserialize_json(data: dict) -> CollaborationAnalysisTemplate:
    out: CollaborationAnalysisTemplate = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    else:
        out["collaboration_id"] = ""
    if data.get("collaborationArn") is not None:
        out["collaboration_arn"] = data["collaborationArn"]
    else:
        out["collaboration_arn"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("creatorAccountId") is not None:
        out["creator_account_id"] = data["creatorAccountId"]
    else:
        out["creator_account_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("createTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["create_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["createTime"]
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import capo_cleanrooms.types._prelude.timestamp

        out["update_time"] = capo_cleanrooms.types._prelude.timestamp.deserialize_json(
            data["updateTime"]
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("schema") is not None:
        import capo_cleanrooms.types.analysis_schema

        out["schema"] = capo_cleanrooms.types.analysis_schema.deserialize_json(
            data["schema"]
        )
    else:
        raise DeserializationError("CollaborationAnalysisTemplate.schema required")
    if data.get("format") is not None:
        import capo_cleanrooms.types.analysis_format

        out["format"] = capo_cleanrooms.types.analysis_format.deserialize_json(
            data["format"]
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_cleanrooms.types.analysis_format.AnalysisFormat", ""
        )
    if data.get("source") is not None:
        import capo_cleanrooms.types.analysis_source

        out["source"] = capo_cleanrooms.types.analysis_source.deserialize_json(
            data["source"]
        )
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


def redact_sensitive(value: CollaborationAnalysisTemplate) -> dict[str, Any]:
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
