"""Generated from Smithy shape ``com.amazonaws.sagemaker#DataProcessing``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.join_source
    import capo_sagemaker.types.json_path


class DataProcessing(TypedDict, closed=True):
    input_filter: NotRequired["capo_sagemaker.types.json_path.JsonPath"]
    """<p>A <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#data-processing-operators">JSONPath</a> expression used to select a portion of the input data to pass to the algorithm. Use the <code>InputFilter</code> parameter to exclude fields, such as an ID column, from the input. If you want SageMaker to pass the entire input dataset to the algorithm, accept the default value <code>$</code>.</p> <p>Examples: <code>"$"</code>, <code>"$[1:]"</code>, <code>"$.features"</code> </p>"""
    output_filter: NotRequired["capo_sagemaker.types.json_path.JsonPath"]
    """<p>A <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#data-processing-operators">JSONPath</a> expression used to select a portion of the joined dataset to save in the output file for a batch transform job. If you want SageMaker to store the entire input dataset in the output file, leave the default value, <code>$</code>. If you specify indexes that aren't within the dimension size of the joined dataset, you get an error.</p> <p>Examples: <code>"$"</code>, <code>"$[0,5:]"</code>, <code>"$['id','SageMakerOutput']"</code> </p>"""
    join_source: NotRequired["capo_sagemaker.types.join_source.JoinSource"]
    """<p>Specifies the source of the data to join with the transformed data. The valid values are <code>None</code> and <code>Input</code>. The default value is <code>None</code>, which specifies not to join the input with the transformed data. If you want the batch transform job to join the original input data with the transformed data, set <code>JoinSource</code> to <code>Input</code>. You can specify <code>OutputFilter</code> as an additional filter to select a portion of the joined dataset and store it in the output file.</p> <p>For JSON or JSONLines objects, such as a JSON array, SageMaker adds the transformed data to the input JSON object in an attribute called <code>SageMakerOutput</code>. The joined result for JSON must be a key-value pair object. If the input is not a key-value pair object, SageMaker creates a new JSON file. In the new JSON file, and the input data is stored under the <code>SageMakerInput</code> key and the results are stored in <code>SageMakerOutput</code>.</p> <p>For CSV data, SageMaker takes each row as a JSON array and joins the transformed data with the input by appending each transformed row to the end of the input. The joined data has the original input data followed by the transformed data and the output is a CSV file.</p> <p>For information on how joining in applied, see <a href="https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform-data-processing.html#batch-transform-data-processing-workflow">Workflow for Associating Inferences with Input Records</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataProcessing) -> dict:
    out: dict = {}
    if "input_filter" in value:
        out["InputFilter"] = value["input_filter"]
    if "output_filter" in value:
        out["OutputFilter"] = value["output_filter"]
    if "join_source" in value:
        import capo_sagemaker.types.join_source

        out["JoinSource"] = capo_sagemaker.types.join_source.serialize_aws_json_1_1(
            value["join_source"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataProcessing:
    out: DataProcessing = {}  # type: ignore[typeddict-item]
    if data.get("InputFilter") is not None:
        out["input_filter"] = data["InputFilter"]
    if data.get("OutputFilter") is not None:
        out["output_filter"] = data["OutputFilter"]
    if data.get("JoinSource") is not None:
        import capo_sagemaker.types.join_source

        out["join_source"] = capo_sagemaker.types.join_source.deserialize_aws_json_1_1(
            data["JoinSource"]
        )
    return out
