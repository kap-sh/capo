"""Generated from Smithy shape ``com.amazonaws.wafv2#ResponseInspectionJson``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.field_identifier
    import capo_wafv2.types.response_inspection_json_failure_values
    import capo_wafv2.types.response_inspection_json_success_values


class ResponseInspectionJson(TypedDict, closed=True):
    identifier: "capo_wafv2.types.field_identifier.FieldIdentifier"
    """<p>The identifier for the value to match against in the JSON. The identifier must be an exact match, including case.</p> <p>JSON examples: <code>"Identifier": [ "/login/success" ]</code> and <code>"Identifier": [ "/sign-up/success" ]</code> </p>"""
    success_values: "capo_wafv2.types.response_inspection_json_success_values.ResponseInspectionJsonSuccessValues"
    """<p>Values for the specified identifier in the response JSON that indicate a successful login or account creation attempt. To be counted as a success, the value must be an exact match, including case. Each value must be unique among the success and failure values. </p> <p>JSON example: <code>"SuccessValues": [ "True", "Succeeded" ]</code> </p>"""
    failure_values: "capo_wafv2.types.response_inspection_json_failure_values.ResponseInspectionJsonFailureValues"
    """<p>Values for the specified identifier in the response JSON that indicate a failed login or account creation attempt. To be counted as a failure, the value must be an exact match, including case. Each value must be unique among the success and failure values. </p> <p>JSON example: <code>"FailureValues": [ "False", "Failed" ]</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponseInspectionJson) -> dict:
    out: dict = {}
    out["Identifier"] = value["identifier"]
    import capo_wafv2.types.response_inspection_json_success_values

    out["SuccessValues"] = (
        capo_wafv2.types.response_inspection_json_success_values.serialize_aws_json_1_1(
            value["success_values"]
        )
    )
    import capo_wafv2.types.response_inspection_json_failure_values

    out["FailureValues"] = (
        capo_wafv2.types.response_inspection_json_failure_values.serialize_aws_json_1_1(
            value["failure_values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponseInspectionJson:
    out: ResponseInspectionJson = {}  # type: ignore[typeddict-item]
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("ResponseInspectionJson.identifier required")
    if data.get("SuccessValues") is not None:
        import capo_wafv2.types.response_inspection_json_success_values

        out["success_values"] = (
            capo_wafv2.types.response_inspection_json_success_values.deserialize_aws_json_1_1(
                data["SuccessValues"]
            )
        )
    else:
        raise DeserializationError("ResponseInspectionJson.success_values required")
    if data.get("FailureValues") is not None:
        import capo_wafv2.types.response_inspection_json_failure_values

        out["failure_values"] = (
            capo_wafv2.types.response_inspection_json_failure_values.deserialize_aws_json_1_1(
                data["FailureValues"]
            )
        )
    else:
        raise DeserializationError("ResponseInspectionJson.failure_values required")
    return out
