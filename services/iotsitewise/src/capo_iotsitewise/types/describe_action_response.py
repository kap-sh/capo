"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeActionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.action_payload
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.resolve_to
    import capo_iotsitewise.types.target_resource
    import capo_iotsitewise.types.timestamp


class DescribeActionResponse(TypedDict, closed=True):
    action_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the action.</p>"""
    target_resource: "capo_iotsitewise.types.target_resource.TargetResource"
    """<p>The resource the action will be taken on.</p>"""
    action_definition_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the action definition.</p>"""
    action_payload: "capo_iotsitewise.types.action_payload.ActionPayload"
    """<p>The JSON payload of the action.</p>"""
    execution_time: "capo_iotsitewise.types.timestamp.Timestamp"
    """<p>The time the action was executed.</p>"""
    resolve_to: NotRequired["capo_iotsitewise.types.resolve_to.ResolveTo"]
    """<p>The detailed resource this action resolves to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeActionResponse) -> dict:
    out: dict = {}
    out["actionId"] = value["action_id"]
    import capo_iotsitewise.types.target_resource

    out["targetResource"] = capo_iotsitewise.types.target_resource.serialize_json(
        value["target_resource"]
    )
    out["actionDefinitionId"] = value["action_definition_id"]
    import capo_iotsitewise.types.action_payload

    out["actionPayload"] = capo_iotsitewise.types.action_payload.serialize_json(
        value["action_payload"]
    )
    import capo_iotsitewise.types.timestamp

    out["executionTime"] = capo_iotsitewise.types.timestamp.serialize_json(
        value["execution_time"]
    )
    if "resolve_to" in value:
        import capo_iotsitewise.types.resolve_to

        out["resolveTo"] = capo_iotsitewise.types.resolve_to.serialize_json(
            value["resolve_to"]
        )
    return out


def deserialize_json(data: dict) -> DescribeActionResponse:
    out: DescribeActionResponse = {}  # type: ignore[typeddict-item]
    if data.get("actionId") is not None:
        out["action_id"] = data["actionId"]
    else:
        out["action_id"] = ""
    if data.get("targetResource") is not None:
        import capo_iotsitewise.types.target_resource

        out["target_resource"] = (
            capo_iotsitewise.types.target_resource.deserialize_json(
                data["targetResource"]
            )
        )
    else:
        raise DeserializationError("DescribeActionResponse.target_resource required")
    if data.get("actionDefinitionId") is not None:
        out["action_definition_id"] = data["actionDefinitionId"]
    else:
        out["action_definition_id"] = ""
    if data.get("actionPayload") is not None:
        import capo_iotsitewise.types.action_payload

        out["action_payload"] = capo_iotsitewise.types.action_payload.deserialize_json(
            data["actionPayload"]
        )
    else:
        raise DeserializationError("DescribeActionResponse.action_payload required")
    if data.get("executionTime") is not None:
        import capo_iotsitewise.types.timestamp

        out["execution_time"] = capo_iotsitewise.types.timestamp.deserialize_json(
            data["executionTime"]
        )
    else:
        import datetime

        out["execution_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("resolveTo") is not None:
        import capo_iotsitewise.types.resolve_to

        out["resolve_to"] = capo_iotsitewise.types.resolve_to.deserialize_json(
            data["resolveTo"]
        )
    return out
