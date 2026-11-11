"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#GetSpaceDataAccessInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.data_access_audit_context
    import capo_cloudwatchomni.types.data_access_target_list
    import capo_cloudwatchomni.types.space_id


class GetSpaceDataAccessInput(TypedDict, closed=True):
    space_id: "capo_cloudwatchomni.types.space_id.SpaceId"
    """The unique ID of the space to return credentials for."""
    target_scopes: (
        "capo_cloudwatchomni.types.data_access_target_list.DataAccessTargetList"
    )
    """The actions to include in the credentials, grouped by service."""
    duration_seconds: NotRequired["int"]
    """The lifetime of the credentials, in seconds. Defaults to 3600."""
    audit_context: NotRequired[
        "capo_cloudwatchomni.types.data_access_audit_context.DataAccessAuditContext"
    ]
    """Caller-supplied key-value pairs that are recorded for auditing. They do not affect authorization or the permissions of the credentials."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetSpaceDataAccessInput) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    import capo_cloudwatchomni.types.data_access_target_list

    out["targetScopes"] = (
        capo_cloudwatchomni.types.data_access_target_list.serialize_cbor(
            value["target_scopes"]
        )
    )
    if "duration_seconds" in value:
        out["durationSeconds"] = value["duration_seconds"]
    if "audit_context" in value:
        import capo_cloudwatchomni.types.data_access_audit_context

        out["auditContext"] = (
            capo_cloudwatchomni.types.data_access_audit_context.serialize_cbor(
                value["audit_context"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetSpaceDataAccessInput:
    out: GetSpaceDataAccessInput = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        out["space_id"] = ""
    if data.get("targetScopes") is not None:
        import capo_cloudwatchomni.types.data_access_target_list

        out["target_scopes"] = (
            capo_cloudwatchomni.types.data_access_target_list.deserialize_cbor(
                data["targetScopes"]
            )
        )
    else:
        out["target_scopes"] = []
    if data.get("durationSeconds") is not None:
        out["duration_seconds"] = data["durationSeconds"]
    if data.get("auditContext") is not None:
        import capo_cloudwatchomni.types.data_access_audit_context

        out["audit_context"] = (
            capo_cloudwatchomni.types.data_access_audit_context.deserialize_cbor(
                data["auditContext"]
            )
        )
    return out
