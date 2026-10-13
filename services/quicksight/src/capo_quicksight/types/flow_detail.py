"""Generated from Smithy shape ``com.amazonaws.quicksight#FlowDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.flow_description
    import capo_quicksight.types.flow_id
    import capo_quicksight.types.flow_publish_state
    import capo_quicksight.types.sensitive_document
    import capo_quicksight.types.step_alias_list
    import capo_quicksight.types.timestamp
    import capo_quicksight.types.title


class FlowDetail(TypedDict, closed=True):
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the flow.</p>"""
    flow_id: "capo_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    name: "capo_quicksight.types.title.Title"
    """<p>The display name of the flow.</p>"""
    description: NotRequired["capo_quicksight.types.flow_description.FlowDescription"]
    """<p>The description of the flow.</p>"""
    publish_state: "capo_quicksight.types.flow_publish_state.FlowPublishState"
    """<p>The publish state of the flow. Valid values are <code>DRAFT</code>, <code>PUBLISHED</code>, or <code>PENDING_APPROVAL</code>.</p>"""
    created_time: "capo_quicksight.types.timestamp.Timestamp"
    """<p>The time this flow was created.</p>"""
    created_by: NotRequired["str"]
    """<p>The identifier of the principal who created the flow.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The last time this flow was modified.</p>"""
    last_updated_by: NotRequired["str"]
    """<p>The identifier of the last principal who updated the flow.</p>"""
    flow_definition: "capo_quicksight.types.sensitive_document.SensitiveDocument"
    """<p>The definition of the flow, specifying the steps and configurations. This is the flow definition in Quick Flow's internal format. The format is subject to change.</p>"""
    step_aliases: NotRequired["capo_quicksight.types.step_alias_list.StepAliasList"]
    """<p>A list of step alias mappings for the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowDetail) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["FlowId"] = value["flow_id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    import capo_quicksight.types.flow_publish_state

    out["PublishState"] = capo_quicksight.types.flow_publish_state.serialize_json(
        value["publish_state"]
    )
    import capo_quicksight.types.timestamp

    out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
        value["created_time"]
    )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "last_updated_by" in value:
        out["LastUpdatedBy"] = value["last_updated_by"]
    out["FlowDefinition"] = value["flow_definition"]
    if "step_aliases" in value:
        import capo_quicksight.types.step_alias_list

        out["StepAliases"] = capo_quicksight.types.step_alias_list.serialize_json(
            value["step_aliases"]
        )
    return out


def deserialize_json(data: dict) -> FlowDetail:
    out: FlowDetail = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("FlowDetail.arn required")
    if data.get("FlowId") is not None:
        out["flow_id"] = data["FlowId"]
    else:
        raise DeserializationError("FlowDetail.flow_id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("FlowDetail.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("PublishState") is not None:
        import capo_quicksight.types.flow_publish_state

        out["publish_state"] = (
            capo_quicksight.types.flow_publish_state.deserialize_json(
                data["PublishState"]
            )
        )
    else:
        raise DeserializationError("FlowDetail.publish_state required")
    if data.get("CreatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    else:
        raise DeserializationError("FlowDetail.created_time required")
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("LastUpdatedTime") is not None:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if data.get("LastUpdatedBy") is not None:
        out["last_updated_by"] = data["LastUpdatedBy"]
    if data.get("FlowDefinition") is not None:
        out["flow_definition"] = data["FlowDefinition"]
    else:
        raise DeserializationError("FlowDetail.flow_definition required")
    if data.get("StepAliases") is not None:
        import capo_quicksight.types.step_alias_list

        out["step_aliases"] = capo_quicksight.types.step_alias_list.deserialize_json(
            data["StepAliases"]
        )
    return out


def redact_sensitive(value: FlowDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "flow_definition" in value:
        out["flow_definition"] = "*** Sensitive Data Redacted ***"
    return out
