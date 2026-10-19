"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateTestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.iam_role_name
    import capo_resiliencehubv2.types.logging_configuration
    import capo_resiliencehubv2.types.stop_condition_list
    import capo_resiliencehubv2.types.test_id
    import capo_resiliencehubv2.types.test_parameters


class UpdateTestRequest(TypedDict, closed=True):
    test_id: "capo_resiliencehubv2.types.test_id.TestId"
    """<p>The identifier of the test to update.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service the test belongs to.</p>"""
    logging_configuration: NotRequired[
        "capo_resiliencehubv2.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The updated logging configuration for the test.</p>"""
    stop_conditions: NotRequired[
        "capo_resiliencehubv2.types.stop_condition_list.StopConditionList"
    ]
    """<p>The updated stop conditions for the test.</p>"""
    role_name: NotRequired["capo_resiliencehubv2.types.iam_role_name.IamRoleName"]
    """<p>The updated IAM execution role name.</p>"""
    parameters: NotRequired["capo_resiliencehubv2.types.test_parameters.TestParameters"]
    """<p>The updated parameter values for the test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTestRequest) -> dict:
    out: dict = {}
    out["testId"] = value["test_id"]
    out["serviceArn"] = value["service_arn"]
    if "logging_configuration" in value:
        import capo_resiliencehubv2.types.logging_configuration

        out["loggingConfiguration"] = (
            capo_resiliencehubv2.types.logging_configuration.serialize_json(
                value["logging_configuration"]
            )
        )
    if "stop_conditions" in value:
        import capo_resiliencehubv2.types.stop_condition_list

        out["stopConditions"] = (
            capo_resiliencehubv2.types.stop_condition_list.serialize_json(
                value["stop_conditions"]
            )
        )
    if "role_name" in value:
        out["roleName"] = value["role_name"]
    if "parameters" in value:
        import capo_resiliencehubv2.types.test_parameters

        out["parameters"] = capo_resiliencehubv2.types.test_parameters.serialize_json(
            value["parameters"]
        )
    return out


def deserialize_json(data: dict) -> UpdateTestRequest:
    out: UpdateTestRequest = {}  # type: ignore[typeddict-item]
    if data.get("testId") is not None:
        out["test_id"] = data["testId"]
    else:
        out["test_id"] = ""
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("loggingConfiguration") is not None:
        import capo_resiliencehubv2.types.logging_configuration

        out["logging_configuration"] = (
            capo_resiliencehubv2.types.logging_configuration.deserialize_json(
                data["loggingConfiguration"]
            )
        )
    if data.get("stopConditions") is not None:
        import capo_resiliencehubv2.types.stop_condition_list

        out["stop_conditions"] = (
            capo_resiliencehubv2.types.stop_condition_list.deserialize_json(
                data["stopConditions"]
            )
        )
    if data.get("roleName") is not None:
        out["role_name"] = data["roleName"]
    if data.get("parameters") is not None:
        import capo_resiliencehubv2.types.test_parameters

        out["parameters"] = capo_resiliencehubv2.types.test_parameters.deserialize_json(
            data["parameters"]
        )
    return out
