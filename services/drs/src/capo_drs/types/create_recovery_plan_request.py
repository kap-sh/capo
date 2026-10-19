"""Generated from Smithy shape ``com.amazonaws.drs#CreateRecoveryPlanRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.client_idempotency_token
    import capo_drs.types.recovery_plan_description
    import capo_drs.types.recovery_plan_name
    import capo_drs.types.tags_map


class CreateRecoveryPlanRequest(TypedDict, closed=True):
    name: "capo_drs.types.recovery_plan_name.RecoveryPlanName"
    description: NotRequired[
        "capo_drs.types.recovery_plan_description.RecoveryPlanDescription"
    ]
    client_token: NotRequired[
        "capo_drs.types.client_idempotency_token.ClientIdempotencyToken"
    ]
    """<p>A unique string provided to ensure request idempotency.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>The tags to apply to the Recovery Plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRecoveryPlanRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateRecoveryPlanRequest:
    out: CreateRecoveryPlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateRecoveryPlanRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
