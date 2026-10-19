"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateAnalysisTemplateInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_format
    import capo_cleanrooms.types.analysis_parameter_list
    import capo_cleanrooms.types.analysis_schema
    import capo_cleanrooms.types.analysis_source
    import capo_cleanrooms.types.error_message_configuration
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.synthetic_data_parameters
    import capo_cleanrooms.types.table_alias
    import capo_cleanrooms.types.tag_map


class CreateAnalysisTemplateInput(TypedDict, closed=True):
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the analysis template.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The identifier for a membership resource.</p>"""
    name: "capo_cleanrooms.types.table_alias.TableAlias"
    """<p>The name of the analysis template.</p>"""
    format: "capo_cleanrooms.types.analysis_format.AnalysisFormat"
    """<p>The format of the analysis template.</p>"""
    source: "capo_cleanrooms.types.analysis_source.AnalysisSource"
    """<p>The information in the analysis template.</p>"""
    tags: NotRequired["capo_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""
    analysis_parameters: NotRequired[
        "capo_cleanrooms.types.analysis_parameter_list.AnalysisParameterList"
    ]
    """<p>The parameters of the analysis template.</p>"""
    schema: NotRequired["capo_cleanrooms.types.analysis_schema.AnalysisSchema"]
    error_message_configuration: NotRequired[
        "capo_cleanrooms.types.error_message_configuration.ErrorMessageConfiguration"
    ]
    """<p>The configuration that specifies the level of detail in error messages returned by analyses using this template. When set to <code>DETAILED</code>, error messages include more information to help troubleshoot issues with PySpark jobs. Detailed error messages may expose underlying data, including sensitive information. Recommended for faster troubleshooting in development and testing environments.</p>"""
    synthetic_data_parameters: NotRequired[
        "capo_cleanrooms.types.synthetic_data_parameters.SyntheticDataParameters"
    ]
    """<p>The parameters for generating synthetic data when running the analysis template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnalysisTemplateInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["name"] = value["name"]
    import capo_cleanrooms.types.analysis_format

    out["format"] = capo_cleanrooms.types.analysis_format.serialize_json(
        value["format"]
    )
    import capo_cleanrooms.types.analysis_source

    out["source"] = capo_cleanrooms.types.analysis_source.serialize_json(
        value["source"]
    )
    if "tags" in value:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.serialize_json(value["tags"])
    if "analysis_parameters" in value:
        import capo_cleanrooms.types.analysis_parameter_list

        out["analysisParameters"] = (
            capo_cleanrooms.types.analysis_parameter_list.serialize_json(
                value["analysis_parameters"]
            )
        )
    if "schema" in value:
        import capo_cleanrooms.types.analysis_schema

        out["schema"] = capo_cleanrooms.types.analysis_schema.serialize_json(
            value["schema"]
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


def deserialize_json(data: dict) -> CreateAnalysisTemplateInput:
    out: CreateAnalysisTemplateInput = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
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
    else:
        import capo_cleanrooms.types._unknown

        out["source"] = capo_cleanrooms.types._unknown.UnknownUnionMember("")
    if data.get("tags") is not None:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    if data.get("analysisParameters") is not None:
        import capo_cleanrooms.types.analysis_parameter_list

        out["analysis_parameters"] = (
            capo_cleanrooms.types.analysis_parameter_list.deserialize_json(
                data["analysisParameters"]
            )
        )
    if data.get("schema") is not None:
        import capo_cleanrooms.types.analysis_schema

        out["schema"] = capo_cleanrooms.types.analysis_schema.deserialize_json(
            data["schema"]
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


def redact_sensitive(value: CreateAnalysisTemplateInput) -> dict[str, Any]:
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
