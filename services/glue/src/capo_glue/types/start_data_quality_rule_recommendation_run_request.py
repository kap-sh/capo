"""Generated from Smithy shape ``com.amazonaws.glue#StartDataQualityRuleRecommendationRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.data_quality_rule_recommendation_run_additional_run_options
    import capo_glue.types.data_source
    import capo_glue.types.hash_string
    import capo_glue.types.name_string
    import capo_glue.types.nullable_integer
    import capo_glue.types.recommendation_mode
    import capo_glue.types.role_string
    import capo_glue.types.timeout


class StartDataQualityRuleRecommendationRunRequest(TypedDict, closed=True):
    data_source: "capo_glue.types.data_source.DataSource"
    """<p>The data source (Glue table) associated with this run.</p>"""
    role: "capo_glue.types.role_string.RoleString"
    """<p>The IAM role that Glue assumes to access resources for the run.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/glue/latest/dg/data-quality-authorization.html">Configure IAM permissions for Glue Data Quality</a>.</p>"""
    number_of_workers: NotRequired["capo_glue.types.nullable_integer.NullableInteger"]
    """<p>The number of <code>G.1X</code> workers to be used in the run. The default is 5.</p>"""
    timeout: NotRequired["capo_glue.types.timeout.Timeout"]
    """<p>The timeout for a run in minutes. This is the maximum time that a run can consume resources before it is terminated and enters <code>TIMEOUT</code> status. The default is 2,880 minutes (48 hours).</p>"""
    created_ruleset_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>A name for the ruleset.</p>"""
    data_quality_security_configuration: NotRequired[
        "capo_glue.types.name_string.NameString"
    ]
    """<p>The name of the security configuration created with the data quality encryption option.</p>"""
    client_token: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>Used for idempotency and is recommended to be set to a random ID (such as a UUID) to avoid creating or starting multiple instances of the same resource.</p>"""
    additional_run_options: NotRequired[
        "capo_glue.types.data_quality_rule_recommendation_run_additional_run_options.DataQualityRuleRecommendationRunAdditionalRunOptions"
    ]
    """<p>Additional run options you can specify for a recommendation run.</p>"""
    recommendation_mode: NotRequired[
        "capo_glue.types.recommendation_mode.RecommendationMode"
    ]
    """<p>The mode that Glue Data Quality uses to recommend rules.</p> <p>The default is <code>BASIC</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartDataQualityRuleRecommendationRunRequest) -> dict:
    out: dict = {}
    import capo_glue.types.data_source

    out["DataSource"] = capo_glue.types.data_source.serialize_aws_json_1_1(
        value["data_source"]
    )
    out["Role"] = value["role"]
    if "number_of_workers" in value:
        out["NumberOfWorkers"] = value["number_of_workers"]
    if "timeout" in value:
        out["Timeout"] = value["timeout"]
    if "created_ruleset_name" in value:
        out["CreatedRulesetName"] = value["created_ruleset_name"]
    if "data_quality_security_configuration" in value:
        out["DataQualitySecurityConfiguration"] = value[
            "data_quality_security_configuration"
        ]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "additional_run_options" in value:
        import capo_glue.types.data_quality_rule_recommendation_run_additional_run_options

        out["AdditionalRunOptions"] = (
            capo_glue.types.data_quality_rule_recommendation_run_additional_run_options.serialize_aws_json_1_1(
                value["additional_run_options"]
            )
        )
    if "recommendation_mode" in value:
        import capo_glue.types.recommendation_mode

        out["RecommendationMode"] = (
            capo_glue.types.recommendation_mode.serialize_aws_json_1_1(
                value["recommendation_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> StartDataQualityRuleRecommendationRunRequest:
    out: StartDataQualityRuleRecommendationRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("DataSource") is not None:
        import capo_glue.types.data_source

        out["data_source"] = capo_glue.types.data_source.deserialize_aws_json_1_1(
            data["DataSource"]
        )
    else:
        raise DeserializationError(
            "StartDataQualityRuleRecommendationRunRequest.data_source required"
        )
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    else:
        raise DeserializationError(
            "StartDataQualityRuleRecommendationRunRequest.role required"
        )
    if data.get("NumberOfWorkers") is not None:
        out["number_of_workers"] = data["NumberOfWorkers"]
    if data.get("Timeout") is not None:
        out["timeout"] = data["Timeout"]
    if data.get("CreatedRulesetName") is not None:
        out["created_ruleset_name"] = data["CreatedRulesetName"]
    if data.get("DataQualitySecurityConfiguration") is not None:
        out["data_quality_security_configuration"] = data[
            "DataQualitySecurityConfiguration"
        ]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("AdditionalRunOptions") is not None:
        import capo_glue.types.data_quality_rule_recommendation_run_additional_run_options

        out["additional_run_options"] = (
            capo_glue.types.data_quality_rule_recommendation_run_additional_run_options.deserialize_aws_json_1_1(
                data["AdditionalRunOptions"]
            )
        )
    if data.get("RecommendationMode") is not None:
        import capo_glue.types.recommendation_mode

        out["recommendation_mode"] = (
            capo_glue.types.recommendation_mode.deserialize_aws_json_1_1(
                data["RecommendationMode"]
            )
        )
    return out
