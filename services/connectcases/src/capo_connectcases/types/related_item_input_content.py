"""Generated from Smithy shape ``com.amazonaws.connectcases#RelatedItemInputContent``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.comment_content
    import capo_connectcases.types.connect_case_input_content
    import capo_connectcases.types.contact
    import capo_connectcases.types.custom_input_content
    import capo_connectcases.types.file_content
    import capo_connectcases.types.sla_input_content


class RelatedItemInputContentContactMember(TypedDict, closed=True):
    contact: "capo_connectcases.types.contact.Contact"


class RelatedItemInputContentCommentMember(TypedDict, closed=True):
    comment: "capo_connectcases.types.comment_content.CommentContent"


class RelatedItemInputContentFileMember(TypedDict, closed=True):
    file: "capo_connectcases.types.file_content.FileContent"


class RelatedItemInputContentSlaMember(TypedDict, closed=True):
    sla: "capo_connectcases.types.sla_input_content.SlaInputContent"


class RelatedItemInputContentConnectCaseMember(TypedDict, closed=True):
    connectCase: (
        "capo_connectcases.types.connect_case_input_content.ConnectCaseInputContent"
    )


class RelatedItemInputContentCustomMember(TypedDict, closed=True):
    custom: "capo_connectcases.types.custom_input_content.CustomInputContent"


RelatedItemInputContent: TypeAlias = (
    RelatedItemInputContentContactMember
    | RelatedItemInputContentCommentMember
    | RelatedItemInputContentFileMember
    | RelatedItemInputContentSlaMember
    | RelatedItemInputContentConnectCaseMember
    | RelatedItemInputContentCustomMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemInputContent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RelatedItemInputContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "contact" in value:
        import capo_connectcases.types.contact

        return {
            "contact": capo_connectcases.types.contact.serialize_json(value["contact"])
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
        import capo_connectcases.types.sla_input_content

        return {
            "sla": capo_connectcases.types.sla_input_content.serialize_json(
                value["sla"]
            )
        }
    elif "connectCase" in value:
        import capo_connectcases.types.connect_case_input_content

        return {
            "connectCase": capo_connectcases.types.connect_case_input_content.serialize_json(
                value["connectCase"]
            )
        }
    elif "custom" in value:
        import capo_connectcases.types.custom_input_content

        return {
            "custom": capo_connectcases.types.custom_input_content.serialize_json(
                value["custom"]
            )
        }
    else:
        raise SerializationError("RelatedItemInputContent: no variant present")


def deserialize_json(data: dict) -> RelatedItemInputContent:
    if data.get("contact") is not None:
        import capo_connectcases.types.contact

        return {
            "contact": capo_connectcases.types.contact.deserialize_json(data["contact"])
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
        import capo_connectcases.types.sla_input_content

        return {
            "sla": capo_connectcases.types.sla_input_content.deserialize_json(
                data["sla"]
            )
        }
    elif data.get("connectCase") is not None:
        import capo_connectcases.types.connect_case_input_content

        return {
            "connectCase": capo_connectcases.types.connect_case_input_content.deserialize_json(
                data["connectCase"]
            )
        }
    elif data.get("custom") is not None:
        import capo_connectcases.types.custom_input_content

        return {
            "custom": capo_connectcases.types.custom_input_content.deserialize_json(
                data["custom"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RelatedItemInputContent: no recognized variant key")


def redact_sensitive(value: RelatedItemInputContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sla" in value:
        import capo_connectcases.types.sla_input_content

        out["sla"] = capo_connectcases.types.sla_input_content.redact_sensitive(
            value["sla"]
        )
    return out
