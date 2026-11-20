"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#GetSpaceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.encryption_configuration
    import capo_opensearchmemory.types.event_expiry_days
    import capo_opensearchmemory.types.extraction_model_id
    import capo_opensearchmemory.types.memory_expiry_days
    import capo_opensearchmemory.types.memory_strategy_list
    import capo_opensearchmemory.types.space_arn
    import capo_opensearchmemory.types.space_id
    import capo_opensearchmemory.types.space_name
    import capo_opensearchmemory.types.space_status
    import capo_opensearchmemory.types.timestamp


class GetSpaceResponse(TypedDict, closed=True):
    space_id: "capo_opensearchmemory.types.space_id.SpaceId"
    """<p>The ID of the space.</p>"""
    arn: "capo_opensearchmemory.types.space_arn.SpaceArn"
    """<p>The Amazon Resource Name (ARN) of the space.</p>"""
    name: "capo_opensearchmemory.types.space_name.SpaceName"
    """<p>The name of the space.</p>"""
    status: "capo_opensearchmemory.types.space_status.SpaceStatus"
    """<p>The status of the space.</p>"""
    status_reason: NotRequired["str"]
    """<p>Details about why the space is <code>FAILED</code>. Read it only when <code>status</code> is <code>FAILED</code>: it can still hold the reason for an earlier failure.</p>"""
    created_at: "capo_opensearchmemory.types.timestamp.Timestamp"
    """<p>When the space was created.</p>"""
    memory_strategies: NotRequired[
        "capo_opensearchmemory.types.memory_strategy_list.MemoryStrategyList"
    ]
    """<p>The space's memory strategies, including the names the service generated for strategies created without one. Empty for a space that has no memory strategies.</p>"""
    event_expiry_days: NotRequired[
        "capo_opensearchmemory.types.event_expiry_days.EventExpiryDays"
    ]
    """<p>How many days the space keeps each event. Absent when it was never set, in which case the default of 90 days applies.</p>"""
    memory_expiry_days: NotRequired[
        "capo_opensearchmemory.types.memory_expiry_days.MemoryExpiryDays"
    ]
    """<p>How many days the space keeps each memory. 0 means memories never expire. Absent when it was never set, in which case memories never expire.</p>"""
    extraction_model_id: NotRequired[
        "capo_opensearchmemory.types.extraction_model_id.ExtractionModelId"
    ]
    """<p>The model that extracts and consolidates memories for the space. Absent when it was never set, in which case the service default applies.</p>"""
    encryption_configuration: NotRequired[
        "capo_opensearchmemory.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The AWS KMS key the space was created with. Absent when the space uses an AWS owned key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSpaceResponse) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    import capo_opensearchmemory.types.space_status

    out["status"] = capo_opensearchmemory.types.space_status.serialize_aws_json_1_0(
        value["status"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    import capo_opensearchmemory.types.timestamp

    out["createdAt"] = capo_opensearchmemory.types.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
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
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSpaceResponse:
    out: GetSpaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("status") is not None:
        import capo_opensearchmemory.types.space_status

        out["status"] = (
            capo_opensearchmemory.types.space_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_opensearchmemory.types.space_status.SpaceStatus", ""
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("createdAt") is not None:
        import capo_opensearchmemory.types.timestamp

        out["created_at"] = (
            capo_opensearchmemory.types.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
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
    return out


def redact_sensitive(value: GetSpaceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "memory_strategies" in value:
        import capo_opensearchmemory.types.memory_strategy_list

        out["memory_strategies"] = (
            capo_opensearchmemory.types.memory_strategy_list.redact_sensitive(
                value["memory_strategies"]
            )
        )
    return out
