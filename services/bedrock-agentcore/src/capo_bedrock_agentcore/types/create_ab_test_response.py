"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#CreateABTestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore.types.ab_test_arn
    import capo_bedrock_agentcore.types.ab_test_execution_status
    import capo_bedrock_agentcore.types.ab_test_id
    import capo_bedrock_agentcore.types.ab_test_name
    import capo_bedrock_agentcore.types.ab_test_status


class CreateABTestResponse(TypedDict, closed=True):
    ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the created A/B test.</p>"""
    ab_test_arn: "capo_bedrock_agentcore.types.ab_test_arn.ABTestArn"
    """<p>The Amazon Resource Name (ARN) of the created A/B test.</p>"""
    name: NotRequired["capo_bedrock_agentcore.types.ab_test_name.ABTestName"]
    """<p>The name of the A/B test.</p>"""
    status: "capo_bedrock_agentcore.types.ab_test_status.ABTestStatus"
    """<p>The status of the A/B test.</p>"""
    execution_status: (
        "capo_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"
    )
    """<p>The execution status indicating whether the A/B test is currently running.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the A/B test was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateABTestResponse) -> dict:
    out: dict = {}
    out["abTestId"] = value["ab_test_id"]
    out["abTestArn"] = value["ab_test_arn"]
    if "name" in value:
        out["name"] = value["name"]
    import capo_bedrock_agentcore.types.ab_test_status

    out["status"] = capo_bedrock_agentcore.types.ab_test_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore.types.ab_test_execution_status

    out["executionStatus"] = (
        capo_bedrock_agentcore.types.ab_test_execution_status.serialize_json(
            value["execution_status"]
        )
    )
    import capo_bedrock_agentcore.types._prelude.timestamp

    out["createdAt"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateABTestResponse:
    out: CreateABTestResponse = {}  # type: ignore[typeddict-item]
    if data.get("abTestId") is not None:
        out["ab_test_id"] = data["abTestId"]
    else:
        out["ab_test_id"] = ""
    if data.get("abTestArn") is not None:
        out["ab_test_arn"] = data["abTestArn"]
    else:
        out["ab_test_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.ab_test_status

        out["status"] = capo_bedrock_agentcore.types.ab_test_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.ab_test_status.ABTestStatus", ""
        )
    if data.get("executionStatus") is not None:
        import capo_bedrock_agentcore.types.ab_test_execution_status

        out["execution_status"] = (
            capo_bedrock_agentcore.types.ab_test_execution_status.deserialize_json(
                data["executionStatus"]
            )
        )
    else:
        import typing

        out["execution_status"] = typing.cast(
            "capo_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
