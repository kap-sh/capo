"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#CreateSpaceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.client_token
    import capo_opensearchmemory.types.encryption_configuration
    import capo_opensearchmemory.types.event_expiry_days
    import capo_opensearchmemory.types.extraction_model_id
    import capo_opensearchmemory.types.memory_expiry_days
    import capo_opensearchmemory.types.memory_strategy_list
    import capo_opensearchmemory.types.space_name
    import capo_opensearchmemory.types.tag_list


class CreateSpaceRequest(TypedDict, closed=True):
    name: "capo_opensearchmemory.types.space_name.SpaceName"
    """<p>A name for the space, unique within your account in the Region. If another space already has the name, the request fails with <code>ConflictException</code>.</p>"""
    memory_strategies: NotRequired[
        "capo_opensearchmemory.types.memory_strategy_list.MemoryStrategyList"
    ]
    """<p>The memory strategies that extract memories from the space's events: up to 10 strategies, each with a name that is unique within the space.</p> <p>Optional. Omit it, or send an empty list, to create a space with no memory strategies. Such a space stores the conversation events you send it and returns them through <code>SearchEvents</code> and <code>ListEvents</code>, but extracts no memories and has none to search. You can add strategies later with <code>UpdateSpace</code>.</p> <p>The serialized list can be at most 384 KiB.</p>"""
    event_expiry_days: NotRequired[
        "capo_opensearchmemory.types.event_expiry_days.EventExpiryDays"
    ]
    """<p>How many days the space keeps each event, from 1 to 365. The default is 90.</p>"""
    memory_expiry_days: NotRequired[
        "capo_opensearchmemory.types.memory_expiry_days.MemoryExpiryDays"
    ]
    """<p>How many days the space keeps each memory, from 0 to 3650, counted from when the service writes the memory. Updating a memory with <code>UpdateMemory</code> doesn't restart the count. 0 means memories never expire. If you omit it, memories never expire.</p> <p>Searches and lists leave out a memory past its expiry, and reading, updating, or deleting it returns <code>ResourceNotFoundException</code>.</p>"""
    extraction_model_id: NotRequired[
        "capo_opensearchmemory.types.extraction_model_id.ExtractionModelId"
    ]
    """<p>The model that extracts and consolidates memories for every strategy in the space, as an Amazon Bedrock model ID without an inference-profile prefix: <code>anthropic.claude-opus-5-5</code> or <code>anthropic.claude-haiku-5-5</code>. Another value fails with <code>ValidationException</code>, and the message lists the supported IDs. Omit it to use the service default, which can change over time and isn't returned by <code>GetSpace</code>. Setting a value pins the model.</p>"""
    encryption_configuration: NotRequired[
        "capo_opensearchmemory.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The AWS KMS key that encrypts the space's data. Omit it, or omit its <code>kmsKeyArn</code>, to use an AWS owned key. You can't change the key after you create the space.</p>"""
    tags: NotRequired["capo_opensearchmemory.types.tag_list.TagList"]
    """<p>The tags to add to the space.</p>"""
    client_token: NotRequired["capo_opensearchmemory.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that makes the request idempotent. A retry with the same token and the same parameters within 2 hours returns the space that the first request created, instead of creating another. Reusing the token with different parameters, or while the first request is still in progress, fails with <code>ConflictException</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateSpaceRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "memory_strategies" in value:
        import capo_opensearchmemory.types.memory_strategy_list

        out["memoryStrategies"] = (
            capo_opensearchmemory.types.memory_strategy_list.serialize_aws_json_1_0(
                value["memory_strategies"]
            )
        )
    if "event_expiry_days" in value:
        out["eventExpiryDays"] = value["event_expiry_days"]
    if "memory_expiry_days" in value:
        out["memoryExpiryDays"] = value["memory_expiry_days"]
    if "extraction_model_id" in value:
        out["extractionModelId"] = value["extraction_model_id"]
    if "encryption_configuration" in value:
        import capo_opensearchmemory.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_opensearchmemory.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "tags" in value:
        import capo_opensearchmemory.types.tag_list

        out["tags"] = capo_opensearchmemory.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateSpaceRequest:
    out: CreateSpaceRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("memoryStrategies") is not None:
        import capo_opensearchmemory.types.memory_strategy_list

        out["memory_strategies"] = (
            capo_opensearchmemory.types.memory_strategy_list.deserialize_aws_json_1_0(
                data["memoryStrategies"]
            )
        )
    if data.get("eventExpiryDays") is not None:
        out["event_expiry_days"] = data["eventExpiryDays"]
    if data.get("memoryExpiryDays") is not None:
        out["memory_expiry_days"] = data["memoryExpiryDays"]
    if data.get("extractionModelId") is not None:
        out["extraction_model_id"] = data["extractionModelId"]
    if data.get("encryptionConfiguration") is not None:
        import capo_opensearchmemory.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_opensearchmemory.types.encryption_configuration.deserialize_aws_json_1_0(
                data["encryptionConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_opensearchmemory.types.tag_list

        out["tags"] = capo_opensearchmemory.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(value: CreateSpaceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "memory_strategies" in value:
        import capo_opensearchmemory.types.memory_strategy_list

        out["memory_strategies"] = (
            capo_opensearchmemory.types.memory_strategy_list.redact_sensitive(
                value["memory_strategies"]
            )
        )
    return out
