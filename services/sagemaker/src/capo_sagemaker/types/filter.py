"""Generated from Smithy shape ``com.amazonaws.sagemaker#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.filter_value
    import capo_sagemaker.types.operator
    import capo_sagemaker.types.resource_property_name


class Filter(TypedDict, closed=True):
    name: NotRequired[
        "capo_sagemaker.types.resource_property_name.ResourcePropertyName"
    ]
    """<p>A resource property name. For example, <code>TrainingJobName</code>. For valid property names, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SearchRecord.html">SearchRecord</a>. You must specify a valid property for the resource.</p>"""
    operator: NotRequired["capo_sagemaker.types.operator.Operator"]
    """<p>A Boolean binary operator that is used to evaluate the filter. The operator field contains one of the following values:</p> <dl> <dt>Equals</dt> <dd> <p>The value of <code>Name</code> equals <code>Value</code>.</p> </dd> <dt>NotEquals</dt> <dd> <p>The value of <code>Name</code> doesn't equal <code>Value</code>.</p> </dd> <dt>Exists</dt> <dd> <p>The <code>Name</code> property exists.</p> </dd> <dt>NotExists</dt> <dd> <p>The <code>Name</code> property does not exist.</p> </dd> <dt>GreaterThan</dt> <dd> <p>The value of <code>Name</code> is greater than <code>Value</code>. Not supported for text properties.</p> </dd> <dt>GreaterThanOrEqualTo</dt> <dd> <p>The value of <code>Name</code> is greater than or equal to <code>Value</code>. Not supported for text properties.</p> </dd> <dt>LessThan</dt> <dd> <p>The value of <code>Name</code> is less than <code>Value</code>. Not supported for text properties.</p> </dd> <dt>LessThanOrEqualTo</dt> <dd> <p>The value of <code>Name</code> is less than or equal to <code>Value</code>. Not supported for text properties.</p> </dd> <dt>In</dt> <dd> <p>The value of <code>Name</code> is one of the comma delimited strings in <code>Value</code>. Only supported for text properties.</p> </dd> <dt>Contains</dt> <dd> <p>The value of <code>Name</code> contains the string <code>Value</code>. Only supported for text properties.</p> <p>A <code>SearchExpression</code> can include the <code>Contains</code> operator multiple times when the value of <code>Name</code> is one of the following:</p> <ul> <li> <p> <code>Experiment.DisplayName</code> </p> </li> <li> <p> <code>Experiment.ExperimentName</code> </p> </li> <li> <p> <code>Experiment.Tags</code> </p> </li> <li> <p> <code>Trial.DisplayName</code> </p> </li> <li> <p> <code>Trial.TrialName</code> </p> </li> <li> <p> <code>Trial.Tags</code> </p> </li> <li> <p> <code>TrialComponent.DisplayName</code> </p> </li> <li> <p> <code>TrialComponent.TrialComponentName</code> </p> </li> <li> <p> <code>TrialComponent.Tags</code> </p> </li> <li> <p> <code>TrialComponent.InputArtifacts</code> </p> </li> <li> <p> <code>TrialComponent.OutputArtifacts</code> </p> </li> </ul> <p>A <code>SearchExpression</code> can include only one <code>Contains</code> operator for all other values of <code>Name</code>. In these cases, if you include multiple <code>Contains</code> operators in the <code>SearchExpression</code>, the result is the following error message: "<code>'CONTAINS' operator usage limit of 1 exceeded.</code>"</p> </dd> </dl>"""
    value: NotRequired["capo_sagemaker.types.filter_value.FilterValue"]
    """<p>A value used with <code>Name</code> and <code>Operator</code> to determine which resources satisfy the filter's condition. For numerical properties, <code>Value</code> must be an integer or floating-point decimal. For timestamp properties, <code>Value</code> must be an ISO 8601 date-time string of the following format: <code>YYYY-mm-dd'T'HH:MM:SS</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "operator" in value:
        import capo_sagemaker.types.operator

        out["Operator"] = capo_sagemaker.types.operator.serialize_aws_json_1_1(
            value["operator"]
        )
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Operator") is not None:
        import capo_sagemaker.types.operator

        out["operator"] = capo_sagemaker.types.operator.deserialize_aws_json_1_1(
            data["Operator"]
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
