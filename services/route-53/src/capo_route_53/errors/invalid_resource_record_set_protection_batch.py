"""Generated from Smithy shape ``com.amazonaws.route53#InvalidResourceRecordSetProtectionBatch``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import ServiceError

if TYPE_CHECKING:
    import capo_route_53.types.error_message
    import capo_route_53.types.protection_errors


class InvalidResourceRecordSetProtectionBatch_(TypedDict, closed=True):
    message: NotRequired["capo_route_53.types.error_message.ErrorMessage"]
    """<p>A message that explains why Route 53 couldn't process the <code>CreateResourceRecordSetProtections</code> or <code>DeleteResourceRecordSetProtections</code> request.</p>"""
    errors: "capo_route_53.types.protection_errors.ProtectionErrors"
    """<p>The entries that failed, with the reason that each one failed.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: InvalidResourceRecordSetProtectionBatch_, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    if "message" in value:
        SubElement(el, "Message").text = str(value["message"])
    import capo_route_53.types.protection_errors

    capo_route_53.types.protection_errors.serialize_xml(value["errors"], el, "Errors")


def deserialize_xml(el: Element) -> InvalidResourceRecordSetProtectionBatch_:
    out: InvalidResourceRecordSetProtectionBatch_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    child_errors = el.find("Errors")
    if child_errors is not None:
        import capo_route_53.types.protection_errors

        out["errors"] = capo_route_53.types.protection_errors.deserialize_xml(
            child_errors
        )
    else:
        out["errors"] = []
    return out


class InvalidResourceRecordSetProtectionBatch(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.route53#InvalidResourceRecordSetProtectionBatch``."""

    code: str | None = "InvalidResourceRecordSetProtectionBatch"

    def __init__(
        self,
        data: InvalidResourceRecordSetProtectionBatch_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidResourceRecordSetProtectionBatch",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_xml(
        cls, el: Element, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidResourceRecordSetProtectionBatch":
        return cls(deserialize_xml(el), message, response=response)
