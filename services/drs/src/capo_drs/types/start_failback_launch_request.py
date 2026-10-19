"""Generated from Smithy shape ``com.amazonaws.drs#StartFailbackLaunchRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.start_failback_request_recovery_instance_i_ds
    import capo_drs.types.tags_map


class StartFailbackLaunchRequest(TypedDict, closed=True):
    recovery_instance_i_ds: "capo_drs.types.start_failback_request_recovery_instance_i_ds.StartFailbackRequestRecoveryInstanceIDs"
    """<p>The IDs of the Recovery Instance whose failback launch we want to request.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>The tags to be associated with the failback launch Job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartFailbackLaunchRequest) -> dict:
    out: dict = {}
    import capo_drs.types.start_failback_request_recovery_instance_i_ds

    out["recoveryInstanceIDs"] = (
        capo_drs.types.start_failback_request_recovery_instance_i_ds.serialize_json(
            value["recovery_instance_i_ds"]
        )
    )
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartFailbackLaunchRequest:
    out: StartFailbackLaunchRequest = {}  # type: ignore[typeddict-item]
    if data.get("recoveryInstanceIDs") is not None:
        import capo_drs.types.start_failback_request_recovery_instance_i_ds

        out["recovery_instance_i_ds"] = (
            capo_drs.types.start_failback_request_recovery_instance_i_ds.deserialize_json(
                data["recoveryInstanceIDs"]
            )
        )
    else:
        out["recovery_instance_i_ds"] = []
    if data.get("tags") is not None:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: StartFailbackLaunchRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
