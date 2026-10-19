"""Generated from Smithy shape ``com.amazonaws.opensearch#OptionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.boolean
    import capo_opensearch.types.option_state
    import capo_opensearch.types.u_int_value
    import capo_opensearch.types.update_timestamp


class OptionStatus(TypedDict, closed=True):
    creation_date: "capo_opensearch.types.update_timestamp.UpdateTimestamp"
    """<p>The timestamp when the entity was created.</p>"""
    update_date: "capo_opensearch.types.update_timestamp.UpdateTimestamp"
    """<p>The timestamp of the last time the entity was updated.</p>"""
    update_version: "capo_opensearch.types.u_int_value.UIntValue"
    """<p>The latest version of the entity.</p>"""
    state: "capo_opensearch.types.option_state.OptionState"
    """<p>The state of the entity.</p>"""
    pending_deletion: NotRequired["capo_opensearch.types.boolean.Boolean"]
    """<p>Indicates whether the entity is being deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OptionStatus) -> dict:
    out: dict = {}
    import capo_opensearch.types.update_timestamp

    out["CreationDate"] = capo_opensearch.types.update_timestamp.serialize_json(
        value["creation_date"]
    )
    import capo_opensearch.types.update_timestamp

    out["UpdateDate"] = capo_opensearch.types.update_timestamp.serialize_json(
        value["update_date"]
    )
    out["UpdateVersion"] = value.get("update_version", 0)
    import capo_opensearch.types.option_state

    out["State"] = capo_opensearch.types.option_state.serialize_json(value["state"])
    if "pending_deletion" in value:
        out["PendingDeletion"] = value["pending_deletion"]
    return out


def deserialize_json(data: dict) -> OptionStatus:
    out: OptionStatus = {}  # type: ignore[typeddict-item]
    if data.get("CreationDate") is not None:
        import capo_opensearch.types.update_timestamp

        out["creation_date"] = capo_opensearch.types.update_timestamp.deserialize_json(
            data["CreationDate"]
        )
    else:
        import datetime

        out["creation_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("UpdateDate") is not None:
        import capo_opensearch.types.update_timestamp

        out["update_date"] = capo_opensearch.types.update_timestamp.deserialize_json(
            data["UpdateDate"]
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
        import capo_opensearch.types.option_state

        out["state"] = capo_opensearch.types.option_state.deserialize_json(
            data["State"]
        )
    else:
        import typing

        out["state"] = typing.cast("capo_opensearch.types.option_state.OptionState", "")
    if data.get("PendingDeletion") is not None:
        out["pending_deletion"] = data["PendingDeletion"]
    return out
