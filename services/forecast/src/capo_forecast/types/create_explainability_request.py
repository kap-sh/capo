"""Generated from Smithy shape ``com.amazonaws.forecast#CreateExplainabilityRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_forecast.errors import DeserializationError

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.boolean
    import capo_forecast.types.data_source
    import capo_forecast.types.explainability_config
    import capo_forecast.types.local_date_time
    import capo_forecast.types.name
    import capo_forecast.types.schema
    import capo_forecast.types.tags


class CreateExplainabilityRequest(TypedDict, closed=True):
    explainability_name: "capo_forecast.types.name.Name"
    """<p>A unique name for the Explainability.</p>"""
    resource_arn: "capo_forecast.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Predictor or Forecast used to create the Explainability.</p>"""
    explainability_config: (
        "capo_forecast.types.explainability_config.ExplainabilityConfig"
    )
    """<p>The configuration settings that define the granularity of time series and time points for the Explainability.</p>"""
    data_source: NotRequired["capo_forecast.types.data_source.DataSource"]
    schema: NotRequired["capo_forecast.types.schema.Schema"]
    enable_visualization: NotRequired["capo_forecast.types.boolean.Boolean"]
    """<p>Create an Explainability visualization that is viewable within the Amazon Web Services console.</p>"""
    start_date_time: NotRequired["capo_forecast.types.local_date_time.LocalDateTime"]
    """<p>If <code>TimePointGranularity</code> is set to <code>SPECIFIC</code>, define the first point for the Explainability.</p> <p>Use the following timestamp format: yyyy-MM-ddTHH:mm:ss (example: 2015-01-01T20:00:00)</p>"""
    end_date_time: NotRequired["capo_forecast.types.local_date_time.LocalDateTime"]
    """<p>If <code>TimePointGranularity</code> is set to <code>SPECIFIC</code>, define the last time point for the Explainability.</p> <p>Use the following timestamp format: yyyy-MM-ddTHH:mm:ss (example: 2015-01-01T20:00:00)</p>"""
    tags: NotRequired["capo_forecast.types.tags.Tags"]
    """<p>Optional metadata to help you categorize and organize your resources. Each tag consists of a key and an optional value, both of which you define. Tag keys and values are case sensitive.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>For each resource, each tag key must be unique and each tag key must have one value.</p> </li> <li> <p>Maximum number of tags per resource: 50.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Accepted characters: all letters and numbers, spaces representable in UTF-8, and + - = . _ : / @. If your tagging schema is used across other services and resources, the character restrictions of those services also apply. </p> </li> <li> <p>Key prefixes cannot include any upper or lowercase combination of <code>aws:</code> or <code>AWS:</code>. Values can have this prefix. If a tag value has <code>aws</code> as its prefix but the key does not, Forecast considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of <code>aws</code> do not count against your tags per resource limit. You cannot edit or delete tag keys with this prefix.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExplainabilityRequest) -> dict:
    out: dict = {}
    out["ExplainabilityName"] = value["explainability_name"]
    out["ResourceArn"] = value["resource_arn"]
    import capo_forecast.types.explainability_config

    out["ExplainabilityConfig"] = (
        capo_forecast.types.explainability_config.serialize_aws_json_1_1(
            value["explainability_config"]
        )
    )
    if "data_source" in value:
        import capo_forecast.types.data_source

        out["DataSource"] = capo_forecast.types.data_source.serialize_aws_json_1_1(
            value["data_source"]
        )
    if "schema" in value:
        import capo_forecast.types.schema

        out["Schema"] = capo_forecast.types.schema.serialize_aws_json_1_1(
            value["schema"]
        )
    if "enable_visualization" in value:
        out["EnableVisualization"] = value["enable_visualization"]
    if "start_date_time" in value:
        out["StartDateTime"] = value["start_date_time"]
    if "end_date_time" in value:
        out["EndDateTime"] = value["end_date_time"]
    if "tags" in value:
        import capo_forecast.types.tags

        out["Tags"] = capo_forecast.types.tags.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExplainabilityRequest:
    out: CreateExplainabilityRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExplainabilityName") is not None:
        out["explainability_name"] = data["ExplainabilityName"]
    else:
        out["explainability_name"] = ""
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("ExplainabilityConfig") is not None:
        import capo_forecast.types.explainability_config

        out["explainability_config"] = (
            capo_forecast.types.explainability_config.deserialize_aws_json_1_1(
                data["ExplainabilityConfig"]
            )
        )
    else:
        raise DeserializationError(
            "CreateExplainabilityRequest.explainability_config required"
        )
    if data.get("DataSource") is not None:
        import capo_forecast.types.data_source

        out["data_source"] = capo_forecast.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    if data.get("Schema") is not None:
        import capo_forecast.types.schema

        out["schema"] = capo_forecast.types.schema.deserialize_aws_json_1_1(
            data["Schema"]
        )
    if data.get("EnableVisualization") is not None:
        out["enable_visualization"] = data["EnableVisualization"]
    if data.get("StartDateTime") is not None:
        out["start_date_time"] = data["StartDateTime"]
    if data.get("EndDateTime") is not None:
        out["end_date_time"] = data["EndDateTime"]
    if data.get("Tags") is not None:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.deserialize_aws_json_1_1(data["Tags"])
    return out


def redact_sensitive(value: CreateExplainabilityRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        import capo_forecast.types.tags

        out["tags"] = capo_forecast.types.tags.redact_sensitive(value["tags"])
    return out
