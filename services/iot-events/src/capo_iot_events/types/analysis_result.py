"""Generated from Smithy shape ``com.amazonaws.iotevents#AnalysisResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.analysis_message
    import capo_iot_events.types.analysis_result_level
    import capo_iot_events.types.analysis_result_locations
    import capo_iot_events.types.analysis_type


class AnalysisResult(TypedDict, closed=True):
    type: NotRequired["capo_iot_events.types.analysis_type.AnalysisType"]
    """<p>The type of the analysis result. Analyses fall into the following types based on the validators used to generate the analysis result:</p> <ul> <li> <p> <code>supported-actions</code> - You must specify AWS IoT Events supported actions that work with other AWS services in a supported AWS Region.</p> </li> <li> <p> <code>service-limits</code> - Resources or API operations can't exceed service quotas (also known as limits). Update your detector model or request a quota increase.</p> </li> <li> <p> <code>structure</code> - The detector model must follow a structure that AWS IoT Events supports. </p> </li> <li> <p> <code>expression-syntax</code> - Your expression must follow the required syntax.</p> </li> <li> <p> <code>data-type</code> - Data types referenced in the detector model must be compatible.</p> </li> <li> <p> <code>referenced-data</code> - You must define the data referenced in your detector model before you can use the data.</p> </li> <li> <p> <code>referenced-resource</code> - Resources that the detector model uses must be available.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-analyze-api.html">Running detector model analyses</a> in the <i>AWS IoT Events Developer Guide</i>.</p>"""
    level: NotRequired[
        "capo_iot_events.types.analysis_result_level.AnalysisResultLevel"
    ]
    """<p>The severity level of the analysis result. Based on the severity level, analysis results fall into three general categories:</p> <ul> <li> <p> <code>INFO</code> - An information result tells you about a significant field in your detector model. This type of result usually doesn't require immediate action.</p> </li> <li> <p> <code>WARNING</code> - A warning result draws special attention to fields that might cause issues for your detector model. We recommend that you review warnings and take necessary actions before you use your detector model in production environments. Otherwise, the detector model might not work as expected.</p> </li> <li> <p> <code>ERROR</code> - An error result notifies you about a problem found in your detector model. You must fix all errors before you can publish your detector model.</p> </li> </ul>"""
    message: NotRequired["capo_iot_events.types.analysis_message.AnalysisMessage"]
    """<p>Contains additional information about the analysis result.</p>"""
    locations: NotRequired[
        "capo_iot_events.types.analysis_result_locations.AnalysisResultLocations"
    ]
    """<p>Contains one or more locations that you can use to locate the fields in your detector model that the analysis result references.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisResult) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "level" in value:
        import capo_iot_events.types.analysis_result_level

        out["level"] = capo_iot_events.types.analysis_result_level.serialize_json(
            value["level"]
        )
    if "message" in value:
        out["message"] = value["message"]
    if "locations" in value:
        import capo_iot_events.types.analysis_result_locations

        out["locations"] = (
            capo_iot_events.types.analysis_result_locations.serialize_json(
                value["locations"]
            )
        )
    return out


def deserialize_json(data: dict) -> AnalysisResult:
    out: AnalysisResult = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        out["type"] = data["type"]
    if data.get("level") is not None:
        import capo_iot_events.types.analysis_result_level

        out["level"] = capo_iot_events.types.analysis_result_level.deserialize_json(
            data["level"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("locations") is not None:
        import capo_iot_events.types.analysis_result_locations

        out["locations"] = (
            capo_iot_events.types.analysis_result_locations.deserialize_json(
                data["locations"]
            )
        )
    return out
