"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CreateTestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.iam_role_name
    import capo_resiliencehubv2.types.logging_configuration
    import capo_resiliencehubv2.types.service_owned_arn
    import capo_resiliencehubv2.types.stop_condition_list
    import capo_resiliencehubv2.types.test_parameters


class CreateTestRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service to create the test for.</p>"""
    test_template_arn: "capo_resiliencehubv2.types.service_owned_arn.ServiceOwnedArn"
    """<p>The ARN of the test template to configure.</p>"""
    logging_configuration: NotRequired[
        "capo_resiliencehubv2.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The logging configuration for the test.</p>"""
    stop_conditions: NotRequired[
        "capo_resiliencehubv2.types.stop_condition_list.StopConditionList"
    ]
    """<p>The stop conditions for the test.</p>"""
    role_name: NotRequired["capo_resiliencehubv2.types.iam_role_name.IamRoleName"]
    """<p>The name of the IAM execution role to use when running the test.</p>"""
    parameters: NotRequired["capo_resiliencehubv2.types.test_parameters.TestParameters"]
    """<p>The parameter values for the test.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTestRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    out["testTemplateArn"] = value["test_template_arn"]
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


def deserialize_json(data: dict) -> CreateTestRequest:
    out: CreateTestRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("testTemplateArn") is not None:
        out["test_template_arn"] = data["testTemplateArn"]
    else:
        out["test_template_arn"] = ""
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
