"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisSegmentExtractedInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.extraction_definition_display_label
    import capo_connect.types.extraction_definition_id
    import capo_connect.types.extraction_definition_name
    import capo_connect.types.real_time_contact_analysis_extracted_information_failure_code
    import capo_connect.types.real_time_contact_analysis_extracted_information_values


class RealTimeContactAnalysisSegmentExtractedInformation(TypedDict, closed=True):
    extraction_definition_id: (
        "capo_connect.types.extraction_definition_id.ExtractionDefinitionId"
    )
    """<p>The identifier of the extraction definition that produced this result.</p>"""
    extraction_definition_name: (
        "capo_connect.types.extraction_definition_name.ExtractionDefinitionName"
    )
    """<p>The name of the extraction definition that produced this result.</p>"""
    extraction_definition_display_label: NotRequired[
        "capo_connect.types.extraction_definition_display_label.ExtractionDefinitionDisplayLabel"
    ]
    """<p>The display label of the extraction definition that produced this result.</p>"""
    extracted_values: NotRequired[
        "capo_connect.types.real_time_contact_analysis_extracted_information_values.RealTimeContactAnalysisExtractedInformationValues"
    ]
    """<p>The list of values extracted from the conversation for this extraction definition. This field is empty when a <code>FailureCode</code> is present.</p>"""
    failure_code: NotRequired[
        "capo_connect.types.real_time_contact_analysis_extracted_information_failure_code.RealTimeContactAnalysisExtractedInformationFailureCode"
    ]
    """<p>If the information failed to be extracted, one of the following failure codes occurs:</p> <ul> <li> <p> <code>QUOTA_EXCEEDED</code>: The number of concurrent analytics jobs reached your service quota.</p> </li> <li> <p> <code>INSUFFICIENT_CONVERSATION_CONTENT</code>: Information extraction requires a conversation with at least one turn from each participant.</p> </li> <li> <p> <code>FAILED_SAFETY_GUIDELINES</code>: The extracted information cannot be provided because it failed to meet system safety guidelines.</p> </li> <li> <p> <code>INTERNAL_ERROR</code>: Internal system error.</p> </li> <li> <p> <code>MAX_PACKAGE_FEATURE_ONLY</code>: Information extraction is only available in Amazon Connect Customer instances.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisSegmentExtractedInformation) -> dict:
    out: dict = {}
    out["ExtractionDefinitionId"] = value["extraction_definition_id"]
    out["ExtractionDefinitionName"] = value["extraction_definition_name"]
    if "extraction_definition_display_label" in value:
        out["ExtractionDefinitionDisplayLabel"] = value[
            "extraction_definition_display_label"
        ]
    if "extracted_values" in value:
        import capo_connect.types.real_time_contact_analysis_extracted_information_values

        out["ExtractedValues"] = (
            capo_connect.types.real_time_contact_analysis_extracted_information_values.serialize_json(
                value["extracted_values"]
            )
        )
    if "failure_code" in value:
        import capo_connect.types.real_time_contact_analysis_extracted_information_failure_code

        out["FailureCode"] = (
            capo_connect.types.real_time_contact_analysis_extracted_information_failure_code.serialize_json(
                value["failure_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> RealTimeContactAnalysisSegmentExtractedInformation:
    out: RealTimeContactAnalysisSegmentExtractedInformation = {}  # type: ignore[typeddict-item]
    if data.get("ExtractionDefinitionId") is not None:
        out["extraction_definition_id"] = data["ExtractionDefinitionId"]
    else:
        out["extraction_definition_id"] = ""
    if data.get("ExtractionDefinitionName") is not None:
        out["extraction_definition_name"] = data["ExtractionDefinitionName"]
    else:
        out["extraction_definition_name"] = ""
    if data.get("ExtractionDefinitionDisplayLabel") is not None:
        out["extraction_definition_display_label"] = data[
            "ExtractionDefinitionDisplayLabel"
        ]
    if data.get("ExtractedValues") is not None:
        import capo_connect.types.real_time_contact_analysis_extracted_information_values

        out["extracted_values"] = (
            capo_connect.types.real_time_contact_analysis_extracted_information_values.deserialize_json(
                data["ExtractedValues"]
            )
        )
    if data.get("FailureCode") is not None:
        import capo_connect.types.real_time_contact_analysis_extracted_information_failure_code

        out["failure_code"] = (
            capo_connect.types.real_time_contact_analysis_extracted_information_failure_code.deserialize_json(
                data["FailureCode"]
            )
        )
    return out
