"""Generated from Smithy shape ``com.amazonaws.sfn#TestStateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.definition
    import capo_sfn.types.inspection_level
    import capo_sfn.types.mock_input
    import capo_sfn.types.reveal_secrets
    import capo_sfn.types.sensitive_data
    import capo_sfn.types.test_state_configuration
    import capo_sfn.types.test_state_state_name


class TestStateInput(TypedDict, closed=True):
    definition: "capo_sfn.types.definition.Definition"
    """<p>The <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">Amazon States Language</a> (ASL) definition of the state or state machine.</p>"""
    role_arn: NotRequired["capo_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the execution role with the required IAM permissions for the state.</p>"""
    input: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>A string that contains the JSON input data for the state.</p>"""
    inspection_level: NotRequired["capo_sfn.types.inspection_level.InspectionLevel"]
    """<p>Determines the values to return when a state is tested. You can specify one of the following types:</p> <ul> <li> <p> <code>INFO</code>: Shows the final state output. By default, Step Functions sets <code>inspectionLevel</code> to <code>INFO</code> if you don't specify a level.</p> </li> <li> <p> <code>DEBUG</code>: Shows the final state output along with the input and output data processing result.</p> </li> <li> <p> <code>TRACE</code>: Shows the HTTP request and response for an HTTP Task. This level also shows the final state output along with the input and output data processing result.</p> </li> </ul> <p>Each of these levels also provide information about the status of the state execution and the next state to transition to.</p>"""
    reveal_secrets: "capo_sfn.types.reveal_secrets.RevealSecrets"
    """<p>Specifies whether or not to include secret information in the test result. For HTTP Tasks, a secret includes the data that an EventBridge connection adds to modify the HTTP request headers, query parameters, and body. Step Functions doesn't omit any information included in the state definition or the HTTP response.</p> <p>If you set <code>revealSecrets</code> to <code>true</code>, you must make sure that the IAM user that calls the <code>TestState</code> API has permission for the <code>states:RevealSecrets</code> action. For an example of IAM policy that sets the <code>states:RevealSecrets</code> permission, see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/test-state-isolation.html#test-state-permissions">IAM permissions to test a state</a>. Without this permission, Step Functions throws an access denied error.</p> <p>By default, <code>revealSecrets</code> is set to <code>false</code>.</p>"""
    variables: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>JSON object literal that sets variables used in the state under test. Object keys are the variable names and values are the variable values.</p>"""
    state_name: NotRequired["capo_sfn.types.test_state_state_name.TestStateStateName"]
    """<p>Denotes the particular state within a state machine definition to be tested. If this field is specified, the <code>definition</code> must contain a fully-formed state machine definition.</p>"""
    mock: NotRequired["capo_sfn.types.mock_input.MockInput"]
    """<p>Defines a mocked result or error for the state under test.</p> <p>A mock can only be specified for Task, Map, or Parallel states. If it is specified for another state type, an exception will be thrown.</p>"""
    context: NotRequired["capo_sfn.types.sensitive_data.SensitiveData"]
    """<p>A JSON string representing a valid Context object for the state under test. This field may only be specified if a mock is specified in the same request.</p>"""
    state_configuration: NotRequired[
        "capo_sfn.types.test_state_configuration.TestStateConfiguration"
    ]
    """<p>Contains configurations for the state under test.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestStateInput) -> dict:
    out: dict = {}
    out["definition"] = value["definition"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "input" in value:
        out["input"] = value["input"]
    if "inspection_level" in value:
        import capo_sfn.types.inspection_level

        out["inspectionLevel"] = capo_sfn.types.inspection_level.serialize_aws_json_1_0(
            value["inspection_level"]
        )
    out["revealSecrets"] = value.get("reveal_secrets", False)
    if "variables" in value:
        out["variables"] = value["variables"]
    if "state_name" in value:
        out["stateName"] = value["state_name"]
    if "mock" in value:
        import capo_sfn.types.mock_input

        out["mock"] = capo_sfn.types.mock_input.serialize_aws_json_1_0(value["mock"])
    if "context" in value:
        out["context"] = value["context"]
    if "state_configuration" in value:
        import capo_sfn.types.test_state_configuration

        out["stateConfiguration"] = (
            capo_sfn.types.test_state_configuration.serialize_aws_json_1_0(
                value["state_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TestStateInput:
    out: TestStateInput = {}  # type: ignore[typeddict-item]
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("TestStateInput.definition required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("input") is not None:
        out["input"] = data["input"]
    if data.get("inspectionLevel") is not None:
        import capo_sfn.types.inspection_level

        out["inspection_level"] = (
            capo_sfn.types.inspection_level.deserialize_aws_json_1_0(
                data["inspectionLevel"]
            )
        )
    if data.get("revealSecrets") is not None:
        out["reveal_secrets"] = data["revealSecrets"]
    else:
        out["reveal_secrets"] = False
    if data.get("variables") is not None:
        out["variables"] = data["variables"]
    if data.get("stateName") is not None:
        out["state_name"] = data["stateName"]
    if data.get("mock") is not None:
        import capo_sfn.types.mock_input

        out["mock"] = capo_sfn.types.mock_input.deserialize_aws_json_1_0(data["mock"])
    if data.get("context") is not None:
        out["context"] = data["context"]
    if data.get("stateConfiguration") is not None:
        import capo_sfn.types.test_state_configuration

        out["state_configuration"] = (
            capo_sfn.types.test_state_configuration.deserialize_aws_json_1_0(
                data["stateConfiguration"]
            )
        )
    return out
