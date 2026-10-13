"""Generated from Smithy shape ``com.amazonaws.connectcases#RelatedItemTypeFilter``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connectcases.types.comment_filter
    import capo_connectcases.types.connect_case_filter
    import capo_connectcases.types.contact_filter
    import capo_connectcases.types.custom_filter
    import capo_connectcases.types.file_filter
    import capo_connectcases.types.sla_filter


class _RelatedItemTypeFilter_contact(TypedDict, closed=True):
    contact: "capo_connectcases.types.contact_filter.ContactFilter"


class _RelatedItemTypeFilter_comment(TypedDict, closed=True):
    comment: "capo_connectcases.types.comment_filter.CommentFilter"


class _RelatedItemTypeFilter_file(TypedDict, closed=True):
    file: "capo_connectcases.types.file_filter.FileFilter"


class _RelatedItemTypeFilter_sla(TypedDict, closed=True):
    sla: "capo_connectcases.types.sla_filter.SlaFilter"


class _RelatedItemTypeFilter_connectCase(TypedDict, closed=True):
    connectCase: "capo_connectcases.types.connect_case_filter.ConnectCaseFilter"


class _RelatedItemTypeFilter_custom(TypedDict, closed=True):
    custom: "capo_connectcases.types.custom_filter.CustomFilter"


RelatedItemTypeFilter: TypeAlias = (
    _RelatedItemTypeFilter_contact
    | _RelatedItemTypeFilter_comment
    | _RelatedItemTypeFilter_file
    | _RelatedItemTypeFilter_sla
    | _RelatedItemTypeFilter_connectCase
    | _RelatedItemTypeFilter_custom
)


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemTypeFilter) -> dict:
    if "contact" in value:
        import capo_connectcases.types.contact_filter

        return {
            "contact": capo_connectcases.types.contact_filter.serialize_json(
                value["contact"]
            )
        }
    elif "comment" in value:
        import capo_connectcases.types.comment_filter

        return {
            "comment": capo_connectcases.types.comment_filter.serialize_json(
                value["comment"]
            )
        }
    elif "file" in value:
        import capo_connectcases.types.file_filter

        return {
            "file": capo_connectcases.types.file_filter.serialize_json(value["file"])
        }
    elif "sla" in value:
        import capo_connectcases.types.sla_filter

        return {"sla": capo_connectcases.types.sla_filter.serialize_json(value["sla"])}
    elif "connectCase" in value:
        import capo_connectcases.types.connect_case_filter

        return {
            "connectCase": capo_connectcases.types.connect_case_filter.serialize_json(
                value["connectCase"]
            )
        }
    elif "custom" in value:
        import capo_connectcases.types.custom_filter

        return {
            "custom": capo_connectcases.types.custom_filter.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError("RelatedItemTypeFilter: no variant present")


def deserialize_json(data: dict) -> RelatedItemTypeFilter:
    if data.get("contact") is not None:
        import capo_connectcases.types.contact_filter

        return {
            "contact": capo_connectcases.types.contact_filter.deserialize_json(
                data["contact"]
            )
        }
    elif data.get("comment") is not None:
        import capo_connectcases.types.comment_filter

        return {
            "comment": capo_connectcases.types.comment_filter.deserialize_json(
                data["comment"]
            )
        }
    elif data.get("file") is not None:
        import capo_connectcases.types.file_filter

        return {
            "file": capo_connectcases.types.file_filter.deserialize_json(data["file"])
        }
    elif data.get("sla") is not None:
        import capo_connectcases.types.sla_filter

        return {"sla": capo_connectcases.types.sla_filter.deserialize_json(data["sla"])}
    elif data.get("connectCase") is not None:
        import capo_connectcases.types.connect_case_filter

        return {
            "connectCase": capo_connectcases.types.connect_case_filter.deserialize_json(
                data["connectCase"]
            )
        }
    elif data.get("custom") is not None:
        import capo_connectcases.types.custom_filter

        return {
            "custom": capo_connectcases.types.custom_filter.deserialize_json(
                data["custom"]
            )
        }
    else:
        raise DeserializationError("RelatedItemTypeFilter: no recognized variant key")


def redact_sensitive(value: RelatedItemTypeFilter) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sla" in value:
        import capo_connectcases.types.sla_filter

        out["sla"] = capo_connectcases.types.sla_filter.redact_sensitive(value["sla"])
    return out
