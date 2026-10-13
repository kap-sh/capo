"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateMemoryInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.arn
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.indexed_keys_list
    import capo_bedrock_agentcore_control.types.memory_strategy_input_list
    import capo_bedrock_agentcore_control.types.name
    import capo_bedrock_agentcore_control.types.namespace_keys_list
    import capo_bedrock_agentcore_control.types.non_empty_string
    import capo_bedrock_agentcore_control.types.stream_delivery_resources
    import capo_bedrock_agentcore_control.types.tags_map


class CreateMemoryInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>"""
    name: "capo_bedrock_agentcore_control.types.name.Name"
    """<p>The name of the memory. The name must be unique within your account.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.description.Description"
    ]
    """<p>The description of the memory.</p>"""
    encryption_key_arn: NotRequired["capo_bedrock_agentcore_control.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the memory data.</p>"""
    memory_execution_role_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.arn.Arn"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the memory to access Amazon Web Services services.</p>"""
    event_expiry_duration: "int"
    """<p>The duration after which memory events expire. Specified as an ISO 8601 duration.</p>"""
    memory_strategies: NotRequired[
        "capo_bedrock_agentcore_control.types.memory_strategy_input_list.MemoryStrategyInputList"
    ]
    """<p>The memory strategies to use for this memory. Strategies define how information is extracted, processed, and consolidated.</p>"""
    indexed_keys: NotRequired[
        "capo_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
    ]
    """<p>Metadata keys to index for filtering. Once declared, indexed keys cannot be removed.</p>"""
    namespace_keys: NotRequired[
        "capo_bedrock_agentcore_control.types.namespace_keys_list.NamespaceKeysList"
    ]
    """<p>The namespace variable key definitions with optional validation rules. Use these <code>namespaceKeys</code> in <code>namespaceTemplates</code> to control namespace hierarchy.</p>"""
    stream_delivery_resources: NotRequired[
        "capo_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
    ]
    """<p>Configuration for streaming memory record data to external resources.</p>"""
    tags: NotRequired["capo_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>A map of tag keys and values to assign to an AgentCore Memory. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMemoryInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "encryption_key_arn" in value:
        out["encryptionKeyArn"] = value["encryption_key_arn"]
    if "memory_execution_role_arn" in value:
        out["memoryExecutionRoleArn"] = value["memory_execution_role_arn"]
    out["eventExpiryDuration"] = value["event_expiry_duration"]
    if "memory_strategies" in value:
        import capo_bedrock_agentcore_control.types.memory_strategy_input_list

        out["memoryStrategies"] = (
            capo_bedrock_agentcore_control.types.memory_strategy_input_list.serialize_json(
                value["memory_strategies"]
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
    if "tags" in value:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateMemoryInput:
    out: CreateMemoryInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateMemoryInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("encryptionKeyArn") is not None:
        out["encryption_key_arn"] = data["encryptionKeyArn"]
    if data.get("memoryExecutionRoleArn") is not None:
        out["memory_execution_role_arn"] = data["memoryExecutionRoleArn"]
    if data.get("eventExpiryDuration") is not None:
        out["event_expiry_duration"] = data["eventExpiryDuration"]
    else:
        raise DeserializationError("CreateMemoryInput.event_expiry_duration required")
    if data.get("memoryStrategies") is not None:
        import capo_bedrock_agentcore_control.types.memory_strategy_input_list

        out["memory_strategies"] = (
            capo_bedrock_agentcore_control.types.memory_strategy_input_list.deserialize_json(
                data["memoryStrategies"]
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
    if data.get("tags") is not None:
        import capo_bedrock_agentcore_control.types.tags_map

        out["tags"] = capo_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(value: CreateMemoryInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    if "memory_strategies" in value:
        import capo_bedrock_agentcore_control.types.memory_strategy_input_list

        out["memory_strategies"] = (
            capo_bedrock_agentcore_control.types.memory_strategy_input_list.redact_sensitive(
                value["memory_strategies"]
            )
        )
    return out
