"""Generated from Smithy shape ``com.amazonaws.connectcases#RelatedItemContent``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.comment_content
    import capo_connectcases.types.connect_case_content
    import capo_connectcases.types.contact_content
    import capo_connectcases.types.custom_content
    import capo_connectcases.types.file_content
    import capo_connectcases.types.sla_content


class _RelatedItemContent_contact(TypedDict, closed=True):
    contact: "capo_connectcases.types.contact_content.ContactContent"


class _RelatedItemContent_comment(TypedDict, closed=True):
    comment: "capo_connectcases.types.comment_content.CommentContent"


class _RelatedItemContent_file(TypedDict, closed=True):
    file: "capo_connectcases.types.file_content.FileContent"


class _RelatedItemContent_sla(TypedDict, closed=True):
    sla: "capo_connectcases.types.sla_content.SlaContent"


class _RelatedItemContent_connectCase(TypedDict, closed=True):
    connectCase: "capo_connectcases.types.connect_case_content.ConnectCaseContent"


class _RelatedItemContent_custom(TypedDict, closed=True):
    custom: "capo_connectcases.types.custom_content.CustomContent"


RelatedItemContent: TypeAlias = (
    _RelatedItemContent_contact
    | _RelatedItemContent_comment
    | _RelatedItemContent_file
    | _RelatedItemContent_sla
    | _RelatedItemContent_connectCase
    | _RelatedItemContent_custom
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemContent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RelatedItemContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "contact" in value:
        import capo_connectcases.types.contact_content

        return {
            "contact": capo_connectcases.types.contact_content.serialize_json(
                value["contact"]
            )
        }
    elif "comment" in value:
        import capo_connectcases.types.comment_content

        return {
            "comment": capo_connectcases.types.comment_content.serialize_json(
                value["comment"]
            )
        }
    elif "file" in value:
        import capo_connectcases.types.file_content

        return {
            "file": capo_connectcases.types.file_content.serialize_json(value["file"])
        }
    elif "sla" in value:
        import capo_connectcases.types.sla_content

        return {"sla": capo_connectcases.types.sla_content.serialize_json(value["sla"])}
    elif "connectCase" in value:
        import capo_connectcases.types.connect_case_content

        return {
            "connectCase": capo_connectcases.types.connect_case_content.serialize_json(
                value["connectCase"]
            )
        }
    elif "custom" in value:
        import capo_connectcases.types.custom_content

        return {
            "custom": capo_connectcases.types.custom_content.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError("RelatedItemContent: no variant present")


def deserialize_json(data: dict) -> RelatedItemContent:
    if data.get("contact") is not None:
        import capo_connectcases.types.contact_content

        return {
            "contact": capo_connectcases.types.contact_content.deserialize_json(
                data["contact"]
            )
        }
    elif data.get("comment") is not None:
        import capo_connectcases.types.comment_content

        return {
            "comment": capo_connectcases.types.comment_content.deserialize_json(
                data["comment"]
            )
        }
    elif data.get("file") is not None:
        import capo_connectcases.types.file_content

        return {
            "file": capo_connectcases.types.file_content.deserialize_json(data["file"])
        }
    elif data.get("sla") is not None:
        import capo_connectcases.types.sla_content

        return {
            "sla": capo_connectcases.types.sla_content.deserialize_json(data["sla"])
        }
    elif data.get("connectCase") is not None:
        import capo_connectcases.types.connect_case_content

        return {
            "connectCase": capo_connectcases.types.connect_case_content.deserialize_json(
                data["connectCase"]
            )
        }
    elif data.get("custom") is not None:
        import capo_connectcases.types.custom_content

        return {
            "custom": capo_connectcases.types.custom_content.deserialize_json(
                data["custom"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RelatedItemContent: no recognized variant key")


def redact_sensitive(value: RelatedItemContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sla" in value:
        import capo_connectcases.types.sla_content

        out["sla"] = capo_connectcases.types.sla_content.redact_sensitive(value["sla"])
    return out
