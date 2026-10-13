"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Memory``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.arn
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.indexed_keys_list
    import capo_bedrock_agentcore_control.types.memory_arn
    import capo_bedrock_agentcore_control.types.memory_id
    import capo_bedrock_agentcore_control.types.memory_status
    import capo_bedrock_agentcore_control.types.memory_strategy_list
    import capo_bedrock_agentcore_control.types.name
    import capo_bedrock_agentcore_control.types.namespace_keys_list
    import capo_bedrock_agentcore_control.types.stream_delivery_resources


class Memory(TypedDict, closed=True):
    arn: "capo_bedrock_agentcore_control.types.memory_arn.MemoryArn"
    """<p>The Amazon Resource Name (ARN) of the memory.</p>"""
    id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId"
    """<p>The unique identifier of the memory.</p>"""
    name: "capo_bedrock_agentcore_control.types.name.Name"
    """<p>The name of the memory.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the memory.</p>"""
    encryption_key_arn: NotRequired["capo_bedrock_agentcore_control.types.arn.Arn"]
    """<p>The ARN of the KMS key used to encrypt the memory.</p>"""
    memory_execution_role_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.arn.Arn"
    ]
    """<p>The ARN of the IAM role that provides permissions for the memory.</p>"""
    event_expiry_duration: "int"
    """<p>The number of days after which memory events will expire.</p>"""
    status: "capo_bedrock_agentcore_control.types.memory_status.MemoryStatus"
    """<p>The current status of the memory.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for failure if the memory is in a failed state.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the memory was created.</p>"""
    updated_at: "datetime.datetime"
    """<p>The timestamp when the memory was last updated.</p>"""
    strategies: NotRequired[
        "capo_bedrock_agentcore_control.types.memory_strategy_list.MemoryStrategyList"
    ]
    """<p>The list of memory strategies associated with this memory.</p>"""
    indexed_keys: NotRequired[
        "capo_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
    ]
    """<p>The indexed metadata keys for this memory. Only indexed keys can be used in metadata filters.</p>"""
    namespace_keys: NotRequired[
        "capo_bedrock_agentcore_control.types.namespace_keys_list.NamespaceKeysList"
    ]
    """<p>The namespace variable key definitions for this memory. Namespace keys define custom variables used in <code>namespaceTemplates</code> with optional validation rules.</p>"""
    stream_delivery_resources: NotRequired[
        "capo_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
    ]
    """<p>Configuration for streaming memory record data to external resources.</p>"""
    managed_by_resource_arn: NotRequired["capo_bedrock_agentcore_control.types.arn.Arn"]
    """<p>ARN of the resource managing this memory (e.g. a harness). When set, strategy modifications and deletion are only allowed through the managing resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Memory) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    if "memory_execution_role_arn" in value:
        out["memoryExecutionRoleArn"] = value["memory_execution_role_arn"]
    out["eventExpiryDuration"] = value["event_expiry_duration"]
    import capo_bedrock_agentcore_control.types.memory_status

    out["status"] = capo_bedrock_agentcore_control.types.memory_status.serialize_json(
        value["status"]
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    if "strategies" in value:
        import capo_bedrock_agentcore_control.types.memory_strategy_list

        out["strategies"] = (
            capo_bedrock_agentcore_control.types.memory_strategy_list.serialize_json(
                value["strategies"]
            )
        )
    if "indexed_keys" in value:
        import capo_bedrock_agentcore_control.types.indexed_keys_list

        out["indexedKeys"] = (
            capo_bedrock_agentcore_control.types.indexed_keys_list.serialize_json(
                value["indexed_keys"]
            )
        )
    if "namespace_keys" in value:
        import capo_bedrock_agentcore_control.types.namespace_keys_list

        out["namespaceKeys"] = (
            capo_bedrock_agentcore_control.types.namespace_keys_list.serialize_json(
                value["namespace_keys"]
            )
        )
    if "stream_delivery_resources" in value:
        import capo_bedrock_agentcore_control.types.stream_delivery_resources

        out["streamDeliveryResources"] = (
            capo_bedrock_agentcore_control.types.stream_delivery_resources.serialize_json(
                value["stream_delivery_resources"]
            )
        )
    if "managed_by_resource_arn" in value:
        out["managedByResourceArn"] = value["managed_by_resource_arn"]
    return out


def deserialize_json(data: dict) -> Memory:
    out: Memory = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Memory.arn required")
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("Memory.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("Memory.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if data.get("memoryExecutionRoleArn") is not None:
        out["memory_execution_role_arn"] = data["memoryExecutionRoleArn"]
    if data.get("eventExpiryDuration") is not None:
        out["event_expiry_duration"] = data["eventExpiryDuration"]
    else:
        raise DeserializationError("Memory.event_expiry_duration required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.memory_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.memory_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("Memory.status required")
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Memory.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("Memory.updated_at required")
    if data.get("strategies") is not None:
        import capo_bedrock_agentcore_control.types.memory_strategy_list

        out["strategies"] = (
            capo_bedrock_agentcore_control.types.memory_strategy_list.deserialize_json(
                data["strategies"]
            )
        )
    if data.get("indexedKeys") is not None:
        import capo_bedrock_agentcore_control.types.indexed_keys_list

        out["indexed_keys"] = (
            capo_bedrock_agentcore_control.types.indexed_keys_list.deserialize_json(
                data["indexedKeys"]
            )
        )
    if data.get("namespaceKeys") is not None:
        import capo_bedrock_agentcore_control.types.namespace_keys_list

        out["namespace_keys"] = (
            capo_bedrock_agentcore_control.types.namespace_keys_list.deserialize_json(
                data["namespaceKeys"]
            )
        )
    if data.get("streamDeliveryResources") is not None:
        import capo_bedrock_agentcore_control.types.stream_delivery_resources

        out["stream_delivery_resources"] = (
            capo_bedrock_agentcore_control.types.stream_delivery_resources.deserialize_json(
                data["streamDeliveryResources"]
            )
        )
    if data.get("managedByResourceArn") is not None:
        out["managed_by_resource_arn"] = data["managedByResourceArn"]
    return out


def redact_sensitive(value: Memory) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "strategies" in value:
        import capo_bedrock_agentcore_control.types.memory_strategy_list

        out["strategies"] = (
            capo_bedrock_agentcore_control.types.memory_strategy_list.redact_sensitive(
                value["strategies"]
            )
        )
    return out
