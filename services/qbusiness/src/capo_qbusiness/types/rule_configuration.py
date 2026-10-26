"""Generated from Smithy shape ``com.amazonaws.qbusiness#RuleConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_qbusiness.errors import DeserializationError, SerializationError
from capo_qbusiness.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_qbusiness.types.content_blocker_rule
    import capo_qbusiness.types.content_retrieval_rule


class _RuleConfiguration_contentBlockerRule(TypedDict, closed=True):
    contentBlockerRule: "capo_qbusiness.types.content_blocker_rule.ContentBlockerRule"


class _RuleConfiguration_contentRetrievalRule(TypedDict, closed=True):
    contentRetrievalRule: (
        "capo_qbusiness.types.content_retrieval_rule.ContentRetrievalRule"
    )


RuleConfiguration: TypeAlias = (
    _RuleConfiguration_contentBlockerRule
    | _RuleConfiguration_contentRetrievalRule
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RuleConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RuleConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "contentBlockerRule" in value:
        import capo_qbusiness.types.content_blocker_rule

        return {
            "contentBlockerRule": capo_qbusiness.types.content_blocker_rule.serialize_json(
                value["contentBlockerRule"]
            )
        }
    elif "contentRetrievalRule" in value:
        import capo_qbusiness.types.content_retrieval_rule

        return {
            "contentRetrievalRule": capo_qbusiness.types.content_retrieval_rule.serialize_json(
                value["contentRetrievalRule"]
            )
        }
    else:
        raise SerializationError("RuleConfiguration: no variant present")


def deserialize_json(data: dict) -> RuleConfiguration:
    if data.get("contentBlockerRule") is not None:
        import capo_qbusiness.types.content_blocker_rule

        return {
            "contentBlockerRule": capo_qbusiness.types.content_blocker_rule.deserialize_json(
                data["contentBlockerRule"]
            )
        }
    elif data.get("contentRetrievalRule") is not None:
        import capo_qbusiness.types.content_retrieval_rule

        return {
            "contentRetrievalRule": capo_qbusiness.types.content_retrieval_rule.deserialize_json(
                data["contentRetrievalRule"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RuleConfiguration: no recognized variant key")
