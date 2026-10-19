"""Generated from Smithy shape ``com.amazonaws.customerprofiles#FlowDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.flow_description
    import capo_customer_profiles.types.flow_name
    import capo_customer_profiles.types.kms_arn
    import capo_customer_profiles.types.source_flow_config
    import capo_customer_profiles.types.tasks
    import capo_customer_profiles.types.trigger_config


class FlowDefinition(TypedDict, closed=True):
    description: NotRequired[
        "capo_customer_profiles.types.flow_description.FlowDescription"
    ]
    """<p>A description of the flow you want to create.</p>"""
    flow_name: "capo_customer_profiles.types.flow_name.FlowName"
    """<p>The specified name of the flow. Use underscores (_) or hyphens (-) only. Spaces are not allowed.</p>"""
    kms_arn: "capo_customer_profiles.types.kms_arn.KmsArn"
    """<p>The Amazon Resource Name of the AWS Key Management Service (KMS) key you provide for encryption.</p>"""
    source_flow_config: (
        "capo_customer_profiles.types.source_flow_config.SourceFlowConfig"
    )
    """<p>The configuration that controls how Customer Profiles retrieves data from the source.</p>"""
    tasks: "capo_customer_profiles.types.tasks.Tasks"
    """<p>A list of tasks that Customer Profiles performs while transferring the data in the flow run.</p>"""
    trigger_config: "capo_customer_profiles.types.trigger_config.TriggerConfig"
    """<p>The trigger settings that determine how and when the flow runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowDefinition) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["FlowName"] = value["flow_name"]
    out["KmsArn"] = value["kms_arn"]
    import capo_customer_profiles.types.source_flow_config

    out["SourceFlowConfig"] = (
        capo_customer_profiles.types.source_flow_config.serialize_json(
            value["source_flow_config"]
        )
    )
    import capo_customer_profiles.types.tasks

    out["Tasks"] = capo_customer_profiles.types.tasks.serialize_json(value["tasks"])
    import capo_customer_profiles.types.trigger_config

    out["TriggerConfig"] = capo_customer_profiles.types.trigger_config.serialize_json(
        value["trigger_config"]
    )
    return out


def deserialize_json(data: dict) -> FlowDefinition:
    out: FlowDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("FlowName") is not None:
        out["flow_name"] = data["FlowName"]
    else:
        out["flow_name"] = ""
    if data.get("KmsArn") is not None:
        out["kms_arn"] = data["KmsArn"]
    else:
        out["kms_arn"] = ""
    if data.get("SourceFlowConfig") is not None:
        import capo_customer_profiles.types.source_flow_config

        out["source_flow_config"] = (
            capo_customer_profiles.types.source_flow_config.deserialize_json(
                data["SourceFlowConfig"]
            )
        )
    else:
        raise DeserializationError("FlowDefinition.source_flow_config required")
    if data.get("Tasks") is not None:
        import capo_customer_profiles.types.tasks

        out["tasks"] = capo_customer_profiles.types.tasks.deserialize_json(
            data["Tasks"]
        )
    else:
        out["tasks"] = []
    if data.get("TriggerConfig") is not None:
        import capo_customer_profiles.types.trigger_config

        out["trigger_config"] = (
            capo_customer_profiles.types.trigger_config.deserialize_json(
                data["TriggerConfig"]
            )
        )
    else:
        raise DeserializationError("FlowDefinition.trigger_config required")
    return out
