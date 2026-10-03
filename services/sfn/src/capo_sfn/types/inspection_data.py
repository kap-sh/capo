"""Generated from Smithy shape ``com.amazonaws.sfn#InspectionData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.inspection_data_request
    import capo_sfn.types.inspection_data_response
    import capo_sfn.types.inspection_error_details
    import capo_sfn.types.inspection_max_concurrency
    import capo_sfn.types.inspection_tolerated_failure_count
    import capo_sfn.types.inspection_tolerated_failure_percentage
    import capo_sfn.types.sensitive_data


class InspectionData(TypedDict, closed=True):
    input: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The raw state input.</p>"""
    after_arguments: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The input after Step Functions applies an Arguments filter. This event will only be present when QueryLanguage for the state machine or individual states is set to JSONata. For more info, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/data-transform.html">Transforming data with Step Functions</a>.</p>"""
    after_input_path: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The input after Step Functions applies the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-inputpath">InputPath</a> filter. Not populated when QueryLanguage is JSONata.</p>"""
    after_parameters: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The effective input after Step Functions applies the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-parameters">Parameters</a> filter. Not populated when QueryLanguage is JSONata.</p>"""
    result: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The state's raw result.</p>"""
    after_result_selector: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The effective result after Step Functions applies the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/input-output-inputpath-params.html#input-output-resultselector">ResultSelector</a> filter. Not populated when QueryLanguage is JSONata.</p>"""
    after_result_path: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The effective result combined with the raw state input after Step Functions applies the <a href="https://docs.aws.amazon.com/step-functions/latest/dg/input-output-resultpath.html">ResultPath</a> filter. Not populated when QueryLanguage is JSONata.</p>"""
    request: NotRequired["capo_sfn.types.inspection_data_request.InspectionDataRequest"]
    """<p>The raw HTTP request that is sent when you test an HTTP Task.</p>"""
    response: NotRequired[
        "capo_sfn.types.inspection_data_response.InspectionDataResponse"
    ]
    """<p>The raw HTTP response that is returned when you test an HTTP Task.</p>"""
    variables: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>JSON string that contains the set of workflow variables after execution of the state. The set will include variables assigned in the state and variables set up as test state input.</p>"""
    error_details: NotRequired[
        "capo_sfn.types.inspection_error_details.InspectionErrorDetails"
    ]
    """<p>An object containing data about a handled exception in the tested state.</p>"""
    after_items_path: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The effective input after the ItemsPath filter is applied. Not populated when the QueryLanguage is JSONata.</p>"""
    after_item_selector: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>An array containing the inputs for each Map iteration, transformed by the ItemSelector specified in a Map state.</p>"""
    after_item_batcher: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The effective input after the ItemBatcher filter is applied in a Map state.</p>"""
    after_items_pointer: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>The effective input after the ItemsPointer filter is applied in a Map state.</p>"""
    tolerated_failure_count: NotRequired[
        "capo_sfn.types.inspection_tolerated_failure_count.InspectionToleratedFailureCount"
    ]
    """<p>The tolerated failure threshold for a Map state as defined in number of Map state iterations.</p>"""
    tolerated_failure_percentage: NotRequired[
        "capo_sfn.types.inspection_tolerated_failure_percentage.InspectionToleratedFailurePercentage"
    ]
    """<p>The tolerated failure threshold for a Map state as defined in percentage of Map state iterations.</p>"""
    max_concurrency: NotRequired[
        "capo_sfn.types.inspection_max_concurrency.InspectionMaxConcurrency"
    ]
    """<p>The max concurrency of the Map state.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InspectionData) -> dict:
    out: dict = {}
    if "input" in value:
        out["input"] = value["input"]
    if "after_arguments" in value:
        out["afterArguments"] = value["after_arguments"]
    if "after_input_path" in value:
        out["afterInputPath"] = value["after_input_path"]
    if "after_parameters" in value:
        out["afterParameters"] = value["after_parameters"]
    if "result" in value:
        out["result"] = value["result"]
    if "after_result_selector" in value:
        out["afterResultSelector"] = value["after_result_selector"]
    if "after_result_path" in value:
        out["afterResultPath"] = value["after_result_path"]
    if "request" in value:
        import capo_sfn.types.inspection_data_request

        out["request"] = capo_sfn.types.inspection_data_request.serialize_aws_json_1_0(
            value["request"]
        )
    if "response" in value:
        import capo_sfn.types.inspection_data_response

        out["response"] = (
            capo_sfn.types.inspection_data_response.serialize_aws_json_1_0(
                value["response"]
            )
        )
    if "variables" in value:
        out["variables"] = value["variables"]
    if "error_details" in value:
        import capo_sfn.types.inspection_error_details

        out["errorDetails"] = (
            capo_sfn.types.inspection_error_details.serialize_aws_json_1_0(
                value["error_details"]
            )
        )
    if "after_items_path" in value:
        out["afterItemsPath"] = value["after_items_path"]
    if "after_item_selector" in value:
        out["afterItemSelector"] = value["after_item_selector"]
    if "after_item_batcher" in value:
        out["afterItemBatcher"] = value["after_item_batcher"]
    if "after_items_pointer" in value:
        out["afterItemsPointer"] = value["after_items_pointer"]
    if "tolerated_failure_count" in value:
        out["toleratedFailureCount"] = value["tolerated_failure_count"]
    if "tolerated_failure_percentage" in value:
        out["toleratedFailurePercentage"] = (
            "NaN"
            if value["tolerated_failure_percentage"]
            != value["tolerated_failure_percentage"]
            else "Infinity"
            if value["tolerated_failure_percentage"] == float("inf")
            else "-Infinity"
            if value["tolerated_failure_percentage"] == float("-inf")
            else value["tolerated_failure_percentage"]
        )
    if "max_concurrency" in value:
        out["maxConcurrency"] = value["max_concurrency"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InspectionData:
    out: InspectionData = {}  # type: ignore[typeddict-item]
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("afterArguments") is not None:
        out["after_arguments"] = data["afterArguments"]
    if data.get("afterInputPath") is not None:
        out["after_input_path"] = data["afterInputPath"]
    if data.get("afterParameters") is not None:
        out["after_parameters"] = data["afterParameters"]
    if data.get("result") is not None:
        out["result"] = data["result"]
    if data.get("afterResultSelector") is not None:
        out["after_result_selector"] = data["afterResultSelector"]
    if data.get("afterResultPath") is not None:
        out["after_result_path"] = data["afterResultPath"]
    if data.get("request") is not None:
        import capo_sfn.types.inspection_data_request

        out["request"] = (
            capo_sfn.types.inspection_data_request.deserialize_aws_json_1_0(
                data["request"]
            )
        )
    if data.get("response") is not None:
        import capo_sfn.types.inspection_data_response

        out["response"] = (
            capo_sfn.types.inspection_data_response.deserialize_aws_json_1_0(
                data["response"]
            )
        )
    if data.get("variables") is not None:
        out["variables"] = data["variables"]
    if data.get("errorDetails") is not None:
        import capo_sfn.types.inspection_error_details

        out["error_details"] = (
            capo_sfn.types.inspection_error_details.deserialize_aws_json_1_0(
                data["errorDetails"]
            )
        )
    if data.get("afterItemsPath") is not None:
        out["after_items_path"] = data["afterItemsPath"]
    if data.get("afterItemSelector") is not None:
        out["after_item_selector"] = data["afterItemSelector"]
    if data.get("afterItemBatcher") is not None:
        out["after_item_batcher"] = data["afterItemBatcher"]
    if data.get("afterItemsPointer") is not None:
        out["after_items_pointer"] = data["afterItemsPointer"]
    if data.get("toleratedFailureCount") is not None:
        out["tolerated_failure_count"] = data["toleratedFailureCount"]
    if data.get("toleratedFailurePercentage") is not None:
        out["tolerated_failure_percentage"] = float(data["toleratedFailurePercentage"])
    if data.get("maxConcurrency") is not None:
        out["max_concurrency"] = data["maxConcurrency"]
    return out
