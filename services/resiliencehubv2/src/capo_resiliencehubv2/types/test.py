"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#Test``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.iam_role_name
    import capo_resiliencehubv2.types.logging_configuration
    import capo_resiliencehubv2.types.service_owned_arn
    import capo_resiliencehubv2.types.stop_condition_list
    import capo_resiliencehubv2.types.test_action_list
    import capo_resiliencehubv2.types.test_id
    import capo_resiliencehubv2.types.test_parameters


class Test(TypedDict, closed=True):
    test_id: "capo_resiliencehubv2.types.test_id.TestId"
    """<p>The unique identifier of the test.</p>"""
    test_template_arn: "capo_resiliencehubv2.types.service_owned_arn.ServiceOwnedArn"
    """<p>The ARN of the test template the test was created from.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service the test belongs to.</p>"""
    name: "str"
    """<p>The name of the test.</p>"""
    actions: NotRequired["capo_resiliencehubv2.types.test_action_list.TestActionList"]
    """<p>The fault actions the test runs.</p>"""
    logging_configuration: NotRequired[
        "capo_resiliencehubv2.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>The logging configuration for the test.</p>"""
    stop_conditions: NotRequired[
        "capo_resiliencehubv2.types.stop_condition_list.StopConditionList"
    ]
    """<p>The stop conditions for the test.</p>"""
    role_name: NotRequired["capo_resiliencehubv2.types.iam_role_name.IamRoleName"]
    """<p>The name of the IAM execution role used to run the test.</p>"""
    parameters: NotRequired["capo_resiliencehubv2.types.test_parameters.TestParameters"]
    """<p>The parameter values configured for the test.</p>"""
    total_test_runs: "int"
    """<p>The total number of runs of the test.</p>"""
    successful_test_runs: "int"
    """<p>The number of successful runs of the test.</p>"""
    creation_time: "datetime.datetime"
    """<p>The timestamp when the test was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Test) -> dict:
    out: dict = {}
    out["testId"] = value["test_id"]
    out["testTemplateArn"] = value["test_template_arn"]
    out["serviceArn"] = value["service_arn"]
    out["name"] = value["name"]
    if "actions" in value:
        import capo_resiliencehubv2.types.test_action_list

        out["actions"] = capo_resiliencehubv2.types.test_action_list.serialize_json(
            value["actions"]
        )
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
    out["totalTestRuns"] = value["total_test_runs"]
    out["successfulTestRuns"] = value["successful_test_runs"]
    import capo_resiliencehubv2.types._prelude.timestamp

    out["creationTime"] = capo_resiliencehubv2.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> Test:
    out: Test = {}  # type: ignore[typeddict-item]
    if data.get("testId") is not None:
        out["test_id"] = data["testId"]
    else:
        out["test_id"] = ""
    if data.get("testTemplateArn") is not None:
        out["test_template_arn"] = data["testTemplateArn"]
    else:
        out["test_template_arn"] = ""
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("actions") is not None:
        import capo_resiliencehubv2.types.test_action_list

        out["actions"] = capo_resiliencehubv2.types.test_action_list.deserialize_json(
            data["actions"]
        )
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
    if data.get("totalTestRuns") is not None:
        out["total_test_runs"] = data["totalTestRuns"]
    else:
        out["total_test_runs"] = 0
    if data.get("successfulTestRuns") is not None:
        out["successful_test_runs"] = data["successfulTestRuns"]
    else:
        out["successful_test_runs"] = 0
    if data.get("creationTime") is not None:
        import capo_resiliencehubv2.types._prelude.timestamp

        out["creation_time"] = (
            capo_resiliencehubv2.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
