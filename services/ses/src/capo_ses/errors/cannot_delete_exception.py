"""Generated from Smithy shape ``com.amazonaws.ses#CannotDeleteException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import ServiceError

if TYPE_CHECKING:
    import capo_ses.types.error_message
    import capo_ses.types.rule_or_rule_set_name


class CannotDeleteException_(TypedDict, closed=True):
    name: NotRequired["capo_ses.types.rule_or_rule_set_name.RuleOrRuleSetName"]
    """<p>Indicates that a resource could not be deleted because no resource with the specified name exists.</p>"""
    message: NotRequired["capo_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CannotDeleteException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "message" in value:
        pairs.append((f"{key_prefix}message", str(value["message"])))


def deserialize_query(el: Element) -> CannotDeleteException_:
    out: CannotDeleteException_ = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CannotDeleteException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#CannotDeleteException``."""

    code: str | None = "CannotDeleteException"

    def __init__(
        self,
        data: CannotDeleteException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CannotDeleteException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_query(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "CannotDeleteException":
        return cls(deserialize_query(el), message, response=response)
