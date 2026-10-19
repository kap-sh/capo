"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#DeleteABTestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ab_test_arn
    import capo_bedrock_agentcore.types.ab_test_id
    import capo_bedrock_agentcore.types.ab_test_status


class DeleteABTestResponse(TypedDict, closed=True):
    ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId"
    """<p>The unique identifier of the deleted A/B test.</p>"""
    ab_test_arn: "capo_bedrock_agentcore.types.ab_test_arn.ABTestArn"
    """<p>The Amazon Resource Name (ARN) of the deleted A/B test.</p>"""
    status: "capo_bedrock_agentcore.types.ab_test_status.ABTestStatus"
    """<p>The status of the A/B test deletion operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteABTestResponse) -> dict:
    out: dict = {}
    out["abTestId"] = value["ab_test_id"]
    out["abTestArn"] = value["ab_test_arn"]
    import capo_bedrock_agentcore.types.ab_test_status

    out["status"] = capo_bedrock_agentcore.types.ab_test_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteABTestResponse:
    out: DeleteABTestResponse = {}  # type: ignore[typeddict-item]
    if data.get("abTestId") is not None:
        out["ab_test_id"] = data["abTestId"]
    else:
        out["ab_test_id"] = ""
    if data.get("abTestArn") is not None:
        out["ab_test_arn"] = data["abTestArn"]
    else:
        out["ab_test_arn"] = ""
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
    return out
