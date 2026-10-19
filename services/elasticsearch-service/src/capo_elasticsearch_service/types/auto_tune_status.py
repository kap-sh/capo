"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutoTuneStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.auto_tune_state
    import capo_elasticsearch_service.types.boolean
    import capo_elasticsearch_service.types.string
    import capo_elasticsearch_service.types.u_int_value
    import capo_elasticsearch_service.types.update_timestamp


class AutoTuneStatus(TypedDict, closed=True):
    creation_date: "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    """<p>Timestamp which tells Auto-Tune options creation date .</p>"""
    update_date: "capo_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    """<p>Timestamp which tells Auto-Tune options last updated time.</p>"""
    update_version: "capo_elasticsearch_service.types.u_int_value.UIntValue"
    """<p>Specifies the Auto-Tune options latest version.</p>"""
    state: "capo_elasticsearch_service.types.auto_tune_state.AutoTuneState"
    """<p>Specifies the <code>AutoTuneState</code> for the Elasticsearch domain.</p>"""
    error_message: NotRequired["capo_elasticsearch_service.types.string.String"]
    """<p>Specifies the error message while enabling or disabling the Auto-Tune options.</p>"""
    pending_deletion: NotRequired["capo_elasticsearch_service.types.boolean.Boolean"]
    """<p>Indicates whether the Elasticsearch domain is being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutoTuneStatus) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.update_timestamp

    out["CreationDate"] = (
        capo_elasticsearch_service.types.update_timestamp.serialize_json(
            value["creation_date"]
        )
    )
    import capo_elasticsearch_service.types.update_timestamp

    out["UpdateDate"] = (
        capo_elasticsearch_service.types.update_timestamp.serialize_json(
            value["update_date"]
        )
    )
    out["UpdateVersion"] = value.get("update_version", 0)
    import capo_elasticsearch_service.types.auto_tune_state

    out["State"] = capo_elasticsearch_service.types.auto_tune_state.serialize_json(
        value["state"]
    )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "pending_deletion" in value:
        out["PendingDeletion"] = value["pending_deletion"]
    return out


def deserialize_json(data: dict) -> AutoTuneStatus:
    out: AutoTuneStatus = {}  # type: ignore[typeddict-item]
    if data.get("CreationDate") is not None:
        import capo_elasticsearch_service.types.update_timestamp

        out["creation_date"] = (
            capo_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["CreationDate"]
            )
        )
    else:
        import datetime

        out["creation_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("UpdateDate") is not None:
        import capo_elasticsearch_service.types.update_timestamp

        out["update_date"] = (
            capo_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["UpdateDate"]
            )
        )
    else:
        import datetime

        out["update_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("UpdateVersion") is not None:
        out["update_version"] = data["UpdateVersion"]
    else:
        out["update_version"] = 0
    if data.get("State") is not None:
        import capo_elasticsearch_service.types.auto_tune_state

        out["state"] = (
            capo_elasticsearch_service.types.auto_tune_state.deserialize_json(
                data["State"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_elasticsearch_service.types.auto_tune_state.AutoTuneState", ""
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    if data.get("PendingDeletion") is not None:
        out["pending_deletion"] = data["PendingDeletion"]
    return out
