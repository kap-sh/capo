"""Generated from Smithy shape ``com.amazonaws.cloudsearch#OptionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.boolean
    import capo_cloudsearch.types.option_state
    import capo_cloudsearch.types.u_int_value
    import capo_cloudsearch.types.update_timestamp


class OptionStatus(TypedDict, closed=True):
    creation_date: "capo_cloudsearch.types.update_timestamp.UpdateTimestamp"
    """<p>A timestamp for when this option was created.</p>"""
    update_date: "capo_cloudsearch.types.update_timestamp.UpdateTimestamp"
    """<p>A timestamp for when this option was last updated.</p>"""
    update_version: "capo_cloudsearch.types.u_int_value.UIntValue"
    """<p>A unique integer that indicates when this option was last updated.</p>"""
    state: "capo_cloudsearch.types.option_state.OptionState"
    """<p>The state of processing a change to an option. Possible values:</p><ul> <li><code>RequiresIndexDocuments</code>: the option's latest value will not be deployed until <a>IndexDocuments</a> has been called and indexing is complete.</li> <li><code>Processing</code>: the option's latest value is in the process of being activated. </li> <li><code>Active</code>: the option's latest value is completely deployed.</li> <li><code>FailedToValidate</code>: the option value is not compatible with the domain's data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.</li> </ul>"""
    pending_deletion: NotRequired["capo_cloudsearch.types.boolean.Boolean"]
    """<p>Indicates that the option will be deleted once processing is complete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_cloudsearch.types.update_timestamp

    capo_cloudsearch.types.update_timestamp.serialize_query(
        value["creation_date"], pairs, f"{key_prefix}CreationDate"
    )
    import capo_cloudsearch.types.update_timestamp

    capo_cloudsearch.types.update_timestamp.serialize_query(
        value["update_date"], pairs, f"{key_prefix}UpdateDate"
    )
    pairs.append((f"{key_prefix}UpdateVersion", str(value.get("update_version", 0))))
    import capo_cloudsearch.types.option_state

    capo_cloudsearch.types.option_state.serialize_query(
        value["state"], pairs, f"{key_prefix}State"
    )
    if "pending_deletion" in value:
        pairs.append(
            (
                f"{key_prefix}PendingDeletion",
                "true" if value["pending_deletion"] else "false",
            )
        )


def deserialize_query(el: Element) -> OptionStatus:
    out: OptionStatus = {}  # type: ignore[typeddict-item]
    child_creation_date = el.find("CreationDate")
    if child_creation_date is not None:
        import capo_cloudsearch.types.update_timestamp

        out["creation_date"] = (
            capo_cloudsearch.types.update_timestamp.deserialize_query(
                child_creation_date
            )
        )
    else:
        import datetime

        out["creation_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_update_date = el.find("UpdateDate")
    if child_update_date is not None:
        import capo_cloudsearch.types.update_timestamp

        out["update_date"] = capo_cloudsearch.types.update_timestamp.deserialize_query(
            child_update_date
        )
    else:
        import datetime

        out["update_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    child_update_version = el.find("UpdateVersion")
    if child_update_version is not None:
        out["update_version"] = int(child_update_version.text or "")
    else:
        out["update_version"] = 0
    child_state = el.find("State")
    if child_state is not None:
        import capo_cloudsearch.types.option_state

        out["state"] = capo_cloudsearch.types.option_state.deserialize_query(
            child_state
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_cloudsearch.types.option_state.OptionState", ""
        )
    child_pending_deletion = el.find("PendingDeletion")
    if child_pending_deletion is not None:
        out["pending_deletion"] = (child_pending_deletion.text or "").lower() == "true"
    return out
