"""Generated from Smithy shape ``com.amazonaws.athena#StartCalculationExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.calculation_configuration
    import capo_athena.types.code_block
    import capo_athena.types.description_string
    import capo_athena.types.idempotency_token
    import capo_athena.types.session_id


class StartCalculationExecutionRequest(TypedDict, closed=True):
    session_id: "capo_athena.types.session_id.SessionId"
    """<p>The session ID.</p>"""
    description: NotRequired["capo_athena.types.description_string.DescriptionString"]
    """<p>A description of the calculation.</p>"""
    calculation_configuration: NotRequired[
        "capo_athena.types.calculation_configuration.CalculationConfiguration"
    ]
    """<p>Contains configuration information for the calculation.</p>"""
    code_block: NotRequired["capo_athena.types.code_block.CodeBlock"]
    """<p>A string that contains the code of the calculation. Use this parameter instead of <a>CalculationConfiguration$CodeBlock</a>, which is deprecated.</p>"""
    client_request_token: NotRequired[
        "capo_athena.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique case-sensitive string used to ensure the request to create the calculation is idempotent (executes only once). If another <code>StartCalculationExecutionRequest</code> is received, the same response is returned and another calculation is not created. If a parameter has changed, an error is returned.</p> <important> <p>This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for users. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartCalculationExecutionRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "calculation_configuration" in value:
        import capo_athena.types.calculation_configuration

        out["CalculationConfiguration"] = (
            capo_athena.types.calculation_configuration.serialize_aws_json_1_1(
                value["calculation_configuration"]
            )
        )
    if "code_block" in value:
        out["CodeBlock"] = value["code_block"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartCalculationExecutionRequest:
    out: StartCalculationExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        out["session_id"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CalculationConfiguration") is not None:
        import capo_athena.types.calculation_configuration

        out["calculation_configuration"] = (
            capo_athena.types.calculation_configuration.deserialize_aws_json_1_1(
                data["CalculationConfiguration"]
            )
        )
    if data.get("CodeBlock") is not None:
        out["code_block"] = data["CodeBlock"]
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    return out
